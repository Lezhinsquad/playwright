import { test, expect } from '@playwright/test';

test('Top 버튼 이동', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko'); //레진 KO 홈 접속
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click(); // 전면배너 오늘 하루 안보기 클릭
  await page.evaluate(() => { // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
      window.scrollBy(0, 1000);
    });
  
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '맨 위로' }).click(); //탑 이동 버튼 클릭*/
  
  const button = await page.getByRole('button', { name: '맨 위로' });
  const isVisible = await button.isVisible(); 
  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }
  
});

test('검색_버튼UI 노출확인', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
 
  //검색창 버튼 노출
  const search_id = await page.waitForSelector('.search__btn');
  const value = await search_id.evaluate((el) => el.id);
  if (value === 'search-btn') {
    console.log('검색 버튼이 노출됩니다. 테스트 종료');
  } else {
    console.log('검색 버튼이 노출되지 않습니다. 재확인 필요!!');
  }
});

test('검색_Placeholder 확인', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
 
  //Placeholder 검증
  const search_id = await page.waitForSelector('.search__input');
  const value = await search_id.evaluate((el) => el.id);
  if (value === 'search-input') {
    console.log('검색_Placeholder가 노출됩니다. 테스트 종료');
  } else {
    console.log('검색_Placeholder가 노출 되지 않습니다. 재확인 필요!!');
  }
});

test('검색_레이어 호출후 닫기', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('button', { name: '닫기' }).click();
 
  //닫기 버튼 비노출 검증
  const search_id = await page.waitForSelector('.search__btn');
  const value = await search_id.evaluate((el) => el.id);
  if (value === 'search-btn') {
    console.log('닫기 버튼이 비노출됩니다. 테스트 종료');
  } else {
    console.log('닫기 버튼이 노출됩니다.. 재확인 필요!!');
  }
});



