import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import navigate_to, close_banner_if_exists, click_hamburger_menu

def test_ACCOUNT_07_Password_Reset_ko(page: Page):

        # 레진코믹스 로그인으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
    
        # 이메일과 패스워드 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa02@gmail.com')
        page.fill('#login-password', 'lezhin123@@')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 햄버거 메뉴 선택 (공통 함수 사용)
        click_hamburger_menu(page)

        # 내 정보 메뉴 클릭
        page.click('a.afterLoginMenuList__listItem__FiMaP[href="/ko/account"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 변경 버튼 클릭
        page.click('#change-password-btn')

        # "현재 비밀번호" 입력
        page.fill('#change-password-old', 'lezhin123@@')

        # "새 비밀버호" 입력
        page.fill('#change-password-new', 'lezhin123@@')

        # "새 비밀번호" 재 입력
        page.fill('#change-password-new-confirmation', 'lezhin123@@')

        # "저장" 버튼 클릭
        page.click('.lzBtn[data-ga-event-label="버튼_비밀번호_변경_저장"]')

        # "확인" 버튼 클릭
        page.click('.lzBtn.lzBtn--small.lzBtn--major[aria-controls="change-password-confirm"]')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('.lzSnackbar__msg')

        # 얼럿 메시지 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = '비밀번호를 변경했습니다.'

        # 예상 기대결과와 실제 결과를 비교하여 일차하는 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}. but got: {alert_text}"

        # 햄버거 메뉴 클릭
        page.click('button#log-nav-btn')

        # "로그아웃" 클릭
        page.click('.logNav__link[data-ga-event-label="메뉴_로그아웃"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 이메일과 패스워드 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa02@gmail.com')
        page.fill('#login-password', 'lezhin123@@')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 내 정보 페이지로 이동 완료될 때까지 대기
        page.wait_for_url('https://www.lezhin.com/ko/account')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/account'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()

def test_ACCOUNT_18_Account_Deletion_UI_ko(page: Page):

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

        # 이메일 입력
        page.wait_for_selector('input[name="username"]', state='visible', timeout=3000)
        page.fill('input[name="username"]', 'lilyqa04@maildrop.cc')

        # 비밀번호 입력
        page.wait_for_selector('#login-password', state='visible', timeout=3000)
        page.fill('#login-password', 'lezhin123@@')

        # 로그인 버튼 클릭
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 햄버거 메뉴 선택 (공통 함수 사용)
        click_hamburger_menu(page)

        # 내 정보 클릭
        page.click('a.afterLoginMenuList__listItem__FiMaP[href="/ko/account"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        #"회원을 탈퇴하시겠습니까?" 버튼 클릭
        page.click('#toggle-unregister-form')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 계정 탈퇴 섹션 UI 확인
        unregister_section = page.query_selector('section#unregister')
        is_unregister_section_visible = unregister_section.is_visible() if unregister_section else False
        print('✅ 계정 탈퇴 섹션 확인:', is_unregister_section_visible)

        if unregister_section:
            # 섹션 제목 확인
            heading_element = unregister_section.query_selector('h3#unregister-heading')
            heading_text = heading_element.text_content() if heading_element else None
            print('✅ 섹션 제목:', heading_text)
            assert heading_text == '계정 탈퇴', f"Error: Expected '계정 탈퇴', but got '{heading_text}'"
            print("✅ '계정 탈퇴' 헤딩 텍스트가 정확합니다.")

            # 양식 내용 확인
            form_content_elements = unregister_section.query_selector_all('form#unregister-form p')
            form_content = [element.text_content().strip() for element in form_content_elements]
            print('✅ 양식 내용:', form_content)

            # 기대하는 결과 배열
            expected_content = [
                "회원님의 탈퇴 사유를 알려주세요. 더 좋은 레진 코믹스가 되기 위해 노력하겠습니다.",
                "레진코믹스 회원을 탈퇴하시면, 보유하신 코인사용 및 구매하셨던 콘텐츠 이용이 더 이상 불가합니다. 그래도 탈퇴하시겠습니까?"
            ]

            # 추출한 내용과 기대하는 결과를 비교
            assert form_content == expected_content, f"Error: Form content does not match. Expected: {expected_content}, but got: {form_content}"

            # "lzCols lzCols--1" 클래스를 가진 div 내부의 라디오 버튼 라벨 요소들의 텍스트 추출
            radio_labels = page.eval_on_selector_all(
                'div.lzCols.lzCols--1 label.lzRadio i',
                'elements => elements.map(element => element.textContent?.trim() || "")'
            )

            print('라디오 버튼 라벨:', radio_labels)
            expected_labels = [
                "이용이 불편하고 장애가 많음",
                "코인이 비싸서",
                "다른 사이트가 더 좋아서",
                "사용빈도가 낮아서",
                "콘텐츠 불만",
                "기타"
            ]

            # 추출된 라벨 텍스트와 기대하는 텍스트를 비교
            assert radio_labels == expected_labels, f"Error: Radio labels do not match. Expected: {expected_labels}, but got: {radio_labels}"
            print("✅ 라디오 버튼 라벨 텍스트가 일치합니다.")

            # 비밀번호 입력 필드의 플레이스홀더 확인
            password_input = page.locator('section#unregister input[type="password"]')
            assert password_input.get_attribute('placeholder') == '비밀번호를 입력해 주세요.', "Error: Placeholder text does not match."
            print("✅ 비밀번호 입력 필드의 Placeholder가 정확합니다.")


            # "탈퇴하기" 버튼 존재 확인
            submit_button = page.locator('section#unregister button[type="submit"]')
            assert submit_button.text_content().strip() == '탈퇴하기', "Error: '탈퇴하기' 버튼 텍스트가 일치하지 않습니다."
            print("✅ '탈퇴하기' 버튼 텍스트가 정확합니다.")

            # 탈퇴 사유 선택
            page.get_by_text('이용이 불편하고 장애가 많음').click()

            # "탈퇴하기" 버튼 찾기
            withdraw_button = page.locator('button[type="submit"]', has_text="탈퇴하기")

            # 탈퇴하기 버튼 클릭
            withdraw_button.click()
        
            # 모달 확인
            modal = page.locator("dialog.lzModal")

            # 제목 확인
            title = modal.locator("#unregister-confirm-title")
            expect(title).to_have_text("계정 탈퇴")
            print("✅ 모달 제목 확인: '계정 탈퇴'")

            # 설명 확인
            description = modal.locator("#unregister-confirm-description")
            expected_text = "정말 레진코믹스를 탈퇴하시겠습니까?탈퇴시 결제 내역 및 내 서재 정보가 삭제됩니다."
            expect(description).to_have_text(expected_text)
            print(f"✅ 모달 설명 확인: '{expected_text}'")

            # 탈퇴 모달 내부에서 "취소" 버튼 찾기
            cancel_button = page.locator("dialog.lzModal").get_by_role("button", name="취소")

            # "확인" 버튼 찾기
            confirm_button = page.locator("dialog.lzModal").get_by_role("button", name="확인")

            # 버튼이 보이는지 확인
            expect(cancel_button).to_be_visible()
            print("✅ '취소' 버튼 확인 완료")

            expect(confirm_button).to_be_visible()
            print("✅ '확인' 버튼 확인 완료")
        
        # 페이지 종료
        page.close()

def test_ACCOUNT_18_Account_Deletion_UI_en(page: Page):

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login')

        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('.lzBtn.lzBtn--wide.lzBtn--large.lzBtn--major')

        # 이메일 입력
        page.wait_for_selector('input[name="username"]', state='visible', timeout=3000)
        page.fill('input[name="username"]', 'lilyqa04@maildrop.cc')

        # 비밀번호 입력
        page.wait_for_selector('#login-password', state='visible', timeout=3000)
        page.fill('#login-password', 'lezhin123@@')

        # 로그인 버튼 클릭
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 햄버거 메뉴 선택 (공통 함수 사용)
        click_hamburger_menu(page)

        # 내 정보 클릭
        page.click('a.afterLoginMenuList__listItem__FiMaP[href="/en/account"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        #"회원을 탈퇴하시겠습니까?" 버튼 클릭
        page.click('#toggle-unregister-form')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 계정 탈퇴 섹션 UI 확인
        unregister_section = page.query_selector('section#unregister')
        is_unregister_section_visible = unregister_section.is_visible() if unregister_section else False
        print('✅ 계정 탈퇴 섹션 확인:', is_unregister_section_visible)

        if unregister_section:
            # 섹션 제목 확인
            heading_element = unregister_section.query_selector('h3#unregister-heading')
            heading_text = heading_element.text_content() if heading_element else None
            print('✅ 섹션 제목:', heading_text)
            assert heading_text == 'Deactivate my account', f"Error: Expected 'Deactivate my account', but got '{heading_text}'"
            print("✅ 'Deactivate my account' 헤딩 텍스트가 정확합니다.")

            # 양식 내용 확인
            form_content_elements = unregister_section.query_selector_all('form#unregister-form p')
            form_content = [element.text_content().strip() for element in form_content_elements]
            print('✅ 양식 내용:', form_content)

            # 기대하는 결과 배열
            expected_content = [
                "Please tell us why you want to deactivate your account.",
                "You won't be able to use your purchased Coins or Titles.Do you still want to deactivate your account?"
            ]

            # 추출한 내용과 기대하는 결과를 비교
            assert form_content == expected_content, f"Error: Form content does not match. Expected: {expected_content}, but got: {form_content}"

            # "lzCols lzCols--1" 클래스를 가진 div 내부의 라디오 버튼 라벨 요소들의 텍스트 추출
            radio_labels = page.eval_on_selector_all(
                'div.lzCols.lzCols--1 label.lzRadio i',
                'elements => elements.map(element => element.textContent?.trim() || "")'
            )

            print('라디오 버튼 라벨:', radio_labels)
            expected_labels = [
                "Difficult to use and too many errors",
                "Coins are too expensive",
                "Like other sites better",
                "Don't use site often",
                "Don't like the contents",
                "Other"
            ]

            # 추출된 라벨 텍스트와 기대하는 텍스트를 비교
            assert radio_labels == expected_labels, f"Error: Radio labels do not match. Expected: {expected_labels}, but got: {radio_labels}"
            print("✅ 라디오 버튼 라벨 텍스트가 일치합니다.")

            # 비밀번호 입력 필드의 플레이스홀더 확인
            password_input = page.locator('section#unregister input[type="password"]')
            assert password_input.get_attribute('placeholder') == 'Please enter your password', "Error: Placeholder text does not match."
            print("✅ 비밀번호 입력 필드의 Placeholder가 정확합니다.")

            # "탈퇴하기" 버튼 존재 확인
            submit_button = page.locator('section#unregister button[type="submit"]')
            assert submit_button.text_content().strip() == 'Deactivate', "Error: '탈퇴하기' 버튼 텍스트가 일치하지 않습니다."
            print("✅ 'Deactivate' 버튼 텍스트가 정확합니다.")

            # "탈퇴하기" 버튼 찾기
            withdraw_button = page.locator('button[type="submit"]', has_text="Deactivate")

            # 탈퇴하기 버튼 클릭
            withdraw_button.click()

            # 모달 확인
            modal = page.locator("dialog.lzModal")

            # 제목 확인
            title = modal.locator("#unregister-confirm-title")
            expect(title).to_have_text("Deactivate my account")
            print("✅ 모달 제목 확인: 'Deactivate my account'")

            # 설명 확인
            description = modal.locator("#unregister-confirm-description")
            expected_text = "Do you really want to deactivate?Your purchase history and My Library records will also be deleted."
            expect(description).to_have_text(expected_text)
            print(f"✅ 모달 설명 확인: '{expected_text}'")

            # 탈퇴 모달 내부에서 "취소" 버튼 찾기
            cancel_button = page.locator("dialog.lzModal").get_by_role("button", name="Cancel")

            # "확인" 버튼 찾기
            confirm_button = page.locator("dialog.lzModal").get_by_role("button", name="OK")

            # 버튼이 보이는지 확인
            expect(cancel_button).to_be_visible()
            print("✅ 'Cancel' 버튼 확인 완료")

            expect(confirm_button).to_be_visible()
            print("✅ 'OK' 버튼 확인 완료")
        
        # 페이지 종료
        page.close()