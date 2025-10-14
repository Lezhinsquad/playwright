from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse, parse_qs, urlencode, quote


def test_Account_01_component_view_ko(page: Page):
        """해당 코드는 레진 kr 내정보에 포함된 각 메뉴 영역 노출을 확인합니다."""

        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')

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
        
        # 검증해야 할 항목 목록 정의
        sections_to_verify = [
                {"id": "myinfo", "name": "계정 관리"},
                {"id": "device", "name": "기기 관리"},
                {"id": "regularPayment", "name": "정기결제관리"},
                {"id": "expiration", "name": "소멸예정 내역"},
                {"id": "charge", "name": "코인 충전 내역"},
                {"id": "usage", "name": "사용 내역"},
                {"id": "order", "name": "주문 내역"},
                {"id": "unregister", "name": "계정 탈퇴"}
        ]

        # 각 섹션의 노출 여부를 순차적으로 검증
        all_sections_visible = True
        for section in sections_to_verify:
                section_id = section["id"]
                section_name = section["name"]
        
        # ID를 기반으로 <section> 요소를 찾습니다.
        section_locator = page.locator(f"#{section_id}")
        
        try:
            # 요소가 화면에 보이는지 5초간 기다립니다.
            expect(section_locator).to_be_visible(timeout=5000)
            print(f"✅ 성공: '{section_name}' 항목이 노출됩니다.")
        except AssertionError:
            print(f"❌ 실패: '{section_name}' 항목이 노출되지 않았습니다.")
            all_sections_visible = False
            # 하나의 섹션이라도 실패하면 루프를 중단할 수 있습니다.
            # break 
    
         # 최종 결과 검증
        assert all_sections_visible, "❌ 페이지에 노출되지 않은 항목이 있습니다."

        print("\n🎉 모든 필수 항목이 정상적으로 노출됨을 확인했습니다.")
        
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
          
        
        
