from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse, parse_qs, urlencode, quote


def test_Search_001_Search_RecentSearch_not_view(page: Page):
        """해당 코드는 레진 최근검색어 삭제 후 최근검색 영역 비노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 입력창에 '야' 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '야')
        page.wait_for_timeout(2000)
        
        # 검색 버튼 클릭
        page.wait_for_selector('button.searchInput__go__yIdqp', state='visible', timeout=3000)
        page.click('button.searchInput__go__yIdqp')
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        page.goto('https://www.lezhin.com/ko/')
        
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # "전체 삭제" 버튼 클릭
        page.wait_for_selector('button.searchPopularTags__remove--all__VqeAQ', state='visible', timeout=3000)
        page.click('button.searchPopularTags__remove--all__VqeAQ')
        
        # "최근 검색" 요소 비노출 검증 (예외 처리 없이)
        element = page.query_selector('h3.searchPopularTags__recents__pWvwc')

        if element and element.is_visible():
                raise AssertionError("❌ '최근 검색' 요소가 노출되고 있습니다.")
        else:
                print("✅ '최근 검색' 요소가 노출되지 않습니다.")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
          
        
        
def test_Search_002_Search_PopularTag_click(page: Page):
        """해당 코드는 검색 미리보기 화면에 인기태그를 클릭하고 페이지이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')
        
        # 1초 대기
        page.wait_for_timeout(1000)

        # 인기태그 첫번째 항목이 나타날 때까지 대기
        first_tag_locator = page.locator("ul.searchPopularTags__items__ikbc8 li a").nth(0)
        first_tag_locator.wait_for(state="visible", timeout=5000)

        # href 추출
        expected_href = first_tag_locator.get_attribute("href")
        
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 첫번째 인기 태그클릭
        first_tag_locator.click()

        # 페이지 이동 대기
        page.wait_for_load_state("load")

        # 현재 URL에서 도메인을 제외한 path만 추출
        actual_path = urlparse(page.url).path  # 예: /ko/tags/짝사랑공

        # 비교
        if actual_path == expected_href:
                print(f"✅ 이동 경로 일치: {actual_path}")
        else:
                raise AssertionError(f"❌ 이동 경로 불일치: expected '{expected_href}' but got '{actual_path}'")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        
def test_Search_003_Search_Autocomplete_comic(page: Page):
        """해당 코드는 레진 검색어 입력시 미리보기 결과 노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 입력창에 '야' 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '야')
        page.wait_for_timeout(2000)
        
        # "작품" 섹션이 노출되는지 검증
        element = page.locator('div.searchPreview__searchContents__M1Ypw')

        # 요소가 visible 상태인지 확인
        if element.is_visible():
                print("✅ '작품' 섹션이 노출됩니다.")
        else:
                raise AssertionError("❌ '작품' 섹션이 노출되지 않습니다.")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        

def test_Search_004_Search_Autocomplete_tag(page: Page):
        """해당 코드는 레진 검색어 입력시 태그 검색 결과확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 입력창에 '로맨스' 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '로맨스')
        page.wait_for_timeout(2000)
        
        # "태그" 섹션이 노출되는지 검증
        element = page.locator('div.searchPreview__tagContainer___qevK')

        # 요소가 visible 상태인지 확인
        if element.is_visible():
                print("✅ '태그' 섹션이 노출됩니다.")
        else:
                raise AssertionError("❌ '태그' 섹션이 노출되지 않습니다.")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        

