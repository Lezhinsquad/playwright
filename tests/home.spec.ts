import { test, expect } from '@playwright/test';

test('Top 버튼 이동_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko'); //레진 KO 홈 접속
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click(); // 전면배너 오늘 하루 안보기 클릭
  await page.evaluate(() => { // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
      window.scrollBy(0, 1000);
    });
  
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '맨 위로' }).click(); //탑 이동 버튼 클릭
  
  const button = await page.getByRole('button', { name: '맨 위로' }); 
  const isVisible = await button.isVisible(); 
  expect(isVisible).toBe(true);  //top 버튼 노출 유무를 판단

  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
  
});

test('Top 버튼 이동_jp', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja'); //레진 jp 홈 접속
    
  /*try { // 오늘 하루 안보기가 노출되지 않을 경우 다음스텝 진행
    await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  } catch (error) {
    console.log('오늘 하루 안보기 버튼을 찾지 못하여 다음 스크립트를 실행합니다.');
  }*/

  await page.evaluate(() => { // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
      window.scrollBy(0, 1000);
    });
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '先頭へ' }).click(); //탑 이동 버튼 클릭
  const button = await page.getByRole('button', { name: '先頭へ' }); 
  const isVisible = await button.isVisible(); 
  expect(isVisible).toBe(true);  //top 버튼 노출 유무를 판단

  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
  
});

test('Top 버튼 이동_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en'); //레진 us 홈 접속
    
  /*try { // 오늘 하루 안보기가 노출되지 않을 경우 다음스텝 진행
    await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  } catch (error) {
    console.log('오늘 하루 안보기 버튼을 찾지 못하여 다음 스크립트를 실행합니다.');
  }*/

  await page.evaluate(() => { // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
      window.scrollBy(0, 1000);
    });
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: 'Go to top' }).click(); //탑 이동 버튼 클릭 
  const button = await page.getByRole('button', { name: 'Go to top' }); 
  const isVisible = await button.isVisible(); 
  expect(isVisible).toBe(true);  //top 버튼 노출 유무를 판단

  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
  
});


