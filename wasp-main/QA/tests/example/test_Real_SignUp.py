import re
from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import login, navigate_to, close_banner_if_exists, click_hamburger_menu, agree_to_terms_ko, agree_to_terms_en


def test_SIGNUP_EM_01_Navigate_To_Signup_Page(page: Page):
        """ 회원가입 페이지 이동 """
        # 레진코믹스 홈으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko')

        # 배너 닫기 (공통함수)
        close_banner_if_exists(page)

        # 햄버거 메뉴 클릭(공통 함수 사용)
        click_hamburger_menu(page)

        # 이메일로 회원가입 클릭
        page.click('a.emailSignup__oah5U[href="/ko/signup?redirect=%2Fko"]')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 현재 페이지의 URL을 가져와 문자열 변수 currentURL에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expectedURL 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/signup?redirect=%2Fko'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_02_Cancel_Signup_Button(page: Page):
        """ 회원가입 취소 버튼 동작 확인 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # "취소" 버튼 클릭
        page.click('[data-ga-event-action="cancel"]')

        # 현재 페이지의 URL을 가져와 문자열 변수 currentURL에 저장
        current_url = page.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expectedURL 변수에 저장
        expected_url = 'https://www.lezhin.com/ko'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_03_Signup_UI_ko(page: Page):
        """ 회원가입 UI 확인"""
        # 레진코믹스 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 타이틀이 나올때까지 대기
        title = page.wait_for_selector('.auth__heading')

        # 타이틀 메시지의 텍스트 가져오기
        title_text = title.text_content()

        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '이메일로 회원가입'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('기대 결과:', title_text)
        assert title_text == expected_text, f"Expected: {expected_text}, but got: {title_text}"

        # 회원가입 약관동의 UI 요소 확인
        page.wait_for_selector('#signup-agree')

        # 전체동의 체크박스 확인
        agree_all_checkbox = page.locator('input[name="chk-all"]')
        is_agree_all_checked = agree_all_checkbox.is_checked()

        # 레진코믹스 이용약관 체크박스 확인
        tos_checkbox = page.locator('input[name="agree-tos"]')
        is_tos_checked = tos_checkbox.is_checked()

        # 개인정보 수집 및 이용에 대한 동의 체크박스 확인
        pp_checkbox = page.locator('input[name="agree-pp"]')
        is_pp_checked = pp_checkbox.is_checked()

        # 이벤트 및 마케팅 활용 동의 체크박스 확인
        market_email_checkbox = page.locator('input[name="agree_market_email"]')
        is_market_email_checked = market_email_checkbox.is_checked()

        # 만 14세 이상 체크박스 확인
        adult_checkbox = page.locator('input[name="adult"]')
        is_adult_checked = adult_checkbox.is_checked()

        # 동의 버튼 확인
        agree_button = page.locator('button[data-action="submit"]')
        is_agree_button_disabled = agree_button.is_disabled()

        # 검증
        assert not is_agree_all_checked, "전체동의 체크박스가 체크된 상태입니다."
        assert not is_tos_checked, "레진코믹스 이용약관 체크박스가 체크된 상태입니다."
        assert not is_pp_checked, "개인정보 수집 및 이용 동의 체크박스가 체크된 상태입니다."
        assert not is_market_email_checked, "이벤트 및 마케팅 활용 동의 체크박스가 체크된 상태입니다."
        assert not is_adult_checked, "만 14세 이상 체크박스가 체크된 상태입니다."
        assert is_agree_button_disabled, "동의 버튼이 활성화된 상태입니다."

        # 예상 결과 출력
        print('UI가 정상적으로 노출되었습니다.')
        print(f'전체동의: {"체크됨" if is_agree_all_checked else "체크되지 않음"}')
        print(f'레진코믹스 이용약관(필수): {"체크됨" if is_tos_checked else "체크되지 않음"}')
        print(f'개인정보 수집 및 이용에 대한 동의(필수): {"체크됨" if is_pp_checked else "체크되지 않음"}')
        print(f'이벤트 및 마케팅 활용 동의(선택): {"체크됨" if is_market_email_checked else "체크되지 않음"}')
        print(f'만 14세 이상입니다.(필수): {"체크됨" if is_adult_checked else "체크되지 않음"}')
        print(f'동의 버튼 비활성화 여부: {"비활성화" if is_agree_button_disabled else "활성화"}')

        # 하단 문구 "이용 중 도움이 필요하시면.."확인
        help_text_locator = page.locator('p.account__help')
        is_visible = help_text_locator.is_visible()
        help_text = help_text_locator.text_content()

        # 예상 문구
        expected_text = '이용 중 도움이 필요하시면 [고객지원] 페이지로, 로그인에 문제가 있다면 help@lezhin.com으로 문의해 주세요.'

        # 검증
        assert is_visible, "도움말 문구가 화면에 표시되지 않습니다."
        assert expected_text in help_text, f"문구가 예상과 다릅니다. 현재 문구: {help_text}"

        # "고객지원" 링크 확인
        help_link_locator = page.locator('p.account__help a[href="/ko/help"]')
        assert help_link_locator.is_visible(), "고객지원 링크가 표시되지 않습니다."

        # 이메일 링크 확인
        email_link_locator = page.locator('p.account__help a[href^="mailto:help@lezhin.com"]')
        assert email_link_locator.is_visible(), "이메일 링크가 표시되지 않습니다."

        # 출력
        print("도움말 문구와 링크가 정상적으로 노출되었습니다.")
        print(f"현재 문구: {help_text}")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_04_Signup_UI_en(page: Page):
        """ 회원가입 UI 확인 """
        # 레진코믹스 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 타이틀이 나올때까지 대기
        title = page.wait_for_selector('.auth__heading')

        # 타이틀 메시지의 텍스트 가져오기
        title_text = title.text_content()

        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Sign Up'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('기대 결과:', title_text)
        assert title_text == expected_text, f"Expected: {expected_text}, but got: {title_text}"

        # 회원가입 약관동의 UI 요소 확인
        page.wait_for_selector('#signup-agree')

        # 레진코믹스 이용약관 체크박스 확인
        tos_checkbox = page.locator('input[name="agree-tos"]')
        is_tos_checked = tos_checkbox.is_checked()

        # 동의 버튼 확인
        agree_button = page.locator('button[data-action="submit"]')
        is_agree_button_disabled = agree_button.is_disabled()

        # 검증
        assert not is_tos_checked, "레진코믹스 이용약관 체크박스가 체크된 상태입니다."
        assert is_agree_button_disabled, "동의 버튼이 활성화된 상태입니다."

        # 예상 결과 출력
        print('UI가 정상적으로 노출되었습니다.')
        print(f'레진코믹스 이용약관(필수): {"체크됨" if is_tos_checked else "체크되지 않음"}')
        print(f'동의 버튼 비활성화 여부: {"비활성화" if is_agree_button_disabled else "활성화"}')

        # 하단 문구 "이용 중 도움이 필요하시면.."확인
        help_text_locator = page.locator('p.account__help')
        is_visible = help_text_locator.is_visible()
        help_text = help_text_locator.text_content()

        # 예상 문구
        expected_text = 'Go to [Customer Support] for help, and contact us through help_us@lezhin.com if you are having trouble logging in.'

        # 검증
        assert is_visible, "도움말 문구가 화면에 표시되지 않습니다."
        assert expected_text in help_text, f"문구가 예상과 다릅니다. 현재 문구: {help_text}"

        # "고객지원" 링크 확인
        help_link_locator = page.locator('p.account__help a[href="/en/help"]')
        assert help_link_locator.is_visible(), "고객지원 링크가 표시되지 않습니다."

        # 이메일 링크 확인
        email_link_locator = page.locator('p.account__help a[href^="mailto:help_us@lezhin.com"]')
        assert email_link_locator.is_visible(), "이메일 링크가 표시되지 않습니다."

        # 출력
        print("도움말 문구와 링크가 정상적으로 노출되었습니다.")
        print(f"현재 문구: {help_text}")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_05_Agreement_Step_Check_All_ko(page: Page):
        """ 약관 동의 단계 - 전체 동의 체크 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 대기할 요소 선택자
        agree_all_checkbox_selector = 'label.lzCheck input.agree-all'

        # 전체동의 체크박스가 나타날 때까지 대기
        page.wait_for_selector(agree_all_checkbox_selector)

        # 전체 동의 체크
        page.click('label:has(input.agree-all)')

        # "동의" 버튼 비활성화
        agree_button = page.locator('button[data-ga-event-label="버튼_약관동의_확인"]')
        is_disabled = agree_button.is_disabled()

        # "동의" 버튼이 비활성화 상태인지 확인
        print(f'동의 버튼 비활성화.: {is_disabled}')
        assert is_disabled, "동의 버튼이 활성화 상태입니다. 비활성화 상태여야 합니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_06_Agreement_Step_Age_14_or_Older_Check_ko(page: Page):
        """ 약관 동의 단계 - 만 14세 이상 체크 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # "만 14세 이상입니다." 선택
        page.click('text="만 14세 이상입니다."')

        # "동의" 버튼 비활성화
        agree_button = page.locator('button[data-ga-event-label="버튼_약관동의_확인"]')
        is_disabled = agree_button.is_disabled()

        # "동의" 버튼이 비활성화 상태인지 확인
        print(f'동의 버튼 비활성화.: {is_disabled}')
        assert is_disabled, "동의 버튼이 활성화 상태입니다. 비활성화 상태여야 합니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_07_Agreement_Step_Terms_and_Conditions_Age_14_or_Older_Check_ko(page: Page):
        """ 약관 동의 단계 - 이용약관 & 만14세이상 체크 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        #'레진코믹스 이용약관' 체크 박스 클릭
        page.click('text="레진코믹스 이용약관"')

        # "만 14세 이상입니다." 선택
        page.click('text="만 14세 이상입니다."')

        # "동의" 버튼 비활성화
        agree_button = page.locator('button[data-ga-event-label="버튼_약관동의_확인"]')
        is_disabled = agree_button.is_disabled()

        # "동의" 버튼이 비활성화 상태인지 확인
        print(f'동의 버튼 비활성화.: {is_disabled}')
        assert is_disabled, "동의 버튼이 활성화 상태입니다. 비활성화 상태여야 합니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_07_Agreement_Step_Privacy_Policy_Age_14_or_Older_Check_ko(page: Page):
        """ 약관 동의 단계 - 개인정보 수집 & 만 14세 이상 체크 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        #'개인정보 수집 및 이용에 대한 동의' 체크 박스 클릭
        page.click('text="개인정보 수집 및 이용에 대한 동의"')

        # "만 14세 이상입니다." 선택
        page.click('text="만 14세 이상입니다."')

        # "동의" 버튼 비활성화
        agree_button = page.locator('button[data-ga-event-label="버튼_약관동의_확인"]')
        is_disabled = agree_button.is_disabled()

        # "동의" 버튼이 비활성화 상태인지 확인
        print(f'동의 버튼 비활성화.: {is_disabled}')
        assert is_disabled, "동의 버튼이 활성화 상태입니다. 비활성화 상태여야 합니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_08_Agreement_Step_Check_All_and_Age_14_or_Older_ko(page: Page):
        """ 약관 동의 단계 - 전체동의 & 만 14세 이상 체크 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # "전체 동의" 체크 박스 클릭
        page.click('label:has(input.agree-all)')

        # "만 14세 이상입니다." 선택
        page.click('text="만 14세 이상입니다."')

        # 동의 버튼이 활성화될 때까지 대기
        page.wait_for_selector('button[data-ga-event-label="버튼_약관동의_확인"]:not([disabled])')
        
        # "동의" 버튼 요소 가져오기
        agree_button = page.locator('button[data-ga-event-label="버튼_약관동의_확인"]')

        # 버튼이 실제로 활성화되었는지 확인
        is_disabled = agree_button.get_attribute("disabled")
        is_enabled = is_disabled is None

        print(f"Button enabled status: {is_enabled}")
        assert is_enabled, "버튼이 활성화되지 않았습니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_09_Agreement_Step_Required_Fields_Check_ko(page: Page):
        """ 약관 동의 단계 -  필수값 체크 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # "레진코믹스 이용약관" 체크 박스 클릭
        page.click('text="레진코믹스 이용약관"')

        # "개인정보 수집 및 이용에 대한 동의" 체크 박스 클릭
        page.click('text="개인정보 수집 및 이용에 대한 동의"')

        # "만 14세 이상입니다." 선택
        page.click('text="만 14세 이상입니다."')

        # 동의 버튼이 활성화될 때까지 대기
        page.wait_for_selector('button[data-ga-event-label="버튼_약관동의_확인"]:not([disabled])')
        
        # "동의" 버튼 요소 가져오기
        agree_button = page.locator('button[data-ga-event-label="버튼_약관동의_확인"]')

        # 버튼이 실제로 활성화되었는지 확인
        is_disabled = agree_button.get_attribute("disabled")
        is_enabled = is_disabled is None

        print(f"Button enabled status: {is_enabled}")
        assert is_enabled, "버튼이 활성화되지 않았습니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_10_Agreement_Step_Terms_of_Service_Link_Navigation_ko(page: Page):
        """ 약관 동의 단계 - 이용약관 링크 이동 """
        # 회원가입 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 팝업 이벤트 대기
        with page.expect_popup() as popup_info:
            page.locator('a[href="/ko/policy/terms"]').click()

        # 새로 열린 팝업 페이지 가져오기
        popup_page = popup_info.value

        # 팝업 페이지가 완전히 로드될 때까지 대기 (networkidle 추가)
        popup_page.wait_for_load_state('load')
        popup_page.wait_for_load_state('networkidle')

        # 팝업 페이지 URL 가져오기
        popup_url = popup_page.url
        expected_url = 'https://www.lezhin.com/ko/policy/terms'
        print(f"팝업 페이지 URL: {popup_url}")

        # 예상 기대결과와 실제 결과 비교
        assert popup_url == expected_url, f"Expected: {expected_url}, but got: {popup_url}"

        # 약관 제목 요소 대기 및 가져오기
        title_locator = popup_page.locator('.law.lzCntnr h2').first
        popup_page.wait_for_selector('.law.lzCntnr h2', timeout=5000)
        assert title_locator.is_visible(), "약관 제목이 팝업 페이지에 표시되지 않습니다."

        # 텍스트 내용 확인
        title_text = title_locator.text_content() or ""  # None 방지
        title_text = title_text.strip()
        expected_text = "레진코믹스 서비스 이용약관"

        # 예상 결과와 비교
        print('예상 결과:', expected_text)
        print('실제 결과:', title_text)
        assert title_text == expected_text, f"Expected: '{expected_text}', but got: '{title_text}'"

        # 결과 출력
        print("✅ 팝업 페이지 약관 제목이 정상적으로 표시되었습니다:", title_text)

        # 팝업 닫기
        popup_page.close()

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_10_Agreement_Step_Terms_of_Service_Link_Navigation_en(page: Page):
        """ 약관 동의 단계 - 이용약관 링크 이동 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 팝업 이벤트 대기
        with page.expect_popup() as popup_info:
            # 상세보기 링크 클릭
            page.locator('a[href="/en/policy/terms"]').click()

        # 새로 열린 팝업 페이지 가져오기
        popup_page = popup_info.value

        # 팝업 페이지가 완전히 로드될 때까지 대기 (networkidle 추가)
        popup_page.wait_for_load_state('load')
        popup_page.wait_for_load_state('networkidle')

        # 팝업 페이지의 URL 가져오기
        popup_url = popup_page.url
        print(f"팝업 페이지 URL: {popup_url}")
        expected_url = 'https://www.lezhinus.com/en/policy/terms'

        # 예상 기대결과와 실제 결과 비교
        assert popup_url == expected_url, f"Expected: {expected_url}, but got: {popup_url}"

        # 약관 제목 요소 대기 및 가져오기
        title_locator = popup_page.locator('.law.lzCntnr h2').first
        popup_page.wait_for_selector('.law.lzCntnr h2', timeout=5000)
        assert title_locator.is_visible(), "약관 제목이 팝업 페이지에 표시되지 않습니다."

        # 텍스트 내용 확인
        title_text = title_locator.text_content() or ""  # None 방지
        title_text = title_text.strip()
        expected_text = "Terms of Use"

        # 예상 결과와 비교
        print('예상 결과:', expected_text)
        print('실제 결과:', title_text)
        assert title_text == expected_text, f"Expected: '{expected_text}', but got: '{title_text}'"

        # 결과 출력
        print("✅ 팝업 페이지 약관 제목이 정상적으로 표시되었습니다:", title_text)

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_11_Agreement_Step_Privacy_Policy_Link_Navigation_ko(page: Page):
        """ 약관 동의 단계 - 개인정보수집 이용동의 링크 이동 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 팝업 이벤트 대기
        with page.expect_popup() as popup_info:
            # 상세보기 링크 클릭
            page.locator('a[href="/ko/policy/privacy-agree"]').click()

        # 새로 열린 팝업 페이지 가져오기
        popup_page = popup_info.value

        # 팝업 페이지가 완전히 로드될 때까지 대기 (networkidle 추가)
        popup_page.wait_for_load_state('load')
        popup_page.wait_for_load_state('networkidle')

        # 팝업 페이지 URL 가져오기
        popup_url = popup_page.url
        expected_url = 'https://www.lezhin.com/ko/policy/privacy-agree'
        print(f"팝업 페이지 URL: {popup_url}")

        # 예상 기대결과와 실제 결과 비교
        assert popup_url == expected_url, f"Expected: {expected_url}, but got: {popup_url}"

        # 약관 제목 요소 대기 및 가져오기
        title_locator = popup_page.locator('.law.lzCntnr h2').first
        popup_page.wait_for_selector('.law.lzCntnr h2', timeout=5000)
        assert title_locator.is_visible(), "약관 제목이 팝업 페이지에 표시되지 않습니다."

        # 텍스트 내용 확인
        title_text = title_locator.text_content() or ""  # None 방지
        title_text = title_text.strip()
        expected_text = "개인정보 수집 및 이용"

        # 예상 결과와 비교
        print('예상 결과:', expected_text)
        print('실제 결과:', title_text)
        assert title_text == expected_text, f"Expected: '{expected_text}', but got: '{title_text}'"

        # 결과 출력
        print("✅ 팝업 페이지 약관 제목이 정상적으로 표시되었습니다:", title_text)

        # 팝업 닫기
        popup_page.close()

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_12_Agreement_Step_Marketing_Consent_Link_Navigation_ko(page: Page):
        """ 약관 동의 단계 - 이벤트 및 마케팅 활용동의 링크 이동 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 팝업 이벤트 대기
        with page.expect_popup() as popup_info:
            # 상세보기 링크 클릭
            page.locator('a[href="/ko/policy/privacy-event-agree"]').click()

        # 새로 열린 팝업 페이지 가져오기
        popup_page = popup_info.value

        # 팝업 페이지가 완전히 로드될 때까지 대기 (networkidle 추가)
        popup_page.wait_for_load_state('load')
        popup_page.wait_for_load_state('networkidle')

        # 팝업 페이지 URL 가져오기
        popup_url = popup_page.url
        expected_url = 'https://www.lezhin.com/ko/policy/privacy-event-agree'
        print(f"팝업 페이지 URL: {popup_url}")

        # 예상 기대결과와 실제 결과 비교
        assert popup_url == expected_url, f"Expected: {expected_url}, but got: {popup_url}"

        # 약관 제목 요소 대기 및 가져오기
        title_locator = popup_page.locator('.law.lzCntnr h2').first
        popup_page.wait_for_selector('.law.lzCntnr h2', timeout=5000)
        assert title_locator.is_visible(), "약관 제목이 팝업 페이지에 표시되지 않습니다."

        # 텍스트 내용 확인
        title_text = title_locator.text_content() or ""  # None 방지
        title_text = title_text.strip()
        expected_text = "이벤트 및 마케팅 활용"

        # 예상 결과와 비교
        print('예상 결과:', expected_text)
        print('실제 결과:', title_text)
        assert title_text == expected_text, f"Expected: '{expected_text}', but got: '{title_text}'"

        # 결과 출력
        print("✅ 팝업 페이지 약관 제목이 정상적으로 표시되었습니다:", title_text)

        # 팝업 닫기
        popup_page.close()

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_13_Email_Input_Step_Verification_Message_Check_ko(page: Page):
        """ 이메일 입력 단계 - 문구 확인 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 이메일 입력 단계에서 '위 이메일로 인증번호가 발송됩니다.' 메시지가 있는지 확인
        message = page.wait_for_selector('#login-email-verify-desc')

        # 타이틀 메시지의 텍스트 가져오기
        message_text = message.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '위 이메일로 인증번호가 발송됩니다.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', message_text)
        assert message_text == expected_text, f"Expected: {expected_text}, but got: {message_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_14_Email_Input_Step_Verification_Message_Check_en(page: Page):
        """ 이메일 입력 단계 - 문구 확인 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 이메일 입력 단계에서 '위 이메일로 인증번호가 발송됩니다.' 메시지가 있는지 확인
        message = page.wait_for_selector('#login-email-verify-desc')

        # 타이틀 메시지의 텍스트 가져오기
        message_text = message.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'A verification code will be sent to the email above.'
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', message_text)
        assert message_text == expected_text, f"Expected: {expected_text}, but got: {message_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_15_Email_Input_Step_Empty_Email_ko(page: Page):
        """ 이메일 입력 단계 - 이메일 미입력 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', '')
        page.click('body')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '로그인에 사용하실 이메일을 입력해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 인증메일 발송 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_16_Email_Input_Step_Empty_Email_en(page: Page):
        """ 이메일 입력 단계 - 이메일 미 입력 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', '')
        page.click('body')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Please enter the email you want to use for your account.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 인증메일 발송 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_17_Email_Input_Step_Invalid_Email_Format_ko(page: Page):
        """ 이메일 입력 단계 - 잘못된 이메일 형식 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lily')
        page.click('body')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '이메일을 정확하게 입력해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 인증메일 발송 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_18_Email_Input_Step_Invalid_Email_Format_en(page: Page):
        """ 이메일 입력 단계 - 잘못된 이메일 형식 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', '')
        page.click('body')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Please enter the email you want to use for your account.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 인증메일 발송 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_19_Email_Input_Step_Already_Registered_Email_ko(page: Page):
        """ 이메일 입력 단계 - 이미 가입된 계정 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa02@gmail.com')
        page.click('#send-verify-email-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '이미 가입된 이메일입니다. '
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 인증메일 발송 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_20_Email_Input_Step_Already_Registered_Email_en(page: Page):
        """ 이메일 입력 단계 - 이미 가입된 계정 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa02@gmail.com')
        page.click('#send-verify-email-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'This email is already registered. '
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 인증메일 발송 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '인증메일 발송' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_21_Email_Input_Step_Domain_Blocked_ko(page: Page):
        """ 이메일 입력 단계 - 도메인 차단 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 차단된 도메인 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa01@ezweb.ne.jp')
        page.click('#send-verify-email-btn')


        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '지원하지 않는 이메일입니다.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_22_Email_Input_Step_Domain_Blocked_en(page: Page):
        """ 이메일 입력 단계 - 도메인 차단 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 차단된 도메인 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lezhin@eoopy.com')
        page.click('#send-verify-email-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'The email you have provided is not supported on our site. Please use another email and try again.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_23_Email_Input_Step_Valid_Email_ko(page: Page):
        """ 이메일 입력 단계 - 유효한 이메일 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa002@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-verify-done')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '위 이메일로 인증번호가 발송되었습니다.메일이 계속 오지 않는다면, 스팸 메일함을 확인해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_24_Email_Input_Step_Valid_Email_en(page: Page):
        """ 이메일 입력 단계 - 유효한 이메일 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa1017@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-verify-done')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'A verification code has been sent to the email above.If you have failed to receive an email, please check your spam.'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_25_Verification_Code_Resend_Button_Activation_ko(page: Page):
        """ 인증번호 재발송 버튼 활성화 확인 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa003@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 재발송 버튼이 나타날 때까지 최대 1초 대기
        resend_verify_email_button = page.wait_for_selector('#resend-verify-email-btn', timeout=1000)

        # 10초 대기
        page.wait_for_timeout(10000)

        # 재발송 버튼 활성화 여부 확인
        is_enabled = resend_verify_email_button.is_enabled()

        if is_enabled:
            print('10초 후에 재발송 버튼이 활성화되었습니다.')
        else:
            print('10초 후에 재발송 버튼이 활성화되지 않았습니다.')
            assert False, "10초 후에도 재발송 버튼이 활성화되지 않았습니다."
    
        # 페이지 종료
        page.close()

def test_SIGNUP_EM_26_Verification_Code_Resend_Email_Sent_ko(page: Page):
        """ 인증번호 재발송 - 재발송 메일 발송 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        email = 'lilyqa0007@maildrop.cc'
        page.fill('input[name="username"]', email)
        page.click('#send-verify-email-btn')

        # 재발송 버튼이 나타날 때까지 대기
        resend_verify_email_button = page.wait_for_selector('#resend-verify-email-btn', timeout=1000)
        page.wait_for_timeout(10000)  # 10초 대기

        if not resend_verify_email_button.is_enabled():
            assert False, "10초 후에도 재발송 버튼이 활성화되지 않았습니다."

        print("10초 후 재발송 버튼이 활성화되었습니다.")

        # 첫 번째 인증번호 추출
        new_page = context.new_page()
        new_page.goto(f'https://maildrop.cc/inbox/?mailbox={email.split("@")[0]}')
        new_page.wait_for_load_state('load', timeout=60000)

        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                first_code = auth_code_match.group(0)
                print(f"첫 번째 인증번호: {first_code}")
            else:
                assert False, "첫 번째 인증번호를 추출하지 못했습니다."
        else:
            assert False, "iframe srcdoc을 가져올 수 없습니다."

        new_page.close()

        # 재발송 버튼 클릭
        page.click('#resend-verify-email-btn')

        # 두 번째 인증번호 추출
        new_page = context.new_page()
        new_page.goto(f'https://maildrop.cc/inbox/?mailbox={email.split("@")[0]}')
        new_page.wait_for_load_state('load', timeout=60000)

        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                second_code = auth_code_match.group(0)
                print(f"두 번째 인증번호: {second_code}")
            else:
                assert False, "두 번째 인증번호를 추출하지 못했습니다."
        else:
            assert False, "iframe srcdoc을 가져올 수 없습니다."

        new_page.close()

       # 인증번호 비교
        assert first_code == second_code, "재발송된 인증번호가 기존 인증번호와 동일하지 않습니다."

        print("테스트 성공: 인증번호가 동일합니다.")
        
        # 페이지 종료
        page.close()

def test_SIGNUP_EM_27_Verification_Code_Send_Limit_10_Per_Day_ko(page: Page):
        """ 인증 번호 발송 - 10회 제한 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context
        request = context.request

        # 요청 URL 및 헤더 설정
        url = "https://www.lezhin.com/lz-api/v2/verifications/send-mail"
        headers = {
            "Content-Type": "application/json",
            "x-lz-adult": "0",
            "x-lz-allowadult": "false",
            "x-lz-country": "kr",
            "x-lz-genres": "",
            "x-lz-locale": "ko-KR"
        }

        # 이메일 설정
        email = "lilyqa1236@maildrop.cc"

        # 10회 반복 실행
        for i in range(10):
            response = request.post(
                url,
                data={"email": email},
                headers=headers
            )

            # 응답 상태 및 내용 출력
            print(f"요청 {i + 1}: 상태코드 - {response.status}")
            print("응답 내용:", response.json())

        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa1236@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
            
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '인증메일 발송은 1일 10회만 가능합니다.'
            
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_28_Verification_Code_Send_Limit_10_Per_Day_en(page: Page):
        """ 인증 번호 발송 - 10회 제한 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context
        request = context.request

        # 요청 URL 및 헤더 설정
        url = "https://www.lezhin.com/lz-api/v2/verifications/send-mail"
        headers = {
            "Content-Type": "application/json",
            "x-lz-adult": "0",
            "x-lz-allowadult": "false",
            "x-lz-country": "us",
            "x-lz-genres": "",
            "x-lz-locale": "en-US"
        }

        # 이메일 설정
        email = "lilyqa1238@maildrop.cc"

        # 10회 반복 실행
        for i in range(10):
            response = request.post(
                url,
                data={"email": email},
                headers=headers
            )

            # 응답 상태 및 내용 출력
            print(f"요청 {i + 1}: 상태코드 - {response.status}")
            print("응답 내용:", response.json())

        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa1238@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-email-msg')

        # 얼럿 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
            
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Email verifications can only be requested up to 10 times in one day.'
            
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close()


def test_SIGNUP_EM_29_Verification_Code_Input_Step_Text_Input_ko(page: Page):
        """ 인증번호 입력 단계 - 문자 입력 """
        # 회원가입 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'llilyqa010@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 인증번호 입력 필드에 문자 입력
        page.fill('#verify-code-input', '가나다라')

        # 입력된 값 가져오기
        input_value = page.input_value('#verify-code-input')

        # 결과 출력 및 검증
        if input_value != '가나다라':
            print("✅ 문자 입력이 되지 않습니다.")
        else:
            print(f"❌ 문자가 입력되었습니다. 입력값: {input_value}")

        # 검증 (문자가 입력되었을 경우 실패 처리)
        assert input_value != '가나다라', f"❌ 문자가 입력되었습니다. 입력값: {input_value}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_30_Verification_Code_Input_Step_Less_Than_4_Digits_ko(page: Page):
        """ 인증번호 입력 단계 - 4자리 이하 입력 """
        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'llilyqa009@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 인증번호 입력 필드에 문자 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', '1234')
        page.click('body')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#verify-code-error')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '인증번호를 정확하게 입력해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # '다음'버튼 선택자
        button_selector = '#verify-code-next-btn'

        # '다음' 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        if is_disabled:
            print("✅ '다음' 버튼이 비활성화 상태입니다.")
        else:
            print("❌ '다음' 버튼이 비활성화 상태가 아닙니다.")

        # 검증 (비활성화 상태가 아닐 경우 실패 처리)
        assert is_disabled, "❌ '다음' 버튼이 비활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_30_Verification_Code_Input_Step_Less_Than_3_Digits_en(page: Page):
        """ 인증 번호 입력 단계 - 3자리 이하 입력 """
        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa011@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 인증번호 입력 필드에 문자 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', '123')

        # 인증메일 발송 버튼 선택자
        button_selector = '#send-verify-email-btn'

        # 인증메일 발송 버튼이 비활성화 상태인지 확인
        button = page.locator(button_selector)
        is_disabled = button.is_disabled()

        # 결과 출력 및 검증
        print(f"'인증메일 발송' 버튼 비활성화 상태: {is_disabled}")
        assert is_disabled, "'인증메일 발송' 버튼이 비활성화 상태가 아닙니다."

        #아무데나 클릭
        page.click('body')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#verify-code-error')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Please enter the accurate verification code.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_31_Verification_Code_Input_Step_More_Than_6_Digits_ko(page: Page):
        """ 인증번호 입력 단계 - 6자리 초과 입력 """
        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa008@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 인증번호 입력 필드에 문자 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', '12345678')
        
        # 입력된 값 가져오기
        input_value = page.input_value('#verify-code-input')

        # 6자리까지만 입력되는지 확인
        assert len(input_value) <= 6, f"Expected length <= 6, but got: {len(input_value)}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_32_Verification_Code_Input_Step_Invalid_Code_ko(page: Page):
        """ 인증번호 입력 단계 - 잘못된 인증번호 """
        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5000@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 인증번호 입력 필드에 문자 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', '123456')
        page.click('#verify-code-next-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#verify-code-error')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '인증번호를 정확하게 입력해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # '다음' 버튼 선택자
        button_selector = '#verify-code-next-btn'

        # '다음' 버튼 요소 가져오기
        button = page.locator(button_selector)

        # '다음' 버튼이 활성화 상태인지 확인
        is_enabled = not button.is_disabled()

        # 결과 출력 및 검증
        if is_enabled:
            print("✅ '다음' 버튼이 활성화 상태입니다.")
        else:
            print("❌ '다음' 버튼이 비활성화 상태입니다.")

        # 검증 (활성화 상태가 아닐 경우 실패 처리)
        assert is_enabled, "❌ '다음' 버튼이 활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_33_Verification_Code_Input_Step_Invalid_Code_en(page: Page):
        """ 인증번호 입력 단계 - 잘못된 인증번호 """
        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)
     
        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5001@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 인증번호 입력 필드에 문자 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', '123456')
        page.click('#verify-code-next-btn')

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#verify-code-error')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Please enter the accurate verification code.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # '다음' 버튼 선택자
        button_selector = '#verify-code-next-btn'

        # '다음' 버튼 요소 가져오기
        button = page.locator(button_selector)

        # '다음' 버튼이 활성화 상태인지 확인
        is_enabled = not button.is_disabled()

        # 결과 출력 및 검증
        if is_enabled:
            print("✅ '다음' 버튼이 활성화 상태입니다.")
        else:
            print("❌ '다음' 버튼이 비활성화 상태입니다.")

        # 검증 (활성화 상태가 아닐 경우 실패 처리)
        assert is_enabled, "❌ '다음' 버튼이 활성화 상태가 아닙니다."

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_34_Password_Input_Step_UI_Validation_ko(page: Page):
        """ 비밀번호 입력 단계 - UI 확인 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5002@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5002')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # UI 확인
        email_sign_up_heading = page.locator('h2.auth__heading:has-text("이메일로 회원가입")')
        assert email_sign_up_heading.is_visible(), "Error: '이메일로 회원가입' 헤딩이 보이지 않습니다."
        print("Success: '이메일로 회원가입' 헤딩이 확인되었습니다.")

        verification_complete_message = page.locator('#login-email-verify-complete')
        verification_complete_message.wait_for(state='visible', timeout=10000)
        assert verification_complete_message.text_content() == '이메일 인증완료!', "Error: '이메일 인증완료!' 메시지가 보이지 않습니다."
        print("Success: '이메일 인증완료!' 메시지가 확인되었습니다.")

        email_input = page.locator('#login-email')
        assert email_input.is_visible(), "Error: 이메일 입력 필드가 보이지 않습니다."
        assert email_input.input_value() == 'lilyqa5002@maildrop.cc', f"Error: 이메일 입력 필드 값이 잘못되었습니다. Expected: 'lilyqa5002@maildrop.cc', Got: '{email_input.input_value()}'"
        print("Success: 이메일 입력 필드가 확인되었습니다.")

        password_label = page.locator('label[for="login-password"]')
        assert password_label.is_visible(), "Error: 비밀번호 레이블이 보이지 않습니다."
        assert password_label.text_content() == '비밀번호(영문, 숫자, 특수문자 포함 8자 이상)', "Error: 비밀번호 레이블 텍스트가 잘못되었습니다."
        print("Success: 비밀번호 레이블이 확인되었습니다.")

        legend = page.locator('legend.signUp__legend')
        assert legend.is_visible(), "Error: '선택정보' 레전드가 보이지 않습니다."
        assert legend.text_content() == '선택정보', "Error: '선택정보' 레전드 텍스트가 잘못되었습니다."
        print("Success: '선택정보' 레전드가 확인되었습니다.")

        gender_fieldset = page.locator('fieldset.login__gender')
        assert gender_fieldset.is_visible(), "Error: 성별 선택 필드셋이 보이지 않습니다."
        print("Success: 성별 선택 필드셋이 확인되었습니다.")

        gender_legend = gender_fieldset.locator('legend.signUp__label')
        assert gender_legend.text_content() == '성별', "Error: '성별' 레전드 텍스트가 잘못되었습니다."
        print("Success: '성별' 레전드 텍스트가 확인되었습니다.")

        female_radio = gender_fieldset.locator('label.lzRadio:has-text("여성")')
        male_radio = gender_fieldset.locator('label.lzRadio:has-text("남성")')
        assert female_radio.is_visible(), "Error: '여성' 라디오 버튼이 보이지 않습니다."
        assert male_radio.is_visible(), "Error: '남성' 라디오 버튼이 보이지 않습니다."
        print("Success: '여성' 및 '남성' 라디오 버튼이 확인되었습니다.")

        assert not female_radio.locator('input[type="radio"]').is_checked(), "Error: '여성' 라디오 버튼이 체크되어 있습니다."
        assert not male_radio.locator('input[type="radio"]').is_checked(), "Error: '남성' 라디오 버튼이 체크되어 있습니다."
        print("Success: 라디오 버튼 초기 상태가 확인되었습니다.")

        birthdate_fieldset = page.locator('fieldset#signup-birthday')
        assert birthdate_fieldset.is_visible(), "Error: 생년월일 필드셋이 보이지 않습니다."
        print("Success: 생년월일 필드셋이 확인되었습니다.")

        birthdate_legend = birthdate_fieldset.locator('legend.signUp__label')
        assert birthdate_legend.text_content() == '생년월일', "Error: '생년월일' 레전드 텍스트가 잘못되었습니다."
        print("Success: '생년월일' 레전드 텍스트가 확인되었습니다.")

        year_select = birthdate_fieldset.locator('select[name="birthYear"]')
        month_select = birthdate_fieldset.locator('select[name="birthMonth"]')
        day_select = birthdate_fieldset.locator('select[name="birthDay"]')
        assert year_select.is_visible(), "Error: '년' 드롭다운이 보이지 않습니다."
        assert month_select.is_visible(), "Error: '월' 드롭다운이 보이지 않습니다."
        assert day_select.is_visible(), "Error: '일' 드롭다운이 보이지 않습니다."
        print("Success: '년', '월', '일' 드롭다운이 확인되었습니다.")

        assert year_select.input_value() == '0', "Error: '년' 드롭다운 초기 값이 잘못되었습니다."
        assert month_select.input_value() == '0', "Error: '월' 드롭다운 초기 값이 잘못되었습니다."
        assert day_select.input_value() == '0', "Error: '일' 드롭다운 초기 값이 잘못되었습니다."
        print("Success: '년', '월', '일' 드롭다운 초기 값이 확인되었습니다.")

        privacy_checkbox_label = page.locator('label.lzCheck:has-text("개인정보 수집 및 이용동의")')
        assert privacy_checkbox_label.is_visible(), "Error: 개인정보 수집 및 이용동의 라벨이 보이지 않습니다."
        assert '개인정보 수집 및 이용동의' in privacy_checkbox_label.text_content(), "Error: 개인정보 수집 및 이용동의 라벨 텍스트가 잘못되었습니다."
        print("Success: 개인정보 수집 및 이용동의 라벨이 확인되었습니다.")

        privacy_checkbox = privacy_checkbox_label.locator('input[type="checkbox"]')
        assert privacy_checkbox.is_disabled(), "Error: 개인정보 수집 및 이용동의 체크박스가 비활성화 상태가 아닙니다."
        assert not privacy_checkbox.is_checked(), "Error: 개인정보 수집 및 이용동의 체크박스가 체크된 상태입니다."
        print("Success: 개인정보 수집 및 이용동의 체크박스가 확인되었습니다.")

        sign_up_button = page.locator('button.lzBtn--major[type="submit"]:has-text("이메일로 회원 가입")')
        assert sign_up_button.is_visible(), "Error: '이메일로 회원 가입' 버튼이 보이지 않습니다."
        assert sign_up_button.text_content() == '이메일로 회원 가입', "Error: '이메일로 회원 가입' 버튼 텍스트가 잘못되었습니다."
        assert sign_up_button.is_disabled(), "Error: '이메일로 회원 가입' 버튼이 비활성화 상태가 아닙니다."
        print("Success: '이메일로 회원 가입' 버튼이 확인되었습니다.")

        help_text = page.locator('p.account__help')
        assert help_text.is_visible(), "Error: 도움말 텍스트가 보이지 않습니다."

        # 텍스트 내용 가져와서 공백과 줄바꿈 제거
        actual_text = help_text.text_content().replace('\n', '').replace('  ', '').strip()
        expected_text = '이용 중 도움이 필요하시면 [고객지원] 페이지로, 로그인에 문제가 있다면 help@lezhin.com으로 문의해 주세요.'

        # 예상 텍스트와 실제 텍스트 비교
        print('예상 결과:', expected_text)
        print('실제 결과:', actual_text)
        assert actual_text == expected_text, f"Error: 도움말 텍스트가 잘못되었습니다.\nExpected: '{expected_text}'\nGot: '{actual_text}'"
        
        print("Success: 도움말 텍스트가 확인되었습니다.")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_35_Password_Input_Step_UI_Validation_en(page: Page):
        """ 비밀번호 입력 단계 - UI 확인 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5003@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5003')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # UI 확인
        sign_up_heading = page.locator('h2.auth__heading:has-text("Sign Up")').nth(0)
        assert sign_up_heading.is_visible(), "Error: 'Sign Up' 헤딩이 보이지 않습니다."
        print("Success: 'Sign Up' 헤딩이 확인되었습니다.")

        verification_complete_message = page.locator('#login-email-verify-complete')
        verification_complete_message.wait_for(state='visible', timeout=10000)
        assert verification_complete_message.text_content() == 'Email verification complete!', "Error: 'Email verification complete!' 메시지가 보이지 않습니다."
        print("Success: 'Email verification complete!' 메시지가 확인되었습니다.")

        email_input = page.locator('#login-email')
        assert email_input.is_visible(), "Error: 이메일 입력 필드가 보이지 않습니다."
        assert email_input.input_value() == 'lilyqa5003@maildrop.cc', f"Error: 이메일 입력 필드 값이 잘못되었습니다. Expected: 'lilyqa5003@maildrop.cc', Got: '{email_input.input_value()}'"
        print("Success: 이메일 입력 필드가 확인되었습니다.")

        password_label = page.locator('label[for="login-password"]')
        assert password_label.is_visible(), "Error: 비밀번호 레이블이 보이지 않습니다."
        assert password_label.text_content() == 'Password(Min. 8 characters including letters, numbers and more than 1 special character(e.g.!@#$))', "Error: 비밀번호 레이블 텍스트가 잘못되었습니다."
        print("Success: 비밀번호 레이블이 확인되었습니다.")

        legend = page.locator('legend.signUp__legend')
        assert legend.is_visible(), "Error: 'Optional Information' 레전드가 보이지 않습니다."
        assert legend.text_content() == 'Optional Information', "Error: 'Optional Information' 레전드 텍스트가 잘못되었습니다."
        print("Success: 'Optional Information' 레전드가 확인되었습니다.")

        gender_fieldset = page.locator('fieldset.login__gender')
        assert gender_fieldset.is_visible(), "Error: 성별 선택 필드셋이 보이지 않습니다."
        print("Success: 성별 선택 필드셋이 확인되었습니다.")

        gender_legend = gender_fieldset.locator('legend.signUp__label')
        assert gender_legend.text_content() == 'Gender', "Error: 'Gender' 레전드 텍스트가 잘못되었습니다."
        print("Success: 'Gender' 레전드 텍스트가 확인되었습니다.")

        female_radio = gender_fieldset.locator('label.lzRadio:has-text("Female")')
        male_radio_label = page.locator('fieldset.login__gender').locator('label.lzRadio:has-text("Male")').nth(1)
        assert female_radio.is_visible(), "Error: 여성 라디오 버튼이 보이지 않습니다."
        assert male_radio_label.is_visible(), "Error: 남성 라디오 버튼이 보이지 않습니다."
        print("Success: 'Female' 및 'Male' 라디오 버튼이 확인되었습니다.")
       

        # 선택된 라디오 버튼이 없는지 확인 (기본 상태 검사)
        assert not female_radio.locator('input[type="radio"]').is_checked(), "Error: 여성 라디오 버튼이 기본 상태에서 선택되어 있습니다."
        assert not male_radio_label.locator('input[type="radio"]').is_checked(), "Error: 남성 라디오 버튼이 기본 상태에서 선택되어 있습니다."
        print("Success: 라디오 버튼 초기 상태가 확인되었습니다.")

        birthdate_fieldset = page.locator('fieldset#signup-birthday')
        assert birthdate_fieldset.is_visible(), "Error: 생년월일 필드셋이 보이지 않습니다."
        print("Success: 생년월일 필드셋이 확인되었습니다.")

        birthdate_legend = birthdate_fieldset.locator('legend.signUp__label')
        assert birthdate_legend.text_content() == 'Date of Birth', "Error: 'Date of Birth' 레전드 텍스트가 잘못되었습니다."
        print("Success: 'Date of Birth' 레전드 텍스트가 확인되었습니다.")

        month_select = birthdate_fieldset.locator('select[name="birthMonth"]')
        day_select = birthdate_fieldset.locator('select[name="birthDay"]')
        year_select = birthdate_fieldset.locator('select[name="birthYear"]')
        assert month_select.is_visible(), "Error: '월' 드롭다운이 보이지 않습니다."
        assert day_select.is_visible(), "Error: '일' 드롭다운이 보이지 않습니다."
        assert year_select.is_visible(), "Error: '년' 드롭다운이 보이지 않습니다."
        print("Success: '월', '일', '년' 드롭다운이 확인되었습니다.")

        assert month_select.input_value() == '0', "Error: '월' 드롭다운 초기 값이 잘못되었습니다."
        assert day_select.input_value() == '0', "Error: '일' 드롭다운 초기 값이 잘못되었습니다."
        assert year_select.input_value() == '0', "Error: '년' 드롭다운 초기 값이 잘못되었습니다."
        print("Success: '월', '일', '년' 드롭다운 초기 값이 확인되었습니다.")

        privacy_checkbox_label = page.locator('label.lzCheck:has-text("Collection and Use of Personal Information")')
        assert privacy_checkbox_label.is_visible(), "Error: 개인정보 수집 및 이용동의 라벨이 보이지 않습니다."
        assert 'Collection and Use of Personal Information' in privacy_checkbox_label.text_content(), "Error: Collection and Use of Personal Information 라벨 텍스트가 잘못되었습니다."
        print("Success: Collection and Use of Personal Information 라벨이 확인되었습니다.")

        privacy_checkbox = privacy_checkbox_label.locator('input[type="checkbox"]')
        assert privacy_checkbox.is_disabled(), "Error: 개인정보 수집 및 이용동의 체크박스가 비활성화 상태가 아닙니다."
        assert not privacy_checkbox.is_checked(), "Error: 개인정보 수집 및 이용동의 체크박스가 체크된 상태입니다."
        print("Success: 개인정보 수집 및 이용동의 체크박스가 확인되었습니다.")

        sign_up_button = page.locator('button.lzBtn--major[type="submit"]:has-text("Sign up with email")')
        assert sign_up_button.is_visible(), "Error: 'Sign up with email' 버튼이 보이지 않습니다."
        assert sign_up_button.text_content() == 'Sign up with email', "Error: 'Sign up with email' 버튼 텍스트가 잘못되었습니다."
        assert sign_up_button.is_disabled(), "Error: 'Sign up with email' 버튼이 비활성화 상태가 아닙니다."
        print("Success: 'Sign up with email' 버튼이 확인되었습니다.")

        help_text = page.locator('p.account__help')
        assert help_text.is_visible(), "Error: 도움말 텍스트가 보이지 않습니다."

        # 텍스트 내용 가져와서 공백과 줄바꿈 제거
        actual_text = help_text.text_content().replace('\n', '').replace('  ', '').strip()
        expected_text = 'Go to [Customer Support] for help, and contact us through help_us@lezhin.com if you are having trouble logging in.'

        # 예상 텍스트와 실제 텍스트 비교
        print('예상 결과:', expected_text)
        print('실제 결과:', actual_text)
        assert actual_text == expected_text, f"Error: 도움말 텍스트가 잘못되었습니다.\nExpected: '{expected_text}'\nGot: '{actual_text}'"

        print("Success: 도움말 텍스트가 확인되었습니다.")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_36_Password_Input_Step_Validation_ko(page: Page):
        """ 비밀번호 입력 단계 - 비밀번호 유효성 체크 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5004@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5004')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 미입력 후 로그인 시도
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('')  # 비밀번호 입력란을 빈 문자열로 채움
        page.get_by_text('이메일로 회원가입').click() 

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '로그인에 사용하실 비밀번호를 입력해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 비밀번호 8자리 미만 입력 후 로그인 시도
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin@')
        page.get_by_text('이메일로 회원가입').click() 

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '영문, 숫자 및 특수문자 포함 8자 이상으로 입력해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 비밀번호 영문로만 입력 후 로그인 시도
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhintest')
        page.get_by_text('이메일로 회원가입').click() 

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = '영문, 숫자 및 특수문자 포함 8자 이상으로 입력해주세요.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 비밀번호가 기본적으로 마스킹되어 있는지 확인 (type="password")
        password_type = password_input.get_attribute('type')
        assert password_type == 'password', "Error: 비밀번호가 기본적으로 마스킹되지 않았습니다."
        print("Password is correctly masked (type='password').")

        # 패스워드 토글 버튼 클릭
        page.click('.login__passwordToggle')

        # 비밀번호가 마스킹 해제되었는지 확인 (type="text")
        password_type_after_toggle = password_input.get_attribute('type')
        assert password_type_after_toggle == 'text', "Error: 비밀번호가 마스킹 해제되지 않았습니다."
        print("Password is correctly unmasked (type='text').")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_37_Password_Input_Step_Validation_en(page: Page):
        """ 비밀번호 입력 단계 - 비밀번호 유효성 체크 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체동의 체크박스가 나타날 때까지 대기
        agree_all_checkbox_selector = 'label.lzCheck input.agree-tos'
        
        # 전체동의 체크
        page.click('text="Agree to the Lezhin Comics Terms of Use"')

        # 동의 버튼 클릭
        page.click('button[data-ga-event-label="버튼_약관동의_확인"]')

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5005@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5005')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 미입력 후 로그인 시도
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('')  # 비밀번호 입력란을 빈 문자열로 채움
        page.locator("div").filter(has_text="Sign up with email").click()

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Please enter the password you want to login with.'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 비밀번호 8자리 미만 입력 후 로그인 시도
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin@')
        page.locator("div").filter(has_text="Sign up with email").click()

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Min. 8 characters including letters, numbers and more than 1 special character(e.g.!@#$)'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

        # 비밀번호 영문로만 입력 후 로그인 시도
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhintest')
        page.locator("div").filter(has_text="Sign up with email").click()

        # 얼럿 메시지 노출 대기
        alert = page.wait_for_selector('#login-password-msg')

        # 타이틀 메시지의 텍스트 가져오기
        alert_text = alert.text_content()
   
        # 예상되는 텍스트를 expectedText 변수에 선언하여 저장
        expected_text = 'Min. 8 characters including letters, numbers and more than 1 special character(e.g.!@#$)'
        
        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_text)
        print('실제 결과:', alert_text)
        assert alert_text == expected_text, f"Expected: {expected_text}, but got: {alert_text}"

         # 비밀번호가 기본적으로 마스킹되어 있는지 확인 (type="password")
        password_type = password_input.get_attribute('type')
        assert password_type == 'password', "Error: 비밀번호가 기본적으로 마스킹되지 않았습니다."
        print("Password is correctly masked (type='password').")

        # 패스워드 토글 버튼 클릭
        page.click('.login__passwordToggle')

        # 비밀번호가 마스킹 해제되었는지 확인 (type="text")
        password_type_after_toggle = password_input.get_attribute('type')
        assert password_type_after_toggle == 'text', "Error: 비밀번호가 마스킹 해제되지 않았습니다."
        print("Password is correctly unmasked (type='text').")


        # 페이지 종료
        page.close()

