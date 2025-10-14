##
#   app/routes/celery_task.pyz
##
from fastapi import APIRouter
from celery.result import AsyncResult

router = APIRouter(tags=["Celery Task 상태 확인"])


@router.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    """
    Celery Task의 상태를 확인하는 API

    :param task_id: str
    :return:
    """
    task_result = AsyncResult(task_id)

    if task_result.state == "PENDING":
        return {"task_id": task_id, "status": "PENDING"}
    elif task_result.state == "SUCCESS":
        return {"task_id": task_id, "status": "SUCCESS", "result": task_result.result}
    elif task_result.state == "FAILURE":
        return {"task_id": task_id, "status": "FAILURE", "error": str(task_result.info)}