def test_Search_005_Search_Autocomplete_tag_click(page: Page):
        """해당 코드는 레진 검색어 입력 후 태그 검색결과를 클릭 후 이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 입력창에 '야' 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '로맨스')
        page.wait_for_timeout(2000)
        
        # 태그 검색결과 항목이 나타날 때까지 대기
        first_tag_locator = page.locator("div.searchPreview__tagContainer___qevK  li a").nth(0)
        first_tag_locator.wait_for(state="visible", timeout=3000)

        # href 추출
        expected_href = first_tag_locator.get_attribute("href")
        
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 검색결과 태그클릭
        first_tag_locator.click()

        # 페이지 이동 대기
        page.wait_for_load_state("load")

        # 현재 URL에서 도메인을 제외한 path만 추출
        actual_path = urlparse(page.url).path  # 예: /ko/tags/짝사랑공

        # 비교
        if actual_path == expected_href:
                print(f"✅ 이동 경로 일치: {actual_path}")
        else:
                raise AssertionError(f"❌ 이동 경로 불일치: expected '{expected_href}' but got '{actual_path}'")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        

def test_Search_006_Search_Autocomplete_adultag(page: Page):
        """해당 코드는 비성인, 비로그인 상태 레진 성인 태그 검색어 입력시 태그 검색 결과 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 입력창에 '야' 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '고수위')
        page.wait_for_timeout(2000)
        
        # "태그" 섹션이 노출되는지 검증
        element = page.locator('div.searchPreview__tagContainer___qevK')

        # 노출 여부 검증
        if element.is_visible() == False:
                raise AssertionError("❌ '태그' 섹션이 노출되고 있습니다.")
        else:
                print("✅ '태그' 섹션이 비노출 상태입니다.")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        

