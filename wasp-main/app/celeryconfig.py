##
#   app/celeryconfig.py
##
from celery import Celery
import os

redis_url = os.getenv("REDIS_URL")

REDIS_BROKER_URL = redis_url
REDIS_BACKEND_URL = redis_url


celery_app = Celery(
    "app", broker=REDIS_BROKER_URL, backend=REDIS_BACKEND_URL, include=["app.tasks"]
)
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Seoul",
    enable_utc=True,
    worker_redirect_stdouts=True,  # stdout 과 stderr 를 Celery 로그로 리다이렉션
)
