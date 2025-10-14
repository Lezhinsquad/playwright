
from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import login, navigate_to, close_banner_if_exists


def test_RESET_PW_01_Check_UI(page: Page):
        """ 비밀번호찾기 UI확인 """
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login/forgot_password')

        # 메시지가 나올 때까지 대기
        message = page.wait_for_selector('form.account p')

        # 메시지의 텍스트 가져오기
        message_text = message.text_content()

        # 예상 기대결과 확인 (메시지 내용이 일치하는지 확인)
        expected_text = '비밀번호를 다시 설정하시려면 아래 입력창에 본인의 메일 주소를 입력하세요.'
        print('예상 결과:', expected_text)
        print('실제 결과:', message_text)
        assert message_text == expected_text

        # 이메일 입력란이 존재하는지 확인
        email_input = page.query_selector('#login-email-address')

        if email_input is not None:
            print("✅ 이메일 입력란이 정상적으로 존재합니다.")
        else:
            print("❌ 이메일 입력란을 찾지 못했습니다.")

        assert email_input is not None, "이메일 입력란을 찾지 못했습니다."

        # 확인 버튼이 존재하는지 확인
        submit_button = page.query_selector('button[type="submit"]')

        if submit_button is not None:
            print("✅ 확인 버튼이 정상적으로 존재합니다.")
        else:
            print("❌ 확인 버튼을 찾지 못했습니다.")

        assert submit_button is not None, "확인 버튼을 찾지 못했습니다."

        # 하단 메시지 확인
        help_message = page.wait_for_selector('.account__help')
        message_text1 = help_message.text_content()
        expected_help_text = '이용 중 도움이 필요하시면 [고객지원] 페이지로, 로그인에 문제가 있다면 help@lezhin.com으로 문의해 주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_help_text}")
        print(f"실제 결과: {message_text1}")
        assert message_text1.strip() == expected_help_text, f"Expected: {expected_help_text}, Got: {message_text1.strip()}"

        # 고객지원 링크가 존재하는지 확인
        help_link = page.query_selector('a[href="/ko/help"]')

        if help_link is not None:
            print("✅ 고객지원 링크가 정상적으로 존재합니다.")
        else:
            print("❌ 고객지원 링크를 찾지 못했습니다.")
        
        assert help_link is not None, "고객지원 링크를 찾지 못했습니다."

        # help@lezhin.com 링크가 존재하는지 확인
        help_email_link = page.query_selector('a[href="mailto:help@lezhin.com"]')
        assert help_email_link is not None, "help@lezhin.com 링크를 찾지 못했습니다."

        # 페이지 종료
        page.close()

def test_RESET_PW_02_Email_Sent_Success_ko(page: Page):
        """ 이메일 전송 성공_ko """        
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login/forgot_password')

        # 유효한 이메일 형식으로 입력
        page.fill('input[name="login-email"]', 'lilyqa03@gmail.com')

        # 확인 버튼 클릭
        page.get_by_role('button', name='확인').click()

        # 메시지가 나올 때까지 대기
        message = page.wait_for_selector('#reset-password-success > p')

        # 메시지의 텍스트 가져오기
        message_text = message.text_content()
        expected_text = '비밀번호 재설정 메일을 보냈습니다. 메일함을 확인해 보세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {message_text}")

        # 검증
        assert message_text == expected_text, f"Expected: {expected_text}, Got: {message_text}"

        # "레진코믹스 홈으로" 버튼 클릭
        page.click('a:has-text("레진코믹스 홈으로")')

        # 대기 시간 추가
        page.wait_for_timeout(1000)

        # 현재 페이지의 URL 가져오기
        current_url = page.url
        expected_url = 'https://www.lezhin.com/ko'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_url}")
        print(f"실제 결과: {current_url}")
        assert current_url == expected_url, f"Expected: {expected_url}, Got: {current_url}"

        # 페이지 종료
        page.close()