def test_Account_02_component_view_en(page: Page):
        """해당 코드는 레진 en 내정보에 포함된 각 메뉴 영역 노출을 확인합니다."""

        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://www.lezhinus.com/en/account')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
        # 쿠키 이용 동의 'Accept All' 클릭
        page.locator('button:has-text("Accept All")').click()
        
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")

        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")

        # 로그인 버튼 클릭
        page.locator('button:has-text("Login with email")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 검증해야 할 항목 목록 정의
        sections_to_verify = [
                {"id": "myinfo", "name": "Manage Account"},
                {"id": "device", "name": "Manage Devices"},
                {"id": "regularPayment", "name": "Manage VIP Membership"},
                {"id": "expiration", "name": "Expected Expiration Dates"},
                {"id": "charge", "name": "Coin Purchase History"},
                {"id": "usage", "name": "Usage History"},
                {"id": "unregister", "name": "Deactivate my account"}
        ]

        # 각 섹션의 노출 여부를 순차적으로 검증
        all_sections_visible = True
        for section in sections_to_verify:
                section_id = section["id"]
                section_name = section["name"]
        
        # ID를 기반으로 <section> 요소를 찾습니다.
        section_locator = page.locator(f"#{section_id}")
        
        try:
            # 요소가 화면에 보이는지 5초간 기다립니다.
            expect(section_locator).to_be_visible(timeout=5000)
            print(f"✅ 성공: '{section_name}' 항목이 노출됩니다.")
        except AssertionError:
            print(f"❌ 실패: '{section_name}' 항목이 노출되지 않았습니다.")
            all_sections_visible = False
            # 하나의 섹션이라도 실패하면 루프를 중단할 수 있습니다.
            # break 
    
         # 최종 결과 검증
        assert all_sections_visible, "❌ 페이지에 노출되지 않은 항목이 있습니다."

        print("\n🎉 모든 필수 항목이 정상적으로 노출됨을 확인했습니다.")
        
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        
def test_Account_03_sns_component_view_kakao(page: Page):
        """해당 코드는 카카오 SNS 계정의 내정보 계정관리 영역 구성을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 카카오로 로그인 버튼 클릭
        kakao_button = page.locator('section.oauth__HhjpF').get_by_role("button", name="카카오로 로그인")
        kakao_button.click()
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 카카오 아이디 입력
        page.get_by_placeholder("카카오메일 아이디, 이메일, 전화번호 ").fill("hidelove999@naver.com")

        # 카카오 비밀번호 입력
        page.get_by_placeholder("비밀번호").fill("wlscogus7!@#")

        # 카카오 로그인 실행
        page.locator('button[type="submit"]').click()
        
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
        
        # 2. 검증할 요소 목록 정의
        elements_to_verify = [
                {"selector": page.locator("dl", has_text="이메일 계정 연결"), "name": "이메일 계정 연결"},
                {"selector": page.locator("dl", has_text="휴대폰번호"), "name": "휴대폰번호"},
                {"selector": page.locator("dl", has_text="카카오"), "name": "카카오"}
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
        
        # 회원탈퇴
        page.get_by_role("button", name="회원을 탈퇴하시겠습니까?").click()
        
        page.wait_for_timeout(1000)
        
        page.get_by_role("button", name="탈퇴하기").click()
        
        page.wait_for_timeout(1000)
        
        page.get_by_role("button", name="확인").click()

        # 페이지 종료
        page.close()
        

def test_Account_04_sns_component_view_naver(page: Page):
        """해당 코드는 네이버 SNS 계정의 내정보 계정관리 영역 구성을 확인합니다."""

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
        
        # 2. 검증할 요소 목록 정의
        elements_to_verify = [
                {"selector": page.locator("dl", has_text="이메일 계정 연결"), "name": "이메일 계정 연결"},
                {"selector": page.locator("dl", has_text="휴대폰번호"), "name": "휴대폰번호"},
                {"selector": page.locator("dl", has_text="네이버"), "name": "네이버"}
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
        
        # 회원탈퇴
        page.get_by_role("button", name="회원을 탈퇴하시겠습니까?").click()
        
        page.wait_for_timeout(1000)
        
        page.get_by_role("button", name="탈퇴하기").click()
        
        page.wait_for_timeout(1000)
        
        page.get_by_role("button", name="확인").click()

        # 페이지 종료
        page.close()
        
        

def test_Account_05_email_component_view(page: Page):
        """해당 코드는 이메일 계정의 내정보 계정관리 영역 구성을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')

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
        
        page.goto('https://www.lezhin.com/ko/account')
        
        elements_to_verify = [
                {"selector": page.locator("dl", has_text="카카오"), "name": "SNS 계정 연동"},
                {"selector": page.locator("dl", has_text="이메일"), "name": "이메일"},
                {"selector": page.locator("dl", has_text="비밀번호"), "name": "비밀번호"},
                {"selector": page.locator("dl", has_text="언어/국가"), "name": "언어/국가"}
        ]

        # 2. 각 요소의 노출 여부를 순차적으로 검증
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

        # 3. 모든 요소 검증 후, 하나라도 실패했다면 최종적으로 테스트를 실패시킴
        assert all_items_visible, "❌ 페이지에 노출되지 않은 필수 요소가 있습니다."

        print("\n🎉 모든 검증이 완료되었습니다.")
        

        # 페이지 종료
        page.close()    
        

def test_Account_06_email_SNS_component_view(page: Page):
        """해당 코드는 이메일 + 네이버 계정의 내정보 계정관리 영역 구성을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/account')

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
        
        page.goto('https://www.lezhin.com/ko/account')
        
        
        # '네이버' 텍스트를 포함하는 부모 요소 안에서 '연결' 링크를 찾습니다.
        naver_connect_link = page.locator('div.userManagementSection__item__MAFyw:has-text("네이버")').get_by_role("link", name="연결")

        # 찾은 링크를 클릭합니다.
        naver_connect_link.click()
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 네이버 아이디 입력
        page.get_by_label("아이디 또는 전화번호").fill("hidelove999")

        # 네이버 비밀번호 입력
        page.get_by_label("비밀번호").fill("cogus7qwe!@#")

        # 네이버 로그인 실행
        page.click('button#log\\.login')
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        elements_to_verify = [
                {"selector": page.locator("dl", has_text="네이버"), "name": "네이버"},
                {"selector": page.locator("dl", has_text="이메일"), "name": "이메일"},
                {"selector": page.locator("dl", has_text="비밀번호"), "name": "비밀번호"},
                {"selector": page.locator("dl", has_text="언어/국가"), "name": "언어/국가"}
        ]

        # 2. 각 요소의 노출 여부를 순차적으로 검증
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

        # 3. 모든 요소 검증 후, 하나라도 실패했다면 최종적으로 테스트를 실패시킴
        assert all_items_visible, "❌ 페이지에 노출되지 않은 필수 요소가 있습니다."

        print("\n🎉 모든 검증이 완료되었습니다.")
        
        page.get_by_role("button", name="연결 해제").click()
        

        # 페이지 종료
        page.close()  
        
        

def test_Account_07_SNS_password_component_view(page: Page):
        """해당 코드는 SNS 계정의 내정보 비밀번호 등록 후 구성을 확인합니다."""

        # 레진코믹스 KR 홈 이동
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
        
        

def test_Account_08_SNS_email_connect(page: Page):
        """네이버 + 이메일 연결정보를 확인합니다."""

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
        
        # '연결 해제' 버튼 클릭
        disconnect_button = page.locator('button.myAccount__btn', has_text="연결 해제")
        disconnect_button.click()

        
        page.wait_for_timeout(1000)

        page.close()
                
                

def test_Account_09_SNS_email_connect_duplicate(page: Page):
        """네이버 연결시 중복체크 확인하는 코드입니다."""

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
        page.get_by_label("아이디 또는 전화번호").fill("hidelove13")
        page.get_by_label("비밀번호").fill("wlscogus7!")
        page.click('button#log\\.login')
        page.wait_for_timeout(2000)
        
        
        # 스낵바 메시지 텍스트 추출 시도
        snackbar = page.locator('p.lzSnackbar__message__7WeE_')
        message = snackbar.text_content(timeout=3000)

        # 검증
        assert message == "다른 계정과 연결되어 있습니다.", f"❌ 예상 메시지가 아님: {message}"
        print("✅ 중복 계정 연결 경고 메시지가 정상적으로 노출되었습니다.")
        
        
        page.wait_for_timeout(1000)

        page.close()
        

def test_Account_10_birthday_sex_input(page: Page):
        """해당 코드는 내정보 > 생년월일 입력 여부를 검증합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("hidelove13@naver.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # '정보입력' 버튼 클릭
        page.locator('button.myAccount__btn', has_text='정보입력').click()
        page.wait_for_timeout(1000)

        # 생년월일 선택
        page.select_option('select[name="birthYear"]', value='1983')
        page.select_option('select[name="birthMonth"]', value='12')
        page.select_option('select[name="birthDay"]', value='20')

        # 성별 '남성' <i> 태그 클릭 (라벨 내부)
        page.locator('label[for="m"] >> i:has-text("남성")').click()

        # 저장 버튼 클릭
        page.get_by_role("button", name="저장").click()
        page.wait_for_timeout(3000)

        # 결과 메시지 확인
        snackbar = page.locator('p.lzSnackbar__message__7WeE_')
        message = snackbar.text_content(timeout=3000)

        # 검증
        assert message == "생년월일/성별 정보가 변경됐습니다.", f"❌ 메시지 미노출 또는 불일치: {message}"
        print("✅ 생년월일 및 성별 정보 변경 성공 메시지가 노출되었습니다.") 
        
        page.wait_for_timeout(1000)
        
        
        page.goto('https://www.lezhin.com/ko/account')
        page.wait_for_timeout(1000)
        
        # API 호출을 동기적으로 대기
        with page.expect_response("**/lz-api/v2/users/6755399443233029") as resp_info:
                page.reload()  # 다시 account 페이지 진입 (API 호출 트리거)
                page.wait_for_load_state('load')
                page.wait_for_timeout(1000)

        # 응답 확인
        response = resp_info.value
        json_data = response.json()
        data = json_data.get("data", {})

        assert data.get("birthdate") == "19831220", f"❌ birthdate 값이 일치하지 않음: {data.get('birthdate')}"
        assert data.get("gender") == "m", f"❌ gender 값이 일치하지 않음: {data.get('gender')}"
        print("✅ API 응답에 birthdate/gender 정보가 정확히 포함되어 있음")
        

        page.close()
        


def test_Account_11_birthday_sex_input_clear(page: Page):
        """해당 코드는 내정보 > 생년월일 입력 초기화."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("hidelove13@naver.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # '정보입력' 버튼 클릭
        page.locator('button.myAccount__btn', has_text='정보변경').click()
        page.wait_for_timeout(1000)

        # 개인정보 수집동의 체크 박스 선택
        page.locator('label[for="agree-personal-info"] >> i:has-text("개인정보 수집 및 이용동의")').click()
        
        # 저장 버튼 클릭
        page.get_by_role("button", name="저장").click()
        page.wait_for_timeout(3000)
        
        # 생년월일/성별 정보가 노출되지 않는지 확인
        # 생년월일/성별 섹션의 첫 번째 dd 텍스트 추출
        dd_element = page.locator('dl.userManagementSection__item__MAFyw >> dt:has-text("생년월일/성별") + dd')
        dd_text = dd_element.text_content()

        # 비어 있는지 검증
        assert dd_text.strip() == "", f"❌ 생년월일/성별 정보가 노출되고 있음: '{dd_text.strip()}'"
        print("✅ 생년월일/성별 정보가 노출되지 않아 성공입니다.")
        
        
        page.goto('https://www.lezhin.com/ko/account')
        page.wait_for_timeout(1000)
        
        # API 호출을 동기적으로 대기
        with page.expect_response("**/lz-api/v2/users/6755399443233029") as resp_info:
                page.reload()  # 다시 account 페이지 진입 (API 호출 트리거)
                page.wait_for_load_state('load')
                page.wait_for_timeout(1000)

        # 응답 확인
        response = resp_info.value
        json_data = response.json()
        data = json_data.get("data", {})

        assert data.get("birthdate") == "", f"❌ birthdate 값이 일치하지 않음: {data.get('birthdate')}"
        assert data.get("gender") == "", f"❌ gender 값이 일치하지 않음: {data.get('gender')}"
        print("✅ API 응답에 birthdate/gender 초기화 되었습니다.")
        

        page.close()
        
        

def test_Account_12_Manage_Devices_empty(page: Page):
        """해당 코드는 내정보 > 기기관리 > 등록된 기기가 없을경우를 체크합니다. """

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("hidelove13@naver.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # 정확한 텍스트를 포함한 셀 찾기
        empty_device = page.locator('td.account__tableEmpty__Biit1', has_text="등록한 기기가 없습니다.")
        message = empty_device.text_content(timeout=3000)

        assert message.strip() == "등록한 기기가 없습니다.", f"❌ 기기 없음 메시지가 노출되지 않음 또는 다른 내용입니다: '{message.strip()}'"
        print("✅ 등록된 기기가 없음을 알리는 메시지가 정상 노출되었습니다.")
        

        page.close()
        
        

def test_Account_13_Manage_Devices_Device_Reset_fail(page: Page):
        """해당 코드는 내정보 > 기기관리 > 기기초기화 불가 메세지로 검증 합니다."""

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("squad@lezhin.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # 기기 초기화 버튼 클릭
        reset_button = page.locator('button.myDevice__resetBtn__9qOYj', has_text="기기 초기화")
        reset_button.click()
        page.wait_for_timeout(1000)

        # 확인 버튼 클릭
        confirm_button = page.locator('button:has-text("확인")')
        confirm_button.click()
        page.wait_for_timeout(3000)

        # 결과 메시지 확인
        snackbar = page.locator('p.lzSnackbar__message__7WeE_')
        message = snackbar.text_content(timeout=3000)

        assert message == "최근에 디바이스 연결 해제를 이미 하였습니다.", \
                f"❌ 실패 메시지가 노출되지 않음 또는 불일치: {message}"
        print("✅ 디바이스 초기화 실패 메시지가 정상적으로 노출되었습니다.")

        page.close()
        
def test_Account_14_Coin_Purchase_History_empty(page: Page):
        """해당 코드는 내정보 > 코인충전내역 > 충전 내역이 없을경우를 체크합니다. """

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("hidelove13@naver.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # 정확한 텍스트를 포함한 셀 찾기
        empty_device = page.locator('td.account__tableEmpty__Biit1', has_text="코인 충전 내역이 없습니다.")
        message = empty_device.text_content(timeout=3000)

        assert message.strip() == "코인 충전 내역이 없습니다.", f"❌ 충전내역 없음 메시지가 노출되지 않음 또는 다른 내용입니다: '{message.strip()}'"
        print("✅ 충전내역 없음  메시지가 정상 노출되었습니다.")
        

        page.close()
        
        
        

def test_Search_015_Usage_History_empty(page: Page):
        """해당 코드는 내정보 > 사용내역 > 사용 내역이 없을경우를 체크합니다. """

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("hidelove13@naver.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # 정확한 텍스트를 포함한 셀 찾기
        empty_device = page.locator('td.account__tableEmpty__Biit1', has_text="사용 내역이 없습니다.")
        message = empty_device.text_content(timeout=3000)

        assert message.strip() == "사용 내역이 없습니다.", f"❌ 사용내역 없음 메시지가 노출되지 않음 또는 다른 내용입니다: '{message.strip()}'"
        print("✅ 사용내역 없음  메시지가 정상 노출되었습니다.")
        

        page.close()
        


def test_Search_016_Expected_Expiration_Dates_empty(page: Page):
        """해당 코드는 내정보 > 소멸예정 내역 > 소멸 내역이 없을경우를 체크합니다. """

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("hidelove13@naver.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # 정확한 텍스트를 포함한 셀 찾기
        empty_device = page.locator('td.account__tableEmpty__Biit1', has_text="소멸 예정 내역이 없습니다.")
        message = empty_device.text_content(timeout=3000)

        assert message.strip() == "소멸 예정 내역이 없습니다.", f"❌ 소멸 예정 내역 없음 메시지가 노출되지 않음 또는 다른 내용입니다: '{message.strip()}'"
        print("✅ 소멸예정 내역 없음  메시지가 정상 노출되었습니다.")
        

        page.close()
        
        


def test_Search_017_Order_Details_empty(page: Page):
        """해당 코드는 내정보 > 주문 내역 > 주문 내역이 없을경우를 체크합니다. """

        # 로그인 페이지 접근
        navigate_to(page, 'https://www.lezhin.com/ko/account')
        page.wait_for_load_state('load')

        # 이메일 로그인
        page.locator("#email").fill("hidelove13@naver.com")
        page.locator("#password").fill("wlscogus7!")
        page.locator('button:has-text("이메일로 로그인")').click()
        page.wait_for_timeout(2000)
        
        # "주문 내역이 없습니다." 메시지 확인
        empty_order_locator = page.locator('div.orderList__item--empty__LltmJ')
        message = empty_order_locator.text_content(timeout=3000)

        assert message == "주문 내역이 없습니다.", f"❌ 메시지 미노출 또는 불일치: {message}"
        print("✅ 주문 내역 없음 메시지가 정상적으로 노출되었습니다.")
        

        page.close()
        
        

