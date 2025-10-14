##
#   LoginService
#    - login_service.py 파일은 Playwright를 사용하여 웹사이트에 로그인하는 서비스를 제공합니다.
##
import subprocess
import json
import os
import logging
from app.models.schemas import URLLogin

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class LoginService:
    def __init__(self):
        self.env_path = os.getenv("ENV_PATH", "local")

        if self.env_path == "docker":
            self.python_path = "/usr/local/bin/python"
            self.script_path = os.path.join("app", "utils", "playwright_login.py")
        else:
            self.python_path = "/opt/miniconda3/envs/wasp-playwright/bin/python"
            self.script_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../utils/playwright_login.py")
            )

        logging.info(
            f"Environment Path: {self.env_path}, Python Path: {self.python_path}, Script Path: {self.script_path}"
        )

    async def run_playwright_process(self, data: URLLogin) -> dict:
        try:
            input_data = data.json()
            print(f"Input Data: {input_data}")

            # playwright_login.py의 절대 경로 설정
            script_path = self.script_path

            # 현재 가상환경 Python 절대 경로
            python_path = self.python_path

            # print(f"URL: input_data}")
            # subprocess 실행 및 stderr, stdout 분리
            process = subprocess.Popen(
                [python_path, script_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            # 입력 데이터 전달
            stdout, stderr = process.communicate(input=input_data)
            logging.info(f"STDERR: {stderr}")

            # 결과 출력
            # result = stdout.split("\n")

            parsed_output = json.loads(stdout.strip())  # strip()으로 불필요한 공백 제거
            # parsed_output = stdout.strip()
            logging.info(f"PARSED OUTPUT: {parsed_output}")
            logging.info(f"STDOUT: {stdout}")

            # logging.info(f"Result: {stdout}")
            #
            return parsed_output
            # return {"result": "Success"}

        except Exception as e:
            logging.error(f"Error during Playwright execution: {e}")
            return {"error": str(e)}
