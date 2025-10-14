import { test, expect, Browser, BrowserContext } from '@playwright/test';
import fs from 'fs';
import axios from 'axios';

const urls = [
  //홈
  'https://www.lezhin.jp/ja', 
  //연재
  'https://www.lezhin.jp/ja/original?day=2',
  //만화
  'https://www.lezhin.jp/ja/bookshome?genre=_all&page=0&order=new_episode',
  //전시메뉴 - 男性向け
  'https://www.lezhin.jp/ja/male?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴 - 女性向け
  'https://www.lezhin.jp/ja/female?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴 - BL
  'https://www.lezhin.jp/ja/bl?sub_tags=all&page=0&filter=all&order=popular',
  //전시메뉴 - オトナ
  'https://www.lezhin.jp/ja/otona?sub_tags=all&page=0&filter=all&order=popular',
  //무료
  'https://www.lezhin.jp/ja/free?genre=_all&page=0&order=popular',
  // 이벤트
  'https://www.lezhin.jp/ja/sale',
  //에피소드 목록
  'https://www.lezhin.jp/ja/comic/couponsima',
  //에피소드 뷰어
  'https://www.lezhin.jp/ja/comic/couponsima/3',
  //태그 상세 페이지
  'https://www.lezhin.jp/ja/tags/%E3%83%A1%E3%83%B3%E3%82%BA?page=0',
  //알림함
  'https://www.lezhin.jp/ja/notifications',
  //선물함 - 전체
  'https://www.lezhin.jp/ja/presents?t=all',
  //내서재
  'https://www.lezhin.jp/ja/library',
  //랭킹 - 전체
  'https://www.lezhin.jp/ja/ranking?genre=_all',
  //실시간 랭킹 상세 페이지
  'https://www.lezhin.jp/ja/ranking/detail?genre=_all&type=realtime',
  //신작 랭킹 상세 페이지
  'https://www.lezhin.jp/ja/ranking/detail?genre=_all&type=new',
  //만화 랭킹 상세 페이지
  'https://www.lezhin.jp/ja/ranking/detail?genre=_all&type=printed',
  //이벤트 랭킹 상세 페이지
  'https://www.lezhin.jp/ja/ranking/detail?genre=_all&type=event',
  //2023년 연도별 랭킹 상세 페이지
  'https://www.lezhin.jp/ja/ranking/detail?genre=_all&type=annual&year=2023',
  //신작 연재 더보기 - 전체
  'https://www.lezhin.jp/ja/original/new-released?t=all',
  //신작 연재 더보기 - 전연령
  'https://www.lezhin.jp/ja/original/new-released?t=kid',
  //신작 연재 더보기 - 성인
  'https://www.lezhin.jp/ja/original/new-released?t=adult',
  //신작 연재 더보기 - BL
  'https://www.lezhin.jp/ja/original/new-released?t=bl',
  //신규 만화 더보기 - 전체
  'https://www.lezhin.jp/ja/bookshome/new-released?t=all',
  //신규 만화 더보기 - 전연령
  'https://www.lezhin.jp/ja/bookshome/new-released?t=kid',
  //신규 만화 더보기 - 성인
  'https://www.lezhin.jp/ja/bookshome/new-released?t=adult',
  //신규 만화 더보기 - BL
  'https://www.lezhin.jp/ja/bookshome/new-released?t=bl',
  //검색결과 페이지 - 전체 / 키워드 : せ
  'https://www.lezhin.jp/ja/search?t=all&q=%E3%81%9B',
  //검색결과 페이지 - 태그 / 키워드 : せ
  'https://www.lezhin.jp/ja/search?t=tag&q=%E3%81%9B',
  //검색결과 페이지 - 출판사 / 키워드 : 코믹스
  'https://www.lezhin.jp/ja/search?t=publisher&q=comico',
  //검색결과 페이지 - 작가 / 키워드 : 코믹스
  'https://www.lezhin.jp/ja/search?t=artist&q=comico',
  //검색결과 페이지 - 작품 / 키워드 : せ
  'https://www.lezhin.jp/ja/search?t=title&q=%E3%81%9B',
  //작가페이지
  'https://www.lezhin.jp/ja/artist/chakanidea?page=0',
  //내정보
  'https://www.lezhin.jp/ja/account',
  //코인 충전 페이지
  'https://www.lezhin.jp/ja/payment',
  //소장 목록
  'https://www.lezhin.jp/ja/library/comic/ja-JP/couponsima',
  //JP 출판사 페이지
  'https://www.lezhin.jp/ja/artists?page=0'
];



const SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbx2tIejNtsURfZG5TlJGPdwK8DnlAnm4iU3yhht5Z6s3md3ZQ_SoEDkAAIGfPwQbceDKg/exec'; // Google Apps Script URL
const sheetName = 'JP';
const cookieFile = 'cookies_JP.json';

const performLogin = async (context: BrowserContext) => {
  const page = await context.newPage();
  await page.goto('https://www.lezhin.jp/ja/login');
  await page.waitForLoadState('load');
  await page.fill('input[name="username"]', 'lilyqa01@gmail.com');
  await page.fill('#login-password', 'lezhin123@@');
  await page.click('button[data-ga-event-label="버튼_이메일_로그인"]');
  await page.waitForURL('https://www.lezhin.jp/ja');
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



