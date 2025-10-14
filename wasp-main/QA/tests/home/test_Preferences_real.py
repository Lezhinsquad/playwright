from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse
from urllib.parse import urlparse, parse_qs, urlencode


def test_Preferences_001_Preferences_view_not_login_ko(page: Page):
        """해당 코드는 레진 KR 홈에 접속하여 비로그인상태에서 취향설정 템플릿이 노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 취향설정 템플릿 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 템플릿 탐색 및 존재 확인
        element = page.wait_for_selector(selector, timeout=3000)
        assert element is not None, "❌ preferenceTemplate 요소를 찾을 수 없습니다."

        # 클래스명 변수에 저장
        class_name = element.get_attribute("class")
        print("✅ 취향설정 템플릿이 노출됩니다.", class_name)

        # 페이지 종료
        page.close()
          
        
        
def test_Preferences_002_Preferences_view_not_login_en(page: Page):
        """해당 코드는 레진 US 홈에 접속하여 비로그인상태에서 취향설정 템플릿이 노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 2초 대기
        page.wait_for_timeout(2000)

        # 취향설정 템플릿 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 템플릿 탐색 및 존재 확인
        element = page.wait_for_selector(selector, timeout=3000)
        assert element is not None, "❌ preferenceTemplate 요소를 찾을 수 없습니다."

        # 클래스명 변수에 저장
        class_name = element.get_attribute("class")
        print("✅ US 취향설정 템플릿이 노출됩니다.", class_name)

        # 페이지 종료
        page.close()
        
        
def test_Preferences_003_Preferences_view_login_ko(page: Page):
        """해당 코드는 레진 KR 홈에 접속하여 로그인상태에서 취향설정 템플릿이 노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
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

        # 취향설정 템플릿 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 템플릿 탐색 및 존재 확인
        element = page.wait_for_selector(selector, timeout=3000)
        assert element is not None, "❌ preferenceTemplate 요소를 찾을 수 없습니다."

        # 클래스명 변수에 저장
        class_name = element.get_attribute("class")
        print("✅ 로그인 상태에서 KR 취향설정 템플릿이 노출됩니다.", class_name)

        # 페이지 종료
        page.close()
        
        

def test_Preferences_004_Preferences_view_login_en(page: Page):
        """해당 코드는 레진 US 홈에 접속하여 로그인상태에서 취향설정 템플릿이 노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 2초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)

        # 취향설정 템플릿 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 템플릿 탐색 및 존재 확인
        element = page.wait_for_selector(selector, timeout=3000)
        assert element is not None, "❌ preferenceTemplate 요소를 찾을 수 없습니다."

        # 클래스명 변수에 저장
        class_name = element.get_attribute("class")
        print("✅ 로그인 상태에서 US 취향설정 템플릿이 노출됩니다.", class_name)

        # 페이지 종료
        page.close()       
        
def test_Preferences_005_Preferences_not_view_login_ko(page: Page):
        """해당 코드는 KR 로그인상태에서 취향설정 이력이 있을경우 취향설정 템플릿이 비노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
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
        

        # 취향설정 요소 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 요소 탐색 및 비노출 확인
        element = page.query_selector(selector)
        assert element is None, "❌ preferenceTemplate 이 노출 됩니다."

        # 취향설정 템플릿이 아닌 경우에만 클래스명 출력 (예외 방지)
        if element:
                class_name = element.get_attribute("class")
                print("❌ preferenceTemplate 클래스:", class_name)
        else:
                print("✅ 로그인 상태에서 KR 취향설정 템플릿이 비노출됩니다.")

        # 페이지 종료
        page.close()
        

def test_Preferences_006_Preferences_not_view_login_en(page: Page):
        """해당 코드는 us 로그인상태에서 취향설정 이력이 있을경우 취향설정 템플릿이 비노출되는지 확인하는 코드 입니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 취향설정 요소 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 요소 탐색 및 비노출 확인
        element = page.query_selector(selector)
        assert element is None, "❌ preferenceTemplate 이 노출 됩니다."

        # 취향설정 템플릿이 아닌 경우에만 클래스명 출력 (예외 방지)
        if element:
                class_name = element.get_attribute("class")
                print("❌ preferenceTemplate 클래스:", class_name)
        else:
                print("✅ 로그인 상태에서 KR 취향설정 템플릿이 비노출됩니다.")

        # 페이지 종료
        page.close()
        