def test_Search_007_Search_Result_max_count(page: Page):
        """해당 코드는 작품 검색결과의 최대 작품 갯수를 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 입력창에 '야' 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, 'dcw')
        page.wait_for_timeout(2000)
        
        # 작품 리스트 내 <li> 태그 선택자
        items = page.locator("div.searchPreview__searchContents__M1Ypw ul.hy__list li")

        # <li> 개수 확인
        count = items.count()

        # 검증
        if count == 8:
                print("✅ 작품 목록 항목 수가 8개로 정상입니다.")
        else:
                raise AssertionError(f"❌ 작품 항목 수가 {count}개로 8개가 아닙니다.")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        

def test_Search_08_Search_Result_kidAccount(page: Page):
        """해당 코드는 전연령 계정에서 검색시 전연령 + 성인작품 노출을 확인합니다."""

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

        
        adult_flag_found = False

        # 응답 핸들러 정의
        def handle_response(response):
                nonlocal adult_flag_found 

                if "lz-api/v2/advanced-search" in response.url and "t=preview" in response.url and "q=dcw" in response.url:
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", {}).get("contents", []):
                                        if "adult" in item and isinstance(item["adult"], bool):
                                                adult_flag_found = True
                                                break
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 응답 이벤트 등록
        page.on("response", handle_response)
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, 'dcw')
        page.wait_for_timeout(2000)



        # 결과 검증
        if adult_flag_found:
                print("✅ adult 필드가 포함된 항목이 존재합니다.")
        else:
                raise AssertionError("❌ adult 필드를 가진 항목이 존재하지 않습니다.")
        
        
        # 블라인드 이미지 요소 존재 확인
        img_locator = page.locator('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]')

        if img_locator.count() > 0:
                print("✅ 블라인드 썸네일 이미지가 존재합니다.")
        else:
                raise AssertionError("❌ 블라인드 썸네일 이미지가 존재하지 않습니다.")
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        

def test_Search_09_Search_Result_notLogin(page: Page):
        """해당 코드는 비로그인상태 검색시 전연령 + 성인작품 노출을 확인합니다."""

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        
        adult_flag_found = False

        # 응답 핸들러 정의
        def handle_response(response):
                nonlocal adult_flag_found 

                if "lz-api/v2/advanced-search" in response.url and "t=preview" in response.url and "q=dcw" in response.url:
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", {}).get("contents", []):
                                        if "adult" in item and isinstance(item["adult"], bool):
                                                adult_flag_found = True
                                                break
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 응답 이벤트 등록
        page.on("response", handle_response)
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, 'dcw')
        page.wait_for_timeout(2000)



        # 결과 검증
        if adult_flag_found:
                print("✅ adult 필드가 포함된 항목이 존재합니다.")
        else:
                raise AssertionError("❌ adult 필드를 가진 항목이 존재하지 않습니다.")
        
        
        # 블라인드 이미지 요소 존재 확인
        img_locator = page.locator('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]')

        if img_locator.count() > 0:
                print("✅ adult 썸네일 이미지가 존재합니다.")
        else:
                raise AssertionError("❌ adult 썸네일 이미지가 존재하지 않습니다.")
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        

def test_Search_10_Search_Result_AdultAccount_19off(page: Page):
        """해당 코드는 성인 계정에서 19 Off 상태에서 검색시 전연령 + 성인작품 노출을 확인합니다."""

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
        
        page.wait_for_timeout(1000)
        
        # 19 off 실행
        button_selector = 'button.toggleContentMode__btn__99VKl.toggleContentMode__btn--on__2OQ_F'
        page.wait_for_selector(button_selector, state='visible', timeout=3000)
        page.click(button_selector)
        
        page.wait_for_timeout(2000)

        
        adult_flag_found = False

        # 응답 핸들러 정의
        def handle_response(response):
                nonlocal adult_flag_found 

                if "lz-api/v2/advanced-search" in response.url and "t=preview" in response.url and "q=dcw" in response.url:
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", {}).get("contents", []):
                                        if "adult" in item and isinstance(item["adult"], bool):
                                                adult_flag_found = True
                                                break
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 응답 이벤트 등록
        page.on("response", handle_response)
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, 'dcw')
        page.wait_for_timeout(2000)



        # 결과 검증
        if adult_flag_found:
                print("✅ adult 필드가 포함된 항목이 존재합니다.")
        else:
                raise AssertionError("❌ adult 필드를 가진 항목이 존재하지 않습니다.")
        
        
        # 블라인드 이미지 요소 존재 확인
        img_locator = page.locator('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]')

        if img_locator.count() == 0:
                print("✅  블라인드 썸네일 이미지가 존재하지 않습니다.")
        else:
                raise AssertionError("❌ 블라인드 썸네일 이미지가 존재합니다.")
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        


def test_Search_11_Search_Result_AdultAccount_19on(page: Page):
        """해당 코드는 성인 계정에서 19 On 상태에서 검색시 전연령 + 성인작품 노출을 확인합니다."""

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
        
        page.wait_for_timeout(1000)
        
        
        adult_flag_found = False

        # 응답 핸들러 정의
        def handle_response(response):
                nonlocal adult_flag_found 

                if "lz-api/v2/advanced-search" in response.url and "t=preview" in response.url and "q=dcw" in response.url:
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", {}).get("contents", []):
                                        if "adult" in item and isinstance(item["adult"], bool):
                                                adult_flag_found = True
                                                break
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 응답 이벤트 등록
        page.on("response", handle_response)
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, 'dcw')
        page.wait_for_timeout(2000)



        # 결과 검증
        if adult_flag_found:
                print("✅ adult 필드가 포함된 항목이 존재합니다.")
        else:
                raise AssertionError("❌ adult 필드를 가진 항목이 존재하지 않습니다.")
        
        
        # 블라인드 이미지 요소 존재 확인
        img_locator = page.locator('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]')

        if img_locator.count() == 0:
                print("✅  블라인드 썸네일 이미지가 존재하지 않습니다.")
        else:
                raise AssertionError("❌ 블라인드 썸네일 이미지가 존재합니다.")
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        

def test_Search_012_Search_Autocomplete_comic_click(page: Page):
        """해당 코드는 레진 검색어 입력 후 작품 검색결과를 클릭 후 이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 검색어 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '귀멸의칼날[단행본]')
        page.wait_for_timeout(2000)
        
        # 작품 검색결과 항목이 나타날 때까지 대기
        first_tag_locator = page.locator("div.searchPreview__searchContents__M1Ypw  li a").nth(0)
        first_tag_locator.wait_for(state="visible", timeout=3000)

        # href 추출
        expected_href = first_tag_locator.get_attribute("href")
        
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 검색결과 작품클릭
        first_tag_locator.click()

        # 페이지가 해당 href로 바뀔 때까지 대기
        page.wait_for_url(f"**{expected_href}", timeout=5000)

        # 현재 URL에서 도메인을 제외한 path만 추출
        actual_path = urlparse(page.url).path  

        # 비교
        if actual_path == expected_href:
                print(f"✅ 이동 경로 일치: {actual_path}")
        else:
                raise AssertionError(f"❌ 이동 경로 불일치: expected '{expected_href}' but got '{actual_path}'")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        

