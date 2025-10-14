from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse, parse_qs, urlencode, quote

def test_Account_01_SNS_password_component_view(page: Page):
        """해당 코드는 SNS 계정의 내정보 비밀번호 등록 후 구성을 확인합니다."""
        
        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 네이버로 로그인 버튼 클릭
        naver_button = page.locator('section.oauth__HhjpF').get_by_role("button", name="네이버로 로그인")
        naver_button.click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 네이버 아이디 입력
        page.get_by_label("아이디 또는 전화번호").fill("hidelove999")

        # 네이버 비밀번호 입력
        page.get_by_label("비밀번호").fill("cogus7qwe!@#")

        # 네이버 로그인 실행
        page.get_by_role("button", name="로그인").click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 전체동의 클릭
        page.locator('label:has-text("전체동의")').click()
        
        # '만 14세 이상' 체크박스  클릭
        page.locator('label:has-text("만 14세 이상입니다.")').click()
        
        # 회원가입 실행
        agree_button = page.get_by_role("button", name="동의")
        agree_button.click()

        # 2초 대기
        page.wait_for_timeout(2000)
        
        page.goto('https://www.lezhin.com/ko/account')
        
        # 비밀번호 설정 버튼 클릭
        page.get_by_role("button", name="비밀번호 설정").click()
        
        # 1. 새 비밀번호 입력
        # id가 'password'인 입력 필드를 찾아 비밀번호를 입력합니다.
        page.locator("#password").fill("wlscogus7!")

        # 2. 새 비밀번호 확인 입력
        # id가 're-password'인 입력 필드를 찾아 비밀번호를 다시 입력합니다.
        page.locator("#re-password").fill("wlscogus7!")

        # 3. 저장 버튼 클릭
        # 'button' 역할을 하고 이름(텍스트)이 "저장"인 요소를 찾아 클릭합니다.
        page.get_by_role("button", name="저장").click()
        
        # 2. 검증할 요소 목록 정의
        elements_to_verify = [
                {"selector": page.locator("dl", has_text="비밀번호"), "name": "비밀번호"},
        ]

        # 3. 각 요소의 노출 여부를 순차적으로 검증 (if/else 방식과 유사하게)
        # 전체 검증 결과를 추적하기 위한 변수
        all_items_visible = True

        for item in elements_to_verify:
                locator = item["selector"]
                name = item["name"]

                try:
                        # 요소가 5초 안에 보이면 이 블록이 실행됩니다. (성공 케이스)
                        expect(locator).to_be_visible(timeout=5000)
                        print(f"✅ 성공: '{name}' 요소가 정상적으로 노출됩니다.")
                except AssertionError:
                        # 요소가 보이지 않아 expect가 실패하면 이 블록이 실행됩니다. (실패 케이스)
                        print(f"❌ 실패: '{name}' 요소가 노출되지 않았습니다.")
                        all_items_visible = False  # 전체 결과를 '실패'로 기록

        # 모든 요소 검증 후, 하나라도 실패했다면 최종적으로 테스트를 실패시킴
        assert all_items_visible, "❌ 페이지에 노출되지 않은 요소가 있습니다."

        print("\n🎉 모든 검증이 완료되었습니다.")       

        # 페이지 종료
        page.close()

