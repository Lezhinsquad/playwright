import asyncio
import random

import aiohttp
import json
import logging
import time
import traceback
from functools import partial

from app.domain.url_item import URLItem, MeasureRequest
from app.adapters.kafka_adapter import KafkaAdapter
from app.utils.logger import log_with_function_name

# 동시 요청 수를 제한하기 위한 세마포어 설정
# 동시에 최대 5개의 HTTP 요청이 진행되도록 제한
semaphore = asyncio.Semaphore(3)
# Kafka 전송 시 동시 작업 수를 제한하기 위한 세마포어 설정
# 동시에 최대 5개의 Kafka 전송 작업이 진행되도록 제한
kafka_semaphore = asyncio.Semaphore(3)


class MeasureService:
    def __init__(self, kafka_client: KafkaAdapter):
        # KafkaAdapter 인스턴스를 초기화합니다.
        self.kafka_client = kafka_client
        # HTTP 요청 시 사용할 타임아웃 설정 (총 10초)
        self.http_timeout = aiohttp.ClientTimeout(total=10)
        # 비동기 큐 생성 (URL 처리 결과 전송을 위해 사용)
        self.result_queue = asyncio.Queue()

    async def fetch_url(
        self, session: aiohttp.ClientSession, url_item: URLItem, retries=3
    ):
        """
        주어진 URLItem을 사용하여 URL 정보를 POST 요청으로 가져옵니다.

        :param session: aiohttp.ClientSession 객체로 HTTP 요청을 보내기 위해 사용됩니다.
        :param url_item: URLItem 객체로 URL과 타이틀 정보를 포함합니다.
        :param retries: 요청 재시도 횟수를 지정합니다. z
        :return: 요청의 결과를 JSON 형식으로 반환하거나 오류 정보를 포함한 딕셔너리를 반환합니다.
        """
        async with semaphore:  # 동시 요청 수를 제한합니다.
            for attempt in range(retries):
                try:
                    # 현재 시도 회차와 URL을 로깅합니다.
                    log_with_function_name(
                        logging.INFO,
                        f"Attempt {attempt + 1}/{retries} - Fetching URL: {url_item.url} with title: {url_item.title}",
                    )
                    # URL과 타이틀을 POST 요청으로 보냅니다.
                    async with session.post(
                        url="https://lz-mpw.lezhin.net/measure",
                        json={"url": str(url_item.url), "title": url_item.title},
                    ) as response:
                        try:

                            # 응답의 상태 코드와 콘텐츠 유형을 검사합니다.
                            temp = await response.json()
                            # print(f"***** response : {response.status}")
                            # print(f"***** response : {temp}")

                            if temp.get("status") == 500:
                                # 내부 status가 500이면 재시도 대상
                                log_with_function_name(
                                    logging.WARNING,
                                    f"Internal status 500 for URL: {url_item.url} title: {url_item.title}. Retrying...",
                                )
                                if attempt < retries - 1:
                                    await asyncio.sleep(1 + random.uniform(0, 0.5))
                                    continue
                                else:
                                    log_with_function_name(
                                        logging.ERROR,
                                        f"Failed due to internal status 500 after {retries} attempts for URL: {url_item.url}",
                                    )
                                    return {
                                        "url": url_item.url,
                                        "error": "Internal status 500 after retries",
                                    }
                            else:
                                return temp
                            # 응답을 JSON으로 파싱하여 반환합니다.
                            # return await response.json()
                        except aiohttp.ContentTypeError:
                            # JSON 파싱 실패 시 오류 메시지를 반환하고 로깅합니다.
                            log_with_function_name(
                                logging.ERROR,
                                f"Invalid JSON response from URL: {url_item.url}",
                            )
                            return {
                                "url": url_item.url,
                                "error": "Invalid JSON response",
                            }
                except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                    # 예외를 구체적으로 구분하여 로깅
                    error_type = type(
                        e
                    ).__name__  # 예외 클래스 이름 (예: ClientConnectorError)
                    error_details = repr(e)  # 자세한 예외 디버깅 정보
                    traceback_info = traceback.format_exc()  # 전체 스택 트레이스

                    # 요청 실패 시 재시도 횟수가 남아 있으면 재시도합니다.
                    if attempt < retries - 1:
                        # 재시도 횟수가 남아 있을 경우 로그
                        log_with_function_name(
                            logging.WARNING,
                            (
                                f"Retrying ({attempt + 1}/{retries}) for URL: {url_item.url} due to error: {error_type}. "
                                f"Details: {error_details}\nTraceback: {traceback_info}"
                            ),
                        )
                        # 지수 백오프를 사용하여 재시도 대기
                        await asyncio.sleep(1 + random.uniform(0, 0.5))
                    else:
                        # 재시도 실패 시 로그에 전체 예외 디버깅 정보 출력
                        log_with_function_name(
                            logging.ERROR,
                            (
                                f"Failed to fetch URL: {url_item.url} after {retries} attempts. "
                                f"Error Type: {error_type}. Details: {error_details}\nTraceback: {traceback_info}"
                            ),
                        )
                        # 에러 반환
                        return {"url": url_item.url, "error": error_details}

    async def fetch_url2(
        self, session: aiohttp.ClientSession, url_item: URLItem, retries=3
    ):
        """
        주어진 URLItem을 사용하여 URL 정보를 POST 요청으로 가져옵니다.

        :param session: aiohttp.ClientSession 객체로 HTTP 요청을 보내기 위해 사용됩니다.
        :param url_item: URLItem 객체로 URL과 타이틀 정보를 포함합니다.
        :param retries: 요청 재시도 횟수를 지정합니다.
        :return: 요청의 결과를 JSON 형식으로 반환하거나 오류 정보를 포함한 딕셔너리를 반환합니다.
        """
        async with semaphore:
            # 재시도 가능한 작업 정의
            async def operation():
                async with session.post(
                    url="https://lz-mpw.lezhin.net/measure",
                    json={"url": str(url_item.url), "title": url_item.title},
                ) as response:
                    if response.status == 200:
                        try:
                            temp = await response.json()
                            # print(f"***** response : {response.status}")
                            # print(f"***** response : {temp}")
                            log_with_function_name(
                                logging.INFO,
                                (
                                    f"Fetching URL: {temp['url']} title: {temp['title']} load_time: {temp['load_time']} status: {temp['status']}",
                                ),
                            )

                            # JSON 데이터의 내부 상태 확인
                            if temp.get("status") == 500:
                                raise ValueError(
                                    f"Internal status 500 for URL: {url_item.url} title: {url_item.title}"
                                )
                            return temp
                        except aiohttp.ContentTypeError:
                            raise ValueError(
                                f"Invalid JSON response from URL: {url_item.url} title: {url_item.title}"
                            )
                    else:
                        raise ValueError(
                            f"HTTP status {response.status} for URL: {url_item.url} title: {url_item.title}"
                        )

            # retry_operation을 사용하여 재시도 로직 적용
            try:
                return await self.retry_operation(operation, retries=retries)
            except Exception as e:
                log_with_function_name(
                    logging.ERROR,
                    f"Failed to fetch URL: {url_item.url} title: {url_item.title} after {retries} retries. Error: {str(e)}",
                )
                return {"url": url_item.url, "error": str(e)}

    async def retry_operation(self, operation, retries=3, backoff_factor=1):
        """
        주어진 operation을 최대 retries 횟수만큼 재시도하고, backoff_factor를 사용하여 재시도 간격을 조정합니다.

        :param operation: 비동기로 실행할 작업(예: Kafka 전송 함수)
        :param retries: 재시도 횟수
        :param backoff_factor: 재시도 간격을 늘리기 위한 요인 (지수 백오프에 사용)
        :return: 성공 시 작업의 결과를 반환하거나 실패 시 오류 정보를 반환합니다.
        """
        for attempt in range(retries):
            try:
                # operation 함수 실행
                return await operation()
            except Exception as e:
                # 작업이 실패할 경우 지정된 재시도 횟수만큼 재시도합니다.
                if attempt < retries - 1:
                    # 재시도 간격을 점점 늘리기 위해 지수 백오프 사용
                    await asyncio.sleep(
                        backoff_factor * (2**attempt) + random.uniform(0, 0.5)
                    )
                else:
                    # 예외를 구체적으로 구분하여 로깅
                    error_type = type(
                        e
                    ).__name__  # 예외 클래스 이름 (예: ClientConnectorError)
                    error_details = repr(e)  # 자세한 예외 디버깅 정보
                    traceback_info = traceback.format_exc()  # 전체 스택 트레이스

                    # 최대 재시도 횟수 초과 시 오류를 로깅하고 반환합니다.
                    log_with_function_name(
                        logging.ERROR,
                        (
                            f"{operation} Operation failed after {retries} retries. Error: {str(e)}",
                            f"Details: {error_details}\nTraceback: {traceback_info}",
                        ),
                    )
                    return {"error": str(e)}

    async def stream_results(self, measure_request: MeasureRequest, retries=3):
        """
        MeasureRequest 내의 모든 URL을 처리하고, 각 결과를 Kafka로 스트리밍합니다.

        :param measure_request: MeasureRequest 객체로 여러 URLItem 객체를 포함합니다.
        :param retries: Kafka 전송 재시도 횟수
        :return: Kafka에 전송한 결과를 JSON 형식의 문자열로 반환합니다.
        """
        # 전체 소요시간 측정
        overall_start_time = time.time()

        # 클라이언트 연결 풀 설정
        conn = aiohttp.TCPConnector(limit=20)
        async with aiohttp.ClientSession(
            connector=conn, timeout=self.http_timeout
        ) as session:
            # URLItem에 대한 비동기 fetch_url 작업을 준비
            tasks = [self.fetch_url2(session, item) for item in measure_request.urls]

            # 작업을 as_completed로 처리하여 완료된 작업부터 처리
            for task in asyncio.as_completed(tasks):
                try:
                    # 각 작업의 결과를 가져옴
                    result = await task

                    if isinstance(result, Exception):
                        # fetch_url 실패의 경우 로그를 남기고 다음 작업으로 넘어감
                        log_with_function_name(
                            logging.ERROR, f"Error in fetch result: {str(result)}"
                        )
                        continue

                    async with kafka_semaphore:
                        # Kafka로 비동기적으로 결과를 전송
                        await self.retry_operation(
                            partial(self.kafka_client.send, result), retries=retries
                        )

                    # 결과를 JSON 형식의 문자열로 변환하여 즉시 반환
                    yield json.dumps(result, ensure_ascii=False)

                except Exception as e:
                    # 작업 중 오류가 발생한 경우 로그를 남기고 계속 진행
                    log_with_function_name(
                        logging.ERROR, f"Error in processing task: {str(e)}"
                    )

        # 전체 소요 시간 계산
        overall_duration = time.time() - overall_start_time
        log_with_function_name(
            logging.INFO, f"Overall duration: {overall_duration} seconds"
        )

    async def producer(self, measure_request: MeasureRequest):
        """
        URL 측정 요청을 비동기로 처리하여 결과를 큐에 저장합니다.

        :param measure_request: MeasureRequest 객체로 여러 URLItem 객체를 포함합니다.
        """
        #
        async with aiohttp.ClientSession(timeout=self.http_timeout) as session:
            tasks = [self.fetch_url(session, item) for item in measure_request.urls]
            for task in asyncio.as_completed(tasks):
                try:
                    result = await task
                    if isinstance(result, Exception):
                        log_with_function_name(
                            logging.ERROR, f"Error in fetch result: {str(result)}"
                        )
                        continue
                    await self.result_queue.put(result)
                except Exception as e:
                    log_with_function_name(
                        logging.ERROR, f"Error in processing task: {str(e)}"
                    )

    async def consumer(self):
        """
        큐에 저장된 결과를 소비하고 Kafka로 전송합니다.
        """
        while True:
            result = await self.result_queue.get()
            async with kafka_semaphore:
                print("/n")
                print(f" ============ result : {result}")
                print("/n")
                await self.retry_operation(partial(self.kafka_client.send, result))
            self.result_queue.task_done()

    async def process(self, measure_request: MeasureRequest):
        """
        생산자 - 소비자 패턴으로 URL 측정 및 Kafka 전송 작업을 실행합니다.

        :param measure_request: MeasureRequest 객체로 여러 URLItem 객체를 포함합니다.
        :return:
        """
        # 전체 소요시간 측정
        overall_start_time = time.time()

        producer_task = asyncio.create_task(self.producer(measure_request))
        consumer_task = asyncio.create_task(self.consumer())
        await producer_task
        await self.result_queue.join()
        consumer_task.cancel()

        # 전체 소요 시간 계산
        overall_duration = time.time() - overall_start_time
        log_with_function_name(
            logging.INFO, f"Overall duration: {overall_duration} seconds"
        )
