##
#   measure.py 파일은 웹 페이지 속도 측정 API를 정의합니다.
##
from app.utils.kafka_adapter import KafkaAdapter
from app.services.measure_service import MeasureService
from app.models.schemas import URLData
from fastapi import APIRouter, HTTPException
from typing import List

import asyncio
import logging

router = APIRouter(tags=["웹 페이지 속도 측정"])
logging.basicConfig(level=logging.INFO)


@router.post("/web/measure")
async def measure_page_load(data: List[URLData]):

    try:
        # 싱글턴 패턴으로 KafkaAdapter 인스턴스 생성
        measure_service = MeasureService()
        kafka_adapter = KafkaAdapter()

        # playwright_runner.py 실행
        try:
            results = await measure_service.run_playwright_process(data)
        except Exception as e:
            logging.error(f"Error during API execution: {e}")

        semaphore = asyncio.Semaphore(10)

        # Kafka로 결과 전송
        async def limited_send(result):
            async with semaphore:
                try:
                    await kafka_adapter.send(
                        result, actor="Page Load Bot", verb="measured"
                    )
                except Exception as e:
                    logging.error(f"Error during Kafka send: {e}")
                    return {"error": str(e), "result": result}

        tasks = [limited_send(result) for result in results]
        task_results = await asyncio.gather(*tasks, return_exceptions=True)

        # 성공 및 실패 처리
        success = [
            res
            for res in task_results
            if not isinstance(res, dict) or "error" not in res
        ]
        errors = [
            res for res in task_results if isinstance(res, dict) and "error" in res
        ]

        return {
            "message": "Processing completed",
            "success_count": len(success),
            "error_count": len(errors),
            "errors": errors,
            "results": results,
        }

    except Exception as e:
        logging.error(f"Error during API execution: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