def test_Search_013_Search_Autocomplete_Artist_view(page: Page):
        """해당 코드는 레진 검색어 입력 후 검색결과에 작가 노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 검색어 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '귀멸의칼날[단행본]')
        page.wait_for_timeout(2000)
        
        # 작가 요소를 지정
        author_locator = page.locator('div.hy__infoMeta')

        # 텍스트 전체를 가져옴
        author_text = author_locator.inner_text()

        # 검증
        if "고토게 코요하루" in author_text:
                print("✅ '고토게 코요하루' 작가 항목이 존재합니다.")
        else:
                raise AssertionError("❌ '고토게 코요하루' 작가 항목이 존재하지 않습니다.")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
def test_Search_014_Search_Autocomplete_publisher_view(page: Page):
        """해당 코드는 레진 검색어 입력 후 검색결과에 출판사 노출을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 검색어 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '귀멸의칼날[단행본]')
        page.wait_for_timeout(2000)
        
        # 작가 요소를 지정
        author_locator = page.locator('div.hy__infoMeta')

        # 텍스트 전체를 가져옴
        author_text = author_locator.inner_text()

        # 검증
        if "DCW" in author_text:
                print("✅ 'DCW' 출판사 항목이 존재합니다.")
        else:
                raise AssertionError("❌ 'DCW' 출판사 항목이 존재하지 않습니다.")
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        
        
        

def test_Search_015_Search_Result_All(page: Page):
        """해당 코드는 검색 결과 페이지 이동 직후 "전체" 탭의 작품 리스트 노출을 확인합니다."""

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
        
        page.wait_for_timeout(1000)
        
        
        text_found = False

        def handle_response(response):
                nonlocal text_found
                if "lz-api/v2/advanced-search" in response.url and "q=%EC%95%84" and "t=all"in response.url:  # "아"의 인코딩
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", []):
                                        # title에 "아" 포함 여부
                                        if "아" in item.get("title", ""):
                                                text_found = True
                                                break

                                        # tags 리스트에 포함 여부
                                        if any("아" in tag for tag in item.get("tags", [])):
                                                text_found = True
                                                break

                                        # artists 리스트 내 name 필드 포함 여부
                                        if any("아" in artist.get("name", "") for artist in item.get("artists", [])):
                                                text_found = True
                                                break
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 이벤트 핸들러 등록
        page.on("response", handle_response)


        # 검색어 입력 및 결과 트리거
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.fill(search_selector, '아')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 결과 검증
        if text_found:
                print("✅ '아' title, tags, artists.name중에서 노출됩니다.")
        else:
                raise AssertionError("❌ '아' 텍스트가 title, tags, artists.name 어디에도 존재하지 않습니다.")

        # 페이지 종료
        page.close()
        


