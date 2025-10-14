from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse
from urllib.parse import urlparse, parse_qs, urlencode


def test_home_001_search_button_view_ko(page: Page):
        """해당 코드는 레진 KR 홈에 접속하여 검색 버튼 요소가 노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 요소 찾기
        search_button = page.wait_for_selector('button[aria-controls="search-container"]', timeout=2000)

        # 검색 버튼의 클래스명 가져와서 변수에 저장
        class_name = search_button.get_attribute("class")

        # 결과 출력
        print("검색 버튼의 클래스명:", class_name)
        
        # 검색 버튼 클래스 명 검증할 기대값 설정
        expected_class_name = "supportsItem__searchLottie__XwGED lzLottie__xFJEs"

        # 검증
        if class_name == expected_class_name:
                print("✅ KR 홈 > 검색 버튼이 노출됩니다.")
        else:
                print(f"❌ 클래스명이 일치하지 않습니다! (현재: {class_name})")
                raise AssertionError("클래스명이 기대값과 다릅니다.")

        # 페이지 종료
        page.close()
          
        
        
def test_home_002_search_button_view_en(page: Page):
        """해당 코드는 레진 us 홈에 접속하여 검색 버튼 요소가 노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')

               # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)

        # 검색 버튼 요소 찾기
        search_button = page.wait_for_selector('button[aria-controls="search-container"]', timeout=2000)

        # 검색 버튼의 클래스명 가져와서 변수에 저장
        class_name = search_button.get_attribute("class")

        # 결과 출력
        print("검색 버튼의 클래스명:", class_name)
        
        # 검색 버튼 클래스 명 검증할 기대값 설정
        expected_class_name = "supportsItem__searchLottie__XwGED lzLottie__xFJEs"

        # 검증
        if class_name == expected_class_name:
                print("✅ KR 홈 > 검색 버튼이 노출됩니다.")
        else:
                print(f"❌ 클래스명이 일치하지 않습니다! (현재: {class_name})")
                raise AssertionError("클래스명이 기대값과 다릅니다.")

        # 페이지 종료
        page.close()
        
        
def test_home_003_search_button_placeholder_ko(page: Page):
        """해당 코드는 레진 KR 홈에 접속하여 검색버튼을 클릭하고 노출되는 placeholder 텍스트를 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # Placeholder 버튼 요소 찾기
        Placeholder = page.wait_for_selector('input.searchInput__input__991FM', timeout=2000)

        # 검색 버튼의 클래스명 가져와서 변수에 저장
        class_name = Placeholder.get_attribute("placeholder")

        # 결과 출력
        print("검색 버튼의 클래스명:", class_name)
        
        # 검색 버튼 클래스 명 검증할 기대값 설정
        expected_class_name = "작품, 작가, 출판사, 태그 검색"

        # 클래스명 검증
        if class_name == expected_class_name:
                print("✅ KR 검색 미리보기 Placeholder 버튼이 정상 노출됩니다.")
        else:
                print(f"❌ 노출 텍스트가 일치하지 않습니다! (현재: {class_name})")
                raise AssertionError("클래스명이 기대값과 다릅니다.")

        # 페이지 종료
        page.close()
        
        

def test_home_004_search_button_placeholder_en(page: Page):
        """해당 코드는 레진 US 홈에 접속하여 검색버튼을 클릭하고 노출되는 placeholder 텍스트를 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

         # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')
        
        # 1초 대기
        page.wait_for_timeout(1000)

        # Placeholder 버튼 요소 찾기
        Placeholder = page.wait_for_selector('input.searchInput__input__991FM', timeout=2000)

        # 검색 버튼의 클래스명 가져와서 변수에 저장
        class_name = Placeholder.get_attribute("placeholder")

        # 결과 출력
        print("검색 버튼의 클래스명:", class_name)
        
        # 검색 버튼 클래스 명 검증할 기대값 설정
        expected_class_name = "Type to begin searching"

        # 클래스명 검증
        if class_name == expected_class_name:
                print("✅ KR 검색 미리보기 Placeholder 버튼이 정상 노출됩니다.")
        else:
                print(f"❌ 노출 텍스트가 일치하지 않습니다! (현재: {class_name})")
                raise AssertionError("클래스명이 기대값과 다릅니다.")

        # 페이지 종료
        page.close()         
        
def test_home_005_search_close_ko(page: Page):
        """해당 코드는 KR 로케일에서 검색 닫기 버튼을 클릭했을때 닫힘 버튼이 정상 클릭되는것을 확인합니다.."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')
        
        # 닫기 버튼 클릭
        page.click('button.searchClose__fRxFW')
        
        # 요소가 존재하는지 확인 (없어야 정상)
        container = page.query_selector('div.container__vu193.container--isShow__uj5nI')

        # `assert`를 활용하여 검색미리보기가 노출되지 않는지 검증
        if container is None:
                print("✅ 검색 미리보기 창이 정상적으로 닫혔습니다.")
        else:
                print("❌ 검색 미리보기 창이 닫히지 않았습니다. 재확인 필요!")
                raise AssertionError("검색 미리보기 창 비노출 검증 실패")
     

        # 페이지 종료
        page.close()
        

def test_home_006_search_close_en(page: Page):
        """해당 코드는 US 로케일에서 검색 닫기 버튼을 클릭했을때 닫힘 버튼이 정상 클릭되는것을 확인합니다.."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')
        
        # 닫기 버튼 클릭
        page.click('button.searchClose__fRxFW')
        
        # 요소가 존재하는지 확인 (없어야 정상)
        container = page.query_selector('div.container__vu193.container--isShow__uj5nI')

        # `assert`를 활용하여 검색미리보기가 노출되지 않는지 검증
        if container is None:
                print("✅ 검색 미리보기 창이 정상적으로 닫혔습니다.")
        else:
                print("❌ 검색 미리보기 창이 닫히지 않았습니다. 재확인 필요!")
                raise AssertionError("검색 미리보기 창 비노출 검증 실패")

        # 페이지 종료
        page.close()          
        