test('검색_버튼UI 노출확인_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
 
  //검색창 버튼 노출
  const search_id = await page.waitForSelector('.search__btn'); // search__btn 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-btn"); //value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-btn') {
    console.log('검색 버튼이 노출됩니다. 테스트 종료');
  } else {
    console.log('검색 버튼이 노출되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});

test('검색_버튼UI 노출확인_jp', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  //await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
 
  //검색창 버튼 노출
  const search_id = await page.waitForSelector('.search__btn'); // search__btn 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-btn"); //value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-btn') {
    console.log('검색 버튼이 노출됩니다. 테스트 종료');
  } else {
    console.log('검색 버튼이 노출되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});

test('검색_버튼UI 노출확인_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  //await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
 
  //검색창 버튼 노출
  const search_id = await page.waitForSelector('.search__btn'); // search__btn 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-btn"); //value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-btn') {
    console.log('검색 버튼이 노출됩니다. 테스트 종료');
  } else {
    console.log('검색 버튼이 노출되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});

test('검색_Placeholder 확인_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
 
  //Placeholder 검증
  const search_id = await page.waitForSelector('.search__input'); // search__input 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-input");//value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-input') {
    console.log('검색_Placeholder가 노출됩니다. 테스트 종료');
  } else {
    console.log('검색_Placeholder가 노출 되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});

test('검색_Placeholder 확인_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  //Placeholder 검증
  const search_id = await page.waitForSelector('.search__input'); // search__input 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-input");//value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-input') {
    console.log('검색_Placeholder가 노출됩니다. 테스트 종료');
  } else {
    console.log('검색_Placeholder가 노출 되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});

test('검색_Placeholder 확인_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  //Placeholder 검증
  const search_id = await page.waitForSelector('.search__input'); // search__input 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-input");//value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-input') {
    console.log('검색_Placeholder가 노출됩니다. 테스트 종료');
  } else {
    console.log('검색_Placeholder가 노출 되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});


test('검색_레이어 호출후 닫기_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('button', { name: '닫기' }).click();
 
  //닫기 버튼 비노출 검증
  const search_id = await page.waitForSelector('.search__btn'); // search__btn 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-btn");//value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-btn') {
    console.log('닫기 버튼이 비노출됩니다. 테스트 종료');
  } else {
    console.log('닫기 버튼이 노출됩니다.. 재확인 필요!!');
  }
  await page.close();
});

test('검색_레이어 호출후 닫기_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  await page.getByRole('button', { name: '閉じる' }).click();
 
  //닫기 버튼 비노출 검증
  const search_id = await page.waitForSelector('.search__btn'); // search__btn 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-btn");//value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-btn') {
    console.log('닫기 버튼이 비노출됩니다. 테스트 종료');
  } else {
    console.log('닫기 버튼이 노출됩니다.. 재확인 필요!!');
  }
  await page.close();
});

test('검색_레이어 호출후 닫기_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  await page.getByRole('button', { name: 'Close', exact: true }).click();
 
  //닫기 버튼 비노출 검증
  const search_id = await page.waitForSelector('.search__btn'); // search__btn 클래스에서 요소 정보를 search_id에 저장
  const value = await search_id.evaluate((el) => el.id); // search_id에 저장된 텍스트를 value에 저장 
  expect(value).toBe("search-btn");//value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (value === 'search-btn') {
    console.log('닫기 버튼이 비노출됩니다. 테스트 종료');
  } else {
    console.log('닫기 버튼이 노출됩니다.. 재확인 필요!!');
  }
  await page.close();
});



test('랭킹 영역 노출 확인_KR', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //랭킹 버튼 노출 유무
  const element_1 = await page.waitForSelector('#ranking-section-header');  //ranking-section-header 에서 요소 정보를 element_1 에 저장
  const text_1 = await element_1.evaluate((el) => el.textContent); // element_1에 저장된 텍스트를 text_1 저장 
  expect(text_1).toBe("랭킹");//text_1 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  
  if (text_1?.trim() === '랭킹') {
    console.log('랭킹 영역이 노출됩니다.');
  } else {
    console.log('랭킹 영역이 노출되지 않습니다.');
  }

  //더보기 버튼 노출 유무
  const element_2 = await page.waitForSelector('.lzComic__more'); //lzComic__more 클래스 에서 요소 정보를 element_1에 저장
  const text_2 = await element_2.evaluate((el) => el.textContent); // element_2에 저장된 텍스트를 text_2 저장
  expect(text_2?.trim()).toBe("더보기");//text_2 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  
  if (text_2?.trim() === '더보기') {
    console.log('더보기 영역이 노출됩니다.');
  } else {
    console.log('더보기 영역이 노출되지 않습니다.');
  }

  //실시간 영역 노출 유무
  const element_3 = await page.waitForSelector('#rank-realtime'); //rank-realtime 에서 요소 정보를 element_3 에 저장
  const isVisible_realtime = await element_3.isVisible(); //isVisible_realtime 변수에 element_3 노출 유무 검증
  expect(isVisible_realtime).toBeTruthy; //실시간 랭킹 요소 노출 검증
  const realtime_id = await element_3.evaluate((el) => el.id); //realtime_id 변수에 element_3 요소 텍스트를 저장
  expect(realtime_id?.trim()).toBe("rank-realtime"); // 실시간 랭킹 노출 확인
  
  if (isVisible_realtime && realtime_id) {
    console.log('실시간 랭킹 영역이 노출됩니다.');
  } else {
    console.log('실시간 랭킹 영역이 노출되지 않습니다.');
  }

  //신작 영역 노출 유무
  const element_4 = await page.waitForSelector('#rank-new'); //rank-new 에서 요소 정보를 element_4 에 저장
  const isVisible_new = await element_4.isVisible(); //isVisible_new 변수에 element_4 노출 유무 검증
  expect(isVisible_new).toBeTruthy; //신작 랭킹 요소 노출 검증
  const ranking_new_id = await element_4.evaluate((el) => el.id); //ranking_new_id 변수에 element_4 요소 텍스트를 저장
  expect(ranking_new_id?.trim()).toBe("rank-new"); // 신작 랭킹 노출 확인
  
  if (isVisible_new && ranking_new_id) {
    console.log('신작 랭킹 영역이 노출됩니다.');
  } else {
    console.log('신작 랭킹 영역이 노출되지 않습니다.');
  }

  //이벤트 영역 노출 유무
  const element_5 = await page.waitForSelector('#rank-event'); //rank-event 에서 요소 정보를 element_5 에 저장
  const isVisible_event = await element_5.isVisible(); //isVisible_event 변수에 element_5 노출 유무 검증
  expect(isVisible_event).toBeTruthy; //이벤트 랭킹 요소 노출 검증
  const ranking_event_id = await element_5.evaluate((el) => el.id); //ranking_event_id 변수에 element_5 요소 텍스트를 저장
  expect(ranking_event_id?.trim()).toBe("rank-event"); // 이벤트  랭킹 노출 확인
  
  if (isVisible_event && ranking_event_id) {
    console.log('이벤트 랭킹 영역이 노출됩니다.');
  } else {
    console.log('이벤트 랭킹 영역이 노출되지 않습니다.');
  }

  await page.close();
});


test('랭킹 영역 노출 확인_JP', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');


  //랭킹 버튼 노출 유무
  const element_1 = await page.waitForSelector('#ranking-section-header'); // ranking-section-header 요소를 element_1 변수에 저장 
  const text_jp_1 = await element_1.evaluate((el) => el.textContent); // element_1 변수에 저장된 요소의 텍스트를 text_jp_1 에 저장
  expect(text_jp_1?.trim()).toBe("ランキング"); //JP 랭킹 텍스트 확인

  if (text_jp_1?.trim() === 'ランキング') {
    console.log('랭킹 영역이 노출됩니다.');
  } else {
    console.log('랭킹 영역이 노출되지 않습니다.');
  }

  //더보기 버튼 노출 유무
  const element_2 = await page.waitForSelector('.lzComic__more');  // lzComic__more 요소를 element_2 변수에 저장 
  const text_jp_2 = await element_2.evaluate((el) => el.textContent); // element_2 변수에 저장된 요소의 텍스트를 text_jp_2 에 저장
  expect(text_jp_2?.trim()).toBe("もっと見る"); //JP 랭킹 텍스트 확인

  if (text_jp_2?.trim() === 'もっと見る') {
    console.log('더보기 영역이 노출됩니다.');
  } else {
    console.log('더보기 영역이 노출되지 않습니다.');
  }

  //실시간 영역 노출 유무
  const element_3 = await page.waitForSelector('#rank-realtime'); //rank-realtime 에서 요소 정보를 element_3 에 저장
  const isVisible_realtime = await element_3.isVisible(); //isVisible_realtime 변수에 element_3 노출 유무 검증
  expect(isVisible_realtime).toBeTruthy; //실시간 랭킹 요소 노출 검증
  const realtime_id = await element_3.evaluate((el) => el.id); //realtime_id 변수에 element_3 요소 텍스트를 저장
  expect(realtime_id?.trim()).toBe("rank-realtime"); // 실시간 랭킹 노출 확인
  
  if (isVisible_realtime && realtime_id) {
    console.log('실시간 랭킹 영역이 노출됩니다.');
  } else {
    console.log('실시간 랭킹 영역이 노출되지 않습니다.');
  }

  //신작 영역 노출 유무
  const element_4 = await page.waitForSelector('#rank-new'); //rank-new 에서 요소 정보를 element_4 에 저장
  const isVisible_new = await element_4.isVisible(); //isVisible_new 변수에 element_4 노출 유무 검증
  expect(isVisible_new).toBeTruthy; //신작 랭킹 요소 노출 검증
  const ranking_new_id = await element_4.evaluate((el) => el.id); //ranking_new_id 변수에 element_4 요소 텍스트를 저장
  expect(ranking_new_id?.trim()).toBe("rank-new"); // 신작 랭킹 노출 확인
  
  if (isVisible_new && ranking_new_id) {
    console.log('신작 랭킹 영역이 노출됩니다.');
  } else {
    console.log('신작 랭킹 영역이 노출되지 않습니다.');
  }

  //이벤트 영역 노출 유무
  const element_5 = await page.waitForSelector('#rank-event'); //rank-event 에서 요소 정보를 element_5 에 저장
  const isVisible_event = await element_5.isVisible(); //isVisible_event 변수에 element_5 노출 유무 검증
  expect(isVisible_event).toBeTruthy; //이벤트 랭킹 요소 노출 검증
  const ranking_event_id = await element_5.evaluate((el) => el.id); //ranking_event_id 변수에 element_5 요소 텍스트를 저장
  expect(ranking_event_id?.trim()).toBe("rank-event"); // 이벤트  랭킹 노출 확인
  
  if (isVisible_event && ranking_event_id) {
    console.log('이벤트 랭킹 영역이 노출됩니다.');
  } else {
    console.log('이벤트 랭킹 영역이 노출되지 않습니다.');
  }

  await page.close();
});

test('랭킹 영역 노출 확인_US', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  //await page.getByRole('button', { name: '今後表示しない' }).click();

  //랭킹 버튼 노출 유무
  const element_1 = await page.waitForSelector('#ranking-section-header');  //ranking-section-header 에서 요소 정보를 element_1 에 저장
  const text_us_1 = await element_1.evaluate((el) => el.textContent); // element_1에 저장된 텍스트를 text_1 저장 
  expect(text_us_1?.trim()).toBe("Rankings");//text_1 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교

  if (text_us_1?.trim() === 'Rankings') {
    console.log('랭킹 영역이 노출됩니다.');
  } else {
    console.log('랭킹 영역이 노출되지 않습니다.');
  }

 //더보기 버튼 노출 유무
  const element_2 = await page.waitForSelector('.lzComic__more'); //lzComic__more 클래스 에서 요소 정보를 element_1에 저장
  const text_us_2 = await element_2.evaluate((el) => el.textContent); // element_2에 저장된 텍스트를 text_2 저장
  expect(text_us_2?.trim()).toBe("More");//text_2 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  if (text_us_2?.trim() === 'More') {
    console.log('더보기 영역이 노출됩니다.');
  } else {
    console.log('더보기 영역이 노출되지 않습니다.');
  }

  //실시간 영역 노출 유무
  const element_3 = await page.waitForSelector('#rank-realtime'); //rank-realtime 에서 요소 정보를 element_3 에 저장
  const isVisible_realtime = await element_3.isVisible(); //isVisible_realtime 변수에 element_3 노출 유무 검증
  expect(isVisible_realtime).toBeTruthy; //실시간 랭킹 요소 노출 검증
  const realtime_id = await element_3.evaluate((el) => el.id); //realtime_id 변수에 element_3 요소 텍스트를 저장
  expect(realtime_id?.trim()).toBe("rank-realtime"); // 실시간 랭킹 노출 확인
  
  if (isVisible_realtime && realtime_id) {
    console.log('실시간 랭킹 영역이 노출됩니다.');
  } else {
    console.log('실시간 랭킹 영역이 노출되지 않습니다.');
  }

  //신작 영역 노출 유무
  const element_4 = await page.waitForSelector('#rank-new'); //rank-new 에서 요소 정보를 element_4 에 저장
  const isVisible_new = await element_4.isVisible(); //isVisible_new 변수에 element_4 노출 유무 검증
  expect(isVisible_new).toBeTruthy; //신작 랭킹 요소 노출 검증
  const ranking_new_id = await element_4.evaluate((el) => el.id); //ranking_new_id 변수에 element_4 요소 텍스트를 저장
  expect(ranking_new_id?.trim()).toBe("rank-new"); // 신작 랭킹 노출 확인
  
  if (isVisible_new && ranking_new_id) {
    console.log('신작 랭킹 영역이 노출됩니다.');
  } else {
    console.log('신작 랭킹 영역이 노출되지 않습니다.');
  }

  //이벤트 영역 노출 유무
  const element_5 = await page.waitForSelector('#rank-event'); //rank-event 에서 요소 정보를 element_5 에 저장
  const isVisible_event = await element_5.isVisible(); //isVisible_event 변수에 element_5 노출 유무 검증
  expect(isVisible_event).toBeTruthy; //이벤트 랭킹 요소 노출 검증
  const ranking_event_id = await element_5.evaluate((el) => el.id); //ranking_event_id 변수에 element_5 요소 텍스트를 저장
  expect(ranking_event_id?.trim()).toBe("rank-event"); // 이벤트  랭킹 노출 확인
  
  if (isVisible_event && ranking_event_id) {
    console.log('이벤트 랭킹 영역이 노출됩니다.');
  } else {
    console.log('이벤트 랭킹 영역이 노출되지 않습니다.');
  }

  await page.close();
});

test('신작연재 노출_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_scheduled_latest_k'); //comic_scheduled_latest_k 에서 요소 정보를 element 에 저장
  const isVisible_scheduled_latest = await element.isVisible(); //isVisible_event 변수에 element_5 노출 여부 저장 
  expect(isVisible_scheduled_latest).toBeTruthy; //신작 연재 요소 영역 노출여부 확인
  const scheduled_latest_id = await element.evaluate((el) => el.id); //comic_scheduled_latest_k의 텍스트를 scheduled_latest_id에 저장
  expect(scheduled_latest_id?.trim()).toBe("comic_scheduled_latest_k"); //신작연재 노출 확인 
  
  if (isVisible_scheduled_latest && scheduled_latest_id) {
    console.log('신작 연재 영역이 노출됩니다.');
  } else {
    console.log('신작 연재 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('신작연재 노출_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_scheduled_latest_k'); //comic_scheduled_latest_k 에서 요소 정보를 element 에 저장
  const isVisible_scheduled_latest = await element.isVisible(); //isVisible_event 변수에 element_5 노출 여부 저장 
  expect(isVisible_scheduled_latest).toBeTruthy; //신작 연재 요소 영역 노출여부 확인
  const scheduled_latest_id = await element.evaluate((el) => el.id); //comic_scheduled_latest_k의 텍스트를 scheduled_latest_id에 저장
  expect(scheduled_latest_id?.trim()).toBe("comic_scheduled_latest_k"); //신작연재 노출 확인 
  
  if (isVisible_scheduled_latest && scheduled_latest_id) {
    console.log('신작 연재 영역이 노출됩니다.');
  } else {
    console.log('신작 연재 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('신작연재 노출_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_scheduled_latest_k'); //comic_scheduled_latest_k 에서 요소 정보를 element 에 저장
  const isVisible_scheduled_latest = await element.isVisible(); //isVisible_event 변수에 element_5 노출 여부 저장 
  expect(isVisible_scheduled_latest).toBeTruthy; //신작 연재 요소 영역 노출여부 확인
  const scheduled_latest_id = await element.evaluate((el) => el.id); //comic_scheduled_latest_k의 텍스트를 scheduled_latest_id에 저장
  expect(scheduled_latest_id?.trim()).toBe("comic_scheduled_latest_k"); //신작연재 노출 확인 
  
  if (isVisible_scheduled_latest && scheduled_latest_id) {
    console.log('신작 연재 영역이 노출됩니다.');
  } else {
    console.log('신작 연재 영역이 노출되지 않습니다.');
  }
  await page.close();
});


test('신규만화 노출_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_new_k'); //comic_new_k 에서 요소 정보를 element 에 저장
  const isVisible_comic_new_k = await element.isVisible(); //isVisible_comic_new_k 변수에 element 노출 여부 저장 
  expect(isVisible_comic_new_k).toBeTruthy; //신규 만화 요소 영역 노출여부 확인
  const comic_new_k_id = await element.evaluate((el) => el.id);//comic_new_k의 텍스트를 comic_new_k_id에 저장
  expect(comic_new_k_id?.trim()).toBe("comic_new_k"); // 신규 만화 노출 확인
  
  if (isVisible_comic_new_k && comic_new_k_id) {
    console.log('신규 만화 영역이 노출됩니다.');
  } else {
    console.log('신규 만화 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('신규만화 노출_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_new_k'); //comic_new_k 에서 요소 정보를 element 에 저장
  const isVisible_comic_new_k = await element.isVisible(); //isVisible_comic_new_k 변수에 element 노출 여부 저장 
  expect(isVisible_comic_new_k).toBeTruthy; //신규 만화 요소 영역 노출여부 확인
  const comic_new_k_id = await element.evaluate((el) => el.id);//comic_new_k의 텍스트를 comic_new_k_id에 저장
  expect(comic_new_k_id?.trim()).toBe("comic_new_k"); // 신규 만화 노출 확인
  
  if (isVisible_comic_new_k && comic_new_k_id) {
    console.log('신규 만화 영역이 노출됩니다.');
  } else {
    console.log('신규 만화 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('신규만화 노출_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');

  //신작연재 영역 비노출 검증
  const element = await page.waitForSelector('#comic_new_k'); //comic_new_k 에서 요소 정보를 element 에 저장
  const isVisible_comic_new_k = await element.isVisible(); //isVisible_comic_new_k 변수에 element 노출 여부 저장 
  expect(isVisible_comic_new_k).toBeTruthy; //신규 만화 요소 영역 노출여부 확인
  const comic_new_k_id = await element.evaluate((el) => el.id);//comic_new_k의 텍스트를 comic_new_k_id에 저장
  expect(comic_new_k_id?.trim()).toBe("comic_new_k"); // 신규 만화 노출 확인
  
  if (isVisible_comic_new_k && comic_new_k_id) {
    console.log('신규 만화 영역이 노출됩니다.');
  } else {
    console.log('신규 만화 영역이 노출되지 않습니다.');
  }
  await page.close();
});


test('업데이트 된 찜한 작품 노출_kr', async ({ page }) => {
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
  const element = await page.waitForSelector('#order_up_subscription'); //order_up_subscription 에서 요소 정보를 element 에 저장
  const isVisible_subscription = await element.isVisible();//isVisible_subscription 변수에 element 노출 여부 저장 
  expect(isVisible_subscription).toBeTruthy; //업데이트된 찜한 작품 영역 노출여부 확인
  const subscription_id = await element.evaluate((el) => el.id); //order_up_subscription의 텍스트를 subscription_id에 저장
  expect(subscription_id?.trim()).toBe("order_up_subscription"); // 신규 만화 노출 확인

  if (isVisible_subscription && subscription_id) {
    console.log('업데이트 된 찜한 작품 영역이 노출됩니다.');
  } else {
    console.log('업데이트 된 찜한 작품 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('업데이트 된 찜한 작품 노출_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();


  // 업데이트 된 찜한작품 영역 노출 검증
  const element = await page.waitForSelector('#order_up_subscription'); //order_up_subscription 에서 요소 정보를 element 에 저장
  const isVisible_subscription = await element.isVisible();//isVisible_subscription 변수에 element 노출 여부 저장 
  expect(isVisible_subscription).toBeTruthy; //업데이트된 찜한 작품 영역 노출여부 확인
  const subscription_id = await element.evaluate((el) => el.id); //order_up_subscription의 텍스트를 subscription_id에 저장
  expect(subscription_id?.trim()).toBe("order_up_subscription"); // 업데이트된 찜한 작품 텍스트 검증

  if (isVisible_subscription && subscription_id) {
    console.log('업데이트 된 찜한 작품 영역이 노출됩니다.');
  } else {
    console.log('업데이트 된 찜한 작품 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('업데이트 된 찜한 작품 노출_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'Login with email' }).click();



  // 업데이트 된 찜한작품 영역 노출 검증
  const element = await page.waitForSelector('#order_up_subscription'); //order_up_subscription 에서 요소 정보를 element 에 저장
  const isVisible_subscription = await element.isVisible();//isVisible_subscription 변수에 element 노출 여부 저장 
  expect(isVisible_subscription).toBeTruthy; //업데이트된 찜한 작품 영역 노출여부 확인
  const subscription_id = await element.evaluate((el) => el.id); //order_up_subscription의 텍스트를 subscription_id에 저장
  expect(subscription_id?.trim()).toBe("order_up_subscription"); // 업데이트된 찜한 작품 텍스트 검증

  if (isVisible_subscription && subscription_id) {
    console.log('업데이트 된 찜한 작품 영역이 노출됩니다.');
  } else {
    console.log('업데이트 된 찜한 작품 영역이 노출되지 않습니다.');
  }
  await page.close();
});




test('최근 본 작품_kr', async ({ page }) => {
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
  const element = await page.waitForSelector('#order_recent'); //order_recent 에서 요소 정보를 element 에 저장
  const isVisible_recent = await element.isVisible(); //isVisible_recent 변수에 element 노출 여부 저장 
  expect(isVisible_recent).toBeTruthy; //최근 본 작품 영역 노출여부 확인
  const recent_id = await element.evaluate((el) => el.id);
  expect(recent_id?.trim()).toBe("order_recent"); // 신규 만화 노출 확인
  
  if (isVisible_recent && recent_id) {
    console.log('최근 본 작품 영역이 노출됩니다.');
  } else {
    console.log('최근 본 작품 영역이 노출되지 않습니다.');
  }

  await page.close();
});

test('최근 본 작품_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();

  // 업데이트 된 찜한작품 영역 노출 검증
  const element = await page.waitForSelector('#order_recent'); //order_recent 에서 요소 정보를 element 에 저장
  const isVisible_recent = await element.isVisible(); //isVisible_recent 변수에 element 노출 여부 저장 
  expect(isVisible_recent).toBeTruthy; //최근 본 작품 영역 노출여부 확인
  const recent_id = await element.evaluate((el) => el.id);
  expect(recent_id?.trim()).toBe("order_recent"); // 신규 만화 노출 확인
  
  if (isVisible_recent && recent_id) {
    console.log('최근 본 작품 영역이 노출됩니다.');
  } else {
    console.log('최근 본 작품 영역이 노출되지 않습니다.');
  }

  await page.close();
});

test('최근 본 작품_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'Login with email' }).click();

  // 업데이트 된 찜한작품 영역 노출 검증
  const element = await page.waitForSelector('#order_recent'); //order_recent 에서 요소 정보를 element 에 저장
  const isVisible_recent = await element.isVisible(); //isVisible_recent 변수에 element 노출 여부 저장 
  expect(isVisible_recent).toBeTruthy; //최근 본 작품 영역 노출여부 확인
  const recent_id = await element.evaluate((el) => el.id);
  expect(recent_id?.trim()).toBe("order_recent"); // 신규 만화 노출 확인
  
  if (isVisible_recent && recent_id) {
    console.log('최근 본 작품 영역이 노출됩니다.');
  } else {
    console.log('최근 본 작품 영역이 노출되지 않습니다.');
  }

  await page.close();
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
  const spanText = await page.$eval('span.setMyGenre__txt--sub', (element) => element.textContent); //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  expect(spanText?.trim()).toBe("홈에서 보고 싶은 장르"); // 홈에서 보고 싶은 장르 취향 설정 노출 확인

  if (spanText?.trim() === '홈에서 보고 싶은 장르') {
    console.log('홈에서 보고 싶은 장르가 노출 됩니다.');
  } else {
    console.log('홈에서 보고 싶은 장르가 노출 되지 않습니다.');
  }

  await page.close();
});



test('취향 설정 하기 버튼 노출_kr', async ({ page }) => {
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
  const spanText = await page.$eval('span.setMyGenre__txt--go', (element) => element.textContent); //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  expect(spanText?.trim()).toBe("취향 설정 하기"); // 취향 설정 하기 노출 확인

  if (spanText?.trim() === '취향 설정 하기') {
    console.log('취향 설정 하기가 노출 됩니다.');
  } else {
    console.log('취향 설정 하기가 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 설정 하기 버튼 노출_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForTimeout(4000);


//취향 설정 하기 텍스트 변수 선언
  const spanText = await page.$eval('span.setMyGenre__txt--go', (element) => element.textContent); //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  expect(spanText?.trim()).toBe("好みのジャンルを設定する"); // 취향 설정 하기 노출 확인

  if (spanText?.trim() === '好みのジャンルを設定する') {
    console.log('취향 설정 하기가 노출 됩니다.');
  } else {
    console.log('취향 설정 하기가 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 설정 하기 버튼 노출_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.waitForTimeout(4000);


//취향 설정 하기 텍스트 변수 선언
  const spanText = await page.$eval('span.setMyGenre__txt--go', (element) => element.textContent); //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  expect(spanText?.trim()).toBe("My Recommendations Settings"); // 취향 설정 하기 노출 확인

  if (spanText?.trim() === 'My Recommendations Settings') {
    console.log('취향 설정 하기가 노출 됩니다.');
  } else {
    console.log('취향 설정 하기가 노출 되지 않습니다.');
  }
  await page.close();
});


test('취향 적용 중_kr', async ({ page }) => {
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
  const spanText = await page.$eval('span.setMyGenre__txt--on', (element) => element.textContent); //취향 적용 중 버튼의 텍스트 요소 를 spanText에 저장
  expect(spanText?.trim()).toBe("취향 적용 중"); // 취향적용 중 노출 확인

  if (spanText?.trim() === '취향 적용 중') {
    console.log('취향 적용 중이 노출 됩니다.');
  } else {
    console.log('취향 적용 중이 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 적용 중_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad_01@yopmail.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForTimeout(4000);
 


  //취향 적용 중 텍스트 변수 선언
  const spanText = await page.$eval('span.setMyGenre__txt--on', (element) => element.textContent); //취향 적용 중 버튼의 텍스트 요소 를 spanText에 저장
  expect(spanText?.trim()).toBe("好みのジャンル設定適用中"); // 취향적용 중 노출 확인

  if (spanText?.trim() === '好みのジャンル設定適用中') {
    console.log('취향 적용 중이 노출 됩니다.');
  } else {
    console.log('취향 적용 중이 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 적용 중_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad_01@yopmail.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.waitForTimeout(4000);
 


//취향 적용 중 텍스트 변수 선언
  const spanText = await page.$eval('span.setMyGenre__txt--on', (element) => element.textContent); //취향 적용 중 버튼의 텍스트 요소 를 spanText에 저장
  expect(spanText?.trim()).toBe("My Recommendations On"); // 취향적용 중 노출 확인

  if (spanText?.trim() === 'My Recommendations On') {
    console.log('취향 적용 중이 노출 됩니다.');
  } else {
    console.log('취향 적용 중이 노출 되지 않습니다.');
  }
  await page.close();
});

