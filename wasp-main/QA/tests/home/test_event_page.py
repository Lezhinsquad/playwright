from playwright.sync_api import sync_playwright, Page, expect
from QA.utils.utils import close_banner_if_exists_US, navigate_to, close_banner_if_exists, click_hamburger_menu, accept_all_cookies
from urllib.parse import urlparse, parse_qs, urlencode, quote,urljoin
import datetime


def test_eventPage_01_prelaunch_all(page: Page):
        """해당 코드는 선공개 이벤트 페이지(전연령) 진입 후 주요 요소 노출을 확인합니다."""
        

        # 레진코믹스 로그인 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/promotions/prelaunch/all')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
            # 요소 선택자
        prelaunch_article = page.locator("article#prelaunch.prelaunch")

        # 검증
        if prelaunch_article.is_visible():
                print("✅ 선 공개 이벤트(전연령) 페이지가 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 선 공개 이벤트(전연령) 페이지가 노출되지 않습니다.")
        

def test_eventPage_02_prelaunch_adult(page: Page):
        """해당 코드는 선공개 이벤트 페이지(성인) 진입 후 주요 요소 노출을 확인합니다."""
                
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
        

        # 성인 선공개 페이지로 이동
        page.goto('https://q-www.lezhin.com/ko/promotions/prelaunch/adult')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
            # 요소 선택자
        prelaunch_article = page.locator("article#prelaunch.prelaunch")

        # 검증
        if prelaunch_article.is_visible():
                print("✅ 선 공개 이벤트(성인) 페이지가 정상적으로 노출됩니다.")
        else:
                raise AssertionError("❌ 선 공개 이벤트(성인) 페이지가 노출되지 않습니다.")
                

        page.close() 
        

def test_eventPage_03_prelaunch_comic_image_click(page: Page):
        """해당 코드는 선공개 이벤트 페이지 진입 후 작품 이미지 클릭시 에피소드 목록 이동을 확인합니다."""
                
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
        

        # 성인 선공개 페이지로 이동
        page.goto('https://q-www.lezhin.com/ko/promotions/prelaunch/adult')

        # 페이지가 로드될 때까지 대기
        page.wait_for_load_state('load')
        # 2초 대기
        page.wait_for_timeout(2000)
        
        # 링크 요소 찾기
        target_link = page.locator('a.prelaunch__thumb[href="/ko/comic/bananatoon"]')
        
        # href 값 추출
        expected_path = target_link.get_attribute("href")

        # 링크 클릭
        target_link.click()
        
        # 페이지 이동 완료 대기
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        # 실제 이동한 URL의 path 부분 추출
        actual_path = page.url.split(".com")[-1]

        # 검증
        if actual_path == expected_path:
                print(f"✅ 링크 클릭 후 URL 경로가 일치합니다: {actual_path}")
        else:
                raise AssertionError(f"❌ URL 경로 불일치! 예상: {expected_path}, 실제: {actual_path}")
                

        page.close() 
        

def test_eventPage_05_templete_eventPage_image_click(page: Page):
        """해당 코드는 템플릿 이벤트 페이지 진입 후 작품이미지 클릭시 에피소드 목록 이동을 확인합니다."""
                
        # 레진코믹스 템플릿 이벤트 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/page/qatest/test112')
          
        # 링크 요소 선택 및 href 추출
        link = page.locator('a.cstmList__link[href="/comic/revatoon"]')
        expected_path = link.get_attribute("href")

        # 링크 클릭
        link.click()
        
        # 페이지 이동 완료 대기
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        # 실제 이동한 URL의 path 부분 추출
        current_path = page.url.replace("https://q-www.lezhin.com", "").split("?")[0]
        
        # '/ko' 언어 prefix 제거
        normalized_expected = expected_path.replace("/ko", "")
        normalized_current = current_path.replace("/ko", "")

        # 검증
        if normalized_current == normalized_expected:
                print("✅ 에피소드 목록으로 정상 이동 되었습니다. (PASS)")
        else:
                raise AssertionError(f"❌ 이동 경로 불일치: expected '{normalized_expected}', got '{normalized_current}'")
                

        page.close() 
        

def test_eventPage_06_templete_eventPage_first_episode_click(page: Page):
        """해당 코드는 템플릿 이벤트 페이지 진입 후 첫화보기 클릭시 첫화 에피소드 뷰어 이동을 확인합니다."""
                
        # 레진코믹스 템플릿 이벤트 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/page/qatest/test112')
          
        # 링크 요소 선택 및 href 추출
        link = page.locator('a.view-episode').first
        expected_path = link.get_attribute("href")

        # 링크 클릭
        link.click()
        
        # 페이지 이동 완료 대기
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        # 실제 이동한 URL의 path 부분 추출
        current_path = page.url.replace("https://q-www.lezhin.com", "").split("?")[0]
        
        # '/ko' 언어 prefix 제거
        normalized_expected = expected_path.replace("/ko", "")
        normalized_current = current_path.replace("/ko", "")
        
        page.wait_for_timeout(1000)

        # 검증
        if normalized_current == normalized_expected:
                print("✅ 첫화 에피소드 뷰어로 정상 이동 되었습니다. (PASS)")
        else:
                raise AssertionError(f"❌ 이동 경로 불일치: expected '{normalized_expected}', got '{normalized_current}'")
                

        page.close() 
        


def test_eventPage_07_image_eventPage_main_image(page: Page):
        """해당 코드는 이미지 이벤트 페이지 진입 후 메인이미지 정상 노출을 확인합니다."""
                
        # 레진코믹스 템플릿 이벤트 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/page/squad_image_event_1')
          
        
        # 페이지 이동 완료 대기
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

        # 이미지 요소 검증
        img = page.locator('img.cut-paper__picture')
        if img.is_visible():
            print("✅ 이미지가 정상적으로 노출되었습니다.")
        else:
            raise AssertionError("❌ 이미지가 노출되지 않았습니다.")
                

        page.close() 
        

def test_eventPage_08_image_eventPage_comic_click(page: Page):
        """해당 코드는 이미지 이벤트 페이지 진입 후 작품 클릭시 대상 링크 이동을 확인합니다."""
                
        # 레진코믹스 템플릿 이벤트 페이지로 이동
        navigate_to(page, 'https://q-www.lezhin.com/ko/page/squad_image_event_1')
          
        
        # 페이지 이동 완료 대기
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)

      # polygon 요소 선택
        polygon = page.locator('polygon[data-url*="cartoon_hero"]').first

        # data-url 속성에서 경로 추출 및 보정
        expected_url = polygon.get_attribute("data-url")
        if expected_url.startswith("//"):
            expected_url = "https:" + expected_url
        expected_path = expected_url.replace("https://q-www.lezhin.com", "").strip()

        # polygon 클릭
        polygon.click()
        page.wait_for_load_state("load")
        page.wait_for_timeout(1000)

        # 현재 경로 확인 및 비교
        current_path = page.url.replace("https://q-www.lezhin.com", "").strip()

        if current_path == expected_path:
            print(f"✅ 설정된 링크로 정상 이동 완료 되었습니다.: {current_path}")
        else:
            raise AssertionError(f"❌ 이동 경로 불일치: expected '{expected_path}', got '{current_path}'")
                

        page.close() 
        
        