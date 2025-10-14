##
#   MeasureService
#   - measure_service.py URL 측정을 위한 비즈니스 로직을 처리하는 클래스
##
from typing import List
import subprocess
import json  # JSON 파싱을 위한 라이브러
import os
import logging
from app.models.schemas import URLData


# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class MeasureService:
    def __init__(self):
        self.env_path = os.getenv("ENV_PATH", "local")

        if self.env_path == "docker":
            self.python_path = "/usr/local/bin/python"
            self.script_path = os.path.join("app", "utils", "playwright_runner.py")
        else:
            self.python_path = "/opt/miniconda3/envs/wasp-playwright/bin/python"
            self.script_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../utils/playwright_runner.py")
            )

        logging.info(
            f"Environment Path: {self.env_path}, Python Path: {self.python_path}, Script Path: {self.script_path}"
        )

    async def run_playwright_process(self, data: List[URLData]) -> List[dict]:
        try:
            input_data = json.dumps([item.dict() for item in data])

            # playwright_runner_2.py의 절대 경로 설정
            script_path = self.script_path

            # 현재 가상환경 Python 절대 경로
            python_path = self.python_path

            # # 스크립트의 상대 경로 설정 (도커 내부 경로 기준)
            # script_path = os.path.join("app" , "utils", "playwright_runner_4.py")
            #
            # # Python 실행 경로는 도커 기본 python 사용
            # python_path = "/usr/local/bin/python"

            # subprocess 실행 및 stderr, stdout 분리
            process = subprocess.Popen(
                [python_path, script_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            stdout, stderr = process.communicate(input=input_data)

            # # 디버깅 로그 출력
            # print("---- Subprocess Logs ----")
            # print(f"STDOUT: {repr(stdout)}")  # repr() 사용해서 출력의 정확한 내용 확인
            # print(f"STDERR: {stderr}")

            if stderr:
                logging.error(f"Error in Playwright process: {stderr}")
                return [{"error": stderr.strip()}]

            # stdout 파싱
            try:
                parsed_output = json.loads(
                    stdout.strip()
                )  # strip()으로 불필요한 공백 제거
                logging.info(f"PARSED OUTPUT: {parsed_output}")
                return parsed_output
            except json.JSONDecodeError as e:
                logging.error(f"JSON Decode Error: {e}")
                logging.error(f"RAW STDOUT: {repr(stdout)}")
                return [{"error": "Invalid JSON format returned from subprocess"}]

        except Exception as e:
            print(f"Exception occurred: {e}")
            return [{"error": str(e)}]
