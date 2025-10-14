from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import login, navigate_to, close_banner_if_exists, click_hamburger_menu

def test_LOGIN_EM_01_Navigate_to_Login_Page(page: Page):
        """ 로그인 페이지로이동 확인 """
        # 레진코믹스 홈으로 이동
        navigate_to(page, "https://www.lezhin.com/ko")

        # 배너 닫기
        close_banner_if_exists(page)

        # 햄버거 메뉴 선택
        page.click('.supportsItem__Yj397.supportsItem__userMenu__v_WtU')

        # 이메일로 로그인 버튼 클릭
        page.click('a.emailLogin__Mguo_[href="/ko/login?redirect=%2Fko"]')

       # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko/login?redirect=%2Fko')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/login?redirect=%2Fko'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_02_Email_Login_Button_Disabled(page: Page):
        """ 로그인 버튼 비활성화 확인 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhin.com/ko/login')

        # 이메일 로그인 버튼 선택자
        button_selector = 'button[data-ga-event-label="버튼_이메일_로그인"]'

        # 버튼의 비활성화 상태 확인
        page.wait_for_selector(f'{button_selector}[disabled]')
        is_button_disabled = page.locator(button_selector).get_attribute('disabled') is not None

        # 'disabled' 속성 확인
        button_disabled_attr = page.locator(button_selector).get_attribute('disabled')
        print(f"'disabled' 속성 값: {button_disabled_attr}")

        # 상태 출력 (assert 전에 항상 출력)
        if is_button_disabled:
            print("✅ 이메일 로그인 버튼이 비활성화 상태입니다.")
        else:
            print("❌ 이메일 로그인 버튼이 비활성화 상태가 아닙니다!")

        # 검증 (assert는 검증만 수행)
        assert is_button_disabled, "이메일 로그인 버튼이 비활성화 상태가 아닙니다!"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_03_Invalid_Email_Format_ko(page: Page):
        """ 잘못된 이메일 형식으로 입력 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhin.com/ko/login')

        # 잘못된 이메일형식으로 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01')
        page.fill('#login-password', 'lezhin123')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = '이메일을 정확하게 입력해주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_04_Invalid_Email_Format_en(page: Page):
        """ 잘못된 이메일 형식으로 입력 """
       # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhinus.com/en/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01')
        page.fill('#login-password', 'lezhin123')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = 'Invalid Email format.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_05_Only_Password_Entered_ko(page: Page):
        """ 비밀번호만 입력 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhin.com/ko/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-password', 'lezhin123')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = '로그인에 사용하실 이메일을 입력해주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_06_Only_Password_Entered_en(page: Page):
        """ 비밀번호만 입력 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhinus.com/en/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-password', 'lezhin123')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = 'Please enter the email you want to use for your account.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_07_Only_Email_Entered_ko(page: Page):
        """ 이메일만 입력 """ 
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhin.com/ko/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01@gmail.com')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = '로그인에 사용하실 비밀번호를 입력해주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_08_Only_Email_Entered_en(page: Page):
        """ 이메일만 입력 """ 
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhinus.com/en/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01@gmail.com')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = 'Please enter the password you want to login with.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_09_Password_Length_5_ko(page: Page):
        """ 비밀번호 5자리만 입력 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhin.com/ko/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01@gmail.com')
        page.fill('#login-password', 'lezhi')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 알럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = '영문, 숫자 및 특수문자 포함 8자 이상으로 입력해주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_10_Password_Length_5_en(page: Page):
        """ 비밀번호 5자리만 입력 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhinus.com/en/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01@gmail.com')
        page.fill('#login-password', 'lezhi')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 알럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = 'Min. 8 characters including letters, numbers and more than 1 special character(e.g.!@#$)'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_11_Incorrect_Password_ko(page: Page):
        """ 틀린 비밀번호 입력 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhin.com/ko/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01@gmail.com')
        page.fill('#login-password', 'lezhin123')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 스낵바 메시지 노출 대기
        alert = page.wait_for_selector('.lzSnackbar__msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = '정확한 정보 입력 후, 다시 시도해주세요.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_12_Incorrect_Password_en(page: Page):
        """ 틀린 비밀번호 입력 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,'https://www.lezhinus.com/en/login')

        # 비밀번호만 입력 후 로그인 시도
        page.fill('#login-email', 'lilyqa01@gmail.com')
        page.fill('#login-password', 'lezhin123')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # 스낵바 메시지 노출 대기
        alert = page.wait_for_selector('.lzSnackbar__msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()

        # 예상되는 텍스트 선언
        expected_text = 'Please enter your information accurately and try again.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_13_Login_Success_ko(page: Page):
        """ 특정 계정 (user4)으로 로그인 성공 테스트 """
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page,"https://www.lezhin.com/ko/login")

        # 이메일 계정 정보 입ㅕ
        page.fill("#login-email", "lilyqa01@gmail.com")
        page.fill("#login-password", "lezhin123@@")
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"❌ 로그인 실패! {current_url} != {expected_url}"

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_13_Login_Success_from_Episode_Viewer_ko(page: Page):
        """ 에피소드 뷰어에서 로그인 성공 """
        # 에피소드 뷰어 선택 (너의 돈이 보여 2화)
        page.goto('https://www.lezhin.com/ko/comic/moneylover/2')

        # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko/login?redirect=%2Fko%2Fcomic%2Fmoneylover%2F2')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/login?redirect=%2Fko%2Fcomic%2Fmoneylover%2F2'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url

        # 로그인 정보 입력
        page.fill("#login-email", 'lilyqa01@gmail.com')
        page.fill("#login-password", 'lezhin123@@')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko/comic/moneylover/2')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/comic/moneylover/2'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_13_Login_Success_when_Subscribing_ko(page: Page):
        """ 찜하기 시 로그인 성공 """


        # 에피소드 목록 이동 (너의 돈이 보여)
        navigate_to(page, 'https://www.lezhin.com/ko/comic/moneylover')

        # 찜하기 버튼 클릭
        page.click('.episodeListSupports__item__LsQyr.episodeListSupports__itemSubscribe__A1MnR')

        # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko/login?redirect=%2Fko%2Fcomic%2Fmoneylover')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/login?redirect=%2Fko%2Fcomic%2Fmoneylover'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url
    
        #로그인 정보 입력
        page.fill("#login-email", 'lilyqa01@gmail.com')
        page.fill("#login-password", 'lezhin123@@')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko/comic/moneylover')

        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/comic/moneylover'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url

        # 페이지 종료
        page.close() 

