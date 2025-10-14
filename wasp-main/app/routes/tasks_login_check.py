##
#   app/routes/tasks_login_check.py
##
from fastapi import APIRouter, HTTPException
from app.models.schemas import URLLogin
from app.celeryconfig import celery_app
from app.tasks.login_check_tasks import run_login_test


router = APIRouter(tags=["웹 페이지 로그인 테스트(celery)"])


@router.post("/web/login")
async def test_login(data: URLLogin):
    """
    로그인 테스트 API
    :param data: URLLogin
    :return:
    """
    try:
        print("data: ", data)
        # results = run_login_test.apply_async(args=[data.dict()])
        # Celery 태스크 호출
        task = celery_app.send_task(
            "app.tasks.login_check_tasks.run_login_test", args=[data.dict()]
        )
        return {"message": "Task submitted", "task_id": task.id}
    except Exception as e:
        print(f"Error during API execution: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