def test_Preferences_007_Preferences_templete_ko(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 정상적용되었는지 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()     
         
        
def test_Preferences_008_Preferences_templete_en(page: Page):
        """해당 코드는 us 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 정상적용되었는지 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,adult,action,fantasy,drama"
        # request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhinus.com/en")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_009_Preferences_manual_ko(page: Page):
        """해당 코드는 ko 로케일에서 서랍메뉴에서 취향설정을 직접 선택하고 정상적용되었는지 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 장르 직접 설정 탭 버튼 클릭
        page.click('button.tab__9c31y[role="tab"][data-value="genres"]')
        
        # 취향설정 장르 드라마 / 로맨스 / 판타지 / 학원 / 개그 / 백합 / 일상 / 액션 / 미스터리 선택
        page.click('label[data-value="drama"]')
        page.click('label[data-value="romance"]')
        page.click('label[data-value="fantasy"]')
        page.click('label[data-value="school"]')
        page.click('label[data-value="gag"]')
        page.click('label[data-value="gl"]')
        page.click('label[data-value="day"]')
        page.click('label[data-value="action"]')
        page.click('label[data-value="mystery"]')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()     
         
        
def test_Preferences_010_Preferences_manual_en(page: Page):
        """해당 코드는 us 로케일에서 서랍메뉴에서 취향설정을 직접 선택하고 정상적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 장르 직접 설정 탭 버튼 클릭
        page.click('button.tab__9c31y[role="tab"][data-value="genres"]')
        
        # 취향설정 장르 romance / gl / adult / action / fantasy / drama선택
        page.click('label[data-value="romance"]')
        page.click('label[data-value="gl"]')
        page.click('label[data-value="adult"]')
        page.click('label[data-value="action"]')
        page.click('label[data-value="fantasy"]')
        page.click('label[data-value="drama"]')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,adult,action,fantasy,drama"
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/en")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()   
        
def test_Preferences_011_Preferences_manual_inventory_ko(page: Page):
        """해당 코드는 KR 로케일에서 수동인벤토리 취향설정 적용을 확인 합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        # response 중 수동 인벤토리에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "curation_promotion_adult":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'curation_promotion_adult' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'curation_promotion_adult' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()
        
def test_Preferences_012_Preferences_manual_inventory_en(page: Page):
        """해당 코드는 us 로케일에서 수동인벤토리 취향설정 적용을 확인 합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,adult,action,fantasy,drama"
        # request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhinus.com/en")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        # response 중 수동 인벤토리에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "newnonexclusive":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'newnonexclusive' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'newnonexclusive' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")


        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_013_Preferences_jaymee_shop_ko(page: Page):
        """해당 코드는 KR 로케일에서 재이미샵에 취향설정 적용을 확인 합니다.
        재이미 샵은 KR에만 운영하고 있음"""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/sections/home_lezhinshop" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2//sections/home_lezhinshop' 요청이 감지되지 않았습니다.")
        
        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/sections/home_lezhinshop" in response.url:
                        try:
                                json_data = response.json()
                                for item in json_data.get("data", []):
                                        if item.get("id") == 393:
                                                raise AssertionError(f"❌ BL 상품이 포함되어 있습니다: {item}")
                                print("✅ BL 상품이 포함되어 있지 않습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")


        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()

def test_Preferences_014_Preferences_subBanner_ko(page: Page):
        """해당 코드는 KR 로케일에서 서브배너에 취향설정 적용을 확인 합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        # response 중 서브배너에 bl 장르 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "home_sub_2":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'home_sub_2' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'home_sub_2' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # # 페이지 종료
        page.close()

def test_Preferences_015_Preferences_comic_manual_inventory_ko(page: Page):
        """해당 코드는 KR 로케일에서 만화페이지 수동인벤토리에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 KR 만화 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/bookshome')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/comic_printed" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/bookshome")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/comic_printed' 요청이 감지되지 않았습니다.")
        
        # response 중 수동 인벤토리에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/comic_printed" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "comic_printed_manual_3":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'comic_printed_manual_3' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'comic_printed_manual_3' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()

def test_Preferences_016_Preferences_comic_genre_ko(page: Page):
        """해당 코드는 KO 로케일에서 만화페이지 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 KR 만화 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/bookshome')
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_018_Preferences_adult_19_ko(page: Page):
        """해당 코드는 KO 로케일에서 성인19+ 태그리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/nsfw')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/menu" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/nsfw")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/menu' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/menu" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)

     
        # 페이지 종료
        page.close() 
        
def test_Preferences_019_Preferences_genrePlus_ko(page: Page):
        """해당 코드는 KO 로케일에서 장르+ 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/genreplus')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close() 

def test_Preferences_020_Preferences_genrePlus_en(page: Page):
        """해당 코드는 EN 로케일에서 장르+ 장르리스트에 취향설정을 확인합니다."""

         # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        
        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN genre+ 이동
        navigate_to(page, 'https://www.lezhinus.com/en/genreplus')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/menu" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhinus.com/en/genreplus")
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_021_Preferences_free_comiclist_ko(page: Page):
        """해당 코드는 KO 로케일에서 무료페이지 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 무료페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/free')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/free" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/free")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/free' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/free" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()  
        
def test_Preferences_022_Preferences_free_comiclist_en(page: Page):
        """해당 코드는 EN 로케일에서 무료페이지 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 무료페이지 이동
        navigate_to(page, 'https://www.lezhinus.com/en/free')
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,action,fantasy,drama"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/free" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhinus.com/en/free")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/free' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/free" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close() 
        

