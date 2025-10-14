##
#   playwright_runner.py URL 목록의 로딩 시간을 측정하는 코드 입니다.
##
import asyncio
from playwright.async_api import async_playwright
import time
import json
import sys
from asyncio import Semaphore
import logging
from datetime import datetime
from typing import Union


# 날짜별 로그 파일 설정
log_filename = f"/tmp/playwright_runner_{datetime.now().strftime('%Y-%m-%d')}.log"

# 로깅 설정
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

CONCURRENT_TASKS = 5
semaphore = Semaphore(CONCURRENT_TASKS)


async def fetch_page_info(browser, url: str, title: str) -> dict:
    async with semaphore:
        logging.info(f"Measuring load time for URL: {url}")
        page = await browser.new_page()
        # result = {"url": url, "title": title, "status": None, "load_time": None}
        result: dict[str, Union[int, str, float, None]] = {
            "url": url,
            "title": title,
            "status": None | int,
            "load_time": None | float,
            "login_type": None,
        }
        try:
            start_time = time.perf_counter()
            response = await page.goto(url, timeout=30000)
            end_time = time.perf_counter()
            result["status"] = response.status if response else "No Response"
            result["load_time"] = end_time - start_time

            # 페이지 타이틀 가져오기
            page_title = await page.title()
            logging.info(
                f"Load time for {url}: {result['load_time']} seconds, Status: {result['status']}, page_title : {page_title}"
            )
        except Exception as e:
            result["status"] = f"Error: {str(e)}"
        finally:
            await page.close()
        return result


async def process_urls(url_list: list) -> list:
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # 미리 빈 페이지로 워밍업
        page = await browser.new_page()
        await page.goto("about:blank")
        await page.close()

        tasks = [
            fetch_page_info(browser, item["url"], item["title"]) for item in url_list
        ]
        results = await asyncio.gather(*tasks)
        await browser.close()
    return results


def main():
    input_data = sys.stdin.read()
    urls = json.loads(input_data)
    results = asyncio.run(process_urls(urls))
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
