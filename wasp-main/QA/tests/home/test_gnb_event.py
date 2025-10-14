from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_gnb_event_01_bannerClick(page: Page):
        """해당 코드는 이벤트 페이지 내 '배너' 클릭 후 링크 이동을 확인합니다."""
        
        def extract_path(url):
                return urlparse(url).path

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/sale')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        #   배너 링크 요소 찾기
        first_banner = page.locator("section.saleBanner__zrcjx ul.saleBanner__list__sJWVE li").first.locator("a.bannerList__link")
        href_value = first_banner.get_attribute("href")
        
        #  배너 클릭
        first_banner.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        with page.expect_navigation(wait_until="load"):
                first_banner.click(force=True)
        
        # 1초 대기
        page.wait_for_timeout(2000)


        # 경로 비교
        expected_path = extract_path(href_value)
        actual_path = extract_path(page.url)

        # 검증
        if expected_path == actual_path:
            print(f"✅ 경로 일치 확인: {actual_path}")
        else:
            raise AssertionError(f"❌ 경로 불일치: {expected_path} vs {actual_path}")

        page.close() 
        
def test_gnb_event_02_top_move(page: Page):
        """해당 코드는 이벤트 페이지 탭 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://beta-www.lezhin.com/ko/login')
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')


        # 신규 만화 더보기 페이지 이동
        page.goto('https://beta-www.lezhin.com/ko/sale')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # Top이동이 노출되도록 스크롤 진행
        page.evaluate("window.scrollTo(0, 1200)")
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 탑 이동 버튼 요소 찾기
        top_button = page.wait_for_selector('button.topBtn__9U4u1.topBtn--isShow__ELZZT', timeout=2000)
        
        # 탑 이동 버튼의 클래스명 가져와서 변수에 저장
        button_class = top_button.get_attribute("class")

        # 버튼이 존재하는지 검증
        if top_button is not None:
                print("✅ 탑 이동 버튼이 정상 노출됩니다.", button_class)
        else:
                raise AssertionError("❌ 탑 이동 버튼이 노출되지 않습니다.")
        
        # 버튼 클릭
        top_button.click()
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 현재 스크롤 위치 가져오기
        scroll_position = page.evaluate("window.scrollY")

        # 스크롤 위치가 Y축 최상단중 1에 가까운지 검증
        if scroll_position <= 1:
                print("✅ 현재 스크롤 위치는 맨 위입니다!", "window.scrollY :", scroll_position)
        else:
                raise AssertionError(f"❌ 현재 스크롤 위치는 맨 위가 아닙니다! (현재 위치: {scroll_position}px)")
        
        # 탑이동 버튼이 존재하는지 확인 (없으면 None 반환)
        top_button = page.query_selector('button.topBtn__9U4u1.topBtn--isShow__ELZZT')

        # '맨 위로' 버튼이 보이지 않는지 검증
        if top_button is None or not top_button.is_visible():
                print("✅ 탑이동 버튼이 정상적으로 사라졌습니다!", top_button)
        else:
                raise AssertionError("❌ '맨 위로' 버튼이 아직 화면에 표시되고 있습니다!")
     
        # 페이지 종료
        page.close()


def test_gnb_event_03_ko_empty(page: Page):
        """해당 코드는 이벤트 페이지에 노출될 배너가 없을 경우 노출되는 empty 화면 노출을 확인합니다."""
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://mirror-www.lezhin.com/ko/sale')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 요소 선택자
        empty_box = page.locator("div.lzEmpty__qHwoc.saleBannerEmpty__uoB_0.lzEmpty--hasImage__cTXcj")

        # 텍스트 기대값
        expected_title = "진행중인 이벤트가 없습니다."
        expected_subtitle = "[서랍 메뉴>취향 재설정]에서\n취향 장르를 추가 후 다시 시도해 보세요."

        # 검증
        if empty_box.is_visible():
                title_text = empty_box.locator("p.lzEmpty--title___s5Go").inner_text().strip()
                subtitle_text = empty_box.locator("p.lzEmpty--subtitle__ZRwAr").inner_text().strip()

                if expected_title == title_text and expected_subtitle == subtitle_text:
                        print("✅ 이벤트 없음 안내 요소 및 텍스트가 정상적으로 노출되었습니다.")
                else:
                        raise AssertionError(
                                f"❌ 안내 텍스트 불일치\n[예상 제목] {expected_title}\n[실제 제목] {title_text}\n"
                                f"[예상 부제] {expected_subtitle}\n[실제 부제] {subtitle_text}"
                )
        else:
                raise AssertionError("❌ 이벤트 없음 안내 요소가 페이지에 노출되지 않았습니다.")

        page.close() 


def test_gnb_event_04_us_empty(page: Page):
        """해당 코드는 us 이벤트 페이지에 노출될 배너가 없을 경우 노출되는 empty 화면 노출을 확인합니다."""
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://beta-www.lezhinus.com/en/sale')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 요소 선택자
        empty_box = page.locator("div.lzEmpty__qHwoc.saleBannerEmpty__uoB_0.lzEmpty--hasImage__cTXcj")

        # 텍스트 기대값
        expected_title = "No Ongoing Events"
        expected_subtitle = "You might want to add more genres\nto your preferences under [Preferences Setting] and try again"

        # 검증
        if empty_box.is_visible():
                title_text = empty_box.locator("p.lzEmpty--title___s5Go").inner_text().strip()
                subtitle_text = empty_box.locator("p.lzEmpty--subtitle__ZRwAr").inner_text().strip()

                if expected_title == title_text and expected_subtitle == subtitle_text:
                        print("✅ 이벤트 없음 안내 요소 및 텍스트가 정상적으로 노출되었습니다.")
                else:
                        raise AssertionError(
                                f"❌ 안내 텍스트 불일치\n[예상 제목] {expected_title}\n[실제 제목] {title_text}\n"
                                f"[예상 부제] {expected_subtitle}\n[실제 부제] {subtitle_text}"
                )
        else:
                raise AssertionError("❌ 이벤트 없음 안내 요소가 페이지에 노출되지 않았습니다.")

        page.close() 
