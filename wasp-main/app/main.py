##
# main.py
##
from fastapi import FastAPI

from app.routes.measure import router as origin_measure_page_load
from app.routes.tasks_page_loading_measure import router as measure_page_load

# from app.routes.login_check_web import router as test_login
from app.routes.tasks_login_check import router as test_login

app = FastAPI()
app.include_router(origin_measure_page_load, prefix="/v1/origin")
app.include_router(measure_page_load, prefix="/v1")
app.include_router(test_login, prefix="/v1")


@app.get("/", tags=["Root"], include_in_schema=False)
async def root():
    return {"message": "Hello World"}  # test


# @app.get("/hello/{name}", tags=["Root"], include_in_schema=False)
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
