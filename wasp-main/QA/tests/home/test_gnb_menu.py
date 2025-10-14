from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_gnbmenu_01_adult_Certified(page: Page):
        """해당 코드는 레진 성인19 비성인계정으로 접근시 성인인증페이지 이동을 확인합니다"""

        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("squad_115@yopmail.com")
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
        page.goto("https://q-www.lezhin.com/ko/nsfw")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
        
        #성인인증 페이지 url 변수선언        
        expected_url = "https://q-www.lezhin.com/ko/adult?redirect=%2Fko%2Fcontent-mode%3Fpath%3D%252Fko%252Fnsfw%26sw%3Dall"
        actual_url = page.url

        if actual_url == expected_url:
                print(f"✅ 현재 페이지 URL이 예상과 일치합니다: {actual_url}")
        else:
                raise AssertionError(f"❌ 현재 페이지 URL 불일치!\n기대값: {expected_url}\n실제값: {actual_url}")

        page.close() 
        

def test_gnbmenu_02_adultaccount_19on(page: Page):
        """해당 코드는 19OFF 상태에서 성인계정으로 성인19 메뉴 진입시 정상진입과 19ON처리를 확인합니다"""
        
        # 레진코믹스 로그인페이지 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        # 19 off 실행
        button_selector = 'button.toggleContentMode__btn__99VKl.toggleContentMode__btn--on__2OQ_F'
        page.wait_for_selector(button_selector, state='visible', timeout=3000)
        page.click(button_selector)
        
        page.wait_for_timeout(2000)
        
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1500)
        
        # 대상 요소 선택
        adult_menu_link = page.locator('a.navMenu__menuListLink__SV6Kw.isAdult')

        if adult_menu_link.count() > 0:
                # href 속성 추출
                expected_path = adult_menu_link.first.get_attribute("href")
                
                # 클릭
                adult_menu_link.first.click()

                # 페이지 로딩 대기
                page.wait_for_load_state("load")
                page.wait_for_timeout(1000)

                # 현재 URL의 path 부분 추출
                actual_path = urlparse(page.url).path

                # 경로 비교
                if actual_path == expected_path:
                        print(f"✅ 이동한 경로가 일치합니다: {actual_path}")
                else:
                        raise AssertionError(f"❌ 경로가 일치하지 않습니다. expected: {expected_path}, actual: {actual_path}")
        else:
                raise AssertionError("❌ '성인19' 메뉴 링크를 찾을 수 없습니다.")
        

        page.wait_for_timeout(1500)
        # 19 On/Off 토글 버튼 선택자 지정
        toggle_button = page.locator("button.toggleContentMode__btn__99VKl.toggleContentMode__btn--on__2OQ_F")

        # 노출 여부 검증
        if toggle_button.count() > 0 and toggle_button.first.is_visible():
                print("✅ 19On 상태로 정상 변경되었습니다.")
        else:
                raise AssertionError("❌ '19On 상태로 변경되지 않았습니다.")

        page.close() 

def test_gnbmenu_03_adultComic(page: Page):
        """해당 코드는 성인계정으로 성인19 메뉴 진입시 성인작품 노출을 확인합니다."""
        
        # 레진코믹스 로그인페이지 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        # 대상 요소 선택
        adult_menu_link = page.locator('a.navMenu__menuListLink__SV6Kw.isAdult')       
        # 19+ 선택클릭
        adult_menu_link.first.click()
        
        page.wait_for_timeout(1500)

        # vy__thumbnail vy__thumbnail--tall 요소 모두 가져오기
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")

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
        

def test_gnbmenu_04_genreplus(page: Page):
        """해당 코드는 장르+ 페이지 진입시 정상 진입여부를 확인합니다."""
        
        # 레진코믹스 로그인페이지 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        
        # 대상 요소 선택
        genreplus_link = page.locator('a.navMenu__menuListLink__SV6Kw[href="/ko/genreplus"]')
        href_path = genreplus_link.get_attribute("href")     
        # 19+ 선택클릭
        genreplus_link.first.click()
        
        page.wait_for_timeout(1500)
        
        current_path = urlparse(page.url).path

        # 검증
        if href_path == current_path:
                print(f"✅ 경로 일치 확인 성공: {current_path}")
        else:
                raise AssertionError(f"❌ 경로 불일치 - 기대값: {href_path}, 실제값: {current_path}")


        page.close() 
        

def test_gnbmenu_05_genreplus_genrelist(page: Page):
        """해당 코드는 장르+ 페이지의 장르리스트가 정상 노출되는지 확인합니다."""
        
        # API 응답 인터셉트 핸들러
        api_genre_labels = []
        def handle_response(response):
                if "genres/filtered" in response.url:
                        try:
                                json_data = response.json()

                                # 리스트 형태가 아닐 경우 무시
                                if not isinstance(json_data, list):
                                        print(f"⚠️ 예외: 예상치 못한 응답 형식(type={type(json_data)}), 무시됨.")
                                        return

                                for item in json_data:
                                        label = item.get("label")
                                        if label:
                                                api_genre_labels.append(label.strip())

                        except Exception as e:
                                print(f"⚠️ 응답 파싱 중 오류 발생(무시됨): {e}")

        # 응답 핸들러 등록
        page.on("response", handle_response)
        
        # 레진코믹스 로그인페이지 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        
        # 대상 요소 선택
        genreplus_link = page.locator('a.navMenu__menuListLink__SV6Kw[href="/ko/genreplus"]')
        # 장르+ 클릭
        genreplus_link.first.click()
        
        page.wait_for_timeout(1500)
        
        # 장르버튼 텍스트 수집
        tab_buttons = page.locator(".tabs--round__OGX_0.tabs--isSticky__CTBSU button")
        dom_labels = [tab_buttons.nth(i).inner_text().strip() for i in range(tab_buttons.count())]

        
        # 검증
        missing_labels = [label for label in api_genre_labels if label not in dom_labels]

        if missing_labels:
                raise AssertionError(f"❌ 응답된 장르리스트 API와 노출 장르가 다릅니다.: {missing_labels}")
        else:
                print("✅ 모든 API label이 장르 탭에 정상적으로 노출됨")


        page.close() 
          
          

def test_gnbmenu_06_top_move(page: Page):
        """해당 코드는 장르+ 페이지 탭 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # KR 오리지널 완결 탭 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/genreplus')


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
        
        