def test_Preferences_023_Preferences_free_genrelist_ko(page: Page):
        """해당 코드는 KO 로케일에서 무료페이지 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/free')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()

def test_Preferences_024_Preferences_free_genrelist_en(page: Page):
        """해당 코드는 EN 로케일에서 무료페이지 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스  페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 US 무료 이동
        navigate_to(page, 'https://www.lezhinus.com/en/free')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()  


def test_Preferences_025_Preferences_free_genrelist_not_visible_ko(page: Page):
        """해당 코드는 KO 로케일에서 선택한 취향이 1개일때 무료페이지 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 주세요🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/free')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_026_Preferences_free_genrelist_not_visible_en(page: Page):
        """해당 코드는 EN 로케일에서 선택한 취향이 1개일때 무료페이지 장르리스트 비노출을 확인합니다."""

         # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("🍌Boys Finding Love🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/free')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
        # 페이지 종료
        page.close()              

def test_Preferences_027_Preferences_ranking_reailtime_genrelist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 실시간 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()


def test_Preferences_028_Preferences_ranking_reailtime_genrelist_en(page: Page):
        """해당 코드는 EN 로케일에서 랭킹 > 실시간 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_029_Preferences_ranking_reailtime_comiclist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 실시간 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=all')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=all")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()  

def test_Preferences_030_Preferences_ranking_reailtime_comiclist_en(page: Page):
        """해당 코드는 EN 로케일에서 무료페이지 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=all')
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,action,fantasy,drama"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=all")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_031_Preferences_ranking_reailtime_genrelist_not_visible_ko(page: Page):
        """해당 코드는 KO 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 실시간 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 주세요🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_032_Preferences_ranking_reailtime_genrelist_not_visible_en(page: Page):
        """해당 코드는 EN 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 실시간 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 EN 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("🍌Boys Finding Love🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 > 실시간 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_033_Preferences_ranking_newComic_genrelist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 신작 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 > 신작 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=new')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()


def test_Preferences_034_Preferences_ranking_newComic_genrelist_en(page: Page):
        """해당 코드는 EN 로케일에서 랭킹 > 신작 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 > 신작 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=new')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_035_Preferences_ranking_newComic_comiclist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 신작 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 신작 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=new')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=new")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()  

