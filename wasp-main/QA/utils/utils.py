from playwright.sync_api import sync_playwright, Page
import json

# JSON 파일에서 테스트 계정 정보 로드
def load_accounts():
    """accounts.json 파일에서 계정 정보를 불러옴"""
    with open("QA/accounts.json", "r", encoding="utf-8") as file:
        return json.load(file)


# 로그인 기능 (테스트 계정별 자동 선택 가능)
def login(page: Page, account_type: str):
    """
    특정 계정으로 로그인
    """
    accounts = load_accounts()  # 계정 데이터 로드
    email = accounts[account_type]["email"]
    password = accounts[account_type]["password"]

    page.goto("https://www.lezhin.com/ko/login")
    page.fill("#login-email", email)
    page.fill("#login-password", password)
    page.click('button[data-ga-event-label="버튼_이메일_로그인"]')
    page.wait_for_load_state("networkidle")  # 네트워크 안정화 대기
    print(f"✅ 로그인 완료: {email}")


# 공통적으로 사용할 페이지 이동 함수
def navigate_to(page: Page, url: str):
    """특정 페이지로 이동"""
    page.goto(url)
    page.wait_for_load_state("load")

# KR 전면 배너 닫기 (있다면 클릭)
def close_banner_if_exists(page: Page):
    """배너가 있으면 닫기"""
    try:
        # 배너(dialog)가 있는지 확인 (최대 2초 대기)
        banner = page.wait_for_selector("dialog.frontBanner__uoT0X[open]", timeout=3000)
        
        if banner:  # 배너가 존재하면 버튼 클릭
            page.click("dialog.frontBanner__uoT0X button:has-text('오늘 하루 안보기')")
            print("✅ '오늘 하루 안보기' 버튼을 클릭했습니다.")
    
    except Exception:
        # TimeoutError 또는 다른 예외가 발생하면 배너가 없다고 간주
        print("⏳ 배너가 표시되지 않음.")
        
# # KR 전면 배너 닫기 (있다면 클릭)
# def close_banner_if_exists(page: Page):
#     """배너가 있으면 닫기"""
#     try:
#         # 배너(dialog)가 존재하고 open 상태일 경우 최대 3초 대기
#         front_banner = page.locator("dialog.frontBanner__uoT0X[open]")
#         front_banner.wait_for(state="visible", timeout=3000)

#         # "Don't show again" 버튼 존재 여부 확인 후 클릭
#         dont_show_button_1 = front_banner.locator("button", has_text="오늘 하루 안보기")
#         if dont_show_button_1.is_visible():
#             dont_show_button_1.click()
#             print("✅ '오늘 하루 안보기' 버튼 클릭 완료.")
#     except Exception:
#         # TimeoutError 또는 다른 예외가 발생하면 배너가 없다고 간주
#         print("⏳ 배너가 표시되지 않음.")
        
# US 전면 배너 닫기 (있다면 클릭)
def close_banner_if_exists_US(page: Page):
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

# 햄버거 메뉴 클릭 공통 함수
def click_hamburger_menu(page: Page):
    try:
        page.click(".supportsItem__Yj397.supportsItem__userMenu__v_WtU", timeout=5000)
        print("✅ 햄버거 메뉴 클릭 성공")
    except Exception as e:
        print(f"❌ 햄버거 메뉴 클릭 실패: {e}")

# 회원가입 시 약관 동의 공통 함수(ko)
def agree_to_terms_ko(page: Page):
    # 전체동의 체크박스가 나타날 때까지 대기
    agree_all_checkbox_selector = 'label.lzCheck input.agree-all'
    page.wait_for_selector(agree_all_checkbox_selector)
    
    # 전체 동의 체크
    page.click('text="전체동의"')

    # "만 14세 이상입니다." 체크
    page.click('text="만 14세 이상입니다."')

    # "동의" 버튼 클릭
    page.click('button[data-ga-event-label="버튼_약관동의_확인"]')

    print("✅ 약관 동의 완료")

# 회원가입 시 약관 동의 공통 함수(en)
def agree_to_terms_en(page: Page):
    # 전체동의 체크박스가 나타날 때까지 대기
    signup_agree_checkbox_selector = 'label.lzCheck'
    page.wait_for_selector(signup_agree_checkbox_selector)

    # 전체 동의 체크
    page.click('text="Agree to the Lezhin Comics Terms of Use"')

    # "동의" 버튼 클릭
    page.click('button[data-ga-event-label="버튼_약관동의_확인"]')

    print("✅ 약관 동의 완료")

# 네이버 로그인 수행
def login_to_naver(page: Page, username: str, password: str):  
    # 아이디 입력
    page.get_by_label('아이디 또는 전화번호').click()
    page.get_by_label('아이디 또는 전화번호').fill(username)

    # 비밀번호 입력
    page.get_by_label('비밀번호').click()
    page.get_by_label('비밀번호').fill(password)

    # 로그인 버튼 클릭
    page.click("button.btn_login.next_step.nlog-click")

    print("✅ 네이버 로그인 성공")

# 트위터 로그인 수행
def login_to_twitter(page: Page, username: str, password: str):
    # 앱 승인
        page.wait_for_selector("#allow", state="visible", timeout=10000)
        page.locator("#allow").click()

        login_field = page.locator("input[name='text']")
        login_field.wait_for(timeout=60000)

        # 트위터 로그인 페이지 이동 후 로그인
        page.get_by_label('휴대폰 번호, 이메일 주소 또는 사용자 아이디').click()
        page.get_by_label('휴대폰 번호, 이메일 주소 또는 사용자 아이디').fill(username)
        page.get_by_role('button',  name = '다음' ).click()
        password_input = page.locator('input[type="password"]')
        password_input.fill(password)
        page.get_by_test_id('LoginForm_Login_Button').click()

        print("✅ 트위터 로그인 성공")


# 카카오 로그인 수행
def login_to_kakao(page: Page, username: str, password: str):
    
        # 카카오 로그인 페이지 이동 후 로그인
        page.get_by_placeholder('카카오메일 아이디, 이메일, 전화번호 ').click()
        page.get_by_placeholder('카카오메일 아이디, 이메일, 전화번호 ').fill(username)
        page.get_by_placeholder('비밀번호').click()
        page.get_by_placeholder('비밀번호').fill(password)
        page.get_by_role('button',  name= '로그인', exact= True ).click()

        print("✅ 카카오 로그인 성공")

# 쿠키 Accept All 클릭
def accept_all_cookies(page: Page) -> None:
    #해당 버튼이 없으면 무시하고 테스트 계속 진행.
    try:
        page.get_by_role("button", name="Accept All", exact=True).click(timeout=3000)
        print("✅ 'Accept All' 버튼을 클릭했습니다.")
    except Exception:
        print("⏭️ 'Accept All' 버튼이 표시되지 않음 (또는 이미 처리됨).")
