from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote

def test_payments_01_KO_CreditCard(page: Page):
        """해당 코드는 KR 로케일에서 신용카드 결제시 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 '신용카드' 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # 신용카드 선택
        page.click('.methodsBtn__KaOuX.methodsBtn--active__ICo25')
        print('✅ 신용카드 결제수단 선택 완료')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "payletter.com/pg/plcard" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close()  

def test_payments_02_KO_kakaoPay(page: Page):
        """해당 코드는 KR 로케일에서 카카오페이 결제시 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 '카카오페이' 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 카카오페이 결제수단 토글 클릭 완료')

        page.wait_for_timeout(1000)

        # 카카오페이 결제수단 선택
        kakao_btn = page.locator('button:has(img[alt="카카오페이"])')
        if kakao_btn.count() > 0:
            kakao_btn.first.click()
            print('✅ 카카오페이 결제수단 선택 완료')
        else:
            raise Exception('❌ 카카오페이 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "online-payment.kakaopay.com/bridge/pc/pg/one-time/payment" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close() 
        
def test_payments_03_KO_naverPay(page: Page):
        """해당 코드는 KR 로케일에서 네이버페이 결제시 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # 네이버페이 결제수단 선택
        naver_btn = page.locator('button:has(img[alt="네이버페이"])')
        if naver_btn.count() > 0:
            naver_btn.first.click()
            print('✅ 네이버페이 결제수단 선택 완료')
        else:
            raise Exception('❌ 네이버 페이 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "nid.naver.com/nidlogin.login" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close() 
        

def test_payments_04_KO_Toss(page: Page):
        """해당 코드는 KR 로케일에서 토스 결제시 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # 토스 결제수단 선택
        TOSS_btn = page.locator('button:has(img[alt="TOSS 간편결제"])')
        if TOSS_btn.count() > 0:
            TOSS_btn.first.click()
            print('✅ 토스 결제수단 선택 완료')
        else:
            raise Exception('❌ 토스 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "pay.toss.im/payfront/" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close() 
        


def test_payments_05_KO_Payco(page: Page):
        """해당 코드는 KR 로케일에서 페이코 결제시 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # 페이코 결제수단 선택
        PAYCO_btn = page.locator('button:has(img[alt="PAYCO"])')
        if PAYCO_btn.count() > 0:
            PAYCO_btn.first.click()
            print('✅ 페이코 결제수단 선택 완료')
        else:
            raise Exception('❌ 페이코 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "id.payco.com/login" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close() 
        

def test_payments_06_KO_phonePay(page: Page):
        """해당 코드는 KR 로케일에서 휴대폰 결제시 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        #휴대폰결제 결제수단 선택
        mobilepay_btn = page.locator('button:has-text("휴대폰결제")')
        if mobilepay_btn.count() > 0:
            mobilepay_btn.first.click()
            print('✅ 휴대폰결제 결제수단 선택 완료')
        else:
            raise Exception('❌ 휴대폰결제 결제 수단이 존재하지 않습니다.')
        

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "pgweb.payletter.com/pg/impaymobile" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close()
        

def test_payments_07_KO_bankBook(page: Page):
        """해당 코드는 KR 로케일에서 무통장입금 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # 무통장입금 결제수단 선택
        BANKBOOK_btn = page.locator('button:has-text("무통장입금")')
        if BANKBOOK_btn.count() > 0:
            BANKBOOK_btn.first.click()
            print('✅ 무통장입금 결제수단 선택 완료')
        else:
            raise Exception('❌ 무통장입금 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "pgweb.payletter.com/pg/settlevacct" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close()
        

def test_payments_08_KO_Tmoney(page: Page):
        """해당 코드는 KR 로케일에서 티머니 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # T-money 결제수단 선택
        tmoney_btn = page.locator('button:has-text("T-money")')
        if tmoney_btn.count() > 0:
            tmoney_btn.first.click()
            print('✅ T-money 결제수단 선택 완료')
        else:
            raise Exception('❌ T-money 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "mup.mobilians.co.kr/MUP" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close()

def test_payments_09_KO_cultureland(page: Page):
        """해당 코드는 KR 로케일에서 컬쳐랜드 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # 컬쳐랜드상품권 결제수단 선택
        cultureland_btn = page.locator('button:has-text("컬쳐랜드상품권")')
        if cultureland_btn.count() > 0:
            cultureland_btn.first.click()
            print('✅ 컬쳐랜드상품권 결제수단 선택 완료')
        else:
            raise Exception('❌ 컬쳐랜드상품권 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "mup.mobilians.co.kr/MUP/" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close()

def test_payments_10_KO_OKCASHBAG(page: Page):
        """해당 코드는 KR 로케일에서 ok캐시백 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # OK캐쉬백 결제수단 선택
        okcashbag_btn = page.locator('button:has-text("OK캐쉬백")')
        if okcashbag_btn.count() > 0:
            okcashbag_btn.first.click()
            print('✅  OK캐쉬백 결제수단 선택 완료')
        else:
            raise Exception('❌  OK캐쉬백 결제 수단이 존재하지 않습니다.')
        
        # 카드번호 입력
        page.locator("#okcashbag-num1").fill("2100")
        page.locator("#okcashbag-num2").fill("4969")
        page.locator("#okcashbag-num3").fill("1420")
        page.locator("#okcashbag-num4").fill("0698")
        
        # 패스워드 입력 (예: 테스트용 비밀번호)
        page.locator("#okcashbag-password").fill("wlscogus7!")

        # 조회 버튼 클릭
        page.locator("button.okcashbag__submit__GqQwR").click()
        
        
        # OK캐쉬백 포인트 결과 노출 검증
        try:
            element = page.wait_for_selector("label.okcashbag__resultPoint__m3bSq", timeout=5000)
            if element.is_visible():
                print("✅ OK캐쉬백 포인트 정보 노출 확인됨")
            else:
                print("❌ OK캐쉬백 포인트 정보가 화면에 보이지 않습니다.")
                raise AssertionError("❌ OK캐쉬백 포인트 정보가 화면에 보이지 않습니다.")
        except Exception:
            raise AssertionError("❌ OK캐쉬백 포인트 정보가 DOM에 존재하지 않거나 시간 내 로딩되지 않았습니다.")


     
        # 페이지 종료
        page.close()
        

def test_payments_11_KO_ingenico(page: Page):
        """해당 코드는 KR 로케일에서 해외 신용카드 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('일반 상품'))")

        # 해당 섹션 내부의 네 번째 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
        second_button.click()

        # 결제수단 토글 클릭
        page.click('.methodsToggle__x2eu9')
        print('✅ 결제수단 토글 클릭 완료')

        # 해외 신용카드 결제수단 선택
        ingenico_btn = page.locator('button:has-text("해외 신용카드")')
        if ingenico_btn.count() > 0:
            ingenico_btn.first.click()
            print('✅ 해외 신용카드 결제수단 선택 완료')
        else:
            raise Exception('❌ 해외 신용카드 결제 수단이 존재하지 않습니다.')

        # 전체동의 체크
        page.click('text=전체동의')
        print('✅ 전체동의 선택 완료')

        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증 (둘 중 하나만 포함되면 성공)
        if (
            "www.lezhin.com/ko/payment/ingenico" in current_url
            or "payment.pay1.checkout.worldline-solutions.com" in current_url
        ):
            print("✅ 해외신용카드 결제 PG사 URL 이동 확인 성공")
        else:
            raise AssertionError(f"❌ 해외신용카드 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close()
        

def test_payments_12_KO_walwal_naverpay(page: Page):
        """해당 코드는 KR 로케일에서 네이버 정기결제 PG 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment')

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
        
        # "정기결제 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('월월충전 상품'))")

        # 해당 섹션 내부의 첫번째 정기결제 상품 버튼 클릭
        second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(0)
        second_button.click()

        # 첫 번째 필수 항목: 매월 정기결제 동의
        page.click('text=위 사항을 확인하였으며 매월 정기결제에 동의합니다. ')

        # 두 번째 필수 항목: 이용 약관 동의
        page.click('text=이용 약관에 동의합니다. ')

        # 세 번째 필수 항목: 개인정보 수집 동의
        page.click('text=개인 정보 수집에 동의합니다. ')
        
        
        # 결제 요청 버튼 클릭 → 새 창 열림 대기
        with page.context.expect_page() as new_page_info:
            page.click(
                'button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC.agreements__goToPG__ZHO8K')
            print('✅ 결제 요청 버튼 클릭 완료')

        page.wait_for_timeout(1500)

        # 새 창 핸들링
        new_page = new_page_info.value
        print('✅ 결제 PG사 새 창 열림 감지 완료')

        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "nid.naver.com/nidlogin.login" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
        # 페이지 종료
        page.close()
        


def test_payments_13_KO_freecoin_change_lpoint(page: Page):
        """해당 코드는 KR 로케일에서 엘포인트 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment/freecoin-change')

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
        
        # L.POINT 전용 상품 요소 클릭
        page.locator("div.freeCoinPaymentBtn__text__F4XBp.freeCoinPaymentBtn__isNew__0BYJ6").click()
        
        # L.POINT 섹션의 노출 여부 확인
        is_visible = page.locator("div.lpoint__container__uxenc").is_visible()

        if is_visible:
            print("✅ L.POINT 섹션이 정상적으로 노출되었습니다.")
        else:
            raise Exception("❌ L.POINT 섹션이 노출되지 않았습니다. (hidden 속성 있음)")

        # 페이지 종료
        page.close()
        

def test_payments_14_KO_freecoin_change_pointpark(page: Page):
        """해당 코드는 KR 로케일에서 포인트파크 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/payment/freecoin-change')

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
        
        # 포인트 파크 전용 상품 요소 클릭
        page.locator("button:has(h4:has-text('10개 제휴사 포인트 전환'))").click()
        
        # 포인트파크 영역이 있는지 확인
        is_visible = page.locator("iframe.freeCoinPointPark__x6_5l").is_visible()

        if is_visible:
            print("✅ 포인트파크 영역이 정상적으로 노출되었습니다.")
        else:
            raise Exception("❌ 포인트파크 영역이 노출되지 않았습니다.")

        # 페이지 종료
        page.close()
        

def test_payments_15_us_GPOQ(page: Page):
        """해당 코드는 us  로케일에서 신용카드 결제시 GPOQ 페이지 진입 경로를 확인합니다."""
        
        # 레진코믹스 코인충전페이지 으로 이동
        navigate_to(page, 'https://www.lezhinus.com/en/payment')
        
        # 쿠키동의 
        page.click("button:has-text('Accept All')")

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
        
        # "일반 상품" 섹션 찾기
        section = page.locator("section:has(h3:has-text('Coin Bundle'))")

              
        with page.context.expect_page() as new_page_info:
            # 해당 섹션 내부의 네 번째 버튼 클릭
            second_button = section.locator("button.paymentCoinProduct__NUWF5").nth(3)
            second_button.click()

        # 새로 열린 페이지 핸들 가져오기
        new_page = new_page_info.value
        
        # 새 창이 로드될 때까지 대기
        new_page.wait_for_load_state('load')
        page.wait_for_timeout(1500)
        
        with page.context.expect_page() as new_page_info_2:
            # 'OK' 버튼 클릭
            ok_button = new_page.locator("button.lzBtn__tyLuS.lzBtn--large__v_uNA.lzBtn--filled_red__mb2yC", has_text="OK")
            ok_button.click()
        
        # 새로 열린 페이지 핸들 가져오기
        new_page2 = new_page_info_2.value
    
        # VISA 카드 선택
        new_page2.click("button.paylz__btn >> img[src='/Img/visa.png']")
        
        # 'Next' 버튼 요소 선택
        new_page2.click("#btnNext") 

        # 결제 PG사 페이지 이동 대기
        # 실제 URL 확인
        current_url = new_page.url
        print(f'현재 PG URL: {current_url}')

        # URL 검증
        # 포함 여부로 검증 (정확히 일치가 아닐 수도 있으므로)
        if "psp.payletter.com/Web/Payment/PLCard/CreditCardMpi/CreditCardFrm" in current_url:
                print("✅ 결제 PG사 URL 이동 확인 성공")
        else:
                raise AssertionError(f"❌ 예상된 PG사 URL이 아님: {current_url}")
     
        # 페이지 종료
        page.close() 