def test_Preferences_036_Preferences_ranking_newComic_comiclist_en(page: Page):
        """해당 코드는 EN 로케일에서 랭킹 > 신작 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 신작 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=new')
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,action,fantasy,drama"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=new")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_037_Preferences_ranking_newComic_genrelist_not_visible_ko(page: Page):
        """해당 코드는 KO 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 신작 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 주세요🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 신작 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=new')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_038_Preferences_ranking_newComic_genrelist_not_visible_en(page: Page):
        """해당 코드는 EN 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 신작 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 EN 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("🍌Boys Finding Love🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 > 신작 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=new')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()


        
def test_Preferences_039_Preferences_ranking_event_genrelist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 이벤트 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 >  이벤트 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=event')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()


def test_Preferences_040_Preferences_ranking_event_genrelist_en(page: Page):
        """해당 코드는 EN 로케일에서 랭킹 > 이벤트 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 > 이벤트 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=event')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_041_Preferences_ranking_event_comiclist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 이벤트 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 이벤트 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=event')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=event")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()  

def test_Preferences_042_Preferences_ranking_event_comiclist_en(page: Page):
        """해당 코드는 EN 로케일에서 랭킹 > 이벤트 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 이벤트 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=event')
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,action,fantasy,drama"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=event")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_043_Preferences_ranking_event_genrelist_not_visible_ko(page: Page):
        """해당 코드는 KO 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 이벤트 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 주세요🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 이벤트 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=realtime&filter=event')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_044_Preferences_ranking_event_genrelist_not_visible_en(page: Page):
        """해당 코드는 EN 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 이벤트 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 EN 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("🍌Boys Finding Love🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 > 이벤트 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=realtime&filter=event')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
        ##################################################################################
        
def test_Preferences_045_Preferences_ranking_year_genrelist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 연도별 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 > 연도별 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=annual&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()


def test_Preferences_046_Preferences_ranking_year_genrelist_en(page: Page):
        """해당 코드는 EN 로케일에서 랭킹 > 연도별 장르리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(1000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 > 연도별 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=annual&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 탭 버튼 유무 확인
        bl_genre_selector = 'button.tab__9c31y[data-value="bl"]'
        bl_genre = page.query_selector_all(bl_genre_selector)

        if bl_genre:
                raise AssertionError("❌ BL 장르가 노출됩니다.")
        else:
                print("✅ BL 장르가 노출 되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_047_Preferences_ranking_year_comiclist_ko(page: Page):
        """해당 코드는 KO 로케일에서 랭킹 > 연도별 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 연도별 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=annual&filter=all')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/ranking?genre=_all&rankType=annual&filter=all")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()  

def test_Preferences_048_Preferences_ranking_year_comiclist_en(page: Page):
        """해당 코드는 EN 로케일에서 랭킹 > 연도별 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 이벤트 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=annual&filter=all')
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,action,fantasy,drama"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhinus.com/en/ranking?genre=_all&rankType=annual&filter=all")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close() 
        
def test_Preferences_049_Preferences_ranking_year_genrelist_not_visible_ko(page: Page):
        """해당 코드는 KO 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 연도별 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 주세요🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KR 랭킹 이벤트 이동
        navigate_to(page, 'https://www.lezhin.com/ko/ranking?genre=_all&rankType=annual&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_050_Preferences_ranking_year_genrelist_not_visible_en(page: Page):
        """해당 코드는 EN 로케일에서 선택한 취향이 1개일때 랭킹페이지 > 연도별 장르리스트 비노출을 확인합니다."""

        # 레진코믹스 EN 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("🍌Boys Finding Love🍆")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 EN 랭킹 > 이벤트 이동
        navigate_to(page, 'https://www.lezhinus.com/en/ranking?genre=_all&rankType=annual&filter=all')

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 'BL' 장르 탭 전체 영역 유무 확인
        genre_tabs_selector = 'div.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU'
        genre_tabs_element = page.query_selector(genre_tabs_selector)

        if genre_tabs_element:
                raise AssertionError("❌ 장르리스트가 노출됩니다.")
        else:
                print("✅ 장르리스트가 노출되지 않습니다.")
     
        # 페이지 종료
        page.close()
        
def test_Preferences_051_Preferences_event_ko(page: Page):
        """해당 코드는 KR 로케일에서 GNB > Event 페이지의 취향설정 적용을 확인 합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 KR 랭킹 신작 이동
        navigate_to(page, 'https://www.lezhin.com/ko/sale')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/event" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/sale")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/event' 요청이 감지되지 않았습니다.")
        
        # response 중 서브배너에 bl 장르 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/event" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "event_big":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'event_big' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'event_big' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # # 페이지 종료
        page.close()
        
        