def test_SIGNUP_EM_38_Additional_Info_Input_Step_Birthdate_UI_ko(page: Page):
        """ 추가 정보 입력 단계 - 생년월일 UI """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5006@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5006')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

       # 입력할 '년', '월', '일' 값
        year = '1993'
        month = '08'
        day = '16'

        # '년' 선택
        page.select_option('select[name="birthYear"]', year)
        # '월' 선택
        page.select_option('select[name="birthMonth"]', month)
        # '일' 선택
        page.select_option('select[name="birthDay"]', day)

        # 콘솔에 입력된 년월일을 표시
        print(f"입력된 년월일: {year}-{month}-{day}")

        # 체크박스가 페이지에 로드될 때까지 대기
        page.wait_for_selector('input[name="agree_privacy"]')

        # "개인정보 수집 및 이용동의" 체크박스의 활성화 상태를 확인
        is_enabled = page.is_enabled('input[name="agree_privacy"]')

        if is_enabled:
            print("개인정보 수집 및 이용동의 체크박스는 활성화 상태입니다.")
        else:
            print("개인정보 수집 및 이용동의 체크박스가 비활성화 상태입니다. 검사가 필요합니다.")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_39_Additional_Info_Input_Step_Birthdate_UI_en(page: Page):
        """ 추가 정보 입력 단계 - 생년월일 UI """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체동의 체크박스가 나타날 때까지 대기
        agree_all_checkbox_selector = 'label.lzCheck input.agree-tos'

        # 전체동의 체크
        page.click('text="Agree to the Lezhin Comics Terms of Use"')

        # 동의 버튼 클릭
        page.click('button[data-ga-event-label="버튼_약관동의_확인"]')

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5007@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5007')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load')

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."

        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

       # 입력할 '년', '월', '일' 값
        month = '08'
        year = '1993'
        day = '16'

        # '월' 선택
        page.select_option('select[name="birthMonth"]', month)
        # '년' 선택
        page.select_option('select[name="birthYear"]', year)
        # '일' 선택
        page.select_option('select[name="birthDay"]', day)

        # 콘솔에 입력된 년월일을 표시
        print(f"입력된 년월일: {month}-{year}-{day}")

        # 체크박스가 페이지에 로드될 때까지 대기
        page.wait_for_selector('input[name="agree_privacy"]')

        # "개인정보 수집 및 이용동의" 체크박스의 활성화 상태를 확인
        is_enabled = page.is_enabled('input[name="agree_privacy"]')

        if is_enabled:
            print("개인정보 수집 및 이용동의 체크박스는 활성화 상태입니다.")
        else:
            print("개인정보 수집 및 이용동의 체크박스가 비활성화 상태입니다. 검사가 필요합니다.")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_40_추Additional_Info_Input_Step_Gender_Selection_ko(page: Page):
        """ 추가 정보 입력 단계 - 성별 선택 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5008@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5008')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # '개인정보 수집 및 이용동의' 체크박스 비활성화 확인
        is_disabled = page.evaluate("() => {"
                                    "  const checkbox = document.querySelector('input[name=\"agree_privacy\"]');"
                                    "  return checkbox ? checkbox.disabled : false;"
                                    "}")

        if is_disabled:
            print("개인정보 수집 및 이용동의 체크박스는 비활성화 상태입니다.")
        else:
            print("개인정보 수집 및 이용동의 체크박스가 활성화 상태입니다. 검사가 필요합니다.")

        # '여성' 라디오 버튼 선택
        gender_fieldset = page.locator('fieldset.login__gender')
        female_radio = gender_fieldset.locator('label.lzRadio:has-text("여성")')
        female_radio.click()

        # '여성' 라디오 버튼이 체크되었는지 확인
        if female_radio.locator('input[type="radio"]').is_checked():
            print("여성 라디오 버튼이 체크되었습니다.")
        else:
            raise AssertionError("Error: 여성 라디오 버튼이 체크되지 않았습니다.")

        # "개인정보 수집 및 이용동의" 체크박스가 페이지에 로드될 때까지 대기
        page.wait_for_selector('input[name="agree_privacy"]')

        # "개인정보 수집 및 이용동의" 체크박스의 활성화 상태를 확인
        is_enabled = page.is_enabled('input[name="agree_privacy"]')

        if is_enabled:
            print("개인정보 수집 및 이용동의 체크박스는 활성화 상태입니다.")
        else:
            print("개인정보 수집 및 이용동의 체크박스가 비활성화 상태입니다. 검사가 필요합니다.")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_41_Additional_Info_Input_Step_Birthdate_Selection_ko(page: Page):
        """ 추가 정보 입력 단계 - 생년월일 선택 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5009@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5009')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # '개인정보 수집 및 이용동의' 체크박스 비활성화 확인
        is_disabled = page.evaluate("() => {"
                                    "  const checkbox = document.querySelector('input[name=\"agree_privacy\"]');"
                                    "  return checkbox ? checkbox.disabled : false;"
                                    "}")

        if is_disabled:
            print("개인정보 수집 및 이용동의 체크박스는 비활성화 상태입니다.")
        else:
            print("개인정보 수집 및 이용동의 체크박스가 활성화 상태입니다. 검사가 필요합니다.")

        # 생년월일 선택
        page.select_option('select[name="birthYear"]', '2011')  # 연도 선택
        page.select_option('select[name="birthMonth"]', '01')  # 월 선택 (예: 1월)
        page.select_option('select[name="birthDay"]', '01')  # 일 선택 (예: 1일)

        # 선택된 값 확인
        selected_year = page.locator('select[name="birthYear"]').input_value()
        selected_month = page.locator('select[name="birthMonth"]').input_value()
        selected_day = page.locator('select[name="birthDay"]').input_value()

        print(f"선택된 생년월일: {selected_year}-{selected_month}-{selected_day}")
        assert selected_year == '2011', "Error: 연도가 잘못 선택되었습니다."
        assert selected_month == '01', "Error: 월이 잘못 선택되었습니다."
        assert selected_day == '01', "Error: 일이 잘못 선택되었습니다."

        # "개인정보 수집 및 이용동의" 체크박스가 페이지에 로드될 때까지 대기
        page.wait_for_selector('input[name="agree_privacy"]')

        # "개인정보 수집 및 이용동의" 체크박스의 활성화 상태를 확인
        is_enabled = page.is_enabled('input[name="agree_privacy"]')

        if is_enabled:
            print("개인정보 수집 및 이용동의 체크박스는 활성화 상태입니다.")
        else:
            print("개인정보 수집 및 이용동의 체크박스가 비활성화 상태입니다. 검사가 필요합니다.")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_42_Additional_Info_Input_Step_Display_14_Years_Old_Birth_Year_ko(page: Page):
        """ 추가 정보 입력 단계 - 만 14세 출생년도 노출 확인 """
        from datetime import datetime
        # 브라우저 및 페이지 시작
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5010@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5010')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."

        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # 현재 연도에서 14를 빼 만 14세가 되는 년도를 계산
        current_year = datetime.now().year
        min_year = current_year - 14
        next_year = min_year + 1

        # 만 14세가 되는 년도가 선택박스에 존재하는지 확인
        is_min_year_available = page.query_selector(f'select[name="birthYear"] option[value="{min_year}"]') is not None
        # 만 14세가 되는 출생년도 이후 년도가 선택박스에 존재하지 않는지 확인
        is_next_year_not_available = page.query_selector(f'select[name="birthYear"] option[value="{next_year}"]') is None

        # 결과 로깅
        if is_min_year_available and is_next_year_not_available:
            print(f"테스트 성공: 만 14세가 되는 년도({min_year})는 존재하며, 그 이후의 년도({next_year})는 선택박스에 나오지 않습니다.")
        elif not is_min_year_available:
            print(f"테스트 실패: 만 14세가 되는 년도({min_year})가 선택박스에 존재하지 않습니다.")
        else:
            print(f"테스트 실패: 만 14세가 되는 년도 이후의 년도({next_year})가 선택박스에 존재합니다.")

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_43_Additional_Info_Input_Step_Privacy_Policy_Link_Navigation_ko(page: Page):
        """ 추가 정보 입력 단계 - 개인정보 수집 및 이용 동의 링크 이동 """
        
        from datetime import datetime
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5011@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5011')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."

        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # 생년월일 입력 단계에서 개인정보 수집 및 이용동의 '상세보기' 링크 이동 확인
        page.get_by_role('group').filter(has_text='개인정보 수집 및 이용동의').get_by_role('link', name='상세보기').click()
        
        # 상세보기 페이지 새탭으로 열릴때까지 대기
        page1_promise = page.wait_for_event('popup')
        page1 = page1_promise

        # 새 창이 로드될 때까지 대기
        page1.wait_for_load_state()

        # URL이 변경될 때까지 대기
        page1.wait_for_url('https://www.lezhin.com/ko/policy/birth-n-gender')

        # 현재 페이지의 URL을 가져와 문자열 변수 current_url에 저장
        current_url = page1.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhin.com/ko/policy/birth-n-gender'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_43_Additional_Info_Input_Step_Privacy_Policy_Link_Navigation_en(page: Page):
        """ 추가 정보 입력 단계 - 개인정보 수집 및 이용동의 링크 이동 """
        from datetime import datetime
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 전체동의 체크박스가 나타날 때까지 대기
        agree_all_checkbox_selector = 'label.lzCheck input.agree-tos'

        # 전체동의 체크
        page.click('text="Agree to the Lezhin Comics Terms of Use"')

        # 동의 버튼 클릭
        page.click('button[data-ga-event-label="버튼_약관동의_확인"]')

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5012@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5012')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # 생년월일 입력 단계에서 개인정보 수집 및 이용동의 '상세보기' 링크 이동 확인
        page.get_by_role('group').filter(has_text='Collection and Use of Personal Information').get_by_role('link', name='More').click()
        
        # 상세보기 페이지 새탭으로 열릴때까지 대기
        page1_promise = page.wait_for_event('popup')
        page1 = page1_promise

        # 새 창이 로드될 때까지 대기
        page1.wait_for_load_state()

        # URL이 변경될 때까지 대기
        page1.wait_for_url('https://www.lezhinus.com/en/policy/birth-n-gender')

        # 현재 페이지의 URL을 가져와 문자열 변수 current_url에 저장
        current_url = page1.url

        # 예상되는 페이지의 URL을 문자열로 선언하여 expected_url 변수에 저장
        expected_url = 'https://www.lezhinus.com/en/policy/birth-n-gender'

        # 예상 기대결과와 실제 결과를 비교하여 일치하는지 확인
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_44_Email_Signup_And_Deactivation_ko(page: Page):
        """ 이메일 가입 및 탈퇴 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhin.com/ko/signup?redirect=%2Fko')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5013@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5013')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # 생년월일, 성별 건너뛰고 '이메일로 회원가입' 버튼 클릭
        page.click('button[data-ga-event-label="버튼_회원가입"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기 (네트워크 안정성을 위해)
        page.wait_for_timeout(2000)

        # 현재 페이지의 URL을 가져와 비교
        current_url = page.url
        expected_url = 'https://www.lezhin.com/ko/welcome/email?redirect=%2Fko'
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 회원가입 완료 메시지 나타날 때까지 대기
        message = page.wait_for_selector('.auth__heading')
        message_text = message.text_content().strip()

        # 회원가입 완료 메시지 검증
        expected_text = '회원가입완료'
        print('예상 결과:', expected_text)
        print('실제 결과:', message_text)
        assert message_text == expected_text, f"Expected: {expected_text}, but got: {message_text}"

        # 회원가입 축하 메시지 나타날 때까지 대기
        message1 = page.wait_for_selector('.account.welcome > p')
        message_text1 = message1.text_content().strip()

        # 회원가입 축하 메시지 검증
        expected_text1 = '회원가입을 축하합니다. 지금부터 레진코믹스의 프리미엄 웹툰을 즐겨보세요!'
        print('예상 결과:', expected_text1)
        print('실제 결과:', message_text1)

        # 공백 제거 후 비교
        assert message_text1.replace(" ", "") == expected_text1.replace(" ", ""), \
          f"Expected: {expected_text1}, but got: {message_text1}"

        # 도움말 및 연락처 정보가 포함된 문단 선택 및 검증
        help_text = page.locator('p.account__help')
        assert help_text.is_visible(), "Error: 도움말 문단이 보이지 않습니다."

        expected_help_text = '이용 중 도움이 필요하시면 [고객지원] 페이지로, 로그인에 문제가 있다면 help@lezhin.com으로 문의해 주세요.'
        actual_help_text = help_text.text_content().strip()
        print('예상 결과:', expected_help_text)
        print('실제 결과:', actual_help_text)
        assert actual_help_text == expected_help_text, f"Error: 도움말 텍스트가 예상과 다릅니다. (Expected: {expected_help_text}, Actual: {actual_help_text})"

        # '확인' 버튼 클릭
        page.get_by_role('link', name='확인').click()

        # 현재 페이지의 URL을 다시 가져와 비교
        current_url = page.url
        expected_url_after_confirmation = 'https://www.lezhin.com/ko'
        print('예상 결과:', expected_url_after_confirmation)
        print('실제 결과:', current_url)
        assert current_url == expected_url_after_confirmation, f"Expected: {expected_url_after_confirmation}, but got: {current_url}"

        # 내 정보 페이지로 이동
        page.goto('https://www.lezhin.com/ko/account')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 이메일값 가져오기
        email = page.wait_for_selector('.email')

        # 이메일 텍스트 가져오기
        email_text = email.text_content()

        # 회원가입 완료 메시지 검증
        expected_text = 'lilyqa5013@maildrop.cc'
        print('예상 결과:', expected_text)
        print('실제 결과:', email_text)
        assert email_text == expected_text, f"Expected: {expected_text}, but got: {email_text}"

        # 인증하기 버튼 미노출
        certification_button = page.query_selector('.email-certification')

        # 버튼이 존재하는지 확인
        assert certification_button is not None, "Error: '인증하기' 버튼이 존재하지 않습니다."

        # 버튼이 hidden 상태인지 확인
        is_hidden = certification_button.evaluate("element => element.hasAttribute('hidden')")
        assert is_hidden, "Error: '인증하기' 버튼이 hidden 상태가 아닙니다."

        # "회원을 탈퇴하시겠습니까?" 버튼 클릭
        page.click('#toggle-unregister-form')

        # 탈퇴 사유 선택
        page.get_by_text('이용이 불편하고 장애가 많음').click()

        # 비밀번호 입력 필드 클릭 및 비밀번호 입력
        password_input = page.get_by_placeholder('비밀번호를 입력해 주세요.')
        password_input.click()
        password_input.fill('lezhin123@@')

        # 탈퇴하기 버튼 클릭
        page.get_by_text('탈퇴하기').click()

        # '확인' 버튼 클릭
        page.get_by_role('button', name='확인').click()

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # URL이 https://www.lezhin.com/ko/account/bye 로 변경될 때까지 대기
        expected_url = 'https://www.lezhin.com/ko/account/bye'
        page.wait_for_url(expected_url)

        # 현재 페이지의 URL을 가져와 비교
        current_url = page.url
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # '탈퇴 완료' 타이틀이 노출될 때까지 대기
        page.wait_for_selector('h2.bye__head')

        # '탈퇴 완료' 타이틀 요소 가져오기
        title_element = page.query_selector('h2.bye__head')
        assert title_element is not None, "'탈퇴 완료' 타이틀 요소를 찾을 수 없습니다."

        # 타이틀 텍스트 가져오기 및 검증
        title_text = title_element.text_content().strip()
        assert title_text == '탈퇴 완료', f"Error: 타이틀 텍스트가 예상과 다릅니다. (Expected: '탈퇴 완료', Actual: '{title_text}')"

        # '회원탈퇴가 완료되었습니다...' 문구가 노출될 때까지 대기
        page.wait_for_selector('.bye__body p')

        # 문구 요소 가져오기
        message_element = page.query_selector('.bye__body p')
        assert message_element is not None, "Error: 문구 요소를 찾을 수 없습니다."

        # 문구 텍스트 가져오기 및 검증
        message_text = message_element.text_content().strip()
        expected_message = '회원탈퇴가 완료되었습니다. 그 동안 레진코믹스를 이용해 주셔서 감사합니다.'

        # 검증
        print('예상 결과:', expected_message)
        print('실제 결과:', message_text)
        assert message_text == expected_message, f"Expected: {expected_message}, but got: {message_text}"

        # '레진코믹스 홈으로' 버튼 클릭
        page.get_by_role('link', name='레진코믹스 홈으로').click()

        # 현재 페이지의 URL 가져오기 및 검증
        current_url = page.url
        expected_url = 'https://www.lezhin.com/ko'
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()


def test_SIGNUP_EM_44_Email_Signup_And_Deactivation_en(page: Page):
        """ 이메일 가입 및 탈퇴 """
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 회원가입 페이지로 이동(공통 함수 사용)
        navigate_to(page, 'https://www.lezhinus.com/en/signup?redirect=%2Fen')

        # 쿠키 이용 동의 'Accept All' 클릭
        page.click('.lzBtnGrp.acceptCookies__btns')

        # 전체 동의 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_en(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5014@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5014')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # 생년월일, 성별 건너뛰고 '이메일로 회원가입' 버튼 클릭
        page.click('button[data-ga-event-label="버튼_회원가입"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기 (네트워크 안정성을 위해)
        page.wait_for_timeout(2000)

        # 현재 페이지의 URL을 가져와 비교
        current_url = page.url
        expected_url = 'https://www.lezhinus.com/en/welcome/email?redirect=%2Fen'
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 회원가입 완료 메시지 나타날 때까지 대기
        message = page.wait_for_selector('.auth__heading')
        message_text = message.text_content().strip()

        # 회원가입 완료 메시지 검증
        expected_text = 'Sign Up Complete'
        print('예상 결과:', expected_text)
        print('실제 결과:', message_text)
        assert message_text == expected_text, f"Expected: {expected_text}, but got: {message_text}"

        # 회원가입 축하 메시지 나타날 때까지 대기
        message1 = page.wait_for_selector('.account.welcome > p')
        message_text1 = message1.text_content().strip()

        # 회원가입 축하 메시지 검증
        expected_text1 = 'Congratulations! You may now enjoy our collection of premium webtoons at Lezhin Comics!'
        print('예상 결과:', expected_text1)
        print('실제 결과:', message_text1)

        # 공백 제거 후 비교
        assert message_text1.replace(" ", "") == expected_text1.replace(" ", ""), \
          f"Expected: {expected_text1}, but got: {message_text1}"

        # 도움말 및 연락처 정보가 포함된 문단 선택 및 검증
        help_text = page.locator('p.account__help')
        assert help_text.is_visible(), "Error: 도움말 문단이 보이지 않습니다."

        expected_help_text = 'Go to [Customer Support] for help, and contact us through help_us@lezhin.com if you are having trouble logging in.'
        actual_help_text = help_text.text_content().strip()
        print('예상 결과:', expected_help_text)
        print('실제 결과:', actual_help_text)
        assert actual_help_text == expected_help_text, f"Error: 도움말 텍스트가 예상과 다릅니다. (Expected: {expected_help_text}, Actual: {actual_help_text})"

        # '확인' 버튼 클릭
        page.get_by_role('link', name='OK').click()

        # 현재 페이지의 URL을 다시 가져와 비교
        current_url = page.url
        expected_url_after_confirmation = 'https://www.lezhinus.com/en'
        print('예상 결과:', expected_url_after_confirmation)
        print('실제 결과:', current_url)
        assert current_url == expected_url_after_confirmation, f"Expected: {expected_url_after_confirmation}, but got: {current_url}"

        # 내 정보 페이지로 이동
        page.goto('https://www.lezhinus.com/en/account')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 이메일값 가져오기
        email = page.wait_for_selector('.email')

        # 이메일 텍스트 가져오기
        email_text = email.text_content()

        # 회원가입 완료 메시지 검증
        expected_text = 'lilyqa5014@maildrop.cc'
        print('예상 결과:', expected_text)
        print('실제 결과:', email_text)
        assert email_text == expected_text, f"Expected: {expected_text}, but got: {email_text}"

        # 인증하기 버튼 미노출
        certification_button = page.query_selector('.email-certification')

        # 버튼이 존재하는지 확인
        assert certification_button is not None, "Error: '인증하기' 버튼이 존재하지 않습니다."

        # 버튼이 hidden 상태인지 확인
        is_hidden = certification_button.evaluate("element => element.hasAttribute('hidden')")
        assert is_hidden, "Error: '인증하기' 버튼이 hidden 상태가 아닙니다."

        # "회원을 탈퇴하시겠습니까?" 버튼 클릭
        page.click('#toggle-unregister-form')

        # 탈퇴 사유 선택
        page.get_by_text('Difficult to use and too many errors').click()

        # 비밀번호 입력 필드 클릭 및 비밀번호 입력
        password_input = page.get_by_placeholder('Please enter your password')
        password_input.click()
        password_input.fill('lezhin123@@')

        # 탈퇴하기 버튼 클릭
        page.locator("button.lzBtn.lzBtn--small.lzBtn--major", has_text="Deactivate").click()

        # '확인' 버튼 클릭
        page.get_by_role('button', name='OK').click()

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # URL이 https://www.lezhinus.com/en/account/bye 로 변경될 때까지 대기
        expected_url = 'https://www.lezhinus.com/en/account/bye'
        page.wait_for_url(expected_url)

        # 현재 페이지의 URL을 가져와 비교
        current_url = page.url
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # '탈퇴 완료' 타이틀이 노출될 때까지 대기
        page.wait_for_selector('h2.bye__head')

        # '탈퇴 완료' 타이틀 요소 가져오기
        title_element = page.query_selector('h2.bye__head')
        assert title_element is not None, "'Deactivation complete.' 타이틀 요소를 찾을 수 없습니다."

        # 타이틀 텍스트 가져오기 및 검증
        title_text = title_element.text_content().strip()
        assert title_text == 'Deactivation complete.', f"Error: 타이틀 텍스트가 예상과 다릅니다. (Expected: '탈퇴 완료', Actual: '{title_text}')"

        # '회원탈퇴가 완료되었습니다...' 문구가 노출될 때까지 대기
        page.wait_for_selector('.bye__body p')

        # 문구 요소 가져오기
        message_element = page.query_selector('.bye__body p')
        assert message_element is not None, "Error: 문구 요소를 찾을 수 없습니다."

        # 문구 텍스트 가져오기 및 검증
        message_text = message_element.text_content().strip()
        expected_message = 'Account deleted. Thank you for using Lezhin Comics.'
        
        # 검증
        print('예상 결과:', expected_message)
        print('실제 결과:', message_text)
        assert message_text == expected_message, f"Expected: {expected_message}, but got: {message_text}"

        # '레진코믹스 홈으로' 버튼 클릭
        page.get_by_role('link', name='Home').click()

        # 현재 페이지의 URL 가져오기 및 검증
        current_url = page.url
        expected_url = 'https://www.lezhinus.com/en'
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_45_Signup_From_Episode_Viewer_ko(page: Page):
        """ 에피소드 뷰어에서 가입 """ 
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 에피소드 뷰어 선택 (테디베어 3화)
        page.goto('https://www.lezhin.com/ko/comic/teddybear_for_you/3')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 로그인 페이지 이동이 완료될 때까지 대기
        expected_url = 'https://www.lezhin.com/ko/login?redirect=%2Fko%2Fcomic%2Fteddybear_for_you%2F3'
        page.wait_for_url(expected_url)

        # URL 검증
        current_url = page.url
        print('예상 URL:', expected_url)
        print('실제 URL:', current_url)
        assert current_url == expected_url, f"Error: URL이 예상과 다릅니다. (Expected: {expected_url}, Actual: {current_url})"

        # 이메일로 회원가입 버튼 클릭
        page.click('a[data-ga-event-label="버튼_회원가입"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5015@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5015')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # 생년월일, 성별 건너뛰고 '이메일로 회원가입' 버튼 클릭
        page.click('button[data-ga-event-label="버튼_회원가입"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기 (네트워크 안정성을 위해)
        page.wait_for_timeout(2000)

        # userId와 token 추출
        user_data = page.evaluate("""() => {
            return {
                userId: window.__LZ_ME__?.userId,
                token: window.__LZ_CONFIG__?.token
            };
        }""")

        user_id = user_data.get("userId")
        token = user_data.get("token")

        print(f"userId: {user_id}")
        print(f"token: {token}")


        # 현재 페이지의 URL을 가져와 비교
        current_url = page.url
        expected_url = 'https://www.lezhin.com/ko/welcome/email?redirect=%2Fko%2Fcomic%2Fteddybear_for_you%2F3'
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # '확인' 버튼 클릭
        page.get_by_role('link', name='확인').click()

        # URL이 변경될 때까지 대기
        expected_url = 'https://www.lezhin.com/ko/comic/teddybear_for_you/3'
        page.wait_for_url(expected_url)

        # URL 검증
        current_url = page.url
        print('예상 URL:', expected_url)
        print('실제 URL:', current_url)
        assert current_url == expected_url, f"Error: URL이 예상과 다릅니다. (Expected: {expected_url}, Actual: {current_url})"

        # 탈퇴 API 호출
        response = context.request.post(
            f"https://www.lezhin.com/lz-api/v2/users/{user_id}/unregister",
            data={
                "password": "lezhin123@@",  # 실제 비밀번호 필요
                "selected": "errors",         # 예시 탈퇴 사유
                "cause": "",                  # 추가 사유
                "kind": "retired"             # 탈퇴 유형
            },
            headers={
                "Authorization": f"Bearer {token}",  # 토큰 사용
                "Content-Type": "application/json"
            }
        )

        # 응답 결과 확인
        print(f"Status Code: {response.status}")
        if response.ok:
            print("탈퇴 처리 성공")
        else:
            print("탈퇴 처리 실패", response.json())

        # 페이지 종료
        page.close()

def test_SIGNUP_EM_45_Signup_From_Episode_List_ko(page: Page):
        """ 에피소드 목록에서 가입 """ 
        # 현재 페이지 컨텍스트 가져오기
        context = page.context

        # 에피소드 목록 이동 (테디베어)
        page.goto('https://www.lezhin.com/ko/comic/teddybear_for_you')

        # 찜하기 버튼 클릭
        page.click('.episodeListSupports__item__LsQyr.episodeListSupports__itemSubscribe__A1MnR')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 로그인 페이지 이동이 완료될 때까지 대기
        expected_url = 'https://www.lezhin.com/ko/login?redirect=%2Fko%2Fcomic%2Fteddybear_for_you'
        page.wait_for_url(expected_url)

        # URL 검증
        current_url = page.url
        print('예상 URL:', expected_url)
        print('실제 URL:', current_url)
        assert current_url == expected_url, f"Error: URL이 예상과 다릅니다. (Expected: {expected_url}, Actual: {current_url})"

        # 이메일로 회원가입 버튼 클릭
        page.click('a[data-ga-event-label="버튼_회원가입"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 전체동의 / 만 14세 이상 체크 후 동의 버튼 클릭 (공통 함수 사용)
        agree_to_terms_ko(page)

        # 유효한 이메일 입력 후 인증메일 발송
        page.fill('input[name="username"]', 'lilyqa5016@maildrop.cc')
        page.click('#send-verify-email-btn')

        # 2초 대기
        page.wait_for_timeout(2000)

        new_page = context.new_page()
        new_page.goto('https://maildrop.cc/inbox/?mailbox=lilyqa5016')

        # 페이지가 로드될 때까지 대기
        new_page.wait_for_load_state('load', timeout=60000)

        # iframe 선택 및 내용 추출
        iframe_selector = 'iframe'
        iframe_handle = new_page.wait_for_selector(iframe_selector, timeout=10000)
        iframe_srcdoc = iframe_handle.get_attribute('srcdoc')

        if iframe_srcdoc:
            new_page.set_content(iframe_srcdoc)
            auth_code_element = new_page.wait_for_selector('div[style*="font-size:24px;font-weight:bold;text-align:center;"]')
            auth_code_text = auth_code_element.text_content().strip()
            auth_code_match = re.search(r'\d{6}', auth_code_text)
            if auth_code_match:
                auth_code = auth_code_match.group(0)
                print(f"인증번호: {auth_code}")
            else:
                print("인증번호를 찾을 수 없습니다.")
        else:
            print("iframe srcdoc을 가져올 수 없습니다.")
            assert False, "iframe srcdoc을 가져올 수 없습니다."


        # 새 페이지 닫기
        new_page.close()

        # 추출한 인증번호 입력
        page.wait_for_selector('#verify-code-input')
        page.fill('#verify-code-input', auth_code)

        # 다음 버튼이 활성화될 때까지 대기
        page.wait_for_selector('#verify-code-next-btn:not([disabled])')

        # 다음 버튼 클릭
        page.click('#verify-code-next-btn')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 비밀번호 입력
        password_input = page.wait_for_selector('input[name="password"]', state='visible', timeout=3000)
        password_input.fill('lezhin123@@')

        # 생년월일, 성별 건너뛰고 '이메일로 회원가입' 버튼 클릭
        page.click('button[data-ga-event-label="버튼_회원가입"]')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기 (네트워크 안정성을 위해)
        page.wait_for_timeout(2000)

        # userId와 token 추출
        user_data = page.evaluate("""() => {
            return {
                userId: window.__LZ_ME__?.userId,
                token: window.__LZ_CONFIG__?.token
            };
        }""")

        user_id = user_data.get("userId")
        token = user_data.get("token")

        print(f"userId: {user_id}")
        print(f"token: {token}")


        # 현재 페이지의 URL을 가져와 비교
        current_url = page.url
        expected_url = 'https://www.lezhin.com/ko/welcome/email?redirect=%2Fko%2Fcomic%2Fteddybear_for_you'
        print('예상 결과:', expected_url)
        print('실제 결과:', current_url)
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"

        # '확인' 버튼 클릭
        page.get_by_role('link', name='확인').click()

        # URL이 변경될 때까지 대기
        expected_url = 'https://www.lezhin.com/ko/comic/teddybear_for_you'
        page.wait_for_url(expected_url)

        # URL 검증
        current_url = page.url
        print('예상 URL:', expected_url)
        print('실제 URL:', current_url)
        assert current_url == expected_url, f"Error: URL이 예상과 다릅니다. (Expected: {expected_url}, Actual: {current_url})"

        # 탈퇴 API 호출
        response = context.request.post(
            f"https://www.lezhin.com/lz-api/v2/users/{user_id}/unregister",
            data={
                "password": "lezhin123@@",  # 실제 비밀번호 필요
                "selected": "errors",         # 예시 탈퇴 사유
                "cause": "",                  # 추가 사유
                "kind": "retired"             # 탈퇴 유형
            },
            headers={
                "Authorization": f"Bearer {token}",  # 토큰 사용
                "Content-Type": "application/json"
            }
        )

        # 응답 결과 확인
        print(f"Status Code: {response.status}")
        if response.ok:
            print("탈퇴 처리 성공")
        else:
            print("탈퇴 처리 실패", response.json())

        # 페이지 종료
        page.close()