##
#   app/routes/tasks_page_loading_measure.py
##
from fastapi import APIRouter, HTTPException
from app.models.schemas import URLData
from app.celeryconfig import celery_app
from app.tasks.tasks_page_loading_measure import run_page_load_test
from typing import List

router = APIRouter(tags=["웹 페이지 속도 측정(celery)"])


@router.post("/web/measures")
async def test_page_load(data: List[URLData]):
    """
    웹 페이지 속도 측정 API

    :param data: URLData
    :return:
    """
    try:
        serialized_data = [item.dict() for item in data]
        # Celery 태스크 호출
        task = celery_app.send_task(
            "app.tasks.tasks_page_loading_measure.run_page_load_test",
            args=[serialized_data],
        )
        return {"message": "Task submitted", "task_id": task.id}
    except Exception as e:
        print(f"Error during API execution: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