def test_Preferences_052_Preferences_event_en(page: Page):
        """해당 코드는 US 로케일에서 GNB > Event 페이지의 취향설정 적용을 확인 합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 KR 랭킹 신작 이동
        navigate_to(page, 'https://www.lezhinus.com/en/sale')
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,action,fantasy,drama"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/event" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhinus.com/en/sale")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/event' 요청이 감지되지 않았습니다.")
        
        # response 중 서브배너에 bl 장르 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/event" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "event_big":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'event_big' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'event_big' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # # 페이지 종료
        page.close()
        

def test_Preferences_053_Preferences_new_released_comiclist_ko(page: Page):
        """해당 코드는 KO 로케일에서 레진신작 더보기 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KO 레진신작 더보기 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/scheduled/new-released')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/dynamic" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/scheduled/new-released")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/dynamic' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/dynamic" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()
        
def test_Preferences_054_Preferences_new_released_comiclist_en(page: Page):
        """해당 코드는 EN 로케일에서 레진신작 더보기 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('button.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()

        # 1초 대기
        page.wait_for_timeout(2000)

        # US 전면 배너 닫기 (있다면 클릭)
        close_banner_if_exists_en(page)
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("Heart Hustle ❤️‍🩹")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 US 레진신작 더보기 페이지 이동
        navigate_to(page, 'https://www.lezhinus.com/en/daily/new-released')
        
        #적용되어야할 취향장르 선언
        expected_genres = "romance,gl,action,fantasy,drama"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/dynamic" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhinus.com/en/daily/new-released")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/dynamic' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/dynamic" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()  
        
        
def test_Preferences_055_Preferences_bookshome_new_released_comiclist_ko(page: Page):
        """해당 코드는 KO 로케일에서 신규만화 더보기 작품리스트에 취향설정을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KO 레진신작 더보기 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/bookshome/new-released')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/dynamic" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/bookshome/new-released")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/dynamic' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/dynamic" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()
        
        
def test_Preferences_056_Preferences_viewer_bottom_banner_ko(page: Page):
        """해당 코드는 KO 로케일에서 뷰어 하단 배너 취향설정을 확인합니다."""
        """해당 케이스는 리얼의 데이터가 일정치 않아 QA서버로 대체 합니다."""

        # 레진코믹스 KO 홈 이동
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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 임의 뷰어로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/comic/cartoon_hero/5')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/comic_viewer" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://q-www.lezhin.com/ko/comic/cartoon_hero/5")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/comic_viewer' 요청이 감지되지 않았습니다.")
        
        # response 중 배너에 bl 장르 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/comic_viewer" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "comic_viewer_banner":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'comic_viewer_banner' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'comic_viewer_banner' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # # 페이지 종료
        page.close()
        

