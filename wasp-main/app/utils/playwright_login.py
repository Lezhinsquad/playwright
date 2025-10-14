##
#   playwright_login.py 파일은 Playwright를 사용하여 웹사이트에 로그인하는 서비스를 제공합니다.
##
import asyncio
import time
import json
import sys
import logging
from playwright.async_api import async_playwright
from datetime import datetime
from typing import Union


async def login_check(browser, login_data: dict) -> dict:
    page = None
    url = login_data["url"]
    title = login_data["title"]
    username = login_data["username"]
    pwd = login_data["password"]
    idfield = login_data["idField"]
    pwdfield = login_data["pwdField"]
    buttonfield = login_data["buttonField"]
    login_type = login_data["type"]
    error_selector = login_data["error_selector"]
    error_message = None

    logging.info(f"login_data: {login_data}")
    logging.info(f"browser: {browser}")
    logging.info(f"url: {url}, title: {title}, username: {username}, password: {pwd}")
    logging.info(f"Email Login Check time for URL: {url}")

    result: dict[str, Union[int, str, float, None]] = {
        "url": url,
        "title": title,
        "status": None | int,
        "load_time": None | float,
        "login_type": login_type,
    }

    try:
        page = await browser.new_page()
        response = await page.goto(url)
        # response 가 200이 아닌 경우
        if response.status != 200:
            logging.error(f"Failed to load page {url}, status code: {response.status}")
            raise Exception(f"{response.status}")

        # 로그인 처리
        # 중간에 1초씩 대기
        await page.fill(idfield, username)
        await page.wait_for_timeout(1000)
        await page.fill(pwdfield, pwd)
        await page.wait_for_timeout(1000)
        await page.click(buttonfield)
        await page.wait_for_timeout(1000)

        # 리다이렉트 및 타이틀 변경 대기 및 타이틀 확인
        start_time = time.perf_counter()
        await page.wait_for_load_state("domcontentloaded")
        await page.wait_for_timeout(1000)
        current_title = await page.title()
        end_time = time.perf_counter()

        logging.info(f"Current title: {current_title}")

        # 리다이렉트 된 페이지 타이틀을 확인하고 로그인 성공 여부 확인
        if "네이버" in current_title:
            if await page.locator(error_selector).is_visible():
                result["status"] = 401
                logging.error("Error element is visible on the page.")
            else:
                result["status"] = 200
                logging.info("Error element is not visible. Proceeding...")

            # # 네이버 로그인의 경우 xpath={error_selector} 요소가 존재하면 로그인 실패
            # error_element = page.locator(f"xpath={error_selector}")
            #
            # # 요소가 존재하는지 먼저 확인 (최대 10초 대기)
            # is_error_visible = await error_element.wait_for(
            #     timeout=10000
            # ).is_visible()
            #
            # if is_error_visible:
            #     logging.error(f"Error: {error_message}")
            #     logging.error(f"Login failed: Error message detected.")
            #     # 인증 실패 코드 401 반환
            #     result["status"] = "401"
            #     logging.error(f"Login failed: {result['status']}")
        elif "레진" in current_title:
            result["status"] = 200

        result["load_time"] = end_time - start_time
        result["status"] = result["status"] if result["status"] else "415"

        logging.info(
            f"Load time for {url}: {result['load_time']} seconds, Status: {result['status']}"
        )
    except Exception as e:
        result["status"] = f"{str(e)}"
    finally:
        page.close()

    return result


async def process_urls(input_data: dict) -> list:
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # 미리 빈 페이지로 워밍업
        page = await browser.new_page()
        await page.goto("about:blank")
        await page.close()

        login_data = dict(
            url=input_data["url"],
            title=input_data["title"],
            username=input_data["username"],
            password=input_data["password"],
            idField="",
            pwdField="",
            buttonField="",
            type=input_data["type"],
            error_selector="",
        )

        logging.info(f"login_data: {login_data}")

        if login_data["type"] == "email":
            # 레진 이메일 로그인
            login_data["idField"] = '//*[@id="login-email"]'
            login_data["pwdField"] = '//*[@id="login-password"]'
            login_data["buttonField"] = '//*[@id="email"]/div[4]/button'
        elif login_data["type"] == "kakao":
            # 레진 카카오 로그인
            login_data["idField"] = '//*[@id="loginId--1"]'
            login_data["pwdField"] = '//*[@id="password--2"]'
            login_data["buttonField"] = (
                '//*[@id="mainContent"]/div/div/form/div[4]/button[1]'
            )
            login_data["error_selector"] = (
                '//*[@id="mainContent"]/div/div/form/div[4]/p'
            )
        elif login_data["type"] == "naver":
            # 레진 네이버 로그인
            login_data["idField"] = '//*[@id="id"]'
            login_data["pwdField"] = '//*[@id="pw"]'
            login_data["buttonField"] = '//*[@id="log.login"]'
            login_data["error_selector"] = '//*[@id="err_common"]/div'
        tasks = [login_check(browser, login_data)]
        results = await asyncio.gather(*tasks)
        await browser.close()
    return results


def main():
    # 날짜별 로그 파일 설정
    log_filename = f"/tmp/playwright_login_{datetime.now().strftime('%Y-%m-%d')}.log"

    # 로깅 설정
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    input_data = json.loads(sys.stdin.read())
    results = asyncio.run(process_urls(input_data))
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
