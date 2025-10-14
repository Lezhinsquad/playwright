from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_new_Comic_01_kidTap(page: Page):
        """해당 코드는 신규 만화 더보기 > 전연령 탭에 전연령 작품만 노출되는지 확인하는 코드입니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("hidelove99@gmail.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 페이지 접근
        page.goto("https://www.lezhin.com/ko/bookshome/new-released?t=kid&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
        
        # 썸네일 요소 선택
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        has_adult_badge = False
        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if badge:
                has_adult_badge = True
                break  # 하나만 있어도 바로 fail 처리하기 위해 loop 종료

        page.wait_for_timeout(2000)

        #검증
        # 조건: 성인 뱃지가 하나라도 있으면 FAIL
        if not has_adult_badge:
            print("✅ 신규만화 더보기 > 전연령탭에 성인작품이 노출되지 않습니다. (PASS)")
        else:
            raise AssertionError("❌ 신규만화 더보기 > 전연령탭에 성인작품이 노출 됩니다. (FAIL)")

        page.close() 
        

def test_new_Comic_02_adultTap(page: Page):
        """해당 코드는 신규 만화 더보기 > 성인 탭에 성인 작품만 노출되는지 확인하는 코드입니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 페이지 접근
        page.goto("https://www.lezhin.com/ko/bookshome/new-released?t=adult&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
        
        # 썸네일 요소 선택
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        all_adult_badge = True
        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if not badge:
                all_adult_badge = False
                break  # 성인 뱃지가 없는 썸네일 발견 시 바로 실패 처리

        page.wait_for_timeout(2000)

        #검증
        # 조건: 성인 뱃지가 하나라도 있으면 FAIL
        if all_adult_badge:
            print("✅ 신규만화 더보기 > 성인탭에 성인작품만 노출됩니다. (PASS)")
        else:
            raise AssertionError("❌ 신규만화 더보기 > 성인탭에 전연령 작품이 노출됩니다. (FAIL)")

        page.close() 
        

def test_new_Comic_03_non_login (page: Page):
        """해당 코드는 비로그인 상태에서 신규만화 더보기 > 성인탭 선택시 로그인 페이지 이동을 확인합니다."""
        
        # 레진코믹스 신규만화 더보기 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/bookshome/new-released')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # "성인" 탭 버튼 요소 클릭
        adult_tab_button = page.locator("button.tab__9c31y:has-text('성인')")
        adult_tab_button.first.click()   
        
        page.wait_for_timeout(2000)

        #로그인 페이지 url 변수선언        
        expected_url = "https://www.lezhin.com/ko/login?redirect=%2Fcontent-mode%3Fpath%3D%252Fko%252Fbookshome%252Fnew-released%253Ft%253Dadult%2526order%253Dnew_last_year%26sw%3Dall"
        actual_url = page.url

        if actual_url == expected_url:
                print(f"✅ redirect url이 포함된 로그인 페이지로 이동되었습니다.: {actual_url}")
        else:
                raise AssertionError(f"❌ 현재 페이지 URL 불일치!\n기대값: {expected_url}\n실제값: {actual_url}")
       
        page.close() 
        

def test_new_Comic_04_kid_login (page: Page):
        """해당 코드는 비성인계정 로그인 상태에서 신규만화 더보기 > 성인탭 선택시 성인인증 페이지 이동을 확인합니다."""
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("hidelove99@gmail.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 페이지 접근
        page.goto("https://www.lezhin.com/ko/bookshome/new-released?t=all&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        
        # "성인" 탭 버튼 요소 클릭
        adult_tab_button = page.locator("button.tab__9c31y:has-text('성인')")
        adult_tab_button.first.click()   
        
        page.wait_for_timeout(2000)

        #성인인증 페이지 url 변수선언        
        expected_url = "https://www.lezhin.com/ko/adult?redirect=%2Fko%2Fcontent-mode%3Fpath%3D%252Fko%252Fbookshome%252Fnew-released%253Ft%253Dadult%2526order%253Dnew_last_year%26sw%3Dall"
        actual_url = page.url

        if actual_url == expected_url:
                print(f"✅ redirect URL이 포함된 성인인증 페이지로 이동되었습니다.: {actual_url}")
        else:
                raise AssertionError(f"❌ 현재 페이지 URL 불일치!\n기대값: {expected_url}\n실제값: {actual_url}")
       
        page.close() 
        

def test_new_Comic_05_adult_login (page: Page):
        """해당 코드는 성인계정 로그인 + 19OFF 상태에서 신규만화 더보기 > 성인탭 선택시 19ON 처리 및 성인작품 노출을 확인합니다."""
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 페이지 접근
        page.goto("https://www.lezhin.com/ko/bookshome/new-released?t=all&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
        
        # 19 off 실행
        button_selector = 'button.toggleContentMode__btn__99VKl.toggleContentMode__btn--on__2OQ_F'
        page.wait_for_selector(button_selector, state='visible', timeout=3000)
        page.click(button_selector)
        
        page.wait_for_timeout(2000)

        
        # "성인" 탭 버튼 요소 클릭
        adult_tab_button = page.locator("button.tab__9c31y:has-text('성인')")
        adult_tab_button.first.click()   
        
        page.wait_for_timeout(2000)

        # 19 On/Off 토글 버튼 선택자 지정
        toggle_button = page.locator("button.toggleContentMode__btn__99VKl.toggleContentMode__btn--on__2OQ_F")

        # 19on 상태변경 검증
        if toggle_button.count() > 0 and toggle_button.first.is_visible():
                print("✅ 19On 상태로 정상 변경되었습니다.")
        else:
                raise AssertionError("❌ '19On 상태로 변경되지 않았습니다.")
        
                # vy__thumbnail vy__thumbnail--tall 요소 모두 가져오기
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")
        
        page.wait_for_timeout(1000)

        all_adult_badge = True

        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if not badge:
                all_adult_badge = False
                break  # 성인 뱃지가 없는 썸네일 발견 시 바로 실패 처리

        # 검증
        if all_adult_badge:
                print("✅ 모든 작품이 성인작품입니다.")
        else:
                raise AssertionError("❌ 비성인작품이 노출됩니다.")
       
        page.close() 

      

def test_new_Comic_06_top_move(page: Page):
        """해당 코드는 신규 만화 더보기 페이지 탭 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # 신규 만화 더보기 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/bookshome/new-released?t=all&order=new_last_year')


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
        top_button = page.query_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY')

        # '맨 위로' 버튼이 보이지 않는지 검증
        if top_button is None or not top_button.is_visible():
                print("✅ 탑이동 버튼이 정상적으로 사라졌습니다!", top_button)
        else:
                raise AssertionError("❌ '맨 위로' 버튼이 아직 화면에 표시되고 있습니다!")
     
        # 페이지 종료
        page.close()
        
        