def test_RESET_PW_02_Email_Sent_Success_en(page: Page):
        """ 이메일 전송 성공_en """
        
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login/forgot_password')

        # 유효한 이메일 형식으로 입력
        page.fill('input[name="login-email"]', 'lilyqa03@gmail.com')

        # 확인 버튼 클릭
        page.get_by_role('button', name='OK').click()

        # 메시지가 나올 때까지 대기
        message = page.wait_for_selector('#reset-password-success > p')

        # 메시지의 텍스트 가져오기
        message_text = message.text_content()
        expected_text = 'Password reset email has been sent. Please check your inbox.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {message_text}")

        # 검증
        assert message_text == expected_text, f"Expected: {expected_text}, Got: {message_text}"

        # "레진코믹스 홈으로" 버튼 클릭
        page.click('a:has-text("Home")')

        # 대기 시간 추가
        page.wait_for_timeout(1000)

        # 현재 페이지의 URL 가져오기
        current_url = page.url
        expected_url = 'https://www.lezhinus.com/en'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_url}")
        print(f"실제 결과: {current_url}")
        assert current_url == expected_url, f"Expected: {expected_url}, Got: {current_url}"

        # 페이지 종료
        page.close()

def test_RESET_PW_03_Click_Confirm_Button_Without_Email_ko(page: Page):
        """ 이메일 미입력 상태에서 확인버튼 클릭 """
        # 레진코믹스 홈으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko')

        # 배너 닫기(공통 함수 사용)
        close_banner_if_exists(page)

        # 햄버거 메뉴 클릭
        page.click('.supportsItem__Yj397.supportsItem__userMenu__v_WtU')

        # 비밀번호 찾기 클릭
        page.click('.forgotPassword___Ia05')

        # 내 정보 페이지로 이동 완료될 때까지 대기
        page.wait_for_url('https://www.lezhin.com/ko/login/forgot_password')

        # 현재 페이지의 URL을 가져와 문자열 변수 currentURL에 저장
        current_url = page.url
        
        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/login/forgot_password'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_url}")
        print(f"실제 결과: {current_url}")
        assert current_url == expected_url

        # 이메일 미입력 상태에서 확인 버튼 클릭
        page.get_by_role('button', name='확인').click()

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('.lzSnackbar__msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트를 expected_text 변수에 선언하여 저장
        expected_text = '로그인에 사용하실 이메일을 입력해주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {alert_text}")
        assert alert_text == expected_text, f"Expected: {expected_text}, Got: {alert_text}"

        # 페이지 종료
        page.close()

def test_RESET_PW_03_Click_Confirm_Button_Without_Email_en(page: Page):
        """ 이메일 미입력 상태에서 확인버튼 클릭_en """
        # 레진코믹스 홈으로 이동
        navigate_to(page, 'https://www.lezhinus.com/en')

        # 배너 닫기(공통 함수 사용)
        close_banner_if_exists(page)

        # 햄버거 메뉴 클릭
        page.click('.supportsItem__Yj397.supportsItem__userMenu__v_WtU')

        # 비밀번호 찾기 클릭
        page.click('.forgotPassword___Ia05')
        
        # 비밀번호 찾기 페이지로 이동 완료될 때까지 대기
        page.wait_for_url('https://www.lezhinus.com/en/login/forgot_password')

        # 현재 페이지의 URL을 가져와 문자열 변수 currentURL에 저장
        current_url = page.url
        
        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhinus.com/en/login/forgot_password'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_url}")
        print(f"실제 결과: {current_url}")

        # 페이지 URL이 예상한 값과 일치하는지 검증
        assert current_url == expected_url

        # 이메일 미입력 상태에서 확인 버튼 클릭
        page.get_by_role('button', name='OK').click()

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('.lzSnackbar__msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트를 expected_text 변수에 선언하여 저장
        expected_text = 'Please enter the email you want to use for your account.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {alert_text}")
        assert alert_text == expected_text, f"Expected: {expected_text}, Got: {alert_text}"

        # 페이지 종료
        page.close()

def test_RESET_PW_04_Invalid_Email_Format_ko(page: Page):
        """ 잘못된 이메일 형식_ko """
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login/forgot_password')

        # 잘못된 이메일 형식으로 입력
        page.fill('input[name="login-email"]', 'lilyqa01@g')

        # 확인 버튼 클릭
        page.get_by_role('button', name='확인').click()

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('.lzSnackbar__msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트를 expected_text 변수에 선언하여 저장
        expected_text = '이메일을 정확하게 입력해주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {alert_text}")
        assert alert_text == expected_text, f"Expected: {expected_text}, Got: {alert_text}"

        # 페이지 종료
        page.close()

def test_RESET_PW_04_Invalid_Email_Format_en(page: Page):
        """ 잘못된 이메일 형식_ko """
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login/forgot_password')

        # 잘못된 이메일 형식으로 입력
        page.fill('input[name="login-email"]', 'lilyqa01@g')

        # 확인 버튼 클릭
        page.get_by_role('button', name='OK').click()

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('.lzSnackbar__msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트를 expected_text 변수에 선언하여 저장
        expected_text = 'Invalid Email format.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {alert_text}")
        assert alert_text == expected_text, f"Expected: {expected_text}, Got: {alert_text}"

        # 페이지 종료
        page.close()

def test_RESET_PW_05_Unregistered_Email_Input_ko(page: Page):
        """ 미가입 이메일 계정 입력_ko """
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login/forgot_password')

        # 미가입 계정으로 입력
        page.fill('input[name="login-email"]', 'lezhin12345@gmail.com')

        # 확인 버튼 클릭
        page.click('button.lzBtn.lzBtn--medium.lzBtn--major.lzBtn--wide[type="submit"]')

        # 메시지가 나올 때까지 대기
        message = page.wait_for_selector('#reset-password-success > p')

        # 메시지의 텍스트 가져오기
        message_text = message.text_content()

        # 예상되는 텍스트
        expected_text = '비밀번호 재설정 메일을 보냈습니다. 메일함을 확인해 보세요.'

        # 예상 기대결과와 실제 결과 비교
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {message_text}")
        assert message_text == expected_text, f"Expected: {expected_text}, Got: {message_text}"

        # "레진코믹스 홈으로" 버튼 클릭
        page.click('a.lzBtn.lzBtn--medium.lzBtn--major[href="/ko/"]')

        # URL이 변경될 때까지 대기
        page.wait_for_url('https://www.lezhin.com/ko')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 정의하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_url}")
        print(f"실제 결과: {current_url}")
        assert current_url == expected_url, f"URL mismatch: Expected: {expected_url}, Got: {current_url}"

        # 페이지 종료
        page.close()

def test_RESET_PW_05_Unregistered_Email_Input_en(page: Page):
        """ 미가입 이메일계정 입력_en """
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/login/forgot_password')

        # 미가입 계정으로 입력
        page.fill('input[name="login-email"]', 'lezhin12345@gmail.com')

        # 확인 버튼 클릭
        page.click('button.lzBtn.lzBtn--medium.lzBtn--major.lzBtn--wide[type="submit"]')

        # 메시지가 나올 때까지 대기
        message = page.wait_for_selector('#reset-password-success > p')

        # 메시지의 텍스트 가져오기
        message_text = message.text_content()

        # 예상되는 텍스트
        expected_text = 'Password reset email has been sent. Please check your inbox.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_text}")
        print(f"실제 결과: {message_text}")
        assert message_text == expected_text, f"Expected: {expected_text}, Got: {message_text}"

        # "레진코믹스 홈으로" 버튼 클릭
        page.click('a.lzBtn.lzBtn--medium.lzBtn--major[href="/en/"]')

        # URL이 변경될 때까지 대기
        page.wait_for_url('https://www.lezhinus.com/en')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 정의하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhinus.com/en'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print(f"예상 결과: {expected_url}")
        print(f"실제 결과: {current_url}")
        assert current_url == expected_url, f"URL mismatch: Expected: {expected_url}, Got: {current_url}"

        # 페이지 종료
        page.close()

def test_RESET_PW_06_Navigate_To_Customer_Support_ko(page: Page):
        """ 고객지원 링크 이동_ko """
        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login/forgot_password')

        # "고객지원" 링크 클릭
        page.click('p.account__help a[href="/ko/help"]')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 현재 페이지의 URL을 가져와 문자열 변수 currentURL에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expectedURL 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/help#?faq=common&notice=service'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()

def test_RESET_PW_07_Password_Change_Complete_ko(page: Page):
        """ 비밀번호 변경 완료_ko """
        # 페이지 시작
        context = page.context

        # 비밀번호 찾기 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login/forgot_password')

        # 유효한 이메일 형식으로 입력
        page.fill('input[name="login-email"]', 'lilyqa01@maildrop.cc')

        # 확인 버튼 클릭
        page.click('button.lzBtn.lzBtn--medium.lzBtn--major.lzBtn--wide[type="submit"]')

        # 메일 열기
        with context.expect_page() as new_page_info:
            page.evaluate("window.open('https://maildrop.cc/inbox/?mailbox=lilyqa01', '_blank')")
        new_page = new_page_info.value
        new_page.wait_for_load_state('networkidle')

        # iframe 확인 및 링크 찾기
        new_page.wait_for_selector('iframe')
        iframe_handle = new_page.query_selector('iframe')
        if iframe_handle:
            iframe_content = iframe_handle.get_attribute('srcdoc')
            if iframe_content:
                new_page.set_content(iframe_content)
                print("iframe content loaded.")

            # 링크 찾기
            link_selector = 'a[href*="https://www.lezhin.com/ko/reset?key="]'
            link = new_page.query_selector(link_selector)

            # 특정 링크 클릭 (name 속성을 기반으로)
            link_name = 'https://www.lezhin.com/ko/'  # 링크 텍스트
            link = new_page.locator(f'a:has-text("{link_name}")')  # 텍스트를 포함하는 링크 선택

            # 링크 클릭
            link.click()

        # 비밀번호 재설정 페이지 이동 및 입력
        new_page.wait_for_load_state('load')
        new_page.fill('#reset-password', 'lezhin123@@')
        new_page.click('button.lzBtn--medium.lzBtn--major.lzBtn--wide')

        # 페이지가 완전히 로드될 때까지 대기
        new_page.wait_for_load_state('networkidle')

        # 요소가 보이는지 먼저 체크
        if new_page.is_visible('#reset-password-success > p'):
            message = new_page.wait_for_selector('#reset-password-success > p', timeout=10000)
            message_text = message.text_content().strip()
            
            expected_text = '비밀번호 변경이 완료되었습니다.'
            assert message_text == expected_text, f"❌ Expected: '{expected_text}', Got: '{message_text}'"

            print("✅ 비밀번호 변경 성공 메시지 확인 완료!")
        else:
            print("❌ 비밀번호 변경 성공 메시지가 보이지 않습니다.")

        # 레진코믹스 로그인 페이지로 이동
        new_page.goto('https://www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load')

        # 이메일과 패스워드 입력 후 로그인 시도
        new_page.fill('input[name="username"]', 'lilyqa01@maildrop.cc')
        new_page.fill('#login-password', 'lezhin123@@')
        new_page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load')

        # 배너 닫기
        try:
            # 배너(dialog)가 있는지 확인 (최대 3초 대기)
            banner = new_page.wait_for_selector("dialog.frontBanner__uoT0X[open]", timeout=3000)
            
            if banner:  # 배너가 존재하면 버튼 클릭
                new_page.click("dialog.frontBanner__uoT0X button:has-text('오늘 하루 안보기')")
                print("✅ '오늘 하루 안보기' 버튼을 클릭했습니다.")
    
        except Exception:
             # TimeoutError 또는 다른 예외가 발생하면 배너가 없다고 간주
             print("⏳ 배너가 표시되지 않음.")

        # 햄버거 메뉴 클릭
        new_page.click('.supportsItem__Yj397.supportsItem__userMenu__v_WtU')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load')

        # 이메일 값 가져오기
        email = new_page.wait_for_selector('.afterLogin__userEmail__AsBtd')

        # 이메일의 텍스트 가져오기
        email_text = email.text_content()

        # 이메일 값 검증
        expected_email = 'lilyqa01@maildrop.cc'
        print('예상 결과:', expected_email)
        print('실제 결과:', email_text)
        assert email_text == expected_email, f"Expected: {expected_email}, Got: {email_text}"

        # 페이지 종료
        page.close()
        new_page.close()