def test_Account_02_SNS_password_login(page: Page):
        """해당 코드는 SNS 계정의 내정보 비밀번호 등록 후 로그인 여부를 확인합니다."""
        
        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        

        # 이메일 입력
        page.locator("#email").fill("hidelove999@naver.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()
        
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
                
        # 이메일 텍스트 요소 탐색
        email_selector = 'h3.afterLogin__userInfo__J3_RB span.afterLogin__userEmail__AsBtd'
        email_element = page.locator(email_selector)

        # 요소 존재 여부 및 텍스트 검증
        if not email_element.is_visible():
                raise AssertionError("❌ 이메일 요소가 화면에 보이지 않음")

        actual_email = email_element.text_content().strip()

        if actual_email != "hidelove999@naver.com":
                raise AssertionError(f"❌ 이메일 불일치: 기대값='hidelove999@naver.com', 실제값='{actual_email}'")

        print("✅ 이메일이 정상적으로 'hidelove999@naver.com'으로 노출됨")    
        
        # 회원탈퇴
        page.get_by_role("button", name="회원을 탈퇴하시겠습니까?").click()
        
        page.wait_for_timeout(1000)
        
        page.get_by_placeholder("비밀번호를 입력해 주세요.").fill("wlscogus7!")
        
        page.wait_for_timeout(1000)
        
        page.get_by_role("button", name="탈퇴하기").click()
                
        page.wait_for_timeout(1000)
        
        page.get_by_role("button", name="확인").click()

        # 페이지 종료
        page.close()
        
def test_Account_03_SNS_email_connect_naver(page: Page):
        """네이버 + 이메일 연결 후 정상연결 여부를 확인합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("squad@lezhin.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)

        # 네이버 연결 버튼 클릭
        page.wait_for_load_state('load')
        page.wait_for_timeout(2000)
        page.locator('div.userManagementSection__item__MAFyw:has-text("네이버")').get_by_role("link", name="연결").click()
        page.wait_for_timeout(2000)

        # 네이버 로그인
        page.get_by_label("아이디 또는 전화번호").fill("hidelove999")
        page.get_by_label("비밀번호").fill("cogus7qwe!@#")
        page.click('button#log\\.login')
        page.wait_for_timeout(2000)
        
        
        page.goto('https://www.lezhin.com/ko/account')
        page.wait_for_timeout(1000)
        
        # 사용자 정보 API 응답 수신 대기
        with page.expect_response(lambda response: "lz-api/v2/users/5954425043025920" in response.url) as response_info:
                page.reload()
                page.wait_for_load_state("load")
                page.wait_for_timeout(2000)

        # 응답 파싱
        response = response_info.value
        json_data = response.json()

        # socials 필드에 "naver"가 포함되어 있는지 확인
        socials = json_data.get("data", {}).get("socials", [])

        assert "naver" in socials, f"❌ 'naver' 계정 연결 정보가 존재하지 않습니다. 현재 socials 필드: {socials}"
        print("✅ 'naver' 계정 연결이 확인되었습니다.")
        
        
        page.wait_for_timeout(1000)

        page.close()
        


def test_Account_04_SNS_email_connect_naver_login(page: Page):
        """네이버 + 이메일 연결 후 네이버 로그인을 통해 정상 로그인을 확인합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 네이버로 로그인 버튼 클릭
        naver_button = page.locator('section.oauth__HhjpF').get_by_role("button", name="네이버로 로그인")
        naver_button.click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 네이버 아이디 입력
        page.get_by_label("아이디 또는 전화번호").fill("hidelove999")

        # 네이버 비밀번호 입력
        page.get_by_label("비밀번호").fill("cogus7qwe!@#")

        # 네이버 로그인 실행
        page.get_by_role("button", name="로그인").click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')    
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 이메일 텍스트 요소 탐색
        email_selector = 'h3.afterLogin__userInfo__J3_RB span.afterLogin__userEmail__AsBtd'
        email_element = page.locator(email_selector)

        # 요소 존재 여부 및 텍스트 검증
        if not email_element.is_visible():
                raise AssertionError("❌ 이메일 요소가 화면에 보이지 않음")

        actual_email = email_element.text_content().strip()

        if actual_email != "squad@lezhin.com":
                raise AssertionError(f"❌ 이메일 불일치: 기대값='squad@lezhin.com', 실제값='{actual_email}'")

        print("✅ 이메일이 정상적으로 'squad@lezhin.com'으로 노출됨")
        


        
        page.wait_for_timeout(1000)

        page.close()
        
        
def test_Account_05_SNS_email_disconnect_naver(page: Page):
        """네이버 + 이메일 연결해제 후 API 검증을 통해 네이버 계정 연결해제 여부를 확인합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("squad@lezhin.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)

        # '연결 해제' 버튼 클릭
        disconnect_button = page.locator('button.myAccount__btn', has_text="연결 해제")
        disconnect_button.click()
        
        
        page.goto('https://www.lezhin.com/ko/account')
        page.wait_for_timeout(1000)
        
        # 사용자 정보 API 응답 수신 대기
        with page.expect_response(lambda response: "lz-api/v2/users/5954425043025920" in response.url) as response_info:
                page.reload()
                page.wait_for_load_state("load")
                page.wait_for_timeout(2000)

        # 응답 파싱
        response = response_info.value
        json_data = response.json()

        # 'socials' 필드가 data 안에 존재하지 않아야 성공
        has_socials = "socials" in json_data.get("data", {})

        assert not has_socials, f"❌ 'socials' 필드가 존재합니다. 현재 data 필드: {json_data.get('data')}"
        print("✅ 'socials' 필드가 존재하지 않아 연결헤제가 확인되었습니다.")
        
        
        page.wait_for_timeout(1000)

        page.close()
        
        
def test_Account_06_SNS_email_disconnect_naver_login(page: Page):
        """해당 코드는 네이버 SNS 계정 연결해제 후 SNS 로그인 시도시 회원가입페이지(약관동의)로 이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        
        
        # 네이버로 로그인 버튼 클릭
        naver_button = page.locator('section.oauth__HhjpF').get_by_role("button", name="네이버로 로그인")
        naver_button.click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 네이버 아이디 입력
        page.get_by_label("아이디 또는 전화번호").fill("hidelove999")

        # 네이버 비밀번호 입력
        page.get_by_label("비밀번호").fill("cogus7qwe!@#")

        # 네이버 로그인 실행
        page.get_by_role("button", name="로그인").click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        
            # 현재 페이지 URL
        current_url = page.url

        # 기대하는 URL (쿼리스트링 제외)
        expected_base_url = "https://www.lezhin.com/ko/signup"

        # 현재 URL에서 scheme, netloc, path만 추출
        parsed = urlparse(current_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        # 비교
        assert base_url == expected_base_url, f"❌ URL 불일치: 기대값={expected_base_url}, 실제값={base_url}"
        print("✅ 회원가입 페이지로 이동 되었습니다.")

        # 페이지 종료
        page.close()



def test_Account_07_SNS_email_connect_kakao(page: Page):
        """카카오 + 이메일 연결 후 정상연결 여부를 확인합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("squad@lezhin.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)

        # 카카오 연결 버튼 클릭
        page.wait_for_load_state('load')
        page.wait_for_timeout(2000)
        page.locator('div.userManagementSection__item__MAFyw:has-text("카카오")').get_by_role("link", name="연결").click()
        page.wait_for_timeout(2000)

        # 카카오 로그인
        page.get_by_placeholder("카카오메일 아이디, 이메일, 전화번호 ").fill("hidelove999@naver.com")
        page.get_by_placeholder("비밀번호").fill("wlscogus7!@#")
        page.locator('button[type="submit"]').click()
        page.wait_for_timeout(2000)
        
        
        page.goto('https://www.lezhin.com/ko/account')
        page.wait_for_timeout(1000)
        
        # 사용자 정보 API 응답 수신 대기
        with page.expect_response(lambda response: "lz-api/v2/users/5954425043025920" in response.url) as response_info:
                page.reload()
                page.wait_for_load_state("load")
                page.wait_for_timeout(2000)

        # 응답 파싱
        response = response_info.value
        json_data = response.json()

        # socials 필드에 "naver"가 포함되어 있는지 확인
        socials = json_data.get("data", {}).get("socials", [])

        assert "kakao" in socials, f"❌ 'kakao' 계정 연결 정보가 존재하지 않습니다. 현재 socials 필드: {socials}"
        print("✅ 'kakao' 계정 연결이 확인되었습니다.")
        
        
        page.wait_for_timeout(1000)

        page.close()
        


def test_Account_08_SNS_email_connect_kakao_login(page: Page):
        """카카오 + 이메일 연결 후 카카오 로그인을 통해 정상 로그인을 확인합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 네이버로 로그인 버튼 클릭
        naver_button = page.locator('section.oauth__HhjpF').get_by_role("button", name="카카오로 로그인")
        naver_button.click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 카카오 로그인
        page.get_by_placeholder("카카오메일 아이디, 이메일, 전화번호 ").fill("hidelove999@naver.com")
        page.get_by_placeholder("비밀번호").fill("wlscogus7!@#")
        page.locator('button[type="submit"]').click()
        page.wait_for_timeout(2000)
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')    
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 이메일 텍스트 요소 탐색
        email_selector = 'h3.afterLogin__userInfo__J3_RB span.afterLogin__userEmail__AsBtd'
        email_element = page.locator(email_selector)

        # 요소 존재 여부 및 텍스트 검증
        if not email_element.is_visible():
                raise AssertionError("❌ 이메일 요소가 화면에 보이지 않음")

        actual_email = email_element.text_content().strip()

        if actual_email != "squad@lezhin.com":
                raise AssertionError(f"❌ 이메일 불일치: 기대값='squad@lezhin.com', 실제값='{actual_email}'")

        print("✅ 이메일이 정상적으로 'squad@lezhin.com'으로 노출됨")
        


        
        page.wait_for_timeout(1000)

        page.close()
        
        
def test_Account_09_SNS_email_disconnect_kako(page: Page):
        """카카오 + 이메일 연결해제 후 정상 연결해제 여부를 API 결과로 확인합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("squad@lezhin.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)

        # '연결 해제' 버튼 클릭
        disconnect_button = page.locator('button.myAccount__btn', has_text="연결 해제")
        disconnect_button.click()
        
        
        page.goto('https://www.lezhin.com/ko/account')
        page.wait_for_timeout(1000)
        
        # 사용자 정보 API 응답 수신 대기
        with page.expect_response(lambda response: "lz-api/v2/users/5954425043025920" in response.url) as response_info:
                page.reload()
                page.wait_for_load_state("load")
                page.wait_for_timeout(2000)

        # 응답 파싱
        response = response_info.value
        json_data = response.json()

        # 'socials' 필드가 data 안에 존재하지 않아야 성공
        has_socials = "socials" in json_data.get("data", {})

        assert not has_socials, f"❌ 'socials' 필드가 존재합니다. 현재 data 필드: {json_data.get('data')}"
        print("✅ 'socials' 필드가 존재하지 않아 연결헤제가 확인되었습니다.")
        
        
        page.wait_for_timeout(1000)

        page.close()
        
        
def test_Account_10_SNS_email_disconnect_kakao_login(page: Page):
        """해당 코드는 카카오 SNS 계정 연결해제 후 SNS 로그인 시도시 회원가입페이지(약관동의)로 이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        
        
        # 네이버로 로그인 버튼 클릭
        naver_button = page.locator('section.oauth__HhjpF').get_by_role("button", name="카카오로 로그인")
        naver_button.click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 카카오 로그인
        page.get_by_placeholder("카카오메일 아이디, 이메일, 전화번호 ").fill("hidelove999@naver.com")
        page.get_by_placeholder("비밀번호").fill("wlscogus7!@#")
        page.locator('button[type="submit"]').click()
        page.wait_for_timeout(2000)
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        
        # 현재 페이지 URL
        current_url = page.url

        # 기대하는 URL (쿼리스트링 제외)
        expected_base_url = "https://www.lezhin.com/ko/signup"

        # 현재 URL에서 scheme, netloc, path만 추출
        parsed = urlparse(current_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        # 비교
        assert base_url == expected_base_url, f"❌ URL 불일치: 기대값={expected_base_url}, 실제값={base_url}"
        print("✅ 회원가입 페이지로 이동 되었습니다.")

        # 페이지 종료
        page.close()
        


        
        


        
        


                
                


        



