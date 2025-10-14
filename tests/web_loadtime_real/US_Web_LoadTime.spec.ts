import { test, expect, Browser, BrowserContext } from '@playwright/test';
import fs from 'fs';
import axios from 'axios';

const urls = [
  //홈
  'https://www.lezhinus.com/en',
  //연재
  'https://www.lezhinus.com/en/daily?day=1',
  //전시메뉴-blgl
  'https://www.lezhinus.com/en/blgl?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴-LezhinR
  'https://www.lezhinus.com/en/mature?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴- general
  'https://www.lezhinus.com/en/general?sub_tags=all&page=0&filter=all&order=popular',
  //무료
  'https://www.lezhinus.com/en/free?genre=_all&page=0&order=popular',
  //Sale
  'https://www.lezhinus.com/en/sale',
  //에피소드목록
  'https://www.lezhinus.com/en/comic/jinx_en',
  //에피소드 뷰어
  'https://www.lezhinus.com/en/comic/jinx_en/1',
  //태그상세 페이지
  'https://www.lezhinus.com/en/tags/GlobalRelease?page=0',
  //알림함
  'https://www.lezhinus.com/en/notifications',
  //선물함
  'https://www.lezhinus.com/en/presents?t=all',
  //내서재
  'https://www.lezhinus.com/en/library',
  //랭킹-전체
  'https://www.lezhinus.com/en/ranking?genre=_all',
  //실시간 랭킹 상세페이지
  'https://www.lezhinus.com/en/ranking/detail?genre=_all&type=realtime',
  //신작 랭킹 상세 페이지
  'https://www.lezhinus.com/en/ranking/detail?genre=_all&type=new',
  //이벤트 랭킹 상세 페이지
  'https://www.lezhinus.com/en/ranking/detail?genre=_all&type=event',
  //2023 연도별 랭킹 상세 페이지
  'https://www.lezhinus.com/en/ranking/detail?genre=_all&type=annual&year=2023',
  //신작연재 더보기 -전체
  'https://www.lezhinus.com/en/daily/new-released?t=all',
  //신작연재 더보기 - 전연령
  'https://www.lezhinus.com/en/daily/new-released?t=kid',
  //신작연재 더보기 - LezhinR(성인)
  'https://www.lezhinus.com/en/daily/new-released?t=adult',
  //신작연재 더보기 - BL
  'https://www.lezhinus.com/en/daily/new-released?t=bl',
  //검색결과 페이지 - 전체 / 키워드 ji
  'https://www.lezhinus.com/en/search?t=all&q=ji',
  //검색결과 페이지 - title / 키워드 ji
  'https://www.lezhinus.com/en/search?t=title&q=ji',
  //검색결과 페이지 - writer / 키워드 ji
  'https://www.lezhinus.com/en/search?t=artist&q=ji',
  //검색결과 페이지 - publisher / 키워드 comic
  'https://www.lezhinus.com/en/search?t=publisher&q=comic',
    //검색결과 페이지 - tag / 키워드 comic
  'https://www.lezhinus.com/en/search?t=tag&q=comic',
   // 작가상세 페이지
  'https://www.lezhinus.com/en/artist/wann?page=0',
  //내정보
  'https://www.lezhinus.com/en/account',
  //코인 충전 페이지
  'https://www.lezhinus.com/en/payment',
  //소장 목록
  'https://www.lezhinus.com/en/library/comic/en-US/something_about_us'
];

const urls2 = [
  //내정보
  'https://www.lezhinus.com/en/account',
  //코인 충전 페이지
  'https://www.lezhinus.com/en/payment',
  //소장 목록
  'https://www.lezhinus.com/en/library/comic/en-US/something_about_us'
];

const SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbx2tIejNtsURfZG5TlJGPdwK8DnlAnm4iU3yhht5Z6s3md3ZQ_SoEDkAAIGfPwQbceDKg/exec'; // Google Apps Script URL
const sheetName = 'US';
const cookieFile = 'cookies_US.json';

const performLogin = async (context: BrowserContext) => {
  const page = await context.newPage();
  await page.goto('https://www.lezhinus.com/en/login');
  await page.waitForLoadState('load');
  await page.fill('input[name="username"]', 'lilyqa01@gmail.com');
  await page.fill('#login-password', 'lezhin123@@');
  await page.click('button[data-ga-event-label="버튼_이메일_로그인"]');
  await page.waitForURL('https://www.lezhinus.com/en');
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


