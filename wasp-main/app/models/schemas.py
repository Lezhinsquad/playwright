##
#   schemas.py is used to define the Pydantic models for the application.
##
from pydantic import BaseModel, Field


class URLData(BaseModel):
    """
    URLData 모델: URL과 타이틀 정보를 포함한 리스트를 받음
    """

    url: str = Field(default=..., description="측정할 URL")
    title: str = Field(default=..., description="측정할 URL 제목")


class URLLogin(BaseModel):
    """
    URLLogin 모델: 로그인 체크를 할 URL과 로그인 정보를 받음
    """

    url: str = Field(default=..., description="로그인 체크 URL")
    title: str = Field(default=..., description="로그인 체크 URL 제목")
    username: str = Field(default=..., description="로그인 아이디")
    password: str = Field(default=..., description="로그인 비밀번호")
    type: str = Field(default=..., description="로그인 타입 (email, kakao, naver)")
