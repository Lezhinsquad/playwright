from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_free_info_01_not_expierd(page: Page):
        """해당 코드는 에피소드 목록 > 매매무 종료일이 없는 작품 팝업 내용을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/comic/moneylover')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # "매매무 정보 안내" 버튼 노출 위치로 이동하고 클릭
        info_button = page.locator('button.comicEpisodeListRentalAndPrefree__btnHelp__Ef9m3')
        info_button.click()
        
        # 모달 타이틀 확인
        modal_title = page.locator('h2.modalHeader__title__hGXNb')
        expected_title = "매매무 사용안내"

        # 모달 본문 텍스트 확인
        modal_body = page.locator('p.comicEpisodeListRentalAndPrefree__modalBodyItem__z_6Ib')
        expected_body_keywords = ["03화", "에필로그화", "1분", "무료로 공개"]

        # 검증
        if modal_title.is_visible() and modal_title.inner_text().strip() == expected_title:
                body_text = modal_body.inner_text().strip()

                if all(keyword in body_text for keyword in expected_body_keywords):
                        print("✅ 모달 타이틀과 본문 텍스트가 모두 정상적으로 노출되었습니다.")
                else:
                        raise AssertionError(f"❌ 모달 본문에 예상 텍스트가 포함되지 않았습니다: '{body_text}'")
        else:
                raise AssertionError("❌ 모달 제목이 없거나 예상된 텍스트와 다릅니다.")

        page.close() 
        
def test_free_info_02_expierd(page: Page):
        """해당 코드는 에피소드 목록 > 매매무 종료일이 있는 작품 팝업 내용을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/comic/cat_and_grandpapa')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # "매매무 정보 안내" 버튼 노출 위치로 이동하고 클릭
        info_button = page.locator('button.comicEpisodeListRentalAndPrefree__btnHelp__Ef9m3')
        info_button.click()
        
        # 모달 타이틀 확인
        modal_title = page.locator('h2.modalHeader__title__hGXNb')
        expected_title = "매매무 사용안내"

        # 첫 번째 <p> 본문 텍스트 확인
        modal_body_1 = page.locator('p.comicEpisodeListRentalAndPrefree__modalBodyItem__z_6Ib').nth(0)
        expected_keywords_1 = ["03화", "111화", "2분", "무료로 공개"]

        # 두 번째 <p> 텍스트 확인
        modal_body_2 = page.locator('p.comicEpisodeListRentalAndPrefree__modalBodyItem__z_6Ib').nth(1)
        expected_keywords_2 = ["2035-03-01 00:00", "서비스가 종료", "유료로 전환"]

        # 검증
        if modal_title.is_visible() and modal_title.inner_text().strip() == expected_title:
                # 첫 번째 문단 검증
                body_text_1 = modal_body_1.inner_text().strip()
                if not all(keyword in body_text_1 for keyword in expected_keywords_1):
                        raise AssertionError(f"❌ 첫 번째 문단에 예상 키워드가 부족합니다: {body_text_1}")
        
                # 두 번째 문단 검증
                body_text_2 = modal_body_2.inner_text().strip()
                if not all(keyword in body_text_2 for keyword in expected_keywords_2):
                        raise AssertionError(f"❌ 두 번째 문단에 예상 키워드가 부족합니다: {body_text_2}")

                print("✅ 모달 타이틀과 두 문단 텍스트가 모두 정상적으로 노출되었습니다.")
        else:
                raise AssertionError("❌ 모달 타이틀이 비정상적이거나 존재하지 않습니다.")

        page.close() 


def test_free_info_03_not_expierd_notice(page: Page):
        """해당 코드는 에피소드 목록 > 매매무 종료일이 없는 작품 노티스 내용을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/comic/madames_room_share')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # "매매무 공지 요소 추출
        notice_element = page.locator('div.episodeListEventNotice__4xY4N')
        # 기대 텍스트
        expected_text = "02화부터 24화까지 5분마다 1화 무료"
        
        # 요소 노출 여부 및 텍스트 검증
        if notice_element.is_visible():
                actual_text = notice_element.inner_text().strip()
                if expected_text in actual_text:
                        print("✅ 매매무 공지 영역과 텍스트가 정상적으로 노출됩니다.",actual_text)
                else:
                        raise AssertionError(f"❌ 텍스트가 일치하지 않습니다.\n예상: {expected_text}\n실제: {actual_text}")
        else:
                raise AssertionError("❌ 매매무 공지 영역이 페이지에 노출되지 않습니다.")

        page.close() 
        

def test_free_info_04_expierd_notice(page: Page):
        """해당 코드는 에피소드 목록 > 매매무 종료일이 있는 작품 노티스 내용을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/comic/cat_and_grandpapa')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # "매매무 공지 요소 추출
        notice_element = page.locator('div.episodeListEventNotice__4xY4N')
        # 기대 텍스트
        expected_text = "04화부터 111화까지 2분마다 1화 무료 (~2035-03-01 00:00)"
        
        # 요소 노출 여부 및 텍스트 검증
        if notice_element.is_visible():
                actual_text = notice_element.inner_text().strip()
                if expected_text in actual_text:
                        print("✅ 매매무 공지 영역과 텍스트가 정상적으로 노출됩니다.",actual_text)
                else:
                        raise AssertionError(f"❌ 텍스트가 일치하지 않습니다.\n예상: {expected_text}\n실제: {actual_text}")
        else:
                raise AssertionError("❌ 매매무 공지 영역이 페이지에 노출되지 않습니다.")

        page.close() 



