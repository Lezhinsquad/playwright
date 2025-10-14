from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_gnbfree_01_guidebanner_login(page: Page):
        """해당 코드는 레진 무료페이지 접근후 로그인 상태에서 가이드 배너 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("hidelove99@gmail.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 무료 페이지 접근
        page.goto("https://q-www.lezhin.com/ko/free")

        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 타겟 요소 지정
        guide_banner = page.locator("div.dailyFreeGuideBanner__xV6fg")
           

        # 노출 여부 검증
        if guide_banner.is_visible():
                print("✅ '매일매일무료 사용자 가이드' 배너가 정상적으로 노출되었습니다.")
        else:
                raise AssertionError("❌ '매일매일무료 사용자 가이드' 배너가 페이지에 노출되지 않습니다.")

        page.close()
          
          
def test_gnbfree_02_guidebanner_not_login(page: Page):
        """해당 코드는 레진 무료페이지 접근후 비로그인 상태에서 가이드 배너 노출 확인합니다."""
        
        # 레진코믹스 무료 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/free')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 타겟 요소 지정
        guide_banner = page.locator("div.dailyFreeGuideBanner__xV6fg")
           

        # 노출 여부 검증
        is_visible = guide_banner.is_visible()
        if is_visible:
                print("✅ '매일매일무료 사용자 가이드' 배너가 정상적으로 노출되었습니다.")
        else:
                raise AssertionError("❌ '매일매일무료 사용자 가이드' 배너가 페이지에 노출되지 않습니다.")

        page.close()
        

def test_gnbfree_03_ko_guidebanner_landing(page: Page):
        """해당 코드는 KR 로케일에서 매매무 가이드배너 링크 이동을 확인합니다."""
        
        
        # 레진코믹스 무료 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/free')
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(1000)
        
        # dailyfree-guide 배너 요소 클릭
        banner_link = page.locator('a[href="/ko/dailyfree-guide"]')
        if banner_link.count() == 0:
                raise AssertionError("❌ 해당 배너 요소를 찾을 수 없습니다.")

        href_value = banner_link.get_attribute("href")
        assert href_value is not None, "❌ href 속성이 존재하지 않습니다."

        # 클릭 수행
        banner_link.click()
        page.wait_for_load_state("load")
        page.wait_for_timeout(1500)

        # 현재 URL 정보 가져오기
        current_url = page.url
        parsed_url = urlparse(current_url)

        # 예상 경로 및 파라미터
        expected_path = "/ko/dailyfree-guide"

        # 실제 경로 및 파라미터 추출
        actual_path = parsed_url.path

        # 경로 비교
        if actual_path == expected_path:
                print(f"✅ KR 매매무 가이드배너 경로 일치 확인: {actual_path}")
        else:
                raise AssertionError(f"❌ KR 매매무 가이드배너 경로 불일치: 예상 = {expected_path}, 실제 = {actual_path}")


        # 페이지 종료
        page.close()
        
        
def test_gnbfree_04_us_guidebanner_landing(page: Page):
        """해당 코드는 US 로케일에서 매매무 가이드배너 링크 이동을 확인합니다."""
        
        # 레진코믹스 무료 페이지로 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/free')
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(1000)
        
        # dailyfree-guide 배너 요소 클릭
        banner_link = page.locator('a[href="/en/page/wuf101"]')
        if banner_link.count() == 0:
                raise AssertionError("❌ 해당 배너 요소를 찾을 수 없습니다.")

        href_value = banner_link.get_attribute("href")
        assert href_value is not None, "❌ href 속성이 존재하지 않습니다."

        # 클릭 수행
        banner_link.click()
        page.wait_for_load_state("load")
        page.wait_for_timeout(1500)

        # 현재 URL 정보 가져오기
        current_url = page.url
        parsed_url = urlparse(current_url)

        # 예상 경로 및 파라미터
        expected_path = "/en/page/wuf101"

        # 실제 경로 및 파라미터 추출
        actual_path = parsed_url.path

        # 경로 비교
        if actual_path == expected_path:
                print(f"✅ KR 매매무 가이드배너 경로 일치 확인: {actual_path}")
        else:
                raise AssertionError(f"❌ KR 매매무 가이드배너 경로 불일치: 예상 = {expected_path}, 실제 = {actual_path}")


        # 페이지 종료
        page.close()
        

def test_gnbfree_05_guidebanner_login_unvisible(page: Page):
        """해당 코드는 레진 무료페이지 접근후 로그인 상태에서 가이드 배너 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 무료 페이지 접근
        page.goto("https://q-www.lezhin.com/ko/free")

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 타겟 요소 지정
        guide_banner = page.locator("div.dailyFreeGuideBanner__xV6fg")

        # 노출 여부 검증 (비노출이어야 성공)
        if not guide_banner.is_visible():
                print("✅ '매일매일무료 사용자 가이드' 배너가 비노출 상태입니다.")
        else:
                raise AssertionError("❌ '매일매일무료 사용자 가이드' 배너가 화면에 노출되고 있습니다.")

        page.close()


