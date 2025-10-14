from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_calendar_01_pageEntry(page: Page):
        """해당 코드는 홈 > 레진 신작 > 신작 캘린더 버튼 클릭시 신작캘린더 페이지 진입을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 신작캘린더 버튼 요소 지정
        calendar_link = page.locator("a.vx__calendarLink")
        # href 추출
        href_value = calendar_link.get_attribute("href")
        calendar_link.click()
        
        # 페이지 로드 대기
        page.wait_for_load_state("load")
        page.wait_for_timeout(1000)
        
        # 현재 URL 파싱
        current_url = page.url
        parsed_current_path = urlparse(current_url).path

        # 검증
        if parsed_current_path == href_value:
                print(f"✅ 신작 캘린더 페이지 이동 성공: '{parsed_current_path}'가 href와 일치합니다.")
        else:
                raise AssertionError(f"❌ 신작 캘린더 페이지 경로 불일치! 이동된 경로: '{parsed_current_path}', 기대값: '{href_value}'")

        page.close() 
        

def test_calendar_02_ko_info(page: Page):
        """해당 코드는 KO 신작 캘린더 페이지에서 신작캘린더 안내 팝업 호출 및 내용을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/calendar')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # "신작 캘린더 안내" 버튼 노출 위치로 이동하고 클릭
        info_button = page.locator("button.guide__btnInfo__2FmZ5")
        info_button.scroll_into_view_if_needed()
        info_button.click()
        
        # 모달 팝업 요소 지정
        modal = page.locator("div.modal__n8lvY.modal--isBottomModal__v8e_8")
        
        # 모달 노출 여부 검증
        if modal.is_visible():
                print("✅ '신작 캘린더 안내' 모달이 정상적으로 노출되었습니다.")
        else:
                raise AssertionError("❌ '신작 캘린더 안내' 모달이 노출되지 않았습니다.")
        
        
        # 제목 텍스트 추출
        modal_title = page.locator("header.guideModal__header__ALqSO h2.guideModal__title__l7fLW")
        title_text = modal_title.inner_text().strip()

        # 본문 내용 텍스트 추축
        modal_list = page.locator("ul#calendar-info-modal-message li")
        list_texts = [modal_list.nth(i).inner_text().strip() for i in range(modal_list.count())]

        # 검증할 대상 문자열
        expected_title = "신작 캘린더 안내"
        expected_text_1 = "당 월의 신작 캘린더는 매월 1일 00시에 오픈됩니다."
        expected_text_2_keywords = ["작가/출판사의 사정", "예고 없이 변경될 수 있습니다."]
        
        # 검증 
        text_2_matched = any(
                all(keyword in text for keyword in expected_text_2_keywords)
                for text in list_texts
        )

        if (
                title_text == expected_title and
                expected_text_1 in list_texts and
                text_2_matched
        ):
                print("✅ 제목과 안내 텍스트가 모두 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 제목 또는 안내 텍스트가 누락되었거나 잘못되었습니다.")

        page.close() 


def test_calendar_03_US_info(page: Page):
        """해당 코드는 US 신작 캘린더 페이지에서 신작캘린더 안내 팝업 호출 및 내용을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/calendar')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # "신작 캘린더 안내" 버튼 노출 위치로 이동하고 클릭
        info_button = page.locator("button.guide__btnInfo__2FmZ5")
        info_button.scroll_into_view_if_needed()
        info_button.click()
        
        # 모달 팝업 요소 지정
        modal = page.locator("div.modal__n8lvY.modal--isBottomModal__v8e_8")
        
        # 모달 노출 여부 검증
        if modal.is_visible():
                print("✅ 'US 신작 캘린더 안내' 모달이 정상적으로 노출되었습니다.")
        else:
                raise AssertionError("❌ 'US 신작 캘린더 안내' 모달이 노출되지 않았습니다.")
        
        
        # 제목 텍스트 추출
        modal_title = page.locator("header.guideModal__header__ALqSO h2.guideModal__title__l7fLW")
        title_text = modal_title.inner_text().strip()

        # 본문 내용 텍스트 추축
        modal_list = page.locator("ul#calendar-info-modal-message li")
        list_texts = [modal_list.nth(i).inner_text().strip() for i in range(modal_list.count())]

        # 검증할 대상 문자열
        expected_title = "Notice"
        expected_text_1 = "The monthly new releases calendar opens on the 1st of every month at midnight."
        expected_text_2_keywords = [
        "depending on the circumstances of the artists or publishers",
        "may be subject to change without prior notice"
        ]
        
        # 검증 
        text_2_matched = any(
        all(keyword in text for keyword in expected_text_2_keywords)
        for text in list_texts
        )

        if (
        title_text == expected_title and
        expected_text_1 in list_texts and
        text_2_matched
        ):
                print("✅ US 신작캘린더 안내 팝업 제목과 안내 텍스트가 모두 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ US 신작캘린더 안내 팝업 제목 또는 안내 텍스트가 누락되었거나 잘못되었습니다.")

        page.close() 
                