def test_Search_016_Search_Result_title(page: Page):
        """해당 코드는 검색 결과 페이지 이동 직후 "작품" 탭의 작품 리스트 노출을 확인합니다."""

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
        
        page.wait_for_timeout(1000)
        
        
        text_found = False

        def handle_response(response):
                nonlocal text_found
                if "lz-api/v2/advanced-search" in response.url and "q=%EC%95%84" and "t=title"in response.url:  # "아"의 인코딩
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", []):
                                        # title에 "아" 포함 여부
                                        if "아" in item.get("title", ""):
                                                text_found = True
                                                break

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 이벤트 핸들러 등록
        page.on("response", handle_response)
        
        # 검색어 입력 및 결과 트리거
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.fill(search_selector, '아')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 페이지 접근 (이동 + 자동 요청 발생 유도)
        page.goto("https://www.lezhin.com/ko/search?t=title&q=%EC%95%84")
        
        close_banner_if_exists(page)



        # 결과 검증
        if text_found:
                print("✅ '아' 텍스트가 title 에서 노출됩니다.")
        else:
                raise AssertionError("❌ '아' 텍스트가 title 필드에 존재하지 않는 작품이 있습니다.")

        # 페이지 종료
        page.close()
        
        


def test_Search_017_Search_Result_artist_more(page: Page):
        """해당 코드는 레진 검색어 입력 후 작가탭 검색결과를 중 더보기 클릭 후 이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 검색어 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '고토게 코요하루')
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        
        # 페이지 접근 (이동 + 자동 요청 발생 유도)
        page.goto("https://www.lezhin.com/ko/search?t=artist&q=%EA%B3%A0%ED%86%A0%EA%B2%8C+%EC%BD%94%EC%9A%94%ED%95%98%EB%A3%A8")
        
        
        # '더보기' 버튼 선택자
        more_button = page.locator('a.keyword__more__H_IJ9')

        # 노출 여부 검증
        if more_button.is_visible():
                print("✅ '더보기' 버튼이 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ '더보기' 버튼이 노출되지 않습니다.")
        
        more_button.click()
        
        # href 추출 및 path만 사용
        expected_href = more_button.get_attribute("href")
        expected_path = urlparse(expected_href).path  # 쿼리 제거됨
        
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 버튼 클릭
    
        page.wait_for_load_state("load")

        # 현재 URL에서 path만 추출
        actual_path = urlparse(page.url).path

        # 비교
        if actual_path == expected_path:
                print(f"✅ URL 경로 일치: {actual_path}")
        else:
                raise AssertionError(f"❌ URL 경로 불일치: expected '{expected_path}', got '{actual_path}'")

        # 페이지 종료
        page.close()
        
        

def test_Search_018_Search_Result_publisher_more(page: Page):
        """해당 코드는 레진 검색어 입력 후 출판사 검색결과를 중 더보기 클릭 후 이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 검색어 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, 'dcw')
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        
        # 페이지 접근 (이동 + 자동 요청 발생 유도)
        page.goto("https://www.lezhin.com/ko/search?t=publisher&q=dcw")
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 중복 방지를 위해 첫 번째 '더보기' 버튼 선택
        more_button = page.locator('a.keyword__more__H_IJ9').nth(0)

        # 노출 여부 검증
        if more_button.is_visible():
                print("✅ '더보기' 버튼이 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ '더보기' 버튼이 노출되지 않습니다.")
        
        more_button.click()
        
        # href 추출 및 path만 사용
        expected_href = more_button.get_attribute("href")
        expected_path = urlparse(expected_href).path  # 쿼리 제거됨
        
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 버튼 클릭
    
        page.wait_for_load_state("load")

        # 현재 URL에서 path만 추출
        actual_path = urlparse(page.url).path

        # 비교
        if actual_path == expected_path:
                print(f"✅ URL 경로 일치: {actual_path}")
        else:
                raise AssertionError(f"❌ URL 경로 불일치: expected '{expected_path}', got '{actual_path}'")

        # 페이지 종료
        page.close()
        


