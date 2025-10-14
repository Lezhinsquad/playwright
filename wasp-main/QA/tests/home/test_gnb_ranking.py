from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_gnbRangking_01_us_adult_genre_unVisible(page: Page):
        """해당 코드는 US 비로그인 상태에서 랭킹 장르에 성인장르 비노출을 확인합니다."""

        # 레진코믹스 KR 랭킹 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/ranking')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
        # "Lezhin R" 텍스트를 가진 버튼 요소 찾기
        lezhin_r_button = page.locator("button", has_text="Lezhin R")
        
        # 존재 여부 확인
        if lezhin_r_button.count() > 0:
                raise AssertionError(" 비로그인 상태에서 ❌ 'Lezhin R' 성인 장르가 노출됩니다.")
        else:
                print("✅ 비로그인 상태에서 'Lezhin R' 성인 장르가 노출되지 않습니다.")
        

        # 페이지 종료
        page.close()
          
          
def test_gnbRangking_02_login_adult_genre_unVisible(page: Page):
        """해당 코드는 US 비성인 계정 로그인 상태에서 랭킹 장르에 성인장르 비노출을 확인합니다."""
        # 레진코믹스 US 로그인페이지 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/login')
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(1000)
        # 쿠키 허용 닫기
        accept_all_cookies
        # 이메일 입력
        page.locator("#email").fill("squad_115@yopmail.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        # 1초 대기
        page.wait_for_timeout(1000)

        # 레진코믹스 US 랭킹 이동
        page.goto('https://q-www.lezhinus.com/en/ranking')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # "Lezhin R" 텍스트를 가진 버튼 요소 찾기
        lezhin_r_button = page.locator("button", has_text="Lezhin R")
        
        # 존재 여부 확인
        if lezhin_r_button.count() > 0:
                raise AssertionError("❌ 비성인 계정에서 'Lezhin R' 성인 장르가 노출됩니다.")
        else:
                print("✅ 비성인 계정에서 'Lezhin R' 성인 장르가 노출되지 않습니다.")
        
        # 페이지 종료
        page.close()
        

def test_gnbRangking_03_login_adult_genre_Visible(page: Page):
        """해당 코드는 US 비성인 계정 로그인 상태에서 랭킹 장르에 성인장르 비노출을 확인합니다."""
        # 레진코믹스 US 로그인페이지 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/login')
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(1000)
        # 쿠키 허용 닫기
        accept_all_cookies
        # 이메일 입력
        page.locator("#email").fill("squad_115@yopmail.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        # 1초 대기
        page.wait_for_timeout(1000)

        # 레진코믹스 US 랭킹 이동
        page.goto('https://q-www.lezhinus.com/en/ranking')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # "Lezhin R" 텍스트를 가진 버튼 요소 찾기
        lezhin_r_button = page.locator("button", has_text="Lezhin R")
        
        # 검증
        if lezhin_r_button.is_visible():
                raise AssertionError("❌ 비성인 계정에서 'Lezhin R' 성인장르가 노출되고 있습니다.")
        else:
                print("✅ 비성인 계정에서 'Lezhin R' 성인장르가 정상적으로 비노출됩니다.")
        # 페이지 종료
        page.close()
          

def test_gnbRanking_04_top_move(page: Page):
        """해당 코드는 랭킹 페이지 탭 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # KR 오리지널 완결 탭 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/ranking')


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # Top이동이 노출되도록 스크롤 진행
        page.evaluate("window.scrollTo(0, 1000)")
        
        # 탑 이동 버튼 요소 찾기
        top_button = page.wait_for_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY', timeout=2000)
        
        # 탑 이동 버튼의 클래스명 가져와서 변수에 저장
        button_class = top_button.get_attribute("class")

        # 버튼이 존재하는지 검증
        if top_button is not None:
                print("✅ 탑 이동 버튼이 정상 노출됩니다.", button_class)
        else:
                raise AssertionError("❌ 탑 이동 버튼이 노출되지 않습니다.")
        
        # 버튼 클릭
        top_button.click()
        
        # 현재 스크롤 위치 가져오기
        scroll_position = page.evaluate("window.scrollY")

        # 스크롤 위치가 Y축 최상단중 1에 가까운지 검증
        if scroll_position <= 1:
                print("✅ 현재 스크롤 위치는 맨 위입니다!", "window.scrollY :", scroll_position)
        else:
                raise AssertionError(f"❌ 현재 스크롤 위치는 맨 위가 아닙니다! (현재 위치: {scroll_position}px)")
        
        # 탑이동 버튼이 존재하는지 확인 (없으면 None 반환)
        top_button = page.query_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY')

        # '맨 위로' 버튼이 보이지 않는지 검증
        if top_button is None or not top_button.is_visible():
                print("✅ 탑이동 버튼이 정상적으로 사라졌습니다!", top_button)
        else:
                raise AssertionError("❌ '맨 위로' 버튼이 아직 화면에 표시되고 있습니다!")
     
        # 페이지 종료
        page.close()
        
        
