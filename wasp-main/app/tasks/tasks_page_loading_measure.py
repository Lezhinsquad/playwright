##
#   app/tasks/tasks_page_loading_measure.py
##
import asyncio

from celery import shared_task
from app.models.schemas import URLData
from app.services.measure_service import MeasureService
from app.utils.kafka_adapter import KafkaAdapter
from app.utils.error_handler import log_exception


@shared_task(bind=True, default_retry_delay=60, max_retries=1)
def run_page_load_test(self, input_data: list):
    """
    웹 페이지 속도 측정을 실행하는 Celery Task
    :param self:
    :param input_data: dict
    :return:
    """
    measure_service = MeasureService()
    kafka_adapter = KafkaAdapter()
    # 현재 Celery Task ID
    task_id = self.request.id
    print(f"Python Print - Task ID: {task_id}")

    try:
        print(f"celery - input_data: {input_data}")
        # URLData 모델로 변환
        measure_data_list = [URLData(**data) for data in input_data]
        # 웹 페이지 속도 측정 프로세스 실행
        # 비동기 함수 실행
        try:
            results = asyncio.run(
                measure_service.run_playwright_process(measure_data_list)
            )
        except Exception as e:
            print(f"Error in run_playwright_process: {e}")
            raise Exception(f"Page load process failed: {e}")

        # Kafka 메시지 전송
        for result in results:
            try:
                asyncio.run(
                    kafka_adapter.send(result, actor="Page Load Bot", verb="measured")
                )
            except Exception as e:
                print(f"Error in Kafka send: {e}")
                raise Exception(f"Kafka message sending failed: {e}")

    except Exception as e:
        # 예외 발생 시 로깅
        log_exception(e)
        # 예외 발생 -> 작업 상태가 실패로 설정됨
        # 또는 raise Exception("Custom error message")
        raise self.retry(exc=e)