def test_Search_019_Search_Result_publisher_tag(page: Page):
        """해당 코드는 레진 검색어 입력 후 태그 검색결과를 중 더보기 클릭 후 이동을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 검색어 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, '로맨스')
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        
        # 페이지 접근 (이동 + 자동 요청 발생 유도)
        page.goto("https://www.lezhin.com/ko/search?t=tag&q=%EB%A1%9C%EB%A7%A8%EC%8A%A4")
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 중복 방지를 위해 첫 번째 '더보기' 버튼 선택
        more_button = page.locator('a.keyword__more__H_IJ9').nth(0)

        # 노출 여부 검증
        if more_button.is_visible():
                print("✅ '더보기' 버튼이 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ '더보기' 버튼이 노출되지 않습니다.")
        
        more_button.click()
        
        # href 추출 및 path만 사용
        expected_href = more_button.get_attribute("href")
        expected_path = quote(urlparse(expected_href).path, safe='/')
        
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 버튼 클릭
    
        page.wait_for_load_state("load")

        # 현재 URL에서 path만 추출
        actual_path = urlparse(page.url).path

        # 비교
        if actual_path == expected_path:
                print(f"✅ URL 경로 일치: {actual_path}")
        else:
                raise AssertionError(f"❌ URL 경로 불일치: expected '{expected_path}', got '{actual_path}'")

        # 페이지 종료
        page.close()
        

def test_Search_020_Search_Result_empty(page: Page):
        """해당 코드는 레진 검색어 입력 후 검색결과가 없을때 화면을 확인합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')

        # 검색 검색어 입력
        search_selector = 'input.searchInput__input__991FM'
        page.click(search_selector)
        page.fill(search_selector, 'ㅁㄴㅇ')
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        
        
        # <span>0건</span> 요소 확인
        empty_result_span = page.locator('div.searchCheckbox__UMIWY span', has_text='0건')

        # <i>완결만 보기</i> 요소 확인
        completed_only_text = page.locator('div.searchCheckbox__UMIWY i', has_text='완결만 보기')

        if empty_result_span.is_visible() and completed_only_text.is_visible():
                print("✅ '0건'과 '완결만 보기' 요소가 모두 노출됩니다.")
        else:
                raise AssertionError("❌ '0건' 또는 '완결만 보기' 요소가 노출되지 않습니다.")
        
        
        # 전체 섹션 요소
        section = page.locator('section.searchException__detail__Oj0nO')

        # 개별 텍스트 요소
        title_text = page.locator('div.searchException__detailTitle__bNIy7', has_text='검색결과가 없습니다.')
        desc_text = page.locator('div.searchException__detailDesc__8c8jX', has_text='검색어가 정확한지 다시 한 번 확인해주세요.')

        if section.is_visible() and title_text.is_visible() and desc_text.is_visible():
                print("✅ 검색결과 없음 안내 메시지가 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 검색결과 없음 메시지 또는 텍스트가 노출되지 않습니다.")
        
        # '신작 랭킹' 섹션 확인
        ranking_section = page.locator('section.lzComicVX___3l9S.realtime__CrBCX')
        if ranking_section.is_visible():
                print("✅ '신작 랭킹' 섹션이 노출됩니다.")
        else:
                raise AssertionError("❌ '신작 랭킹' 섹션이 노출되지 않습니다.")
        
        # 작품 탭 접근 
        page.goto("https://www.lezhin.com/ko/search?t=title&q=%E3%85%81%E3%84%B4%E3%85%87")
        page.wait_for_timeout(2000)
        
        
        # <span>0건</span> 요소 확인
        empty_result_span = page.locator('div.searchCheckbox__UMIWY span', has_text='0건')

        # <i>완결만 보기</i> 요소 확인
        completed_only_text = page.locator('div.searchCheckbox__UMIWY i', has_text='완결만 보기')

        if empty_result_span.is_visible() and completed_only_text.is_visible():
                print("✅ '0건'과 '완결만 보기' 요소가 모두 노출됩니다.")
        else:
                raise AssertionError("❌ '0건' 또는 '완결만 보기' 요소가 노출되지 않습니다.")
        
        
        # 전체 섹션 요소
        section = page.locator('section.searchException__detail__Oj0nO')

        # 개별 텍스트 요소
        title_text = page.locator('div.searchException__detailTitle__bNIy7', has_text='검색결과가 없습니다.')
        desc_text = page.locator('div.searchException__detailDesc__8c8jX', has_text='검색어가 정확한지 다시 한 번 확인해주세요.')

        if section.is_visible() and title_text.is_visible() and desc_text.is_visible():
                print("✅ 검색결과 없음 안내 메시지가 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 검색결과 없음 메시지 또는 텍스트가 노출되지 않습니다.")
        
        # '신작 랭킹' 섹션 확인
        ranking_section = page.locator('section.lzComicVX___3l9S.realtime__CrBCX')
        if ranking_section.is_visible():
                print("✅ '신작 랭킹' 섹션이 노출됩니다.")
        else:
                raise AssertionError("❌ '신작 랭킹' 섹션이 노출되지 않습니다.")
        
        # 작가 탭 접근 
        page.goto("https://www.lezhin.com/ko/search?t=artist&q=%E3%85%81%E3%84%B4%E3%85%87")
        page.wait_for_timeout(2000)
        
        
        # <span>0건</span> 요소 확인
        empty_result_span = page.locator('div.searchCheckbox__UMIWY span', has_text='0건')

        # <i>완결만 보기</i> 요소 확인
        completed_only_text = page.locator('div.searchCheckbox__UMIWY i', has_text='완결만 보기')

        if empty_result_span.is_visible() and completed_only_text.is_visible():
                print("✅ '0건'과 '완결만 보기' 요소가 모두 노출됩니다.")
        else:
                raise AssertionError("❌ '0건' 또는 '완결만 보기' 요소가 노출되지 않습니다.")
        
        
        # 전체 섹션 요소
        section = page.locator('section.searchException__detail__Oj0nO')

        # 개별 텍스트 요소
        title_text = page.locator('div.searchException__detailTitle__bNIy7', has_text='검색결과가 없습니다.')
        desc_text = page.locator('div.searchException__detailDesc__8c8jX', has_text='검색어가 정확한지 다시 한 번 확인해주세요.')

        if section.is_visible() and title_text.is_visible() and desc_text.is_visible():
                print("✅ 검색결과 없음 안내 메시지가 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 검색결과 없음 메시지 또는 텍스트가 노출되지 않습니다.")
        
        # '신작 랭킹' 섹션 확인
        ranking_section = page.locator('section.lzComicVX___3l9S.realtime__CrBCX')
        if ranking_section.is_visible():
                print("✅ '신작 랭킹' 섹션이 노출됩니다.")
        else:
                raise AssertionError("❌ '신작 랭킹' 섹션이 노출되지 않습니다.")
        
        # 출판사 탭 접근 
        page.goto("https://www.lezhin.com/ko/search?t=publisher&q=%E3%85%81%E3%84%B4%E3%85%87")
        page.wait_for_timeout(2000)
        
        # <span>0건</span> 요소 확인
        empty_result_span = page.locator('div.searchCheckbox__UMIWY span', has_text='0건')

        # <i>완결만 보기</i> 요소 확인
        completed_only_text = page.locator('div.searchCheckbox__UMIWY i', has_text='완결만 보기')

        if empty_result_span.is_visible() and completed_only_text.is_visible():
                print("✅ '0건'과 '완결만 보기' 요소가 모두 노출됩니다.")
        else:
                raise AssertionError("❌ '0건' 또는 '완결만 보기' 요소가 노출되지 않습니다.")
        
        
        # 전체 섹션 요소
        section = page.locator('section.searchException__detail__Oj0nO')

        # 개별 텍스트 요소
        title_text = page.locator('div.searchException__detailTitle__bNIy7', has_text='검색결과가 없습니다.')
        desc_text = page.locator('div.searchException__detailDesc__8c8jX', has_text='검색어가 정확한지 다시 한 번 확인해주세요.')

        if section.is_visible() and title_text.is_visible() and desc_text.is_visible():
                print("✅ 검색결과 없음 안내 메시지가 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 검색결과 없음 메시지 또는 텍스트가 노출되지 않습니다.")
        
        # '신작 랭킹' 섹션 확인
        ranking_section = page.locator('section.lzComicVX___3l9S.realtime__CrBCX')
        if ranking_section.is_visible():
                print("✅ '신작 랭킹' 섹션이 노출됩니다.")
        else:
                raise AssertionError("❌ '신작 랭킹' 섹션이 노출되지 않습니다.")
        
        # 태그 탭 접근 
        page.goto("https://www.lezhin.com/ko/search?t=tag&q=%E3%85%81%E3%84%B4%E3%85%87")
        page.wait_for_timeout(2000)
        
        # <span>0건</span> 요소 확인
        empty_result_span = page.locator('div.searchCheckbox__UMIWY span', has_text='0건')

        # <i>완결만 보기</i> 요소 확인
        completed_only_text = page.locator('div.searchCheckbox__UMIWY i', has_text='완결만 보기')

        if empty_result_span.is_visible() and completed_only_text.is_visible():
                print("✅ '0건'과 '완결만 보기' 요소가 모두 노출됩니다.")
        else:
                raise AssertionError("❌ '0건' 또는 '완결만 보기' 요소가 노출되지 않습니다.")
        
        
        # 전체 섹션 요소
        section = page.locator('section.searchException__detail__Oj0nO')

        # 개별 텍스트 요소
        title_text = page.locator('div.searchException__detailTitle__bNIy7', has_text='검색결과가 없습니다.')
        desc_text = page.locator('div.searchException__detailDesc__8c8jX', has_text='검색어가 정확한지 다시 한 번 확인해주세요.')

        if section.is_visible() and title_text.is_visible() and desc_text.is_visible():
                print("✅ 검색결과 없음 안내 메시지가 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 검색결과 없음 메시지 또는 텍스트가 노출되지 않습니다.")
        
        # '신작 랭킹' 섹션 확인
        ranking_section = page.locator('section.lzComicVX___3l9S.realtime__CrBCX')
        if ranking_section.is_visible():
                print("✅ '신작 랭킹' 섹션이 노출됩니다.")
        else:
                raise AssertionError("❌ '신작 랭킹' 섹션이 노출되지 않습니다.")
        

        # '더보기' 링크 요소
        more_link = ranking_section.locator('a.vx__detailLink', has_text="더보기")
        if not more_link.is_visible():
                raise AssertionError("❌ '더보기' 링크가 노출되지 않습니다.")

        # href 경로 (원래 경로 저장)
        expected_href = more_link.get_attribute("href")
        expected_path = urlparse(expected_href).path

        # 클릭
        more_link.click()
        page.wait_for_load_state("load")
        page.wait_for_timeout(1000)

        # 실제 URL 경로
        actual_path = urlparse(page.url).path

        # 비교
        if actual_path == expected_path:
                print(f"✅ URL 경로 일치: {actual_path}")
        else:
                raise AssertionError(f"❌ URL 경로 불일치: expected '{expected_path}', got '{actual_path}'")


        # 페이지 종료
        page.close()
        
def test_Search_022_artistPage_episodeList(page: Page):
        """해당 코드는 작가페이지 진입 후 첫화보기를 선택합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/artist/howJin?page=1')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # "전체 목록 보기" 버튼 선택
        first_episode_button = page.locator('a[href="/ko/comic/academy_of_card"]', has_text="전체 목록 보기")

        if not first_episode_button.is_visible():
                raise AssertionError("❌ '전체 목록 보기' 버튼이 노출되지 않습니다.")

        # href 추출 후 path 파싱
        expected_href = first_episode_button.get_attribute("href")
        expected_path = urlparse(expected_href).path

        # 클릭
        first_episode_button.click()
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        # 현재 URL path 추출
        actual_path = urlparse(page.url).path

        # 경로 비교
        if actual_path == expected_path:
                print(f"✅ 페이지 이동 성공: {actual_path}")
        else:
                raise AssertionError(f"❌ 페이지 경로 불일치: expected '{expected_path}', got '{actual_path}'")

        # 페이지 종료
        page.close()