def test_LOGIN_EM_13_Login_Success_when_Toggling_19_On_ko(page: Page):
        """ 19 on시 로그인 성공 """
        # 레진코믹스 홈으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko')

        # 배너 닫기
        close_banner_if_exists(page)

        # 19 토글 on
        page.click('.toggleContentMode__btn__99VKl')

        # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko/login?redirect=%2Fcontent-mode%3Fpath%3D%252Fko%26sw%3Dall%26sign%3Dy')
    
        # 로그인 정보 입력
        page.fill("#login-email", 'lilyqa01@gmail.com')
        page.fill("#login-password", 'lezhin123@@')
        page.click('button[data-ga-event-label="버튼_이메일_로그인"]')

        # URL 리디렉션 대기
        page.wait_for_url('https://www.lezhin.com/ko')
    
        # 현재 페이지의 URL을 가져와 current_url 변수에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url

        # 토글 버튼 선택자 정의
        button_selector = 'button.toggleContentMode__btn__99VKl'

        # 토글 상태 확인
        button_class = page.locator(button_selector).get_attribute('class')
        is_on = 'toggleContentMode__btn--on__2OQ_F' in button_class

        # 결과 출력
        if is_on:
            print("✅ 토글 버튼은 ON 상태입니다.")
        else:
            print("❌ 토글 버튼은 OFF 상태입니다!")

        # 검증
        assert is_on, "토글 버튼이 ON 상태가 아닙니다!"

        # 페이지 종료
        page.close() 


