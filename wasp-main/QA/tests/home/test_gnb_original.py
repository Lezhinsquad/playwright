from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_Original_01_page_Entry(page: Page):
        """해당 코드는 레진 kr 오리지널 페이지 접근 url 검증 """

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
        original_menu = page.locator('a.navMenu__menuListLink__SV6Kw', has_text="오리지널")
        href = original_menu.get_attribute("href")
        print(f"✅ 오리지널 메뉴 href: {href}")

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
          
        
        
def test_Original_02_page_component_view_ko(page: Page):
        """해당 코드는 레진 kr 오리지널 페이지 접근후 페이지 노출 요소 확인"""

        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/scheduled?day=fin')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
            # 요소 1: 오리지널 타이틀
        title_locator = page.locator('div.scheduledTitle__BpEE2 >> h2')
        assert title_locator.is_visible(), "❌ 오리지널 타이틀이 노출되지 않음"
        print("✅ 오리지널 타이틀이 정상적으로 노출됨")

        # 요소 2: 요일 탭 메뉴
        tab_locator = page.locator('div.lzSticky__xvJ9i div.lzTabs.tabs--original__oeOUP')
        assert tab_locator.is_visible(), "❌ 요일 탭 메뉴가 노출되지 않음"
        print("✅ 요일 탭 메뉴가 정상적으로 노출됨")
        
        # 요소 3: '완결' 섹션 콘텐츠 노출 확인
        fin_section = page.locator('section#scheduled-fin.lzComicVY__FV8aX')
        assert fin_section.is_visible(), "❌ '완결' 콘텐츠 섹션이 노출되지 않음"
        print("✅ '완결' 콘텐츠 섹션이 정상적으로 노출됨")
        
        

        # 페이지 종료
        page.close()
        
        
def test_Original_03_page_component_view_en(page: Page):
        """해당 코드는 레진 US 오리지널 페이지 접근후 페이지 노출 요소 확인"""

        # 레진코믹스 KR 오리지널 이동
        navigate_to(page, 'https://q-www.lezhinus.com/en/daily?day=fin')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
            # 요소 1: 오리지널 타이틀
        title_locator = page.locator('div.scheduledTitle__BpEE2 >> h2')
        assert title_locator.is_visible(), "❌ 오리지널 타이틀이 노출되지 않음"
        print("✅ 오리지널 타이틀이 정상적으로 노출됨")

        # 요소 2: 요일 탭 메뉴
        tab_locator = page.locator('div.lzSticky__xvJ9i div.lzTabs.tabs--original__oeOUP')
        assert tab_locator.is_visible(), "❌ 요일 탭 메뉴가 노출되지 않음"
        print("✅ 요일 탭 메뉴가 정상적으로 노출됨")
        
        # 요소 3: '완결' 섹션 콘텐츠 노출 확인
        fin_section = page.locator('section#scheduled-fin.lzComicVY__FV8aX')
        assert fin_section.is_visible(), "❌ '완결' 콘텐츠 섹션이 노출되지 않음"
        print("✅ '완결' 콘텐츠 섹션이 정상적으로 노출됨")
        
        

        # 페이지 종료
        page.close()
        

def test_Original_04_day_active(page: Page):
        """해당 코드는 레진 ko 오리지널 페이지 접근후 페이지 현재 요일과 활성화된 요일 탭 확인"""
        
        # 레진코믹스 KR 내정보 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/scheduled')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
        # 오늘 요일 (0=월, ..., 6=일)
        today_index = datetime.datetime.today().weekday()

        # Playwright 기준 요일 → data-value 매핑
        weekday_mapping = {
                0: "1",  # 월
                1: "2",  # 화
                2: "3",  # 수
                3: "4",  # 목
                4: "5",  # 금
                5: "6",  # 토
                6: "0",  # 일
        }
        expected_value = weekday_mapping[today_index]
        print(f"✅ 오늘 요일 인덱스: {today_index} → 기대 data-value: {expected_value}")

        # 현재 활성화된 탭 찾기
        active_tab = page.locator('div[role="tablist"] button[aria-selected="true"]')
        assert active_tab.count() == 1, "❌ 활성화된 요일 탭이 하나가 아님"

        actual_value = active_tab.get_attribute("data-value")
        actual_text = active_tab.text_content()

        assert actual_value == expected_value, f"❌ 활성화된 요일 탭 불일치 (기대: {expected_value}, 실제: {actual_value}, 텍스트: {actual_text})"
        print(f"✅ 활성화된 요일 탭이 오늘 요일과 일치함 → {actual_text}({actual_value})")       

        # 페이지 종료
        page.close()
        
        

def test_Original_05_complete_comic(page: Page):
        """해당 코드는 레진 오리지널 페이지 완결 작품 노출 확인"""

        # 결과 저장용
        validation_result = {'invalid_entries': []}

        # API 응답 핸들러 등록
        def handle_response(response):
                try:
                        if (
                                "lz-api/v2/content-list/weekday" in response.url and
                                "filter=completed" in response.url
                        ):
                                json_data = response.json()

                                # 리스트인 경우 바로 사용
                                if isinstance(json_data, list):
                                        items = json_data
                                # 딕셔너리인 경우 'data' -> 'records' 구조에서 추출
                                elif isinstance(json_data, dict):
                                        items = json_data.get("data", {}).get("records", [])
                                else:
                                        raise AssertionError("❌ 예상치 못한 응답 형식")

                                # contentsState가 'completed'이 아닌 항목 검출
                                for content in items:
                                        state = content.get("contentsState")
                                        if state != "completed":
                                                validation_result['invalid_entries'].append({
                                                "title": content.get("title", "제목 없음"),
                                                "contentsState": state
                                                })

                except Exception as e:
                        print(f"❌ 응답 파싱 중 오류 발생 (무시됨): {e}")  # 내부 로깅만 수행

        # 핸들러 등록
        page.on("response", handle_response)

        # 페이지 접근
        navigate_to(page, 'https://q-www.lezhin.com/ko/scheduled?day=fin')
        page.wait_for_load_state('load')
        page.wait_for_timeout(3000)

        # 검증
        if validation_result['invalid_entries']:
                invalid = validation_result['invalid_entries']
                raise AssertionError(f"❌ 'completed' 외 상태 발견: {invalid}")
        else:
                print("✅ 모든 작품의 contentsState가 'completed' 상태입니다.")

        # 페이지 종료
        page.close()
        

def test_Original_06_top_move(page: Page):
        """해당 코드는 KR 오리지널 완결 탭 Top이동 버튼 노출 및 버튼 동작 후 비노출을 검증합니다."""

        # KR 오리지널 완결 탭 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/scheduled?day=fin')


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
        
        
