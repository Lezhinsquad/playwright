from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu
from urllib.parse import urlparse, parse_qs, urlencode, quote

def test_Contents_01_lezhin_home_TopBanner_view(page: Page):
        """해당 코드는 KR 로케일에서 탑배너 영역이 노출되는것을 확인합니다."""
        
        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 탑 배너 요소 찾기
        top_banner = page.wait_for_selector("div.topBanner__qxAxf", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        class_id = top_banner.get_attribute("class")

        # `assert`를 사용하여 탑배너 영역이 존재하는지 확인
        assert class_id is not None, "❌ 탑배너 영역이 정상적으로 노출되지 않았습니다."

        print(" 탑배너 class : ", class_id)
        print("✅ KR `탑배너` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()  

def test_Contents_02_lezhin_home_heroBanner_view(page: Page):
        """해당 코드는 KR 로케일에서 히어로배너 영역이 노출되는것을 확인합니다."""
        
        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 히어로배너 배너 요소 찾기
        hero_banner = page.wait_for_selector("div.carousel__GXXM_", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        class_id = hero_banner.get_attribute("class")

        # `assert`를 사용하여 히어로배너 영역이 존재하는지 확인
        assert class_id is not None, "❌ 히어로배너 영역이 정상적으로 노출되지 않았습니다."

        print(" 히어로배너 class : ", class_id)
        print("✅ KR `히어로배너` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()  
        
def test_Contents_03_lezhin_home_realtime_rank_view(page: Page):
        """해당 코드는 KR 로케일에서 실시간랭킹 영역이 노출되는것을 확인합니다."""


        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 실시간 랭킹 요소 찾기
        realtime_rank = page.wait_for_selector("section#concept_ranking", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        realtime_id = realtime_rank.get_attribute("id")

        # `assert`를 사용하여 실시간 랭킹 영역이 존재하는지 확인
        assert realtime_id is not None, "❌ 실시간 랭킹 영역이 정상적으로 노출되지 않았습니다."

        print(" 실시간 랭킹  id  : ", realtime_id)
        print("✅ KR `실시간 랭킹` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()
        


def test_Contents_04_lezhin_home_comic_scheduled_view(page: Page):
        """해당 코드는 KR 로케일에서  레진 신작 더보기 영역 노출되는것을 확인합니다."""

        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 레진 신작 영역 요소 찾기
        comic_scheduled = page.wait_for_selector("section#comic_scheduled_latest_k", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        comic_scheduled_id = comic_scheduled.get_attribute("id")

        # `assert`를 사용하여 레진 신작  영역이 존재하는지 확인
        assert comic_scheduled_id is not None, "❌ 레진 신작  영역이 정상적으로 노출되지 않았습니다."

        print(" 레진 신작   id  : ", comic_scheduled_id)
        print("✅ KR `레진 신작 ` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()
        
        
def test_Contents_05_lezhin_home_new_comic_view(page: Page):
        """해당 코드는 KR 로케일에서  신규만화 보기  노출되는것을 확인합니다."""

        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 신규 만화 영역  요소 찾기
        comic_new = page.wait_for_selector("section#comic_scheduled_latest_k", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        comic_new_id = comic_new.get_attribute("id")

        # `assert`를 사용하여 신규만화  영역이 존재하는지 확인
        assert comic_new_id is not None, "❌ 신규만화  영역이 정상적으로 노출되지 않았습니다."

        print(" 신규만화  id  : ", comic_new_id)
        print("✅ KR `신규만화 ` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()
        
        
def test_Contents_06_lezhin_home_subscription_view(page: Page):
        """해당 코드는 KR 로케일에서  업데이트된 찜한 작품 영역 노출되는것을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 업데이트된 찜한 작품 요소 찾기
        subscription = page.wait_for_selector("section#order_up_subscription", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        subscription_id = subscription.get_attribute("id")

        # `assert`를 사용하여 업데이트된 찜한 작품  영역이 존재하는지 확인
        assert subscription_id is not None, "❌ 업데이트된 찜한 작품  영역이 정상적으로 노출되지 않았습니다."

        print(" 업데이트된 찜한 작품  id  : ", subscription_id)
        print("✅ KR `업데이트된 찜한 작품 ` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()



def test_Contents_08_lezhin_home_recents_view(page: Page):
        """해당 코드는 KR 로케일에서  최근 본 작품 영역 노출되는것을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 최근 본 작품 요소 찾기
        recents = page.wait_for_selector("section#order_recent", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        recents_id = recents.get_attribute("id")

        # `assert`를 사용하여 최근 본 작품  영역이 존재하는지 확인
        assert recents_id is not None, "❌ 최근 본 작품 영역이 정상적으로 노출되지 않았습니다."

        print(" 최근 본 작품  id  : ", recents_id)
        print("✅ KR `최근 본 작품 ` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()
        


def test_Contents_09_lezhin_home_origianl_view(page: Page):
        """해당 코드는 KR 로케일에서 레진 오리지널 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 레진 오리지널  요소 찾기
        element = page.wait_for_selector('div.lezhinOriginal__Cauqd', timeout=3000)
        
        # class 속성값 가져와서 변수에 저장
        class_name = element.get_attribute("class")

        # `assert`를 사용하여 레진 오리지널 영역이 존재하는지 확인
        assert class_name is not None, "❌ KR 레진 오리지널 영역이 정상적으로 노출되지 않았습니다."

        print(" 레진 오리지널  class  : ", class_name)
        print("✅ KR `레진 오리지널` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()
        
        
def test_Contents_10_lezhin_home_subBanner1_2_3_view(page: Page):
        """해당 코드는 KR 로케일에서 서브배너 1,2,3 영역이 노출되는것을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        
        # 홈으로 이동
        page.goto("https://www.lezhin.com/ko")
        page.wait_for_load_state('load')
        page.wait_for_timeout(1000)

        
        
        # 각 요소 선택자
        element_ids = ['home_sub_1', 'home_sub_2', 'home_sub_3_a']
        
        # 각 요소가 DOM에 존재하는지 확인
        for element_id in element_ids:
                locator = page.query_selector(f'#{element_id}')
                assert locator is not None, f"❌ 요소 #{element_id} 가 DOM에 존재하지 않습니다."
                print(f"✅ 요소 #{element_id} 가 DOM에 존재합니다.")
                
        # 페이지 종료
        page.close()
        
        
def test_Contents_11_lezhin_home_saleBanner_view(page: Page):
        """해당 코드는 KR 로케일에서  세일배너 노출되는것을 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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
        page.wait_for_timeout(2000)
        
        # 홈 > 세일 배너 요소 찾기
        saleBanner = page.wait_for_selector("section#sale_hooking_promotion_adultBL", timeout=5000)
        

        # class 속성값 가져와서 변수에 저장
        saleBanner_id = saleBanner.get_attribute("id")

        # `assert`를 사용하여 홈 > 세일 배너  영역이 존재하는지 확인
        assert saleBanner_id is not None, "❌ 홈 > 세일 배너 영역이 정상적으로 노출되지 않았습니다."

        print(" 홈 > 세일 배너  : ", saleBanner_id)
        print("✅ KR `홈 > 세일 배너 ` 영역이 정상적으로 노출되었습니다!")
     
        # 페이지 종료
        page.close()
        

def test_Contents_12_lezhin_home_TopBanner_click(page: Page):
        """해당 코드는 KR 로케일에서 탑배너의 첫번째 배너 클릭 후 페이지 이동을 확인합니다."""
        
        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 첫 번째 배너 링크 요소
        banner_link = page.locator(".topBanner__link__QXirT").nth(1)
        
        # href 속성 추출
        href_value = banner_link.get_attribute("href")
        assert href_value, "❌ href 속성이 존재하지 않습니다."
                

        # 클릭 
        banner_link.click(force=True)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 실제 이동한 URL
        current_url = page.url

        # 경로 비교만 수행
        expected_path = urlparse(href_value).path
        actual_path = urlparse(current_url).path

        if expected_path == actual_path:
                print(f"✅ 경로 일치 확인: {actual_path}")
        else:
                raise AssertionError(f"❌ 경로 불일치: {expected_path} vs {actual_path}")
     
        # 페이지 종료
        page.close()  
        
def test_Contents_13_lezhin_home_heroBanner_click(page: Page):
        """해당 코드는 KR 로케일에서 히어로배너 첫번째 배너 클릭 후 페이지 이동을 확인합니다."""
        
        def extract_path(url):
                return urlparse(url).path
        
        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 노출시킬 슬라이드 인덱스 지정 (0 = 첫 배너, 1 = 두 번째, ...)
        target_index = 2  # 세 번째 배너 클릭을 원할 경우
        
        # "다음" 버튼을 target_index 만큼 클릭해서 해당 배너 노출
        next_button = page.locator('button.heroBanner__navBtn--next__N5B17')
        for _ in range(target_index):
                next_button.click()
                page.wait_for_timeout(500)  # 슬라이딩 전환 시간 고려

        # 현재 보이는 슬라이드들 중 a태그가 있는 것만 필터링
        slides = page.locator(".heroBanner__slide__sJpGJ")
        visible_links = []
        for i in range(slides.count()):
                slide = slides.nth(i)
                if slide.is_visible():
                        try:
                                box = slide.bounding_box()
                                if box:
                                        link = slide.locator("a.heroBanner__link__6zGAw")
                                        visible_links.append(link)
                        except:
                                continue

        assert len(visible_links) > 0, "❌ 화면에 노출된 배너가 없습니다."

        # visible_links는 가로 슬라이딩 후 현재 보이는 슬라이드 3개로 구성됨
        # 그 중 마지막에 노출된 배너를 선택하려면 [-1] 또는 원하는 index로
        banner_link = visible_links[-1]  # 세 번째 클릭 후 마지막 노출 배너를 선택
        href_value = banner_link.get_attribute("href")
        assert href_value, "❌ href 속성이 존재하지 않습니다."

        # 클릭 및 페이지 이동 대기
        with page.expect_navigation(wait_until="load"):
                banner_link.click()
                
        # 1초 대기
        page.wait_for_timeout(1000)

        # 도메인 비교
        expected_path = extract_path(href_value)
        actual_path = extract_path(page.url)

        assert expected_path == actual_path, f"❌ 경로 불일치: {expected_path} vs {actual_path}"
        print(f"✅ 경로 일치 확인: {actual_path}")

    
        page.close()
        


def test_Contents_14_lezhin_home_subBanner1_2_3_click(page: Page):
        """해당 코드는 KR 로케일에서 서브배너1,2,3 배너 클릭 후 페이지 이동을 확인합니다."""
        
        def extract_path(url):
                return urlparse(url).path
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        
        # 첫번쨰 서브배너 요소 선택
        banner_1 = page.locator("#home_sub_2 a")
        href_value_1 = banner_1.get_attribute("href")
        assert href_value_1, "❌ href 속성이 존재하지 않습니다."
        
        # 클릭 전 요소가 보이도록 강제 스크롤
        banner_1.scroll_into_view_if_needed()
        page.wait_for_timeout(1500)  # 짧은 대기 추가 
        
        # 클릭 및 이동 대기
        with page.expect_navigation(wait_until="load"):
                banner_1.click(force=True)

        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 경로 비교
        expected_path_1 = extract_path(href_value_1)
        actual_path_1 = extract_path(page.url)

        assert expected_path_1 == actual_path_1, f"❌ 경로 불일치: {expected_path_1} vs {actual_path_1}"
        print(f"✅ 경로 일치 확인: {actual_path_1}")
        
        page.goto('https://www.lezhin.com/ko/')
        page.wait_for_load_state('load')
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 두번째 서브배너 요소 선택
        banner_2 = page.locator("#home_sub_3_a a")
        href_value_2 = banner_2.get_attribute("href")
        assert href_value_2, "❌ href 속성이 존재하지 않습니다."
        
        # 클릭 전 요소가 보이도록 강제 스크롤
        banner_2.scroll_into_view_if_needed()
        page.wait_for_timeout(1500)  # 짧은 대기 추가 
        
        # 클릭 및 이동 대기
        with page.expect_navigation(wait_until="load"):
                banner_2.click(force=True)

        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 경로 비교
        expected_path_2 = extract_path(href_value_2)
        actual_path_2 = extract_path(page.url)

        assert expected_path_2 == actual_path_2, f"❌ 경로 불일치: {expected_path_2} vs {actual_path_2}"
        print(f"✅ 경로 일치 확인: {actual_path_2}")
        
        page.goto('https://www.lezhin.com/ko/')
        page.wait_for_load_state('load')
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 세번째 서브배너 요소 선택
        banner_3 = page.locator("#home_sub_1 a")
        href_value_3 = banner_3.get_attribute("href")
        assert href_value_3, "❌ href 속성이 존재하지 않습니다."
        
        # 클릭 전 요소가 보이도록 강제 스크롤
        banner_3.scroll_into_view_if_needed()
        page.wait_for_timeout(1500)  # 짧은 대기 추가 
        
        # 클릭 및 이동 대기
        with page.expect_navigation(wait_until="load"):
                banner_3.click(force=True)

        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 경로 비교
        expected_path_3 = extract_path(href_value_3)
        actual_path_3 = extract_path(page.url)

        assert expected_path_3 == actual_path_3, f"❌ 경로 불일치: {expected_path_3} vs {actual_path_3}"
        print(f"✅ 경로 일치 확인: {actual_path_3}")
                        
        # 페이지 종료
        page.close()
        
        
def test_Contents_15_lezhin_home_sale_click(page: Page):
        """해당 코드는 KR 로케일에서 성인 세일배너 클릭 후 페이지 이동을 확인합니다."""

         # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("squad@lezhin.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()
        # 2초 대기
        page.wait_for_timeout(2000)
        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)

         # 첫 번째 세일 배너 링크 찾기
        selector = 'section#sale_hooking_promotion_a li.bannerList__item a.bannerList__link'
        link = page.locator(selector).first

        # 요소 존재 확인
        assert link.element_handle() is not None, "❌ 첫 번째 프로모션 배너가 존재하지 않습니다."

        # href 및 class 정보 확인
        target_url = link.get_attribute("href")
        class_name = link.get_attribute("class")
        print("✅ 배너 클래스:", class_name)
        print("➡ 이동 예정 URL:", target_url)

        # 스크롤 및 클릭
        link.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        link.click()

        # 페이지 로딩 후 URL 확인
        page.wait_for_timeout(3000)
        current_url = page.url

        from urllib.parse import urlparse
        parsed_current = urlparse(current_url)
        parsed_target = urlparse(target_url)

        current_path = parsed_current.path + ('?' + parsed_current.query if parsed_current.query else '')
        target_path = parsed_target.path + ('?' + parsed_target.query if parsed_target.query else '')

        assert current_path == target_path, f"❌ 배너 클릭 후 URL 이동 실패 (현재: {current_path}, 기대값: {target_path})"
        print("✅ 배너 클릭 시 정상적으로 이동되었습니다. (", current_path, ")")

        # 종료
        page.close()
        
        
def test_Contents_15_lezhin_gnb_comic_genreList(page: Page):
        """해당 코드는 레진 만화 페이지 접근후 페이지 장르리스트 확인합니다."""

        api_genre_labels = []

        # API 응답 인터셉트 핸들러
        def handle_response(response):
                if "genres/filtered" in response.url:
                        json_data = response.json()
                        if isinstance(json_data, list) and all(isinstance(item, dict) for item in json_data):
                                for item in json_data:
                                        label = item.get("label")
                                        if label:
                                                api_genre_labels.append(label.strip())

        # 응답 핸들러 등록
        page.on("response", handle_response)


        # 페이지 접근
        page.goto("https://www.lezhin.com/ko/bookshome")
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
        

def test_Contents_16_lezhin_gnb_comic_genre_choice(page: Page):
        """해당 코드는 레진 만화 페이지 접근후 페이지 장르선택시 작품 노출 확인합니다."""

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
        page.goto("https://www.lezhin.com/ko/bookshome")
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


def test_Contents_17_lezhin_gnb_comic_bannerClick(page: Page):
        """해당 코드는 레진 만화 페이지의 배너 클릭 후 페이지 이동을 확인합니다"""

        def extract_path(url):
                return urlparse(url).path

        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/bookshome")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        
        
        # 첫 번째 배너 링크 선택
        first_banner = page.locator("#bookshome-banner-list .bannerList__link").first
        href_value = first_banner.get_attribute("href")
        assert href_value, "❌ 첫 번째 배너의 href 속성이 존재하지 않습니다."

        # 요소를 뷰포트에 노출시킴
        first_banner.scroll_into_view_if_needed()
        page.wait_for_timeout(300)

        # 클릭 및 이동
        with page.expect_navigation(wait_until="load"):
                first_banner.click(force=True)

        # 경로 비교
        expected_path = extract_path(href_value)
        actual_path = extract_path(page.url)

        assert expected_path == actual_path, f"❌ 경로 불일치: {expected_path} vs {actual_path}"
        print(f"✅ 경로 일치 확인: {actual_path}")

        page.close()
        

def test_Contents_18_lezhin_gnb_genrePlus_genreList(page: Page):
        """해당 코드는 레진 장르+ 페이지 접근후 페이지 장르리스트 확인합니다."""

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
        page.goto("https://www.lezhin.com/ko/genreplus")
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
        

def test_Contents_19_lezhin_gnb_genrePlus_genre_choice(page: Page):
        """해당 코드는 레진 장르+ 페이지 접근후 페이지 장르선택시 작품 노출 확인합니다."""

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
        page.goto("https://www.lezhin.com/ko/genreplus")
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


def test_Contents_20_lezhin_gnb_genrePlus_bannerClick(page: Page):
        """해당 코드는 레진 장르+  페이지의 배너 클릭 후 페이지 이동을 확인합니다"""

        def extract_path(url):
                return urlparse(url).path
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/genreplus")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # 첫 번째 배너 링크 선택
        first_banner = page.locator("#exhibit-genreplus-banner-list .bannerList__link").first
        href_value = first_banner.get_attribute("href")
        assert href_value, "❌ 첫 번째 배너의 href 속성이 존재하지 않습니다."

        # 요소를 뷰포트에 노출시킴
        first_banner.scroll_into_view_if_needed()
        page.wait_for_timeout(300)

        # 클릭 및 이동
        with page.expect_navigation(wait_until="load"):
                first_banner.click(force=True)
        
        # 경로 비교
        expected_path = extract_path(href_value)
        actual_path = extract_path(page.url)

        assert expected_path == actual_path, f"❌ 경로 불일치: {expected_path} vs {actual_path}"
        print(f"✅ 경로 일치 확인: {actual_path}")


        page.close()
        
        
def test_Contents_21_lezhin_gnb_free_guidebanner_not_login(page: Page):
        """해당 코드는 레진 무료페이지 접근후 비로그인 상태에서 가이드 배너 노출 확인합니다."""
        
        # 레진코믹스 무료 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/free')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 타겟 요소 지정
        guide_banner = page.locator("div.dailyFreeGuideBanner__xV6fg")
           

        # 노출 여부 검증
        is_visible = guide_banner.is_visible()
        assert is_visible, "❌ '매일매일무료 사용자 가이드' 배너가 페이지에 노출되지 않습니다."
        print("✅ '매일매일무료 사용자 가이드' 배너가 정상적으로 노출되었습니다.")

        page.close()
        

def test_Contents_22_lezhin_gnb_free_guidebanner_login(page: Page):
        """해당 코드는 레진 무료페이지 접근후 로그인 상태에서 가이드 배너 노출 확인합니다."""
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("hidelove99@gmail.com")
        # 비밀번호 입력
        page.locator("#password").fill("wlscogus7!")
        # 로그인 버튼 클릭
        page.locator('button:has-text("이메일로 로그인")').click()


        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        
        # 무료 페이지 접근
        page.goto("https://www.lezhin.com/ko/free")

        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 타겟 요소 지정
        guide_banner = page.locator("div.dailyFreeGuideBanner__xV6fg")
           

        # 노출 여부 검증
        is_visible = guide_banner.is_visible()
        assert is_visible, "❌ '매일매일무료 사용자 가이드' 배너가 페이지에 노출되지 않습니다."
        print("✅ '매일매일무료 사용자 가이드' 배너가 정상적으로 노출되었습니다.")

        page.close()


def test_Contents_23_lezhin_gnb_free_genreList(page: Page):
        """해당 코드는 레진 무료 페이지 접근후 페이지 장르리스트 확인합니다."""

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
        page.goto("https://www.lezhin.com/ko/free")
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
        

def test_Contents_24_lezhin_gnb_free_genre_choice(page: Page):
        """해당 코드는 무료페이지 장르 선택시 노출되는 작품의 장르값이 올바른지 확인합니다."""

        # API 응답 인터셉트 핸들러
        def handle_response(response):
                if "https://www.lezhin.com/lz-api/v2/content-list/free" in response.url:
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
        page.goto("https://www.lezhin.com/ko/free?genre=romance")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)


        page.close()


def test_Contents_25_lezhin_gnb_free_herebanner_Click(page: Page):
        """해당 코드는 레진 무료  페이지의 히어로 배너 클릭 후 페이지 이동을 확인합니다"""

        def extract_path(url):
                return urlparse(url).path
        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/free")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # 첫 번째 히어로 배너 링크 선택
        first_banner = page.locator("#dailyfree-banner-list .bannerList__link").first
        href_value = first_banner.get_attribute("href")
        assert href_value, "❌ 첫 번째 히어로배너 href 속성이 존재하지 않습니다."

        # 요소를 뷰포트에 노출시킴
        first_banner.scroll_into_view_if_needed()
        page.wait_for_timeout(300)

        # 클릭 및 이동
        with page.expect_navigation(wait_until="load"):
                first_banner.click(force=True)

        # 도메인 비교
        expected_path = extract_path(href_value)
        actual_path = extract_path(page.url)

        assert expected_path == actual_path, f"❌ 경로 불일치: {expected_path} vs {actual_path}"
        print(f"✅ 경로 일치 확인: {actual_path}")

        page.close() 
        


def test_Contents_26_lezhin_gnb_adult19_bannerClick(page: Page):
        """해당 코드는 레진 성인19  페이지의 배너 클릭 후 페이지 이동을 확인합니다"""

        def extract_path(url):
                return urlparse(url).path

        
        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/nsfw")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # 첫 번째 배너 링크 선택
        first_banner = page.locator("#exhibit-nsfw-banner-list .bannerList__link").first
        href_value = first_banner.get_attribute("href")
        assert href_value, "❌ 첫 번째 배너의 href 속성이 존재하지 않습니다."

        # 요소를 뷰포트에 노출시킴
        first_banner.scroll_into_view_if_needed()
        page.wait_for_timeout(300)

        # 클릭 및 이동
        with page.expect_navigation(wait_until="load"):
                first_banner.click(force=True)

        # 도메인 비교
        expected_path = extract_path(href_value)
        actual_path = extract_path(page.url)

        assert expected_path == actual_path, f"❌ 경로 불일치: {expected_path} vs {actual_path}"
        print(f"✅ 경로 일치 확인: {actual_path}")

        page.close() 
        
def test_Contents_27_lezhin_gnb_ranking_genreList(page: Page):
        """해당 코드는 레진 랭킹 페이지 접근후 페이지 장르리스트 확인합니다."""

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
        page.goto("https://www.lezhin.com/ko/ranking")
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
        

def test_Contents_28_lezhin_gnb_ranking_genre_choice(page: Page):
        """해당 코드는 레진 랭킹 페이지 접근후 페이지 장르선택시 작품 노출 확인합니다."""

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
        page.goto("https://www.lezhin.com/ko/ranking")
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
        


def test_Contents_29_lezhin_newReleases_all(page: Page):
        """해당 코드는 레진 신작 더보기 접근후 전체 탭에 성인 + 비성인 작품 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/scheduled/new-released")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")

        has_adult_badge = False
        has_non_adult_thumbnail = False

        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if badge:
                has_adult_badge = True
            else:
                has_non_adult_thumbnail = True

        # 조건: 19세 뱃지 있는 썸네일 + 없는 썸네일 모두 존재해야 PASS
        assert has_adult_badge and has_non_adult_thumbnail, "❌ 19세 뱃지와 19세 뱃지가 없는 썸네일이 모두 존재해야 합니다."
        print("✅ 19세 뱃지가 있는 썸네일과 없는 썸네일이 모두 존재합니다. (PASS)")

        page.close()
        

def test_Contents_29_lezhin_newReleases_kid(page: Page):
        """해당 코드는 레진 신작 더보기 접근후 전연령 탭에 비성인 작품 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://q-www.lezhin.com/ko/scheduled/new-released?t=kid&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # vy__thumbnail vy__thumbnail--tall 요소 모두 가져오기
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")

        has_adult_badge = False

        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if badge:
                has_adult_badge = True
                break  # 하나만 있어도 바로 fail 처리하기 위해 loop 종료

        # 조건: 성인 뱃지가 하나라도 있으면 FAIL
        assert not has_adult_badge, "❌ 19세 뱃지가 있는 썸네일이 발견되었습니다. (FAIL)"
        print("✅ 19세 뱃지가 있는 썸네일이 없습니다. (PASS)")

        page.close()
        

def test_Contents_30_lezhin_newReleases_adult(page: Page):
        """해당 코드는 레진 신작 더보기 접근후 성인 탭에 성인 작품 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/scheduled/new-released?t=adult&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # vy__thumbnail vy__thumbnail--tall 요소 모두 가져오기
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")

        all_adult_badge = True

        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if not badge:
                all_adult_badge = False
                break  # 성인 뱃지가 없는 썸네일 발견 시 바로 실패 처리

        # 조건: 성인 뱃지가 하나라도 없으면 FAIL
        assert all_adult_badge, "❌ 성인 뱃지가 없는 썸네일이 발견되었습니다. (FAIL)"
        print("✅ 모든 썸네일에 19세 뱃지가 있습니다. (PASS)")

        page.close()


def test_Contents_31_lezhin_newComic_all(page: Page):
        """해당 코드는 레진 신작 더보기 접근후 전체 탭에 성인 + 비성인 작품 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/bookshome/new-released")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")

        has_adult_badge = False
        has_non_adult_thumbnail = False

        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if badge:
                has_adult_badge = True
            else:
                has_non_adult_thumbnail = True

        # 조건: 19세 뱃지 있는 썸네일 + 없는 썸네일 모두 존재해야 PASS
        assert has_adult_badge and has_non_adult_thumbnail, "❌ 19세 뱃지와 19세 뱃지가 없는 썸네일이 모두 존재해야 합니다."
        print("✅ 19세 뱃지가 있는 썸네일과 없는 썸네일이 모두 존재합니다. (PASS)")

        page.close()
        

def test_Contents_32_lezhin_newReleases_kid(page: Page):
        """해당 코드는 레진 신작 더보기 접근후 전연령 탭에 비성인 작품 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://q-www.lezhin.com/ko/bookshome/new-released?t=kid&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # vy__thumbnail vy__thumbnail--tall 요소 모두 가져오기
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")

        has_adult_badge = False

        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if badge:
                has_adult_badge = True
                break  # 하나만 있어도 바로 fail 처리하기 위해 loop 종료

        # 조건: 성인 뱃지가 하나라도 있으면 FAIL
        assert not has_adult_badge, "❌ 19세 뱃지가 있는 썸네일이 발견되었습니다. (FAIL)"
        print("✅ 19세 뱃지가 있는 썸네일이 없습니다. (PASS)")

        page.close()
        

def test_Contents_33_lezhin_newReleases_adult(page: Page):
        """해당 코드는 레진 신작 더보기 접근후 성인 탭에 성인 작품 노출 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        page.goto("https://www.lezhin.com/ko/bookshome/new-released?t=adult&order=new_last_year")
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
                
        # vy__thumbnail vy__thumbnail--tall 요소 모두 가져오기
        thumbnails = page.query_selector_all('.vy__thumbnail.vy__thumbnail--tall')
        print(f"✅ 썸네일 개수: {len(thumbnails)}")

        all_adult_badge = True

        for thumbnail in thumbnails:
            badge = thumbnail.query_selector('i.lzBadge__thumbnail--adult')
            if not badge:
                all_adult_badge = False
                break  # 성인 뱃지가 없는 썸네일 발견 시 바로 실패 처리

        # 조건: 성인 뱃지가 하나라도 없으면 FAIL
        assert all_adult_badge, "❌ 성인 뱃지가 없는 썸네일이 발견되었습니다. (FAIL)"
        print("✅ 모든 썸네일에 19세 뱃지가 있습니다. (PASS)")

        page.close()
        
def test_Contents_34_lezhin_gnb_event_bannerClick(page: Page):
        """해당 코드는 레진 이벤트  페이지의 배너 클릭 후 페이지 이동을 확인합니다"""

        def extract_path(url):
                return urlparse(url).path
        
        # 레진코믹스 이벤트 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/sale')
                
        # 첫 번째 배너 링크 선택
        first_banner = page.locator("section.saleBanner__zrcjx ul.saleBanner__list__sJWVE li").first.locator("a.bannerList__link")
        href_value = first_banner.get_attribute("href")
        assert href_value, "❌ 첫 번째 배너의 href 속성이 존재하지 않습니다."

        # 요소를 뷰포트에 노출시킴
        first_banner.scroll_into_view_if_needed()
        page.wait_for_timeout(300)

        # 클릭 및 이동
        with page.expect_navigation(wait_until="load"):
                first_banner.click(force=True)
        
        # 경로 비교
        expected_path = extract_path(href_value)
        actual_path = extract_path(page.url)

        assert expected_path == actual_path, f"❌ 경로 불일치: {expected_path} vs {actual_path}"
        print(f"✅ 경로 일치 확인: {actual_path}")


        page.close()
        
        

def test_Contents_35_lezhin_Preferences_templete_view_not_login(page: Page):
        """해당 코드는 비로그인상태에서 취향설정 템플릿이 노출되는지 확인 확인합니다"""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)

        # 취향설정 템플릿 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 템플릿 탐색 및 존재 확인
        element = page.wait_for_selector(selector, timeout=3000)
        assert element is not None, "❌ preferenceTemplate 요소를 찾을 수 없습니다."

        # 클래스명 변수에 저장
        class_name = element.get_attribute("class")
        print("✅ 취향설정 템플릿이 노출됩니다.", class_name)

        # 페이지 종료
        page.close()
        

def test_Contents_36_lezhin_Preferences_templete_view_login(page: Page):
        """해당 코드는 로그인상태에서 취향설정 템플릿이 노출되는지 확인합니다"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
        # 이메일 입력
        page.locator("#email").fill("hidelove99@nate.com")
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
        
        # 취향설정 템플릿 선택자 지정
        selector = '.preferenceTemplate__H2I5V'

        # 취향설정 템플릿 탐색 및 존재 확인
        element = page.wait_for_selector(selector, timeout=3000)
        assert element is not None, "❌ preferenceTemplate 요소를 찾을 수 없습니다."

        # 클래스명 변수에 저장
        class_name = element.get_attribute("class")
        print("✅ 취향설정 템플릿이 노출됩니다.", class_name)

        # 페이지 종료
        page.close()
        
def test_Contents_37_lezhin_Preferences_view(page: Page):
        """해당 코드는 서랍메뉴에 적용된 취향설정 내용 UI 노출을 확인합니다"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 요소 정의
        Preferences_section = page.locator("section.logNavGenre___btC_")
        
        # 노출 여부 확인
        assert Preferences_section.is_visible(), "❌ '취향 설정' 섹션이 화면에 노출되지 않았습니다."
        print("✅ '취향 설정' 섹션이 정상적으로 노출되었습니다.")

        # 페이지 종료
        page.close()
        

def test_Contents_38_lezhin_Preferences_templete_view(page: Page):
        """해당 코드는 서랍메뉴에 적용된 취향설정 내용 UI 노출을 확인합니다"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)
        
        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 템플릿 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 템플릿 설정 모달이 정상적으로 노출되었습니다.")

        # 페이지 종료
        page.close()

def test_Contents_39_lezhin_Preferences_genre_view(page: Page):
        """해당 코드는 서랍메뉴에 적용된 취향설정 내용 UI 노출을 확인합니다"""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)
        
        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)

        # 장르 직접 설정 탭 버튼 클릭
        page.click('button.tab__9c31y[role="tab"][data-value="genres"]')
        
        # 대상 요소 선택자
        taste_panel = page.locator("section.tasteSet__tabpanel--genre__tCMY2")

        # 노출 여부 검증
        assert taste_panel.is_visible(), "❌ 취향 설정 장르 선택 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 장르 섹션이 정상적으로 노출되었습니다.")

        # 페이지 종료
        page.close()          
        

def test_Contents_40_lezhin_Preferences_home(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 홈 인벤토리에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/curation_home" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/curation_home' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/curation_home" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close()   
        

def test_Contents_41_lezhin_Preferences_original(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 오리지널페이지에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/weekday" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/scheduled")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/content-list/weekday' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/weekday" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close()
        


def test_Contents_42_lezhin_Preferences_comic(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 만화페이지에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/printed" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/bookshome")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/content-list/printed' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/printed" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close()
        

def test_Contents_43_lezhin_Preferences_comic_ranking_detail(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 만화 랭킹 상세페이지에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/ranking/printed")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close()                        
                         
        
        

def test_Contents_44_lezhin_Preferences_adult19(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 19+ 전시메뉴에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/menu" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/nsfw")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/content-list/menu' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/menu" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close() 
        

def test_Contents_45_lezhin_Preferences_genreplus(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 장르+ 전시메뉴에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/menu" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/genreplus")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/content-list/menu' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/menu" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close() 
        
        
def test_Contents_46_lezhin_Preferences_free(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 무료 전시메뉴에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/free" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/free")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/content-list/free' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/free" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close() 
        

def test_Contents_47_lezhin_Preferences_rangking(page: Page):
        """해당 코드는 KR 로케일에서 서랍메뉴에서 취향설정 템플릿을 선택하고 랭킹 전시메뉴에 적용되었는지 확인합니다."""

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')
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
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/ranking" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/ranking")
        page.wait_for_timeout(3000)
        new_tab_button = page.locator('button.tab__9c31y.tab--line__IF_kS', has_text="신작")
        new_tab_button.click()

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/content-list/ranking' 요청이 감지되지 않았습니다.")
        
        #response에 bl 장르 작품 또는 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/ranking" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if "genres" in group and "bl" in group["genres"]:
                                                raise AssertionError(f"❌ 응답에 bl 장르가 포함되어 있습니다: {group['genres']}")
                                print("✅ 응답에 bl 장르가 포함되지 않았습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)

        # 페이지 종료
        page.close() 

def test_Contents_48_Preferences_event(page: Page):
        """해당 코드는 KR 로케일에서 GNB > Event 페이지의 취향설정 적용을 확인 합니다."""

        # 레진코믹스 KR 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(1000)
        
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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        # 레진코믹스 KR 랭킹 신작 이동
        navigate_to(page, 'https://www.lezhin.com/ko/sale')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/event" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://www.lezhin.com/ko/sale")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/event' 요청이 감지되지 않았습니다.")
        
        # response 중 서브배너에 bl 장르 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/event" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "event_big":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'event_big' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'event_big' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # # 페이지 종료
        page.close()

                
def test_Contents_49_Preferences_new_released_comiclist(page: Page):
        """해당 코드는 KO 로케일에서 레진신작 더보기 작품리스트에 취향설정을 확인합니다."""

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KO 레진신작 더보기 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/scheduled/new-released')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/dynamic" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/scheduled/new-released")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/dynamic' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/dynamic" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()               

def test_Contents_50_Preferences_bookshome_comiclist(page: Page):
        """해당 코드는 KO 로케일에서 신규만화 더보기 작품리스트에 취향설정을 확인합니다."""

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 KO 레진신작 더보기 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/bookshome/new-released')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/content-list/dynamic" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)
        
        # 페이지 이동 및 대기
        page.goto("https://www.lezhin.com/ko/bookshome/new-released")
        page.wait_for_timeout(3000)

        # 마지막 요청 헤더 검사
        if last_request["obj"]:
                genres_header = last_request["obj"].headers.get("x-lz-genres", "")
                print(f"🔍 마지막 요청 URL: {last_request['obj'].url}")
                print(f"🎯 x-lz-genres: {genres_header}")

                expected_genres = "expected_value_here"  # 필요시 설정
                if genres_header == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ x-lz-genres 값이 기대값과 다릅니다.")
        else:
                print("❌ 'lz-api/v2/content-list/dynamic' 요청이 감지되지 않았습니다.")

        # response 중 재이미샵에 bl 장르 작품이 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/content-list/dynamic" in response.url:
                        try:
                                json_data = response.json()
                                bl_found = any("bl" in item.get("genres", []) for item in json_data.get("data", []))

                                if bl_found:
                                        raise AssertionError("❌ BL 장르 작품이 포함되어 있습니다.")
                                else:
                                        print("✅ BL 장르 작품이 포함되어 있지 않습니다.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 핸들러 등록
        page.on("request", handle_request)
        page.on("response", handle_response)
     
        # 페이지 종료
        page.close()
        

def test_Contents_51_Preferences_viewer_bottom_banner(page: Page):
        """해당 코드는 KO 로케일에서 뷰어 하단 배너 취향설정을 확인합니다."""
        """해당 케이스는 리얼의 데이터가 일정치 않아 QA서버로 대체 합니다."""

        # 레진코믹스 KO 홈 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/login')

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
        
        # 1초 대기
        page.wait_for_timeout(3000)
        
        #서랍메뉴 클릭
        click_hamburger_menu(page)
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        # 취향설정 버튼 노출까지 대기
        button_selector = 'button.logNavGenre__btnSet__fze_V'
        page.wait_for_selector(button_selector, timeout=3000)

        # 다시 설정하기 버튼 클릭 수행
        page.click(button_selector)
        
        #취향설정 팝업 노출 확인
        selector = '.modal__n8lvY.modal--isBottomModal__v8e_8.tasteSet__1thMG'
        element = page.wait_for_selector(selector, timeout=5000)
        assert element.is_visible(), "❌ 취향 설정 모달이 화면에 노출되지 않았습니다."
        print("✅ 취향 설정 모달이 정상적으로 노출되었습니다.")
        
        # 취향설정 템플릿 선택
        selector2 = 'span.tasteCheck__title__A3BB8'
        element2 = page.wait_for_selector(selector2, timeout=3000)
        page.click('span.tasteCheck__title__A3BB8:has-text("BL만 빼주세요🥦")')
        
        #선택 완료 버튼 클릭
        button_selector2 = 'button.lzBtn__tyLuS.lzBtn--medium__VwSBj.lzBtn--filled_red__mb2yC.lzBtn--wide__xkRCf'
        page.wait_for_selector(button_selector2, timeout=3000)
        #선택완료 버튼 클릭 수행
        page.click(button_selector2)
        
        
        # 레진코믹스 임의 뷰어로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/comic/cartoon_hero/5')
        
        #적용되어야할 취향장르 선언
        expected_genres = "drama,romance,fantasy,school,gag,gl,day,action,mystery"
        #request header에 실제 적용된 장르값과 적용되어야할 장르값을 비교 
        # 마지막 요청 저장용 변수
        last_request = {"obj": None}

        # 요청 이벤트 핸들러 등록: 가장 마지막 요청만 저장
        def handle_request(request):
                if "lz-api/v2/inventory_groups/comic_viewer" in request.url:
                        last_request["obj"] = request

        page.on("request", handle_request)

        # 페이지 로딩 (API가 호출되는 실제 페이지)
        page.goto("https://q-www.lezhin.com/ko/comic/cartoon_hero/5")
        page.wait_for_timeout(3000)

        # 마지막 요청 검사
        if last_request["obj"]:
                genres = last_request["obj"].headers.get("x-lz-genres")
                print("🔍 마지막 요청 URL: %s", last_request["obj"].url)
                print("🎯 x-lz-genres: %s", genres)
    
                if genres == expected_genres:
                        print("✅ x-lz-genres 값이 기대값과 일치합니다.")
                else:
                        print("❌ 장르 미일치: %s", genres)
        else:
                print("❌ 'lz-api/v2/inventory_groups/comic_viewer' 요청이 감지되지 않았습니다.")
        
        # response 중 배너에 bl 장르 배너가 포함되어있는지 확인
        # 기존 request 핸들러에 response 이벤트 핸들러 추가
        def handle_response(response):
                if "lz-api/v2/inventory_groups/comic_viewer" in response.url:
                        try:
                                json_data = response.json()
                                for group in json_data.get("data", []):
                                        if group.get("id") == "comic_viewer_banner":
                                                items = group.get("items", [])
                                                for item in items:
                                                        genres = item.get("genres", [])
                                                        if "bl" in genres:
                                                                raise AssertionError(f"❌ 'comic_viewer_banner' 항목에 BL 장르가 포함되어 있습니다: {genres}")
                                print("✅ 'comic_viewer_banner' 항목 내에 BL 장르가 없습니다.")
                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패 또는 예외 발생: {e}")

        # 이벤트 등록
        page.on("response", handle_response)
     
        # # 페이지 종료
        page.close()
        

def test_Contents_52_lezhin_search_popular_tag(page: Page):
        """해당 코드는 검색 미리보기 화면에 인기태그 노출을 확인합니다."""
        
        # 레진코믹스 홈 으로 이동
        navigate_to(page, 'https://www.lezhin.com/ko/')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')

        # 2초 대기
        page.wait_for_timeout(2000)

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # 검색 버튼 클릭
        page.click('button[aria-controls="search-container"]')
        
        # 1초 대기
        page.wait_for_timeout(1000)
        
        popular_tags = page.locator(".searchPopularTags__list__At6em")

        # 화면에 노출되는지 검증
        assert popular_tags.is_visible(), "❌ 인기 태그 영역이 화면에 노출되지 않았습니다."
        print("✅ 인기 태그 영역이 정상적으로 노출되었습니다.")
     
        # 페이지 종료
        page.close() 

def test_Contents_53_lezhin_search_preview_tag(page: Page):
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

def test_Contents_54_lezhin_search_preview_comic(page: Page):
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
        



def test_Contents_55_lezhin_search_result_all(page: Page):
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
        


def test_Contents_56_lezhin_search_result_title(page: Page):
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


def test_Contents_57_lezhin_search_result_artist(page: Page):
        """해당 코드는 검색 결과 페이지 이동 직후 "작가" 탭의 작품 리스트 노출을 확인합니다."""

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
                if "lz-api/v2/advanced-search" in response.url and "q=%25EA%25B3%25A0%25ED%2586%25A0%25EA%25B2%258C%2520%25EC%25BD%2594%25EC%259A%2594%25ED%2595%2598%25EB%25A3%25A8" and "t=artist"in response.url:  # "아"의 인코딩
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", []):
                                        # artists 리스트 내 name 필드 포함 여부
                                        if ("고토게 코요하루" in artist.get("name", "") for artist in item.get("artists", [])):
                                                text_found = True
                                                break

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 이벤트 핸들러 등록
        page.on("response", handle_response)
        
        # 검색어 입력 및 결과 트리거
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.fill(search_selector, '고토게 코요하루')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 페이지 접근 (이동 + 자동 요청 발생 유도)
        page.goto("https://www.lezhin.com/ko/search?t=artist&q=%EA%B3%A0%ED%86%A0%EA%B2%8C+%EC%BD%94%EC%9A%94%ED%95%98%EB%A3%A8")
        
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 결과 검증
        if text_found:
                print("✅ '고토게 코요하루' artist 필드에서 노출됩니다.")
        else:
                raise AssertionError("❌ '고토게 코요하루' artist 필드에서 노출되지 않습니다.")

        # 페이지 종료
        page.close()
        

def test_Contents_58_lezhin_search_result_publisher(page: Page):
        """해당 코드는 검색 결과 페이지 이동 직후 "출판사" 탭의 작품 리스트 노출을 확인합니다."""

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
                if "lz-api/v2/advanced-search" in response.url and "q=dcw" and "t=publisher"in response.url:  # "아"의 인코딩
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", []):
                                        # artists 리스트 내 name 필드 포함 여부
                                        if ("dcw" in artist.get("name", "") for artist in item.get("artists", [])):
                                                text_found = True
                                                break

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 이벤트 핸들러 등록
        page.on("response", handle_response)
        
        # 검색어 입력 및 결과 트리거
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.fill(search_selector, 'dcw')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 페이지 접근 (이동 + 자동 요청 발생 유도)
        page.goto("https://www.lezhin.com/ko/search?t=publisher&q=dcw")
        
        page.wait_for_timeout(1000)  # 요청 발생 및 응답 처리 시간 확보

        # 결과 검증
        if text_found:
                print("✅ 'dcw' 가 publisher 필드에서 노출됩니다.")
        else:
                raise AssertionError("❌ 'dcw' 가 publisher 필드에서 노출되지 않습니다.")
        

        # 페이지 종료
        page.close()
        


def test_Contents_59_lezhin_search_result_tag(page: Page):
        """해당 코드는 검색 결과 페이지 이동 직후 "태그" 탭의 작품 리스트 노출을 확인합니다."""

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
                if "lz-api/v2/advanced-search" in response.url and "q=%EB%A1%9C%EB%A7%A8%EC%8A%A4" and "t=tag"in response.url:  # "아"의 인코딩
                        try:
                                json_body = response.json()
                                for item in json_body.get("data", []):
                                        # tags 리스트에 포함 여부
                                        if ("로맨스" in tag for tag in item.get("tags", [])):
                                                text_found = True
                                                break

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 이벤트 핸들러 등록
        page.on("response", handle_response)
        
        # 검색어 입력 및 결과 트리거
        page.click('button[aria-controls="search-container"]')
        search_selector = 'input.searchInput__input__991FM'
        page.fill(search_selector, '로맨스')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보
        # 검색 버튼 클릭
        page.click('button.searchInput__go__yIdqp')
        page.wait_for_timeout(2000)  # 요청 발생 및 응답 처리 시간 확보

        # 페이지 접근 (이동 + 자동 요청 발생 유도)
        page.goto("https://www.lezhin.com/ko/search?t=tag&q=%EB%A1%9C%EB%A7%A8%EC%8A%A4")
        
        page.wait_for_timeout(1000)  # 요청 발생 및 응답 처리 시간 확보

        # 결과 검증
        if text_found:
                print("✅ '로맨스' 가 tags 필드에서 노출됩니다.")
        else:
                raise AssertionError("❌ '로맨스' 가 tags 필드에서 노출되지 않습니다.")

        # 페이지 종료
        page.close()
        

def test_Contents_60_lezhin_tags_exact_match_on(page: Page):
        """해당 코드는 태그 혼합검색 검색결과 완벽적중 결과를 확인합니다."""
        
        tags_found = False

        def handle_response(response):
                nonlocal tags_found

                if "lz-api/v2/advanced-search/multitags" in response.url and "int_id=2153%2C2233" in response.url:
                        try:
                                json_body = response.json()
                                required_tag_ids = {"2153", "2233"}

                                for item in json_body.get("data", []):
                                        tag_ids = {list(tag.keys())[0] for tag in item.get("tags", []) if isinstance(tag, dict)}
                                        if required_tag_ids.issubset(tag_ids):
                                                print(f"✅ '{item.get('title')}' 작품에 고수위와 궁정물 태그 모두 존재함.")
                                                tags_found = True
                                        else:
                                                print(f"⚠️ '{item.get('title')}' 작품에는 두 태그가 모두 존재하지 않음.")

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 응답 핸들러 등록
        page.on("response", handle_response)

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
        
        page.goto("https://www.lezhin.com/ko/tags?filter=exact_match&order=relevant&tab=general&int_id=2153")
        
        
        # 5번째 버튼 클릭
        page.locator('div.panelBody__items__Bzuhu > button').nth(4).click()
        
        page.wait_for_timeout(1000)

        # 페이지 종료
        page.close()
        

def test_Contents_61_lezhin_tags_multiple_match(page: Page):
        """해당 코드는 태그 혼합검색 검색결과 일부적중 결과를 확인합니다."""
        
        tags_found = False

        def handle_response(response):
                nonlocal tags_found

                if "lz-api/v2/advanced-search/multitags" in response.url and "int_id=2153%2C2233" in response.url:
                        try:
                                json_body = response.json()
                                target_tag_ids = {"2153", "2233"}


                                for item in json_body.get("data", []):
                                        tag_ids = {list(tag.keys())[0] for tag in item.get("tags", []) if isinstance(tag, dict)}
                                        
                                        if target_tag_ids.intersection(tag_ids):
                                                print(f"✅ '{item.get('title')}' 작품에 고수위 또는 궁정물 태그가 포함됨.")
                                                tags_found = True

                        except Exception as e:
                                raise AssertionError(f"❌ 응답 파싱 실패: {e}")

        # 응답 핸들러 등록
        page.on("response", handle_response)

        # 레진코믹스 US 홈 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        page.goto("https://www.lezhin.com/ko/tags?filter=multiple_match&order=relevant&tab=general&int_id=2233")
        
        
        # 5번째 버튼 클릭
        page.locator('div.panelBody__items__Bzuhu > button').nth(3).click()
        
        page.wait_for_timeout(3000)


        # 페이지 종료
        page.close()
        
        
def test_Contents_62_lezhin_scrollView(page: Page):
        """해당 코드는 뷰어 진입시 스크롤뷰 이미지 호출 결과를 확인합니다."""

        # 레진코믹스 로그인 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        api_path_substring = "/v2/comics/6210470602932224/episodes/6307634641436672/contents/scrolls"
        api_success = False

        def handle_response(response):
                nonlocal api_success
                if api_path_substring in response.url:
                        print(f"📡 감지된 URL: {response.url}")
                        if response.status == 200:
                                api_success = True

        # 응답 이벤트 핸들러 등록
        page.on("response", handle_response)
        
        page.goto("https://www.lezhin.com/ko/comic/academy_of_card/1", wait_until="networkidle")
        
        assert api_success, f"❌ API 경로 '{api_path_substring}'에 대한 응답이 200이 아님 또는 호출되지 않음"
        print("✅ API 응답이 200 OK 상태로 감지되었습니다.")


        # 페이지 종료
        page.close()
        


def test_Contents_63_lezhin_pageView(page: Page):
        """해당 코드는 뷰어 진입시 페이지뷰 이미지 호출 결과를 확인합니다."""

        # 레진코믹스 로그인 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        api_path_substring = "/v2/comics/5540785488920576/episodes/5794735093972992/contents/pages"
        api_success = False

        def handle_response(response):
                nonlocal api_success
                if api_path_substring in response.url:
                        print(f"📡 감지된 URL: {response.url}")
                        if response.status == 200:
                                api_success = True

        # 응답 이벤트 핸들러 등록
        page.on("response", handle_response)
        
        page.goto("https://www.lezhin.com/ko/comic/dokgo/1", wait_until="networkidle")
        
        
        # 페이지뷰 전환 버튼 클릭
        toggle_button = page.locator('button.vh__btn--crossView__ZvAPc')
        toggle_button.click()
        
        assert api_success, f"❌ API 경로 '{api_path_substring}'에 대한 응답이 200이 아님 또는 호출되지 않음"
        print("✅ API 응답이 200 OK 상태로 감지되었습니다.")


        # 페이지 종료
        page.close()
        

def test_Contents_64_lezhin_notification_click(page: Page):
        """해당 코드는 뷰어 진입시 페이지뷰 이미지 호출 결과를 확인합니다."""

        # 레진코믹스 로그인 페이지 이동
        navigate_to(page, 'https://www.lezhin.com/ko/login')

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

        # 배너 닫기 (공통 함수 사용)
        close_banner_if_exists(page)
        
        page.wait_for_timeout(1000)
        
        page.goto("https://www.lezhin.com/ko/notifications")
        
        # 알림 리스트가 로드될 때까지 대기
        page.wait_for_selector("ul.notiList__JjdLs li")
                               
        # 첫 번째 알림 항목 클릭
        first_noti = page.locator("ul.notiList__JjdLs li").first
        first_noti.click()
        
        page.goto("https://www.lezhin.com/ko/notifications")
        
        # 1초 대기
        page.wait_for_timeout(2000)
        
        # data-read 속성 값 확인
        read_attr = first_noti.get_attribute("data-read")

        # 검증
        if read_attr == "true":
                print("✅ 첫 번째 알림 항목은 읽음 처리됨 (data-read='true')")
        else:
                raise AssertionError(f"❌ 첫 번째 알림 항목은 읽지 않음 (data-read={read_attr})")

        # 페이지 종료
        page.close()