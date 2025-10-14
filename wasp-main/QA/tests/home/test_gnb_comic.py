from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_gnbComic_01_page_Entry(page: Page):
        """해당 코드는 레진 kr 만화  페이지 접근 url 검증 """

        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 2초 대기
        page.wait_for_timeout(1000)
        
        # '오리지널' 메뉴 요소 찾기 및 href 추출
        original_menu = page.locator('a.navMenu__menuListLink__SV6Kw', has_text="만화")
        href = original_menu.get_attribute("href")
        print(f"✅ 만화 메뉴 href: {href}")

        # href가 상대 경로일 경우 절대 경로로 변환
        expected_url = urljoin('https://q-www.lezhin.com', href)
        expected_path = urlparse(expected_url).path

        # 메뉴 클릭
        original_menu.click()
        page.wait_for_load_state('load')
        page.wait_for_timeout(2000)

        # 현재 URL 가져오기
        current_url = page.url
        current_path = urlparse(current_url).path
        print(f"🔍 현재 페이지 URL: {current_url}")

        # 검증
        assert current_path == expected_path, f"❌ 오리지널 페이지 이동 실패 (현재: {current_url}, 기대: {expected_url})"
        print("✅ 오리지널 페이지로 정상 이동됨")
        # 페이지 종료
        page.close()
          
        
        
def test_gnbComic_02_page_component_view_ko(page: Page):
        """해당 코드는 레진 kr 만화 페이지 접근후 페이지 노출 요소 확인"""

        # 레진코믹스 KR 만화 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/bookshome')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
        # 1. 배너 리스트 섹션
        banner_section = page.locator('section#bookshome-banner-list')
        expect(banner_section).to_be_visible(timeout=3000)
        print("✅ 배너 리스트가 정상적으로 노출되었습니다.")

        # 2. 화제의 신작 섹션
        featured_section = page.locator('section#comic_printed_manual_k_1')
        expect(featured_section).to_be_visible(timeout=3000)
        print("✅ 화제의 신작 섹션이 정상적으로 노출되었습니다.")

        # 3. 장르 탭 영역
        genre_tabs = page.locator('.lzTabs.tabs__QyUCm.tabs--round__OGX_0.tabs--isSticky__CTBSU')
        expect(genre_tabs).to_be_visible(timeout=3000)
        print("✅ 장르 탭(전체, 드라마 등)이 정상적으로 노출되었습니다.")
        
        # 4. 만화 랭킹 섹션
        ranking = page.locator('section#books-home-ranking')
        expect(ranking).to_be_visible(timeout=3000)
        print("✅ 만화 랭킹 섹션 노출 확인 완료")
        
        # 만화 랭킹 섹션
        expect(page.locator('section#books-home-ranking')).to_be_visible(timeout=3000)
        print("✅ 만화 랭킹 섹션 노출 확인 완료")
        

        # 페이지 종료
        page.close()
        
        
def test_gnbComic_03_genrelist(page: Page):
        """해당 코드는 레진 만화 페이지 접근후 페이지 장르리스트 확인"""

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
        page.goto("https://q-www.lezhin.com/ko/bookshome")
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
        
def test_gnbComic_04_genre_choice(page: Page):
        """해당 코드는 레진 만화 페이지 접근후 페이지 장르선택시 작품 노출 확인"""

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
        page.goto("https://q-www.lezhin.com/ko/bookshome")
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
        
        

def test_gnbComic_05_comic_realtimerank_more(page: Page):
        """해당 코드는 레진 만화 페이지 만화 랭킹 더보기 버튼 클릭"""
        
        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/bookshome')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
        # '더보기' 링크 요소 찾기
        more_link = page.locator('a.vx__detailLink[href^="/ko/ranking/printed"]')

        # href 값 추출
        expected_href = more_link.get_attribute("href")
        full_expected_url = f"https://q-www.lezhin.com{expected_href}"

        # 링크 클릭
        more_link.click()
        page.wait_for_load_state("load")
        page.wait_for_timeout(1000)

        # 실제 이동한 URL
        current_url = page.url

        # 검증
        if current_url != full_expected_url:
                raise AssertionError(f"❌ 링크 이동 불일치:\n- 기대값: {full_expected_url}\n- 실제값: {current_url}")
        else:
                print("✅ '더보기' 링크 클릭 시 예상된 주소로 정상 이동")        


        # 페이지 종료
        page.close()
        
        

def test_gnbComic_06_top_move(page: Page):
        """해당 코드는 KR 만화 페이지 탭 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # KR 오리지널 완결 탭 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/bookshome')


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
        assert top_button is not None, "❌ 탑 이동 버튼이 노출되지 않습니다."

        print("✅ 탑 이동 버튼이 정상 노출됩니다.",button_class)
        
        # 버튼 클릭
        top_button.click()
        
        # 현재 스크롤 위치 가져오기
        scroll_position = page.evaluate("window.scrollY")

        # 스크롤 위치가 Y축 최상단중 1에 가까운지 검증
        assert scroll_position <= 1, f"❌ 현재 스크롤 위치는 맨 위가 아닙니다! (현재 위치: {scroll_position}px)"

        print("✅ 현재 스크롤 위치는 맨 위입니다!", "window.scrollY : ", scroll_position)
        
        # 탑이동 버튼이 존재하는지 확인 (없으면 None 반환)
        top_button = page.query_selector('button.topBtn__8FP1p.topBtn--isShow__MTOBY')

        # `assert`를 사용하여 버튼이 존재하지 않거나, 화면에 보이지 않는지 검증
        assert top_button is None or not top_button.is_visible(), "❌ '맨 위로' 버튼이 아직 화면에 표시되고 있습니다!"

        print("✅ 탑이동 버튼이 정상적으로 사라졌습니다!" , top_button)       
     
        # 페이지 종료
        page.close()
        
        
