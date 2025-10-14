##
# utils/error_handler.py
##
import traceback
import inspect


def log_exception(exception: Exception):
    """
    예외를 로깅하는 유틸리티 함수. 호출한 함수명을 자동으로 기록합니다.
    :param exception: 발생한 예외 객체
    """
    # 호출한 함수명 가져오기
    caller_frame = inspect.stack()[1]
    caller_name = caller_frame.function

    # 예외와 스택 트레이스 로깅
    traceback_str = traceback.format_exc()
    print(f"[ERROR] Function: {caller_name}")
    print(f"Exception: {exception}")
    print(f"Traceback:\n{traceback_str}")
