##
#   loging_check_web.py 로그인 테스트를 위한 API 라우터
##
from app.utils.kafka_adapter import KafkaAdapter
from app.services.login_service import LoginService
from app.models.schemas import URLLogin
from fastapi import APIRouter, HTTPException
import logging

router = APIRouter(tags=["웹 페이지 로그인 테스트"])
logging.basicConfig(level=logging.INFO)


@router.post("/web/login")
async def test_login(data: URLLogin):
    """
    로그인 테스트 API
    :param data: URLLogin
    :return:
    """
    try:
        login_service = LoginService()
        kafka_adapter = KafkaAdapter()

        try:
            results = await login_service.run_playwright_process(data)
            # print(f"Results: {results}")
            await kafka_adapter.send(results[0], actor="Login Bot", verb="logged in")
            return {"message": "Processing completed", "results": results}
        except Exception as e:
            logging.error(f"Error during API execution: {e}")

    except Exception as e:
        logging.error(f"Error during API execution: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
