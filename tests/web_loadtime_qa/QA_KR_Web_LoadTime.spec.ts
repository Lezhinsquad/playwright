import { test, expect, Browser, BrowserContext } from '@playwright/test';
import fs from 'fs';
import axios from 'axios';

const urls = [
  //홈
  'https://q-www.lezhin.com/ko', 
  //연재
  'https://q-www.lezhin.com/ko/scheduled?day=1',
  //만화
  'https://q-www.lezhin.com/ko/bookshome?genre=_all&page=0&order=new_episode',
  //전시메뉴 - 후방주의
  'https://q-www.lezhin.com/ko/nsfw?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴 - BL
  'https://q-www.lezhin.com/ko/bl?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴 - 로맨스
  'https://q-www.lezhin.com/ko/romance?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴 - 드라마
  'https://q-www.lezhin.com/ko/drama?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴 - 소년
  'https://q-www.lezhin.com/ko/boys?sub_tags=all&page=0&filter=all&order=popular',
  //무료
  'https://q-www.lezhin.com/ko/free?genre=_all&page=0&order=popular',
  // 이벤트
  'https://q-www.lezhin.com/ko/sale',
  //에피소드 목록
  'https://q-www.lezhin.com/ko/comic/smurf_world',
  //에피소드 뷰어
  'https://q-www.lezhin.com/ko/comic/smurf_world/1',
  //태그 상세 페이지
  'https://q-www.lezhin.com/ko/tags/%EC%9E%94%EB%A7%9D%EC%88%98?page=0',
  //알림함
  'https://q-www.lezhin.com/ko/notifications',
  //선물함 - 전체
  'https://q-www.lezhin.com/ko/presents?t=all',
  //내서재
  'https://q-www.lezhin.com/ko/library',
  //랭킹 - 전체
  'https://q-www.lezhin.com/ko/ranking?genre=_all',
  //실시간 랭킹 상세 페이지
  'https://q-www.lezhin.com/ko/ranking/detail?genre=_all&type=realtime',
  //신작 랭킹 상세 페이지
  'https://q-www.lezhin.com/ko/ranking/detail?genre=_all&type=new',
  //이벤트 랭킹 상세 페이지
  'https://q-www.lezhin.com/ko/ranking/detail?genre=_all&type=event',
  //2023년 연도별 랭킹 상세 페이지
  'https://q-www.lezhin.com/ko/ranking/detail?genre=_all&type=annual&year=2023',
  //신작 연재 더보기 - 전체
  'https://q-www.lezhin.com/ko/scheduled/new-released?t=all',
  //신작 연재 더보기 - 전연령
  'https://q-www.lezhin.com/ko/scheduled/new-released?t=kid',
  //신작 연재 더보기 - 성인
  'https://q-www.lezhin.com/ko/scheduled/new-released?t=adult',
  //신작 연재 더보기 - BL
  'https://q-www.lezhin.com/ko/scheduled/new-released?t=bl',
  //신규 만화 더보기 - 전체
  'https://q-www.lezhin.com/ko/bookshome/new-released?t=all',
  //신규 만화 더보기 - 전연령
  'https://q-www.lezhin.com/ko/bookshome/new-released?t=kid',
  //신규 만화 더보기 - 성인
  'https://q-www.lezhin.com/ko/bookshome/new-released?t=adult',
  //신규 만화 더보기 - BL
  'https://q-www.lezhin.com/ko/bookshome/new-released?t=bl',
  //검색결과 페이지 - 전체 / 키워드 : 공
  'https://q-www.lezhin.com/ko/search?t=all&q=%EA%B3%B5',
  //검색결과 페이지 - 태그 / 키워드 : 공
  'https://q-www.lezhin.com/ko/search?t=tag&q=%EA%B3%B5',
  //검색결과 페이지 - 출판사 / 키워드 : 코믹스
  'https://q-www.lezhin.com/ko/search?t=publisher&q=%EC%BD%94%EB%AF%B9%EC%8A%A4',
  //검색결과 페이지 - 작가 / 키워드 : 코믹스
  'https://q-www.lezhin.com/ko/search?t=artist&q=%EC%BD%94%EB%AF%B9%EC%8A%A4',
  //검색결과 페이지 - 작품 / 키워드 : 코믹스
  'https://q-www.lezhin.com/ko/search?t=title&q=%EC%BD%94%EB%AF%B9%EC%8A%A4',
  //작가페이지
  'https://q-www.lezhin.com/ko/artist/anthology?page=0',
  //내정보
  'https://q-www.lezhin.com/ko/account',
  //코인 충전 페이지
  'https://q-www.lezhin.com/ko/payment',
  //소장 목록
  'https://q-www.lezhin.com/ko/library/comic/ko-KR/academy_of_card'
];



const SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbx2tIejNtsURfZG5TlJGPdwK8DnlAnm4iU3yhht5Z6s3md3ZQ_SoEDkAAIGfPwQbceDKg/exec'; // Google Apps Script URL
const sheetName = 'KR_QA';
const cookieFile = 'cookies_QA_KR.json';

const performLogin = async (context: BrowserContext) => {
  const page = await context.newPage();
  await page.goto('https://q-www.lezhin.com/ko/login');
  await page.waitForLoadState('load');
  await page.fill('input[name="username"]', 'squad@lezhin.com');
  await page.fill('#login-password', 'wlscogus7!');
  await page.click('button[data-ga-event-label="버튼_이메일_로그인"]');
  await page.waitForURL('https://q-www.lezhin.com/ko');
  const cookies = await context.cookies();
  fs.writeFileSync(cookieFile, JSON.stringify(cookies, null, 2));
  await page.close();
};

const measureLoadTime = async (browser: Browser, url: string) => {
  const context = await browser.newContext(); // 새 브라우저 컨텍스트 생성

  // 로그인 절차 수행
  if (fs.existsSync(cookieFile)) {
    const cookies = JSON.parse(fs.readFileSync(cookieFile, 'utf-8'));
    await context.addCookies(cookies);
  } else {
    await performLogin(context); // 로그인 후 쿠키 저장
  }

  const page = await context.newPage();
  const startTime = Date.now();

  await page.goto(url);
  await page.waitForLoadState('load'); // 'load' 이벤트까지 대기

  const loadTime = (Date.now() - startTime) / 1000; // 초 단위로 변환
  console.log(`Page load time for ${url}: ${loadTime.toFixed(2)} seconds`);

  try {
    if (loadTime > 4) {
      throw new Error(`Load time exceeded 4 seconds: ${loadTime.toFixed(2)}`);
    }

    // 성공 시 구글 시트로 데이터 전송
    await axios.post(SCRIPT_URL, {
      sheetName: sheetName,
      url: url,
      loadTime: loadTime.toFixed(2),
      status: 'success',
      error: ''
    });
  } catch (error) {
    console.error(`Failed for ${url}: ${error.message}`);
    // 실패 시 구글 시트로 데이터 전송
    await axios.post(SCRIPT_URL, {
      sheetName: sheetName,
      url: url,
      loadTime: loadTime.toFixed(2),
      status: 'failed',
      error: error.message || 'Load time exceeded 4 seconds'
    });
    throw error;
  } finally {
    await context.close(); // 컨텍스트를 닫아 각 테스트가 독립적으로 실행되도록 보장
  }
};

test.describe('Logged-in Page Load Time Tests', () => {
  urls.forEach(url => {
    test(`${url}`, async ({ browser }) => {
      await measureLoadTime(browser, url);
    });
  });
});