def test_Preferences_057_Preferences_viewer_bottom_rolling_banner_ko(page: Page):
        """해당 코드는 KO 로케일에서 뷰어 하단 롤링 배너 취향설정을 확인합니다."""
        """해당 케이스는 리얼의 데이터가 일정치 않아 QA서버로 대체 합니다."""

        # 레진코믹스 KO 홈 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 리액트 버전 적용전 로그인
        # # 이메일 입력
        # page.wait_for_selector('input[name="username"]', state='visible', timeout=3000)
        # page.fill('input[name="username"]', 'squad@lezhin.com')

        # # 비밀번호 입력
        # page.wait_for_selector('#login-password', state='visible', timeout=3000)
        # page.fill('#login-password', 'wlscogus7!')

        # # 로그인 버튼 클릭
        # page.click('button[data-ga-event-label="버튼_이메일_로그인"]')
        
        ## 리액트 대응 버전 로그인
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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 임의 뷰어로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/comic/cartoon_hero/5')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/comic_viewer" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://q-www.lezhin.com/ko/comic/cartoon_hero/5")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/comic_viewer' 요청이 감지되지 않았습니다.")
        
        # response 중 배너에 bl 장르 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/comic_viewer" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "comic_viewer_banner_rolling":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'comic_viewer_banner_rolling' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'comic_viewer_banner_rolling' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # # 페이지 종료
        page.close()
        
def test_Preferences_058_Preferences_not_Reflections_search_Preview_ko(page: Page):
        """해당 코드는 레진 KR 홈에 접속하여 검색 미리보기 화면에 취향설정이 적용되지 않는지 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        

        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/advanced-search" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 입력창에 '야' 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '야')
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/advanced-search' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/advanced-search" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        print("✅ 검색 미리보기에 BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)


        # 페이지 종료
        page.close()
        

def test_Preferences_059_Preferences_not_Reflections_search_result_ko(page: Page):
        """해당 코드는 KR 로케일 검색결과 화면에 취향설정이 적용되지 않는지 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 검색결과페이지 이동
        page.goto("https://www.lezhin.com/ko/search?t=all&q=%EC%95%BC")

        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/advanced-search" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 레진코믹스 검색결과페이지 이동
        page.goto("https://www.lezhin.com/ko/search?t=all&q=%EC%95%BC")
        page.wait_for_timeout(3000)
        
        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/advanced-search' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/advanced-search" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        print("✅ 검색 미리보기에 BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)


        # 페이지 종료
        page.close()
        

def test_Preferences_060_Preferences_free_recent_ko(page: Page):
        """해당 코드는 KR 로케일 무료 > 최근본 취향설정이 적용되지 않는지 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 검색결과페이지 이동
        page.goto("https://www.lezhin.com/ko/free")

        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/users/5954425043025920/dailyfree/recent" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 레진코믹스 검색결과페이지 이동
        page.goto("https://www.lezhin.com/ko/free")
        page.wait_for_timeout(3000)
        
        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/users/5954425043025920/dailyfree/recent' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/users/5954425043025920/dailyfree/recent" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("너란 남자" in item.get("title", []) for item in json_data.get("data", []))

                                if bl_found:
                                        print("✅ 무료 > 최근본 에 BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)


        # 페이지 종료
        page.close()
        


def test_Preferences_061_Preferences_artist_ko(page: Page):
        """해당 코드는 KR 로케일 작가페이지 취향설정이 적용되지 않는지 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 작가페이지 이동
        page.goto("https://www.lezhin.com/ko/artist/ohgye")

        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/artist" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 레진코믹스 검색결과페이지 이동
        page.goto("https://www.lezhin.com/ko/artist/ohgye")
        page.wait_for_timeout(3000)
        
        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/inventory_groups/artist' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/artist" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        print("✅ 작가페이지 에 BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)


        # 페이지 종료
        page.close()
        

def test_Preferences_062_Preferences_library_ko(page: Page):
        """해당 코드는 KR 로케일 내서재 취향설정이 적용되지 않는지 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 내서재 이동
        page.goto("https://www.lezhin.com/ko/library#recent")

        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/users/5954425043025920/recents" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 레진코믹스 검색결과페이지 이동
        page.goto("https://www.lezhin.com/ko/library#recents")
        page.wait_for_timeout(3000)
        
        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/users/5954425043025920/recents' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/users/5954425043025920/recents" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("BL" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        print("✅ 내서재 작품리스트에 BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)


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