test('랭킹 영역 노출 확인_KR', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //랭킹 버튼 노출 유무
  const element_1 = await page.waitForSelector('#ranking-section-header'); // 요소 id에서 텍스트 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent);
  
  if (text_1.trim() === '랭킹') {
    console.log('랭킹 영역이 노출됩니다.');
  } else {
    console.log('랭킹 영역이 노출되지 않습니다.');
  }

  //더보기 버튼 노출 유무
  const element_2 = await page.waitForSelector('.lzComic__more'); // 요소 Class에서 텍스트 가져오기
  const text_2 = await element_2.evaluate((el) => el.textContent);
  if (text_2.trim() === '더보기') {
    console.log('더보기 영역이 노출됩니다.');
  } else {
    console.log('더보기 영역이 노출되지 않습니다.');
  }

  //실시간 영역 노출 유무
  const element_3 = await page.waitForSelector('#rank-realtime'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_realtime = await element_3.isVisible();
  const realtime_id = await element_3.evaluate((el) => el.id);
  
  if (isVisible_realtime && realtime_id) {
    console.log('실시간 랭킹 영역이 노출됩니다.');
  } else {
    console.log('실시간 랭킹 영역이 노출되지 않습니다.');
  }

  //신작 영역 노출 유무
  const element_4 = await page.waitForSelector('#rank-new'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_new = await element_4.isVisible();
  const ranking_new_id = await element_4.evaluate((el) => el.id);
  
  if (isVisible_new && ranking_new_id) {
    console.log('신작 랭킹 영역이 노출됩니다.');
  } else {
    console.log('신작 랭킹 영역이 노출되지 않습니다.');
  }

  //이벤트 영역 노출 유무
  const element_5 = await page.waitForSelector('#rank-new'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_event = await element_5.isVisible();
  const ranking_event_id = await element_5.evaluate((el) => el.id);
  
  if (isVisible_event && ranking_event_id) {
    console.log('이벤트 랭킹 영역이 노출됩니다.');
  } else {
    console.log('이벤트 랭킹 영역이 노출되지 않습니다.');
  }
});

test('랭킹 영역 노출 확인_JP', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  //await page.getByRole('button', { name: '今後表示しない' }).click();

  //랭킹 버튼 노출 유무
  const element_1 = await page.waitForSelector('#ranking-section-header'); // 요소 id에서 텍스트 가져오기
  const text_jp_1 = await element_1.evaluate((el) => el.textContent);
  if (text_jp_1.trim() === 'ランキング') {
    console.log('랭킹 영역이 노출됩니다.');
  } else {
    console.log('랭킹 영역이 노출되지 않습니다.');
  }

  //더보기 버튼 노출 유무
  const element_2 = await page.waitForSelector('.lzComic__more'); // 요소 Class에서 텍스트 가져오기
  const text_jp_2 = await element_2.evaluate((el) => el.textContent);
  if (text_jp_2.trim() === 'もっと見る') {
    console.log('더보기 영역이 노출됩니다.');
  } else {
    console.log('더보기 영역이 노출되지 않습니다.');
  }

  //실시간 영역 노출 유무
  const element_3 = await page.waitForSelector('#rank-realtime'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_realtime = await element_3.isVisible();
  const realtime_id = await element_3.evaluate((el) => el.id);
  
  if (isVisible_realtime && realtime_id) {
    console.log('실시간 랭킹 영역이 노출됩니다.');
  } else {
    console.log('실시간 랭킹 영역이 노출되지 않습니다.');
  }

  //신작 영역 노출 유무
  const element_4 = await page.waitForSelector('#rank-new'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_new = await element_4.isVisible();
  const ranking_new_id = await element_4.evaluate((el) => el.id);
  
  if (isVisible_new && ranking_new_id) {
    console.log('신작 랭킹 영역이 노출됩니다.');
  } else {
    console.log('신작 랭킹 영역이 노출되지 않습니다.');
  }

  //이벤트 영역 노출 유무
  const element_5 = await page.waitForSelector('#rank-new'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_event = await element_5.isVisible();
  const ranking_event_id = await element_5.evaluate((el) => el.id);
  
  if (isVisible_event && ranking_event_id) {
    console.log('이벤트 랭킹 영역이 노출됩니다.');
  } else {
    console.log('이벤트 랭킹 영역이 노출되지 않습니다.');
  }
});

test('랭킹 영역 노출 확인_US', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  //await page.getByRole('button', { name: '今後表示しない' }).click();

  //랭킹 버튼 노출 유무
  const element_1 = await page.waitForSelector('#ranking-section-header'); // 요소 id에서 텍스트 가져오기
  const text_jp_1 = await element_1.evaluate((el) => el.textContent);
  if (text_jp_1.trim() === 'Rankings') {
    console.log('랭킹 영역이 노출됩니다.');
  } else {
    console.log('랭킹 영역이 노출되지 않습니다.');
  }

  //더보기 버튼 노출 유무
  const element_2 = await page.waitForSelector('.lzComic__more'); // 요소 Class에서 텍스트 가져오기
  const text_jp_2 = await element_2.evaluate((el) => el.textContent);
  if (text_jp_2.trim() === 'Read more') {
    console.log('더보기 영역이 노출됩니다.');
  } else {
    console.log('더보기 영역이 노출되지 않습니다.');
  }

  //실시간 영역 노출 유무
  const element_3 = await page.waitForSelector('#rank-realtime'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_realtime = await element_3.isVisible();
  const realtime_id = await element_3.evaluate((el) => el.id);
  
  if (isVisible_realtime && realtime_id) {
    console.log('실시간 랭킹 영역이 노출됩니다.');
  } else {
    console.log('실시간 랭킹 영역이 노출되지 않습니다.');
  }

  //신작 영역 노출 유무
  const element_4 = await page.waitForSelector('#rank-new'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_new = await element_4.isVisible();
  const ranking_new_id = await element_4.evaluate((el) => el.id);
  
  if (isVisible_new && ranking_new_id) {
    console.log('신작 랭킹 영역이 노출됩니다.');
  } else {
    console.log('신작 랭킹 영역이 노출되지 않습니다.');
  }

  //이벤트 영역 노출 유무
  const element_5 = await page.waitForSelector('#rank-new'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_event = await element_5.isVisible();
  const ranking_event_id = await element_5.evaluate((el) => el.id);
  
  if (isVisible_event && ranking_event_id) {
    console.log('이벤트 랭킹 영역이 노출됩니다.');
  } else {
    console.log('이벤트 랭킹 영역이 노출되지 않습니다.');
  }
});

test('신작연재 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_scheduled_latest_k'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_scheduled_latest = await element.isVisible();
  const scheduled_latest_id = await element.evaluate((el) => el.id);
  
  if (isVisible_scheduled_latest && scheduled_latest_id) {
    console.log('신작 연재 영역이 노출됩니다.');
  } else {
    console.log('신작 연재 영역이 노출되지 않습니다.');
  }
});

test('신규만화 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_new_k'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_comic_new_k = await element.isVisible();
  const comic_new_k_id = await element.evaluate((el) => el.id);
  
  if (isVisible_comic_new_k && comic_new_k_id) {
    console.log('신규 만화 영역이 노출됩니다.');
  } else {
    console.log('신규 만화 영역이 노출되지 않습니다.');
  }
});

test('업데이트 된 찜한 작품 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad@lezhin.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!@');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  // 업데이트 된 찜한작품 영역 노출 검증
  const element = await page.waitForSelector('#order_up_subscription'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_subscription = await element.isVisible();
  const subscription_id = await element.evaluate((el) => el.id);
  
  if (isVisible_subscription && subscription_id) {
    console.log('업데이트 된 찜한 작품 영역이 노출됩니다.');
  } else {
    console.log('업데이트 된 찜한 작품 영역이 노출되지 않습니다.');
  }
});

test('최근 본 작품', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad@lezhin.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!@');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  // 업데이트 된 찜한작품 영역 노출 검증
  const element = await page.waitForSelector('#order_recent'); // 요소의 id 로 노출 유무 확인하기
  const isVisible_recent = await element.isVisible();
  const recent_id = await element.evaluate((el) => el.id);
  
  if (isVisible_recent && recent_id) {
    console.log('최근 본 작품 영역이 노출됩니다.');
  } else {
    console.log('최근 본 작품 영역이 노출되지 않습니다.');
  }
});


test('홈에서 보고 싶은 장르 취향 설정 하기', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_04@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForTimeout(4000); 

 

//취향설정하기 버튼 노출
const spanText = await page.$eval('span.setMyGenre__txt--sub', (element) => element.textContent); 
//const text = await element.evaluate((el) => el.textContent);

if (spanText.trim() === '홈에서 보고 싶은 장르') {
  console.log('홈에서 보고 싶은 장르가 노출 됩니다.');
} else {
  console.log('홈에서 보고 싶은 장르가 노출 되지 않습니다.');
}
});

test('취향 설정 하기 버튼 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_04@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForTimeout(4000);
  await page.getByRole('button', { name: '홈에서 보고 싶은 장르 취향 설정 하기' }).click();
  await page.getByRole('button', { name: '취소' }).click();


//취향 설정 하기 텍스트 변수 선언
const spanText = await page.$eval('span.setMyGenre__txt--go', (element) => element.textContent); 
//const text = await element.evaluate((el) => el.textContent);

if (spanText.trim() === '취향 설정 하기') {
  console.log('취향 설정 하기가 노출 됩니다.');
} else {
  console.log('취향 설정 하기가 노출 되지 않습니다.');
}
});

test('취향 적용 중', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_03@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForTimeout(4000);
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
 


//취향 적용 중 텍스트 변수 선언
const spanText = await page.$eval('span.setMyGenre__txt--on', (element) => element.textContent); 
//const text = await element.evaluate((el) => el.textContent);

if (spanText.trim() === '취향 적용 중') {
  console.log('취향 적용 중이 노출 됩니다.');
} else {
  console.log('취향 적용 중이 노출 되지 않습니다.');
}
});