def test_gnbfree_06_dailyFreeRecent(page: Page):
        """해당 코드는 레진 무료페이지 최근 본 매매무 영역 노출을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')
        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()
        
        # 1초 대기
        page.wait_for_timeout(2000)

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 무료 페이지 접근
        page.goto("https://q-www.lezhin.com/ko/free")

        # 1초 대기
        page.wait_for_timeout(2000)
        
        # "최근 본 매매무" 섹션 요소 찾기
        daily_free_section = page.locator("section.dailyFreeRecent__cgfIv")

        # 노출 여부 검증
        if daily_free_section.is_visible():
                print("✅ '매일 매일 무료' 섹션이 화면에 정상적으로 노출되었습니다.")
        else:
                raise AssertionError("❌ '매일 매일 무료' 섹션이 화면에 노출되지 않았습니다.")

        page.close()

def test_gnbfree_07_comic_Click(page: Page):
        """해당 코드는 최근 본 매매무 영역 작품 클릭 후 페이지 이동을 확인합니다"""
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 페이지 접근
        page.goto("https://q-www.lezhin.com/ko/free")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # 1. 타겟 링크 요소 지정 (최근 본 매매무 첫 번째 작품)
        first_item_link = page.locator("section.dailyFreeRecent__cgfIv li.dailyFreeRecent__listItem__wOt8J a.dailyFreeRecent__link__J1Urz").first
        href_value = first_item_link.get_attribute("href")


        # 클릭 및 이동
        first_item_link.click()
        page.wait_for_load_state('load')
        # 1초 대기
        page.wait_for_timeout(1000)

        # 검증
        current_path = urlparse(page.url).path

        if current_path == href_value:
                print(f"✅ 링크 클릭 후 경로 일치 확인: {current_path}")
        else:
                raise AssertionError(f"❌ 링크 클릭 후 경로 불일치! 기대: {href_value}, 실제: {current_path}")

        page.close() 
        

def test_gnbfree_08_ko_genreList(page: Page):
        """해당 코드는 KO 무료 페이지 접근후 페이지 장르리스트 확인합니다."""

        api_genre_labels = []

        # API 응답 인터셉트 핸들러
        def handle_response(response):
                if "genres/filtered" in response.url:
                        try:
                                json_data = response.json()

                                # 리스트 형태가 아닐 경우 무시
                                if not isinstance(json_data, list):
                                        print(f"⚠️ 예외: 예상치 못한 응답 형식(type={type(json_data)}), 무시됨.")
                                        return

                                for item in json_data:
                                        label = item.get("label")
                                        if label:
                                                api_genre_labels.append(label.strip())

                        except Exception as e:
                                print(f"⚠️ 응답 파싱 중 오류 발생(무시됨): {e}")

        # 응답 핸들러 등록
        page.on("response", handle_response)

        # 페이지 접근
        page.goto("https://q-www.lezhin.com/ko/free")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        # DOM에서 장르 버튼 텍스트 수집
        tab_buttons = page.locator(".tabs--round__OGX_0.tabs--isSticky__CTBSU button")
        dom_labels = [tab_buttons.nth(i).inner_text().strip() for i in range(tab_buttons.count())]

        # 검증: 모든 API label이 페이지 버튼에 포함되어야 함
        missing_labels = [label for label in api_genre_labels if label not in dom_labels]

        if missing_labels:
                raise AssertionError(f"❌ 다음 label이 DOM에 존재하지 않음: {missing_labels}")
        else:
                print("✅ 모든 API label이 장르 탭에 정상적으로 노출됨")

        page.close()
        

def test_gnbfree_09_us_genreList(page: Page):
        """해당 코드는 US 무료 페이지 접근후 페이지 장르리스트 확인합니다."""

        api_genre_labels = []

        # API 응답 인터셉트 핸들러
        def handle_response(response):
                if "genres/filtered" in response.url:
                        try:
                                json_data = response.json()

                                # 리스트 형태가 아닐 경우 무시
                                if not isinstance(json_data, list):
                                        print(f"⚠️ 예외: 예상치 못한 응답 형식(type={type(json_data)}), 무시됨.")
                                        return

                                for item in json_data:
                                        label = item.get("label")
                                        if label:
                                                api_genre_labels.append(label.strip())

                        except Exception as e:
                                print(f"⚠️ 응답 파싱 중 오류 발생(무시됨): {e}")

        # 응답 핸들러 등록
        page.on("response", handle_response)

        # 페이지 접근
        page.goto("https://q-www.lezhinus.com/en/free")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        # DOM에서 장르 버튼 텍스트 수집
        tab_buttons = page.locator(".tabs--round__OGX_0.tabs--isSticky__CTBSU button")
        dom_labels = [tab_buttons.nth(i).inner_text().strip() for i in range(tab_buttons.count())]

        # 검증: 모든 API label이 페이지 버튼에 포함되어야 함
        missing_labels = [label for label in api_genre_labels if label not in dom_labels]

        if missing_labels:
                raise AssertionError(f"❌ 다음 label이 DOM에 존재하지 않음: {missing_labels}")
        else:
                print("✅ 모든 API label이 장르 탭에 정상적으로 노출됨")

        page.close()
        

def test_gnbfree_10_genre_choice(page: Page):
        """해당 코드는 무료페이지 장르 선택시 노출되는 작품의 장르값이 올바른지 확인합니다."""

        # API 응답 인터셉트 핸들러
        def handle_response(response):
                if "https://q-www.lezhin.com/lz-api/v2/content-list/free" in response.url:
                        try:
                                json_data = response.json()
                                for item in json_data.get("data", []):
                                        genres = item.get("genres", [])
                                        if "romance" not in genres:
                                                raise AssertionError(f"❌ 'romance' 장르가 포함되지 않은 항목이 있습니다: {item.get('title')}")
                                        print("✅ 모든 콘텐츠에 'romance' 장르가 포함되어 있습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 처리 중 오류 발생: {e}")
                        

        # 응답 핸들러 등록
        page.on("response", handle_response)

        # 페이지 접근
        page.goto("https://q-www.lezhin.com/ko/free?genre=romance")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)


        page.close()
          

def test_gnbfree_11_top_move(page: Page):
        """해당 코드는 무료 페이지 탭 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # KR 오리지널 완결 탭 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/free')


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # Top이동이 노출되도록 스크롤 진행
        page.evaluate("window.scrollTo(0, 1000)")
        
        # 탑 이동 버튼 요소 찾기
        top_button = page.wait_for_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY', timeout=2000)
        
        # 탑 이동 버튼의 클래스명 가져와서 변수에 저장
        button_class = top_button.get_attribute("class")

        # 버튼이 존재하는지 검증
        if top_button is not None:
                print("✅ 탑 이동 버튼이 정상 노출됩니다.", button_class)
        else:
                raise AssertionError("❌ 탑 이동 버튼이 노출되지 않습니다.")
        
        # 버튼 클릭
        top_button.click()
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 현재 스크롤 위치 가져오기
        scroll_position = page.evaluate("window.scrollY")

        # 스크롤 위치가 Y축 최상단중 1에 가까운지 검증
        if scroll_position <= 1:
                print("✅ 현재 스크롤 위치는 맨 위입니다!", "window.scrollY :", scroll_position)
        else:
                raise AssertionError(f"❌ 현재 스크롤 위치는 맨 위가 아닙니다! (현재 위치: {scroll_position}px)")
        
        # 탑이동 버튼이 존재하는지 확인 (없으면 None 반환)
        top_button = page.query_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY')

        # '맨 위로' 버튼이 보이지 않는지 검증
        if top_button is None or not top_button.is_visible():
                print("✅ 탑이동 버튼이 정상적으로 사라졌습니다!", top_button)
        else:
                raise AssertionError("❌ '맨 위로' 버튼이 아직 화면에 표시되고 있습니다!")
     
        # 페이지 종료
        page.close()
        
        