def test_home_007_lezhin_comic_scheduled_ko(page: Page):
        """해당 코드는 KR 로케일에서 레진 신작 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 레진 신작 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#comic_scheduled_latest_k', timeout=2000)
        

        # id 속성값 가져와서 변수에 저장
        section_id = section.get_attribute("id")

        # 레진신작 영역이 존재하는지 검증
        if section is not None:
                print("section :", section_id)
                print("✅ KR `레진 신작` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ KR 레진신작 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("KR 레진신작 영역 비노출")
     
        # 페이지 종료
        page.close()     
         
        
def test_home_008_lezhin_comic_scheduled_en(page: Page):
        """해당 코드는 US 로케일에서 레진 신작 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        page.get_by_role("button", name="Accept All", exact=True).click(timeout=3000)
        
        # 레진 신작 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#comic_scheduled_latest_k', timeout=2000)
        

        # id 속성값 가져와서 변수에 저장
        section_id = section.get_attribute("id")

        # 레진신작 영역이 존재하는지 검증
        if section is not None:
                print("section :", section_id)
                print("✅ KR `레진 신작` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ KR 레진신작 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("KR 레진신작 영역 비노출")
     
        # 페이지 종료
        page.close()  
        
def test_home_009_lezhin_comic_new_ko(page: Page):
        """해당 코드는 KO 로케일에서 신규만화 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 레진 신작 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#comic_new_k', timeout=2000)
        

        # id 속성값 가져와서 변수에 저장
        section_id = section.get_attribute("id")

        # 신작만화 영역이 존재하는지 확인
        if section is not None:
                print("section :", section_id)
                print("✅ KR `신작 만화` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ `신작만화` 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("KR 신작만화 영역 비노출")
     
        # 페이지 종료
        page.close()     
         
        
def test_home_010_lezhin_home_subscription_ko(page: Page):
        """해당 코드는 KR 로케일에서 업데이트 된 찜한 작품 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 업데이트된 찜한작품 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#order_up_subscription', timeout=2000)
        

        # id 속성값 가져와서 변수에 저장
        section_id = section.get_attribute("id")

        # 업데이트된 찜한 작품 영역이 존재하는지 확인
        if section is not None:
                print("section :", section_id)
                print("✅ KR `업데이트된 찜한 작품` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 업데이트된 찜한 작품 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("KR 업데이트된 찜한 작품 영역 비노출")
     
        # 페이지 종료
        page.close()  
        
def test_home_011_lezhin_home_subscription_en(page: Page):
        """해당 코드는 US 로케일에서 업데이트 된 찜한 작품 영역이 노출되는것을 확인합니다. 
        US 리얼은 현재 업데이트된 찜한 작품 영역 운영하지 않음 따라서 QA서버로 대체"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/login')


        # 쿠키 이용 동의 'Accept All' 클릭
        page.wait_for_selector('button:has-text("Accept All")', state='visible', timeout=3000)
        page.click('button:has-text("Accept All")')

        
        ## 리액트 대응 버전 로그인
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 업데이트된 찜한작품 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#order_up_subscription', timeout=2000)
        

        # id 속성값 가져와서 변수에 저장
        section_id = section.get_attribute("id")

        # 업데이트된 찜한 작품 영역이 존재하는지 확인
        if section is not None:
                print("section :", section_id)
                print("✅ US `업데이트된 찜한 작품` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 업데이트된 찜한 작품 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("US 업데이트된 찜한 작품 영역 비노출")
     
        # 페이지 종료
        page.close() 
        
def test_home_012_lezhin_home_recent_ko(page: Page):
        """해당 코드는 KR 로케일에서 최근 본 작품 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 최근 본 작품 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#order_recent', timeout=2000)
        

        # id 속성값 가져와서 변수에 저장
        section_id = section.get_attribute("id")

        # 최근 본 작품 영역이 존재하는지 확인
        if section is not None:
                print("section :", section_id)
                print("✅ KR `최근 본작품` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 최근 본 작품 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("KR 최근 본 작품 영역 비노출")
     
        # 페이지 종료
        page.close()  
        
def test_home_013_lezhin_home_recent_en(page: Page):
        """해당 코드는 US 로케일에서 최근 본 작품 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/login')


        # 쿠키 이용 동의 'Accept All' 클릭
        page.wait_for_selector('button:has-text("Accept All")', state='visible', timeout=3000)
        page.click('button:has-text("Accept All")')
   

        # 리액트 버전 적용전 로그인
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 최근 본 작품 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#order_recent', timeout=2000)
        

        # id 속성값 가져와서 변수에 저장
        section_id = section.get_attribute("id")

        # 최근 본 작품 영역이 존재하는지 확인
        if section is not None:
                print("section :", section_id)
                print("✅ US `최근 본작품` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 최근 본 작품 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("US 최근 본 작품 영역 비노출")
     
        # 페이지 종료
        page.close() 

def test_home_014_lezhin_home_Top_move_button_ko(page: Page):
        """해당 코드는 KR 로케일에서 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
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
                print("❌ 탑 이동 버튼이 노출되지 않습니다.")
                raise AssertionError("탑 이동 버튼이 노출되지 않음")
        
        # 버튼 클릭
        top_button.click()
        
        # 현재 스크롤 위치 가져오기
        scroll_position = page.evaluate("window.scrollY")

        # 스크롤 위치가 Y축 최상단 중 1에 가까운지 검증
        if scroll_position <= 1:
                print("✅ 현재 스크롤 위치는 맨 위입니다!", "window.scrollY :", scroll_position)
        else:
                print(f"❌ 현재 스크롤 위치는 맨 위가 아닙니다! (현재 위치: {scroll_position}px)")
                raise AssertionError(f"현재 스크롤 위치는 맨 위가 아님 (현재 위치: {scroll_position}px)")
        
        # 탑이동 버튼이 존재하는지 확인 (없으면 None 반환)
        top_button = page.query_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY')

        # 버튼이 존재하지 않거나, 화면에 보이지 않는지 검증
        if top_button is None or not top_button.is_visible():
                print("✅ 탑이동 버튼이 정상적으로 사라졌습니다!", top_button)
        else:
                print("❌ '맨 위로' 버튼이 아직 화면에 표시되고 있습니다!", top_button)
                raise AssertionError("'맨 위로' 버튼이 아직 화면에 표시되고 있습니다!")
     
        # 페이지 종료
        page.close()  

def test_home_015_lezhin_home_Top_move_button_en(page: Page):
        """해당 코드는 US 로케일에서 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
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
                print("❌ 탑 이동 버튼이 노출되지 않습니다.")
                raise AssertionError("탑 이동 버튼이 노출되지 않음")
        
        # 버튼 클릭
        top_button.click()
        
        # 현재 스크롤 위치 가져오기
        scroll_position = page.evaluate("window.scrollY")

        # 스크롤 위치가 Y축 최상단 중 1에 가까운지 검증
        if scroll_position <= 1:
                print("✅ 현재 스크롤 위치는 맨 위입니다!", "window.scrollY :", scroll_position)
        else:
                print(f"❌ 현재 스크롤 위치는 맨 위가 아닙니다! (현재 위치: {scroll_position}px)")
                raise AssertionError(f"현재 스크롤 위치는 맨 위가 아님 (현재 위치: {scroll_position}px)")
        
        # 탑이동 버튼이 존재하는지 확인 (없으면 None 반환)
        top_button = page.query_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY')

        # 버튼이 존재하지 않거나, 화면에 보이지 않는지 검증
        if top_button is None or not top_button.is_visible():
                print("✅ 탑이동 버튼이 정상적으로 사라졌습니다!", top_button)
        else:
                print("❌ '맨 위로' 버튼이 아직 화면에 표시되고 있습니다!", top_button)
                raise AssertionError("'맨 위로' 버튼이 아직 화면에 표시되고 있습니다!")     
     
        # 페이지 종료
        page.close()  

def test_home_016_lezhin_home_frontbanner_ko(page: Page):
        """해당 코드는 KR 로케일에서 전면배너 영역이 노출되는것을 확인합니다. 
        리얼은 전면배너 영역 노출이 불규칙하므로  QA서버로 대체"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너(dialog)가 있는지 확인 (최대 2초 대기)
        banner = page.wait_for_selector("dialog.frontBanner__uoT0X[open]", timeout=2000)
            

        # class 속성값 가져와서 변수에 저장
        banner_class = banner.get_attribute("class")
        
        # banner_class 값이 "frontBanner__uoT0X"인지 검증
        if banner_class == "frontBanner__uoT0X":
                print("banner_class :", banner_class)
                print("✅ KR 전면배너가 정상 노출 됩니다.!")
        else:
                print(f"❌ 검증 실패! 현재 banner_class 값: {banner_class}")
                raise AssertionError(f"검증 실패! 현재 banner_class 값: {banner_class}")
        
        # 페이지 종료
        page.close() 
        
def test_home_017_lezhin_home_frontbanner_re_visible_ko(page: Page):
        """해당 코드는 KR 로케일에서 페이지 새로고침시 같은 전면배너가 다시 노출되는것을 확인합니다.  
        리얼은 전면배너 영역 노출이 불규칙하므로  QA서버로 대체"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너(dialog)가 있는지 확인 (최대 2초 대기)
        img_element  = page.wait_for_selector("dialog.frontBanner__uoT0X[open] img", timeout=2000)
            
        # class 속성값 가져와서 변수에 저장
        image_url  = img_element.get_attribute("src")
        
        page.reload()
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 배너(dialog)가 있는지 확인 (최대 2초 대기)
        img_element_2  = page.wait_for_selector("dialog.frontBanner__uoT0X[open] img", timeout=2000)
            
        # class 속성값 가져와서 변수에 저장
        image_url_2  = img_element_2.get_attribute("src")
        
        # image_url 과 image_url_2에 저장된 이미지 url 값이 동일한지 검증
        if image_url == image_url_2:
                print("최초 진입시 전면배너의 이미지 URL(", image_url, ")") 
                print("페이지 새로고침하여 다시 배너 노출시도한 전면배너의 이미지 URL(", image_url_2, ")")     
                print("✅ 같은 전면배너가 노출됩니다.")
        else:
                print(f"❌ 다른 전면배너가 노출됩니다. (이전: {image_url}, 새로고침 후: {image_url_2})")
                raise AssertionError(f"다른 전면배너가 노출됩니다. (이전: {image_url}, 새로고침 후: {image_url_2})")   
     
        # 페이지 종료
        page.close() 
        
def test_home_018_lezhin_home_frontbanner_click(page: Page):
        """해당 코드는 KR 로케일에서  전면배너를 클릭했을떄 이동한 URL을 검증합니다.  
        리얼은 전면배너 영역 노출이 불규칙하므로  QA서버로 대체"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        
        ## 리액트 대응 버전 로그인
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

        # 배너(dialog)가 있는지 확인 (최대 2초 대기)
        front_banner  = page.wait_for_selector("dialog.frontBanner__uoT0X[open] a", timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = front_banner.get_attribute("href")
        
        #전면배너 클릭
        front_banner.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
        # 현재 페이지 URL 가져오기
        current_url = page.url

        # 요소에서 추출한 target_url과 실제 이동한 페이지 current_url 을 비교
        if current_url == target_url:
                print("✅ 배너에 설정된 전면배너 URL로 정상이동하였습니다. (", current_url, ")")
        else:
                print(f"❌ 전면배너의 링크 URL이 정상이동하지 않았습니다. (현재: {current_url}, 기대값: {target_url})")
                raise AssertionError(f"전면배너의 링크 URL이 정상이동하지 않았습니다. (현재: {current_url}, 기대값: {target_url})")
     
        # 페이지 종료
        page.close() 
        
def test_home_019_lezhin_home_top_banner_ko(page: Page):
        """해당 코드는 KR 로케일에서 탑배너 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 탑 배너 요소 찾기
        top_banner = page.wait_for_selector("div.topBanner__qxAxf", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        class_id = top_banner.get_attribute("class")

        # 업데이트된 찜한 작품 영역이 존재하는지 확인
        if class_id is not None:
                print(" 탑배너 class : ", class_id)
                print("✅ KR `탑배너` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 탑배너 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("❌ 탑배너 영역이 정상적으로 노출되지 않았습니다.")
     
        # 페이지 종료
        page.close()  
        
def test_home_020_lezhin_home_top_banner_en(page: Page):
        """해당 코드는 US 로케일에서 탑배너 영역이 노출되는것을 확인합니다. """

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/login')


        # 쿠키 이용 동의 'Accept All' 클릭
        page.wait_for_selector('button:has-text("Accept All")', state='visible', timeout=3000)
        page.click('button:has-text("Accept All")')

        
        ## 리액트 대응 버전 로그인
        # 이메일 입력
        page.wait_for_selector('input[name="email"]', state='visible', timeout=3000)
        page.fill('input[name="email"]', 'squad@lezhin.com')

        # 비밀번호 입력
        page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        page.fill('input[name="password"]', 'wlscogus7!')

        # 로그인 버튼 클릭
        page.click('button:has-text("Login with email")')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 탑배너 요소 찾기
        top_banner = page.wait_for_selector("div.topBanner__qxAxf", timeout=5000)

        # class 속성값 가져와서 변수에 저장
        class_id = top_banner.get_attribute("class")

        # `assert`를 사용하여 업데이트된 찜한 작품 영역이 존재하는지 확인
        if class_id is not None:
                print(" 탑배너 class : ", class_id)
                print("✅ KR `탑배너` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 탑배너 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("❌ 탑배너 영역이 정상적으로 노출되지 않았습니다.")
     
        # 페이지 종료
        page.close()  
        

def test_home_021_lezhin_home_realtime_rank_ko(page: Page):
        """해당 코드는 KR 로케일에서 실시간랭킹 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 탑 배너 요소 찾기
        realtime_rank = page.wait_for_selector("section#concept_ranking", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        realtime_id = realtime_rank.get_attribute("id")

        # 실시간 랭킹 영역이 존재하는지 확인
        if realtime_id is not None:
                print(" 실시간 랭킹 id : ", realtime_id)
                print("✅ KR `실시간 랭킹` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 실시간 랭킹 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("❌ 실시간 랭킹 영역이 정상적으로 노출되지 않았습니다.")
        
        # 페이지 종료
        page.close()

def test_home_022_lezhin_home_realtime_rank_en(page: Page):
        """해당 코드는 US 로케일에서 실시간랭킹 영역이 노출되는것을 확인합니다."""

        # 레진코믹스  페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 실시간 랭킹  요소 찾기
        realtime_rank = page.wait_for_selector("section#concept_ranking", timeout=5000)

        # class 속성값 가져와서 변수에 저장
        realtime_id = realtime_rank.get_attribute("id")

        # 실시간 랭킹 영역이 존재하는지 확인
        if realtime_id is not None:
                print(" 실시간 랭킹 id : ", realtime_id)
                print("✅ KR `실시간 랭킹` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ 실시간 랭킹 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("❌ 실시간 랭킹 영역이 정상적으로 노출되지 않았습니다.")
     
        # 페이지 종료
        page.close()  


def test_home_023_lezhin_home_home_realtime_rank_more_ko(page: Page):
        """해당 코드는 KR 로케일에서 실시간 랭킹 더보기 버튼을 클릭했을때 동작입니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너(dialog)가 있는지 확인 (최대 2초 대기)
        front_banner  = page.wait_for_selector("section#concept_ranking a", timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = front_banner.get_attribute("href")
        
        #전면배너 클릭
        front_banner.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
        # 현재 페이지 URL 가져오기
        current_url = page.url

        # URL에서 www.lezhinus.com/en 도메인 제거하고 변수에 저장
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # 실시간 랭킹 더보기 URL 이동 검증
        if current_path == target_path:
                print("✅ KR 실시간 랭킹 더보기 URL 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ KR 실시간 랭킹 더보기 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 이동 검증 실패")
     
        # 페이지 종료
        page.close()  
        
def test_home_024_lezhin_home_home_realtime_rank_more_en(page: Page):
        """해당 코드는 KR 로케일에서 실시간 랭킹 더보기 버튼을 클릭했을때 동작입니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC')


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너(dialog)가 있는지 확인 (최대 2초 대기)
        front_banner  = page.wait_for_selector("section#concept_ranking a", timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = front_banner.get_attribute("href")
        
        #전면배너 클릭
        front_banner.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
        # 현재 페이지 URL 가져오기
        current_url = page.url

        # URL에서 www.lezhinus.com/en 도메인 제거하고 변수에 저장
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # 실시간 랭킹 더보기 URL 이동 검증
        if current_path == target_path:
                print("✅ KR 실시간 랭킹 더보기 URL 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ KR 실시간 랭킹 더보기 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 이동 검증 실패")
     
        # 페이지 종료
        page.close()              

def test_home_025_lezhin_home_comic_scheduled_ko_more(page: Page):
        """해당 코드는 KR 로케일에서  레진 신작 더보기 버튼을 클릭했을때 동작을 검증합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # "레진 신작 더보기" 링크 요소 찾기
        more_url = page.wait_for_selector('a.vx__detailLink[href="/ko/scheduled/new-released"]', timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = more_url.get_attribute("href")
        
        #레진신작 더보기 클릭
        more_url.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
         # URL에서 www.lezhin.com 도메인 제거하고 변수에 저장
        parsed_url = urlparse(target_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # KR 레진신작 더보기 URL 이동 검증
        if current_path == target_path:
                print("✅ KR 레진신작 더보기 URL 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ KR 레진 신작 더보기 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 이동 검증 실패")
     
        # 페이지 종료
        page.close()

def test_home_026_lezhin_home_comic_scheduled_en_more(page: Page):
        """해당 코드는 US 로케일에서  레진 신작 더보기 버튼을 클릭했을때 동작을 검증합니다."""

        # 레진코믹스  페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)

        # "레진 신작 더보기" 링크 요소 찾기
        more_url = page.wait_for_selector('a.vx__detailLink[href="/en/daily/new-released"]', timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = more_url.get_attribute("href")
        
        #레진신작 더보기 클릭
        more_url.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
         # URL에서 www.lezhinus.com 도메인 제거하고 변수에 저장
        parsed_url = urlparse(target_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # KR 레진신작 더보기 URL 이동 검증
        if current_path == target_path:
                print("✅ KR 레진신작 더보기 URL 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ KR 레진 신작 더보기 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 이동 검증 실패")
     
        # 페이지 종료
        page.close()                            

def test_home_027_lezhin_home_calandar_ko_more(page: Page):
        """해당 코드는 KR 로케일에서  신작캘린더 더보기 버튼을 클릭했을때 동작을 검증합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # "신작캘린더" 링크 요소 찾기
        more_url = page.wait_for_selector('a.vx__calendarLink[href="/ko/calendar"]', timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = more_url.get_attribute("href")
        
        #신작캘린더 더보기 클릭
        more_url.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
         # URL에서 www.lezhin.com 도메인 제거하고 변수에 저장
        parsed_url = urlparse(target_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # KR 신작캘린더 URL 이동 검증
        if current_path == target_path:
                print("✅ KR 신작캘린더 URL 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ KR 신작캘린더 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 이동 검증 실패")
     
        # 페이지 종료
        page.close()

def test_home_028_lezhin_home_calandar_en_more(page: Page):
        """해당 코드는 US 로케일에서  신작캘린더 버튼을 클릭했을때 동작을 검증합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)

        # "신작캘린더" 링크 요소 찾기
        more_url = page.wait_for_selector('a.vx__calendarLink[href="/en/calendar"]', timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = more_url.get_attribute("href")
        
        #신작캘린더 더보기 클릭
        more_url.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
         # URL에서 www.lezhin.com 도메인 제거하고 변수에 저장
        parsed_url = urlparse(target_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # US 신작캘린더 URL 이동 검증
        if current_path == target_path:
                print("✅ US 신작캘린더 URL 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ US 신작캘린더 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 이동 검증 실패")
     
        # 페이지 종료
        page.close()
        

def test_home_029_lezhin_home_comic_more_ko(page: Page):
        """해당 코드는 KR 로케일에서  신규만화 더보기 버튼을 클릭했을때 페이지 동작을 검증합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # "신작캘린더" 링크 요소 찾기
        more_url = page.wait_for_selector('a.vx__detailLink[href="/ko/bookshome/new-released"]', timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url  = more_url.get_attribute("href")
        
        #신작캘린더 더보기 클릭
        more_url.click()    
        
        # 4초 대기
        page.wait_for_timeout(4000)
        
         # URL에서 www.lezhin.com 도메인 제거하고 변수에 저장
        parsed_url = urlparse(target_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # KR 신규만화 더보기 URL 이동 검증
        if current_path == target_path:
                print("✅ KR 신규만화 더보기 URL 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ KR 신규만화 더보기 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 이동 검증 실패")
     
        # 페이지 종료
        page.close()

def test_home_030_lezhin_home_subscription_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 업데이트 된 찜한 작품을 클릭하고 페이지 이동을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 업데이트된 찜한작품 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#order_up_subscription', timeout=2000)
        
        #업데이트 된 찜한 작품에 클릭할 작품이 노출 확인
        selector = 'a.vx__link[href="/ko/comic/changed_brother"]'
        
        element = page.wait_for_selector(selector, timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url = element.get_attribute("href")

        # `업데이트된 찜한 작품`의 작품이 정상적으로 노출되었는지 확인
        if selector is not None:
                print("section : ", selector)
                print("✅ KR `업데이트된 찜한 작품`의 작품이 정상적으로 노출되었습니다!")
        else:
                print("❌ 해당 작품이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("❌ 작품 노출 검증 실패")
        
        # 작품 클릭 하여 에피소드 목록으로 이동
        link = page.wait_for_selector(selector, timeout=3000)
        link.click()
        
        # 2초 대기
        page.wait_for_timeout(2000)
     
        # 현재 페이지 URL 가져오기
        current_url = page.url

        # URL에서 www.lezhinus.com/en 도메인 제거하고 변수에 저장
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # 업데이트된 찜한작품 클릭 후 URL 비교
        if current_path == target_path:
                print("✅ 업데이트된 찜한작품 작품 클릭시 페이지이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ 업데이트된 찜한작품 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ 페이지 이동 URL 불일치")
     
     
        # 페이지 종료
        page.close()  


def test_home_031_lezhin_home_subscription_more_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 업데이트 된 찜한 작품 더보기 클릭하고 페이지 이동을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 업데이트된 찜한작품 `section` 요소가 정상적으로 로드될 때까지 대기
        section = page.wait_for_selector('section#order_up_subscription', timeout=2000)
        
        #업데이트 된 찜한 작품에 클릭할 더보기 버튼 노출 확인
        selector = 'a.vx__detailLink[href="/ko/library#subscription"]'
        
        element = page.wait_for_selector(selector, timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url = element.get_attribute("href")

        # 내서재 > 찜한 작품 영역 존재 여부 확인
        if selector is not None:
                print("section : ", selector)
                print("✅ KR `내서재 > 찜한 작품` 영역으로 이동하였습니다.")
        else:
                print("❌ 내서재 > 찜한 작품 영역으로 이동하지 않았습니다.")
                raise AssertionError("❌ 해당 영역이 존재하지 않습니다.")
        
        # 작품 클릭 하여 에피소드 목록으로 이동
        link = page.wait_for_selector(selector, timeout=3000)
        link.click()
        
        # 2초 대기
        page.wait_for_timeout(2000)
     
        # 현재 페이지 URL 가져오기
        current_url = page.url

        # URL에서 www.lezhinus.com/en 도메인 제거하고 변수에 저장
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # 업데이트된 찜한작품 더보기 URL 비교
        if current_path == target_path:
                print("✅ 업데이트된 찜한작품 더보기 클릭시 페이지 이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ 업데이트된 찜한작품 더보기 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ URL 경로가 일치하지 않습니다.")
     
     
        # 페이지 종료
        page.close() 
        
        
def test_home_032_lezhin_home_recents_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 최근 본 작품을 클릭하고 페이지 이동을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 이메일 입력
        page.locator("#email").fill("squad_03@yopmail.com")

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
        page.wait_for_timeout(2000)
        
        
        #최근 본 작품에 클릭할 작품이 노출 확인
        selector = 'a.vx__link[href="/ko/comic/friends_mom_is_mine"]'
        
        element = page.wait_for_selector(selector, timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url = element.get_attribute("href")

        # 최근 본 작품 영역이 존재하는지 확인
        if selector is not None:
                print("section : ", selector)
                print("✅ KR `최근 본 작품`의 작품이 정상적으로 노출되었습니다!")
        else:
                print("❌ 해당 작품이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("❌ 최근 본 작품 영역이 노출되지 않음.")
        
        # 작품 클릭 하여 에피소드 목록으로 이동
        link = page.wait_for_selector(selector, timeout=3000)
        link.click()
        
        # 2초 대기
        page.wait_for_timeout(2000)
     
        # 현재 페이지 URL 가져오기
        current_url = page.url

        # URL에서 www.lezhinus.com/en 도메인 제거하고 변수에 저장
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # 최근 본 작품 URL 이동이 기대값과 동일한지 비교
        if current_path == target_path:
                print("✅ 최근 본 작품 작품 클릭시 페이지이동이 정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ 최근 본 작품 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ 최근 본 작품 URL 이동 오류 발생.")
     
     
        # 페이지 종료
        page.close()  
        
        
def test_home_033_lezhin_home_recents_more_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 최근 본 작품 더보기 클릭하고 페이지 이동을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)

        
        #최근 본 작품에 클릭할 더보기 버튼 노출 확인
        selector = 'a.vx__detailLink[href="/ko/library#recents"]'
        
        element = page.wait_for_selector(selector, timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url = element.get_attribute("href")

        # '내서재 > 본 작품' 영역이 존재하는지 확인
        if selector is not None:
                print("section : ", selector)
                print("✅ KR `내서재 > 본 작품` 영역으로 이동하였습니다.")
        else:
                print("❌ 내서재 > 본 작품 영역으로 이동하지 않았습니다.")
                raise AssertionError("❌ 내서재 > 본 작품 영역 이동 실패.")
        
        # 더보기 클릭 하여 내서재로 이동
        link = page.wait_for_selector(selector, timeout=3000)
        link.click()
        
        # 2초 대기
        page.wait_for_timeout(2000)
     
        # 현재 페이지 URL 가져오기
        current_url = page.url

        # URL에서 www.lezhinus.com/en 도메인 제거하고 변수에 저장
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        # `target_url`에서도 도메인 제거 (만약 도메인이 포함되어 있다면)
        parsed_target_url = urlparse(target_url)
        target_path = parsed_target_url.path + ('?' + parsed_target_url.query if parsed_target_url.query else '')

        # '최근 본 작품 더보기' URL 이동이 정상적으로 이루어졌는지 비교
        if current_path == target_path:
                print("✅ 최근 본 작품 더보기 클릭시 페이지이동  정상적으로 이루어졌습니다. (", current_path, ")")
        else:
                print(f"❌ 최근 본 작품 더보기 URL 이동이 정상적이지 않습니다. (현재: {current_path}, 기대값: {target_path})")
                raise AssertionError("❌ 최근 본 작품 더보기 URL 이동 실패.")
     
     
        # 페이지 종료
        page.close()
        
        
def test_home_034_lezhin_home_lezhin_original_ko(page: Page):
        """해당 코드는 KR 로케일에서 레진 오리지널 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 레진 오리지널  요소 찾기
        element = page.wait_for_selector('div.lezhinOriginal__Cauqd', timeout=3000)
        
        # class 속성값 가져와서 변수에 저장
        class_name = element.get_attribute("class")

        # KR 레진 오리지널 영역이 정상적으로 노출되었는지 확인
        if class_name is not None:
                print(" 레진 오리지널  class  : ", class_name)
                print("✅ KR `레진 오리지널` 영역이 정상적으로 노출되었습니다!")
        else:
                print("❌ KR 레진 오리지널 영역이 정상적으로 노출되지 않았습니다.")
                raise AssertionError("❌ KR 레진 오리지널 영역이 비노출되었습니다.")
     
        # 페이지 종료
        page.close()
        
def test_home_035_lezhin_home_lezhin_original_en(page: Page):
        """해당 코드는 US 로케일에서 레진 오리지널 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 레진 오리지널  요소 찾기
        element = page.wait_for_selector('div.lezhinOriginal__Cauqd', timeout=3000)
        
        # class 속성값 가져와서 변수에 저장
        class_name = element.get_attribute("class")

        # `assert`를 사용하여 업데이트된 찜한 작품 영역이 존재하는지 확인
        assert class_name is not None, "❌ US 레진 오리지널 영역이 정상적으로 노출되지 않았습니다."

        print(" 레진 오리지널  class  : ", class_name)
        print("✅ US `레진 오리지널` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()
        
        
def test_home_036_lezhin_home_lezhin_original_more_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 레진 오리지널 더보기 클릭하고 페이지 이동을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)

        
        #레진 오리지널 클릭할 더보기 버튼 노출 확인
        selector = 'a.lezhinOriginal__detailLink__azL6q[href="/ko/scheduled?day"]'
        
        element = page.wait_for_selector(selector, timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url = element.get_attribute("href")

        # `assert`를 사용하여 오리지널 영역이 존재하는지 확인
        assert element is not None, "❌ GNB > 오리지널 영역으로 이동하지 않았습니다."

        print("section : ", selector)
        print("✅ KR GNB > 오리지널 영역으로 이동하였습니다.")
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        target_url = element.get_attribute("href")
        element.click()
        
        # 2초 대기
        page.wait_for_timeout(2000)
     
        # 현재 페이지 URL 가져오기
        current_url = page.url
        
        # 현재 URL에서 ?day=5 같은 값 제거
        current_url = page.url
        parsed = urlparse(current_url)
        if parsed.path == "/ko/scheduled" and parsed.query.startswith("day="):
                current_path = f"{parsed.path}?day"
        else:
                current_path = parsed.path + (f"?{parsed.query}" if parsed.query else "")

        # 비교
        assert current_path == target_url, f"❌ 이동 실패! (현재: {current_path}, 기대값: {target_url})"
        print("✅ 레진 오리지널 더보기 클릭 시 이동 정상 (", current_path, ")")

        page.close()
        

def test_home_037_lezhin_home_lezhin_original_more_click_en(page: Page):
        """해당 코드는 US 로케일에서 레진 오리지널 더보기 클릭하고 페이지 이동을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC')
    
        #레진 오리지널 클릭할 더보기 버튼 노출 확인
        selector = 'a.lezhinOriginal__detailLink__azL6q[href="/en/daily?day"]'
        
        element = page.wait_for_selector(selector, timeout=3000)
        
        # a href의 url을 가져와서 변수에 저장
        target_url = element.get_attribute("href")

        # `assert`를 사용하여 오리지널 영역이 존재하는지 확인
        assert element is not None, "❌ GNB > 오리지널 영역으로 이동하지 않았습니다."

        print("section : ", selector)
        print("✅ US GNB > 오리지널 영역으로 이동하였습니다.")
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        target_url = element.get_attribute("href")
        element.click()
        
        # 2초 대기
        page.wait_for_timeout(2000)
     
        # 현재 페이지 URL 가져오기
        current_url = page.url
        
        # 현재 URL에서 ?day=5 같은 값 제거
        current_url = page.url
        parsed = urlparse(current_url)
        if parsed.path == "/en/daily" and parsed.query.startswith("day="):
                current_path = f"{parsed.path}?day"
        else:
                current_path = parsed.path + (f"?{parsed.query}" if parsed.query else "")

        # 비교
        assert current_path == target_url, f"❌ 이동 실패! (현재: {current_path}, 기대값: {target_url})"
        print("✅ 레진 오리지널 더보기 클릭 시 이동 정상 (", current_path, ")")

        page.close()
        
        
def test_home_038_lezhin_home_sun1banner_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 서브배너 1클릭하고 페이지 이동을 확인합니다."""

         # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)

        # 서브배너 요소
        selector = 'a.subBanner__JIzH6'
        link = page.locator(selector).first

        # 요소 존재만 확인
        assert link.element_handle() is not None, "❌ 서브배너 요소가 존재하지 않습니다."

        # 클래스, href 저장
        class_name = link.get_attribute("class")
        target_url = link.get_attribute("href")
        print("✅ 서브배너 클래스:", class_name)
        print("➡ 이동 예정 URL:", target_url)
        
        # 2초 대기
        page.wait_for_timeout(2000)

        # 뷰포트에 보이도록 스크롤 후 클릭
        link.scroll_into_view_if_needed()
        link.click()
        page.wait_for_timeout(2000)

        # 현재 URL
        current_url = page.url
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '')

        parsed_target = urlparse(target_url)
        target_path = parsed_target.path + ('?' + parsed_target.query if parsed_target.query else '')

        assert current_path == target_path, f"❌ 페이지 이동 실패! (현재: {current_path}, 기대: {target_path})"
        print("✅ 서브배너 클릭 후 URL 이동이 정상적으로 이루어졌습니다.")
        
        # 페이지 종료
        page.close()
        
        
def test_home_039_lezhin_home_sun2banner_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 서브배너 2클릭하고 페이지 이동을 확인합니다."""

         # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)

        # 서브배너 3 (id=home_sub_3_a) 내 링크 선택
        container = page.locator('#home_sub_3_a a.subBanner__JIzH6')

        # 존재 확인
        assert container.element_handle() is not None, "❌ 서브배너 2 요소가 존재하지 않습니다."

        # 클래스명과 이동 예정 URL 가져오기
        class_name = container.get_attribute("class")
        target_url = container.get_attribute("href")
        print("✅ 서브배너 2 클래스:", class_name)
        print("➡ 이동 예정 URL:", target_url)

        # 클릭 전 뷰포트로 스크롤
        container.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        container.click()

        # 클릭 후 3초 대기
        page.wait_for_timeout(3000)

        # 현재 페이지 URL
        current_url = page.url

        # 도메인 제외한 경로+쿼리 추출
        from urllib.parse import urlparse
        parsed_current = urlparse(current_url)
        parsed_target = urlparse(target_url)

        current_path = parsed_current.path + ('?' + parsed_current.query if parsed_current.query else '')
        target_path = parsed_target.path + ('?' + parsed_target.query if parsed_target.query else '')

        # 비교
        assert current_path == target_path, f"❌ 서브배너 2 이동 실패 (현재: {current_path}, 기대값: {target_path})"
        print("✅ 서브배너 2 클릭 시 정상 이동 확인 완료")
        
        # 페이지 종료
        page.close()
        
def test_home_040_lezhin_home_all_sale_banner_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 전연령 세일배너 클릭 후 페이지 이동을 확인합니다."""

         # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)

         # 첫 번째 프로모션 배너 링크 찾기
        selector = 'section#sale_hooking_promotion_k li.bannerList__item a.bannerList__link'
        link = page.locator(selector).first

        # 요소 존재 확인
        assert link.element_handle() is not None, "❌ 첫 번째 프로모션 배너가 존재하지 않습니다."

        # href 및 class 정보 확인
        target_url = link.get_attribute("href")
        class_name = link.get_attribute("class")
        print("✅ 배너 클래스:", class_name)
        print("➡ 이동 예정 URL:", target_url)

        # 스크롤 및 클릭
        link.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        link.click()

        # 페이지 로딩 후 URL 확인
        page.wait_for_timeout(3000)
        current_url = page.url

        from urllib.parse import urlparse
        parsed_current = urlparse(current_url)
        parsed_target = urlparse(target_url)

        current_path = parsed_current.path + ('?' + parsed_current.query if parsed_current.query else '')
        target_path = parsed_target.path + ('?' + parsed_target.query if parsed_target.query else '')

        assert current_path == target_path, f"❌ 배너 클릭 후 URL 이동 실패 (현재: {current_path}, 기대값: {target_path})"
        print("✅ 배너 클릭 시 정상적으로 이동되었습니다. (", current_path, ")")

        # 종료
        page.close()
        
def test_home_041_lezhin_home_adult_sale_banner_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 성인 세일배너 클릭 후 페이지 이동을 확인합니다."""

         # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)

         # 첫 번째 세일 배너 링크 찾기
        selector = 'section#sale_hooking_promotion_a li.bannerList__item a.bannerList__link'
        link = page.locator(selector).first

        # 요소 존재 확인
        assert link.element_handle() is not None, "❌ 첫 번째 프로모션 배너가 존재하지 않습니다."

        # href 및 class 정보 확인
        target_url = link.get_attribute("href")
        class_name = link.get_attribute("class")
        print("✅ 배너 클래스:", class_name)
        print("➡ 이동 예정 URL:", target_url)

        # 스크롤 및 클릭
        link.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        link.click()

        # 페이지 로딩 후 URL 확인
        page.wait_for_timeout(3000)
        current_url = page.url

        from urllib.parse import urlparse
        parsed_current = urlparse(current_url)
        parsed_target = urlparse(target_url)

        current_path = parsed_current.path + ('?' + parsed_current.query if parsed_current.query else '')
        target_path = parsed_target.path + ('?' + parsed_target.query if parsed_target.query else '')

        assert current_path == target_path, f"❌ 배너 클릭 후 URL 이동 실패 (현재: {current_path}, 기대값: {target_path})"
        print("✅ 배너 클릭 시 정상적으로 이동되었습니다. (", current_path, ")")

        # 종료
        page.close()
 
def test_home_042_lezhin_home_jaymeeshop_ko(page: Page):
        """해당 코드는 KR 로케일에서 재이미샵 노출을  확인합니다."""

         # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # '재이미샵' 첫 번째 항목의 링크 선택자
        selector = 'section#order_storefarm li.vx__listItem a.vx__link'
        link = page.locator(selector).first

        # 요소 존재 여부 확인
        assert link.element_handle() is not None, "❌ 재이미샵 첫 번째 항목이 존재하지 않습니다."

        page.close()
 
 
        

def test_home_043_lezhin_home_jaymeeshop_click_ko(page: Page):
        """해당 코드는 KR 로케일에서 재이미샵 클릭 후 외부 페이지 이동을 확인합니다."""

         # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # '재이미샵' 첫 번째 항목의 링크 선택자
        selector = 'section#order_storefarm li.vx__listItem a.vx__link'
        link = page.locator(selector).first

        # 요소 존재 여부 확인
        assert link.element_handle() is not None, "❌ 재이미샵 첫 번째 항목이 존재하지 않습니다."

        # href 링크 저장
        target_url = link.get_attribute("href")
        print("➡ 이동 예정 URL:", target_url)

        # 새 탭으로 열릴 수 있으므로 click 전 context 추적
        with page.context.expect_page() as new_page_info:
                link.scroll_into_view_if_needed()
                page.wait_for_timeout(1000)
                link.click()

        # 새 탭으로 열린 페이지 캡처
        new_page = new_page_info.value
        new_page.wait_for_load_state("load")
        new_page.wait_for_timeout(3000)

        # 실제 URL과 기대 URL 비교
        current_url = new_page.url
        from urllib.parse import urlparse

        assert "j-meeshop.com" in urlparse(current_url).netloc, f"❌ 외부 페이지 이동 실패 (현재: {current_url})"
        print("✅ 재이미샵 첫 항목 클릭 시 정상적으로 이동되었습니다. (", current_url, ")")

        new_page.close()
        page.close()
        

def test_home_044_lezhin_home_manual_inventory_click_ko(page: Page):
        """해당 코드는 KO 로케일에서 수동 인벤토리 작품을 클릭하고 페이지 이동을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 수동인벤토리  첫 번째 작품 클릭
        selector = '#curation_promotion_adult .vx__listWrapper ul.vx__list > li.vx__listItem a'
        first_item = page.locator(selector).first
        first_item.wait_for(state="visible", timeout=5000)

        # 요소가 로딩될 때까지 대기
        link_element = page.wait_for_selector(selector, timeout=3000)

        # href 속성 추출
        expected_href = link_element.get_attribute("href")
        print("➡ 기대 이동 URL(href):", expected_href)

        # 클릭 수행
        link_element.click()

        # 페이지가 이동할 시간을 잠시 대기
        page.wait_for_load_state("load")
        page.wait_for_timeout(1000)

        # 현재 URL 확인
        current_url = page.url
        print("🔍 현재 페이지 URL:", current_url)

        # 실제 URL과 href 비교 (도메인 포함 여부에 따라 처리)
        from urllib.parse import urlparse

        parsed_expected = urlparse(expected_href)
        parsed_current = urlparse(current_url)

        # 경로 및 쿼리만 비교 (도메인은 생략)
        expected_path = parsed_expected.path
        current_path = parsed_current.path

        # 검증
        assert current_path == expected_path, f"❌ URL 불일치: 기대값={expected_path}, 실제값={current_path}"
        print("✅ href와 실제 이동 URL이 일치합니다.")
     
        # 페이지 종료
        page.close() 


# US 전면 배너 닫기 (있다면 클릭)
def close_banner_if_exists_en(page: Page):
        """배너가 있으면 닫기"""
        try:
                # 배너(dialog)가 존재하고 open 상태일 경우 최대 3초 대기
                banner = page.locator("dialog.frontBanner__uoT0X[open]")
                banner.wait_for(state="visible", timeout=3000)

                # "Don't show again" 버튼 존재 여부 확인 후 클릭
                dont_show_button = banner.locator("button", has_text="Don't show again")
                if dont_show_button.is_visible():
                        dont_show_button.click()
                        print("✅ 'Don't show again' 버튼 클릭 완료.")
    
        except Exception:
                # TimeoutError 또는 다른 예외가 발생하면 배너가 없다고 간주
                print("⏳ 배너가 표시되지 않음.")

