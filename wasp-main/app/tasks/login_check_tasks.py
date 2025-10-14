##
#   app/tasks/login_check_tasks.py
##
import asyncio
import traceback
from celery import shared_task
from app.models.schemas import URLLogin
from app.services.login_service import LoginService
from app.utils.kafka_adapter import KafkaAdapter
from app.utils.error_handler import log_exception


# 1분 간격, 최대 3회 재시도
@shared_task(bind=True, default_retry_delay=60, max_retries=1)
def run_login_test(self, input_data: dict):
    """
    로그인 테스트를 실행하는 Celery Task
    :param self:
    :param input_data: dict
    :return:
    """
    login_service = LoginService()
    kafka_adapter = KafkaAdapter()
    # 현재 Celery Task ID
    task_id = self.request.id
    print(f"Python Print - Task ID: {task_id}")

    try:
        print(f"celery - input_data: {input_data}")
        # URLLogin 모델로 변환
        login_data = URLLogin(**input_data)
        # 로그인 프로세스 실행
        # 비동기 함수 실행
        try:
            results = asyncio.run(
                login_service.run_playwright_process(login_data, task_id)
            )
        except Exception as e:
            print(f"Error in run_playwright_process: {e}")
            raise Exception(f"Login process failed: {e}")

        # Kafka 메시지 전송
        try:
            asyncio.run(
                kafka_adapter.send(results[0], actor="Login Bot", verb="logged in")
            )
        except Exception as e:
            print(f"Error in Kafka send: {e}")
            raise Exception(f"Kafka message sending failed: {e}")

        # results = asyncio.run(login_service.run_playwright_process(login_data))
        # asyncio.run(kafka_adapter.send(results[0], actor="Login Bot", verb="logged in"))
    except Exception as e:
        # 예외 발생 시 로깅
        # log_exception(e)
        # 예외 발생 -> 작업 상태가 실패로 설정됨
        # 또는 raise Exception("Custom error message")
        raise self.retry(exc=e)  # 재시도
    return {"message": "Processing completed", "results": results}
