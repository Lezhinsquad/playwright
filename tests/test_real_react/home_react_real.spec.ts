import { test, expect } from '@playwright/test';

test('Top 버튼 이동_kr', async ({ page }) => {
  //레진 KO 홈 접속
  await page.goto('https://www.lezhin.com/ko'); 
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
  await page.evaluate(() => { 
      window.scrollBy(0, 1000);
    });
  
  await page.waitForTimeout(2000);
  //탑 이동 버튼 클릭
  await page.getByRole('button', { name: '맨 위로' }).click(); 
  
  const button = await page.getByRole('button', { name: '맨 위로' }); 
   //top 버튼 요소를 isVisible 변수에 저장
  const isVisible = await button.isVisible(); 
   //top 버튼 노출 유무를 판단
  expect(isVisible).toBe(true); 

  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
  
});

test('Top 버튼 이동_jp', async ({ page }) => {
  //레진 jp 홈 접속
  await page.goto('https://www.lezhin.jp/ja'); 
    
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  
  // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
  await page.evaluate(() => { 
      window.scrollBy(0, 1000);
    });
  await page.waitForTimeout(2000);
  //탑 이동 버튼 클릭
  await page.getByRole('button', { name: '先頭へ' }).click(); 
  const button = await page.getByRole('button', { name: '先頭へ' }); 
  //top 버튼 요소를 isVisible 변수에 저장
  const isVisible = await button.isVisible(); 
   //top 버튼 노출 유무를 판단
  expect(isVisible).toBe(true); 

  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
  
});

test('Top 버튼 이동_us', async ({ page }) => {
  //레진 us 홈 접속
  await page.goto('https://www.lezhinus.com/en'); 
    
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
  await page.evaluate(() => { 
      window.scrollBy(0, 1000);
    });
  await page.waitForTimeout(2000);
  //탑 이동 버튼 클릭 
  await page.getByRole('button', { name: 'Go to top' }).click(); 
  const button = await page.getByRole('button', { name: 'Go to top' }); 
  //top 버튼 요소를 isVisible 변수에 저장
  const isVisible = await button.isVisible(); 
  //top 버튼 노출 유무를 판단
  expect(isVisible).toBe(true);  

  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
  
});


test('검색_버튼UI 노출확인_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
 
  //검색창 노출 버튼 요소 저장
  const button = await page.$('.style_supportsItem__OIhu2.style_supportsItem__search__ZPNGK'); 
  // search_id에 저장된 텍스트를 value에 저장 
  const buttonText = await button?.textContent(); 
  //value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  expect(buttonText).toBe("검색창 열기"); 

  if (buttonText === '검색창 열기') {
    console.log('검색 버튼이 노출됩니다. 테스트 종료');
  } else {
    console.log('검색 버튼이 노출되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});


test('검색_버튼UI 노출확인_jp', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
 
  //검색창 노출 버튼 요소
  const button = await page.$('.style_supportsItem__OIhu2.style_supportsItem__search__ZPNGK'); 
  // search_id에 저장된 텍스트를 value에 저장 
  const buttonText = await button?.textContent(); 
  //value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  expect(buttonText).toBe("検索窓を開く"); 

  if (buttonText === '検索窓を開く') {
    console.log('검색 버튼이 노출됩니다. 테스트 종료');
  } else {
    console.log('검색 버튼이 노출되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});



test('검색_버튼UI 노출확인_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
 

  //검색창 노출 버튼 요소 저장
  const button = await page.$('.style_supportsItem__OIhu2.style_supportsItem__search__ZPNGK');
  // search_id에 저장된 텍스트를 value에 저장 
  const buttonText = await button?.textContent(); 
  //value 에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  expect(buttonText).toBe("Open Search Window"); 

  if (buttonText === '検索窓を開く') {
    console.log('검색 버튼이 노출됩니다. 테스트 종료');
  } else {
    console.log('검색 버튼이 노출되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});

test('검색_Placeholder 확인_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  await page.getByRole('button', { name: '검색창 열기' }).click();
 
  // 검색창 활성화 상태에서 placeholder 값 얻기
  const placeholderText = await page.getAttribute('.style_gnbSearch__input__KGtkv', 'placeholder'); 
  // placeholder 값 비교
  expect(placeholderText).toBe("작품, 작가, 출판사, 태그 검색"); 
  if (placeholderText === '작품, 작가, 출판사, 태그 검색') {
    console.log('검색_Placeholder가 노출됩니다. 테스트 종료');
  } else {
    console.log('검색_Placeholder가 노출 되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});


test('검색_Placeholder 확인_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
    try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  await page.getByRole('button', { name: '検索窓を開く' }).click();
  
  // 검색창 활성화 상태에서 placeholder 값 얻기
  const placeholderText = await page.getAttribute('.style_gnbSearch__input__KGtkv', 'placeholder'); 
  // placeholder 값 비교
  expect(placeholderText).toBe("作品, 作家, 出版社, タグ"); 



  if (placeholderText === '作品, 作家, 出版社, タグ') {
    console.log('검색_Placeholder가 노출됩니다. 테스트 종료');
  } else {
    console.log('검색_Placeholder가 노출 되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});


test('검색_Placeholder 확인_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'Open Search Window' }).click();
 
  // 검색창 활성화 상태에서 placeholder 값 얻기
  const placeholderText = await page.getAttribute('.style_gnbSearch__input__KGtkv', 'placeholder'); 
  // placeholder 값 비교
  expect(placeholderText).toBe("Type to begin searching"); 



  if (placeholderText === 'Type to begin searching') {
    console.log('검색_Placeholder가 노출됩니다. 테스트 종료');
  } else {
    console.log('검색_Placeholder가 노출 되지 않습니다. 재확인 필요!!');
  }
  await page.close();
});


test('검색_레이어 호출후 닫기_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('button', { name: '닫기', exact: true }).click();
 
  //검색창 노출 버튼 요소
  const button = await page.$('.style_supportsItem__OIhu2.style_supportsItem__search__ZPNGK'); 
  // search_id에 저장된 텍스트를 value에 저장 
  const buttonText = await button?.textContent(); 
  //buttonText 에 저장된 텍스트를 확인하여 닫기 버튼 텍스트가 미노출되는것으로 비교
  expect(buttonText).toBe("검색창 열기"); 

  if (buttonText === '검색창 열기') {
    console.log('닫기 버튼이 비노출됩니다. 테스트 종료');
  } else {
    console.log('닫기 버튼이 노출됩니다.. 재확인 필요!!');
  }
  await page.close();
});

test('검색_레이어 호출후 닫기_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  await page.getByRole('button', { name: '閉じる', exact: true }).click();
 
  //검색창 노출 버튼 요소
  const button = await page.$('.style_supportsItem__OIhu2.style_supportsItem__search__ZPNGK'); 
  // search_id에 저장된 텍스트를 value에 저장 
  const buttonText = await button?.textContent(); 
  //buttonText 에 저장된 텍스트를 확인하여 닫기 버튼 텍스트가 미노출되는것으로 비교
  expect(buttonText).toBe("検索窓を開く"); 

  if (buttonText === '検索窓を開く') {
    console.log('닫기 버튼이 비노출됩니다. 테스트 종료');
  } else {
    console.log('닫기 버튼이 노출됩니다.. 재확인 필요!!');
  }
  await page.close();
});

test('검색_레이어 호출후 닫기_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  await page.getByRole('button', { name: 'Close', exact: true }).click();
 
 //검색창 노출 버튼 요소
 const button = await page.$('.style_supportsItem__OIhu2.style_supportsItem__search__ZPNGK'); 
 // search_id에 저장된 텍스트를 value에 저장 
 const buttonText = await button?.textContent(); 
 //buttonText 에 저장된 텍스트를 확인하여 닫기 버튼 텍스트가 미노출되는것으로 비교
 expect(buttonText).toBe("Open Search Window"); 

  if (buttonText === 'Open Search Window') {
    console.log('닫기 버튼이 비노출됩니다. 테스트 종료');
  } else {
    console.log('닫기 버튼이 노출됩니다.. 재확인 필요!!');
  }
  await page.close();
});



test('랭킹 영역 노출 확인_KR', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  //랭킹 전체 영역 요소 저장
  const elementHandle = await page.$('.comicCol3_lzComicCol3__356hN.style_homeRootRanking__qhx1C');
  //elementHandle 실제 노출되는 페이지 노출되는지 비교 체크
  expect(elementHandle).toBeTruthy; 
  

  await page.close();
});


test('랭킹 영역 노출 확인_JP', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  //랭킹 전체 영역 요소 저장
  const elementHandle = await page.$('.comicCol3_lzComicCol3__356hN.style_homeRootRanking__qhx1C');
  //elementHandle 실제 노출되는 페이지 노출되는지 비교 체크
  expect(elementHandle).toBeTruthy; 
  
  await page.close();
});


test('랭킹 영역 노출 확인_US', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

   //랭킹 전체 영역 요소 저장
   const elementHandle = await page.$('.comicCol3_lzComicCol3__356hN.style_homeRootRanking__qhx1C');
   //elementHandle 실제 노출되는 페이지 노출되는지 비교 체크
   expect(elementHandle).toBeTruthy; 

  await page.close();
});

test('신작연재 노출_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  //comic_scheduled_latest_k 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#comic_scheduled_latest_k'); 
  //isVisible_event 변수에 element_5 노출 여부 저장 
  const isVisible_scheduled_latest = await element.isVisible(); 
  //신작 연재 요소 영역 노출여부 확인
  expect(isVisible_scheduled_latest).toBeTruthy; 
  //comic_scheduled_latest_k의 텍스트를 scheduled_latest_id에 저장
  const scheduled_latest_id = await element.evaluate((el) => el.id); 
  //신작연재 노출 확인 
  expect(scheduled_latest_id?.trim()).toBe("comic_scheduled_latest_k"); 
  
  if (isVisible_scheduled_latest && scheduled_latest_id) {
    console.log('신작 연재 영역이 노출됩니다.');
  } else {
    console.log('신작 연재 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('신작연재 노출_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  

  //comic_scheduled_latest_k 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#comic_scheduled_latest_k'); 
  //isVisible_event 변수에 element_5 노출 여부 저장 
  const isVisible_scheduled_latest = await element.isVisible(); 
  //신작 연재 요소 영역 노출여부 확인
  expect(isVisible_scheduled_latest).toBeTruthy; 
  //comic_scheduled_latest_k의 텍스트를 scheduled_latest_id에 저장
  const scheduled_latest_id = await element.evaluate((el) => el.id);
   //신작연재 노출 확인  
  expect(scheduled_latest_id?.trim()).toBe("comic_scheduled_latest_k");

  if (isVisible_scheduled_latest && scheduled_latest_id) {
    console.log('신작 연재 영역이 노출됩니다.');
  } else {
    console.log('신작 연재 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('신작연재 노출_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  //comic_scheduled_latest_k 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#comic_scheduled_latest'); 
  //isVisible_event 변수에 element_5 노출 여부 저장 
  const isVisible_scheduled_latest = await element.isVisible(); 
  //신작 연재 요소 영역 노출여부 확인
  expect(isVisible_scheduled_latest).toBeTruthy; 
  //comic_scheduled_latest_k의 텍스트를 scheduled_latest_id에 저장
  const scheduled_latest_id = await element.evaluate((el) => el.id); 
  //신작연재 노출 확인 
  expect(scheduled_latest_id?.trim()).toBe("comic_scheduled_latest"); 
  
  if (isVisible_scheduled_latest && scheduled_latest_id) {
    console.log('신작 연재 영역이 노출됩니다.');
  } else {
    console.log('신작 연재 영역이 노출되지 않습니다.');
  }
  await page.close();
});


test('신규만화 노출_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  //comic_new_k 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#comic_new_k'); 
  //isVisible_comic_new_k 변수에 element 노출 여부 저장 
  const isVisible_comic_new_k = await element.isVisible(); 
  //신규 만화 요소 영역 노출여부 확인
  expect(isVisible_comic_new_k).toBeTruthy; 
  //comic_new_k의 텍스트를 comic_new_k_id에 저장
  const comic_new_k_id = await element.evaluate((el) => el.id);
  // 신규 만화 노출 확인
  expect(comic_new_k_id?.trim()).toBe("comic_new_k"); 

  if (isVisible_comic_new_k && comic_new_k_id) {
    console.log('신규 만화 영역이 노출됩니다.');
  } else {
    console.log('신규 만화 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('신규만화 노출_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  //comic_new_k 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#comic_new_k'); 
  //isVisible_comic_new_k 변수에 element 노출 여부 저장 
  const isVisible_comic_new_k = await element.isVisible(); 
  //신규 만화 요소 영역 노출여부 확인
  expect(isVisible_comic_new_k).toBeTruthy; 
  //comic_new_k의 텍스트를 comic_new_k_id에 저장
  const comic_new_k_id = await element.evaluate((el) => el.id);
  // 신규 만화 노출 확인
  expect(comic_new_k_id?.trim()).toBe("comic_new_k"); 
  
  if (isVisible_comic_new_k && comic_new_k_id) {
    console.log('신규 만화 영역이 노출됩니다.');
  } else {
    console.log('신규 만화 영역이 노출되지 않습니다.');
  }
  await page.close();
});

/* US는 신규만화 인벤토리를 운영하지 않음
test('신규만화 노출_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }

  //comic_new_k 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#comic_new_k'); 
  //isVisible_comic_new_k 변수에 element 노출 여부 저장 
  const isVisible_comic_new_k = await element.isVisible(); 
  //신규 만화 요소 영역 노출여부 확인
  expect(isVisible_comic_new_k).toBeTruthy; 
  //comic_new_k의 텍스트를 comic_new_k_id에 저장
  const comic_new_k_id = await element.evaluate((el) => el.id);
  // 신규 만화 노출 확인
  expect(comic_new_k_id?.trim()).toBe("comic_new_k"); 
  
  if (isVisible_comic_new_k && comic_new_k_id) {
    console.log('신규 만화 영역이 노출됩니다.');
  } else {
    console.log('신규 만화 영역이 노출되지 않습니다.');
  }
  await page.close();
});*/


test('업데이트 된 찜한 작품 노출_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad@lezhin.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  //await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //order_up_subscription 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#order_up_subscription'); 
  //isVisible_subscription 변수에 element 노출 여부 저장 
  const isVisible_subscription = await element.isVisible();
  //업데이트된 찜한 작품 영역 노출여부 확인
  expect(isVisible_subscription).toBeTruthy; 
  //order_up_subscription의 텍스트를 subscription_id에 저장
  const subscription_id = await element.evaluate((el) => el.id); 
  // 신규 만화 노출 확인
  expect(subscription_id?.trim()).toBe("order_up_subscription"); 

  if (isVisible_subscription && subscription_id) {
    console.log('업데이트 된 찜한 작품 영역이 노출됩니다.');
  } else {
    console.log('업데이트 된 찜한 작품 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('업데이트 된 찜한 작품 노출_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();


  //order_up_subscription 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#order_up_subscription'); 
  //isVisible_subscription 변수에 element 노출 여부 저장 
  const isVisible_subscription = await element.isVisible();
  //업데이트된 찜한 작품 영역 노출여부 확인
  expect(isVisible_subscription).toBeTruthy; 
  //order_up_subscription의 텍스트를 subscription_id에 저장
  const subscription_id = await element.evaluate((el) => el.id); 
  // 업데이트된 찜한 작품 텍스트 검증
  expect(subscription_id?.trim()).toBe("order_up_subscription"); 

  if (isVisible_subscription && subscription_id) {
    console.log('업데이트 된 찜한 작품 영역이 노출됩니다.');
  } else {
    console.log('업데이트 된 찜한 작품 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('업데이트 된 찜한 작품 노출_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();



  //order_up_subscription 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#order_up_subscription'); 
  //isVisible_subscription 변수에 element 노출 여부 저장 
  const isVisible_subscription = await element.isVisible();
  //업데이트된 찜한 작품 영역 노출여부 확인
  expect(isVisible_subscription).toBeTruthy; 
  //order_up_subscription의 텍스트를 subscription_id에 저장
  const subscription_id = await element.evaluate((el) => el.id); 
  // 업데이트된 찜한 작품 텍스트 검증
  expect(subscription_id?.trim()).toBe("order_up_subscription"); 

  if (isVisible_subscription && subscription_id) {
    console.log('업데이트 된 찜한 작품 영역이 노출됩니다.');
  } else {
    console.log('업데이트 된 찜한 작품 영역이 노출되지 않습니다.');
  }
  await page.close();
});




test('최근 본 작품_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad@lezhin.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  //await page.getByRole('button', { name: '오늘 하루 안보기' }).click();

  //order_recent 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#order_recent'); 
  //isVisible_recent 변수에 element 노출 여부 저장 
  const isVisible_recent = await element.isVisible(); 
  //최근 본 작품 영역 노출여부 확인
  expect(isVisible_recent).toBeTruthy; 
  //order_recent의 텍스트를 recent_id애 저장
  const recent_id = await element.evaluate((el) => el.id);
  // 최근 본 작품 노출 확인
  expect(recent_id?.trim()).toBe("order_recent"); 
  
  if (isVisible_recent && recent_id) {
    console.log('최근 본 작품 영역이 노출됩니다.');
  } else {
    console.log('최근 본 작품 영역이 노출되지 않습니다.');
  }

  await page.close();
});

test('최근 본 작품_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();

  //order_recent 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#order_recent'); 
  //isVisible_recent 변수에 element 노출 여부 저장 
  const isVisible_recent = await element.isVisible(); 
  //최근 본 작품 영역 노출여부 확인
  expect(isVisible_recent).toBeTruthy; 
  //order_recent의 텍스트를 recent_id애 저장
  const recent_id = await element.evaluate((el) => el.id);
  //최근 본 작품 노출 확인
  expect(recent_id?.trim()).toBe("order_recent"); 
  
  if (isVisible_recent && recent_id) {
    console.log('최근 본 작품 영역이 노출됩니다.');
  } else {
    console.log('최근 본 작품 영역이 노출되지 않습니다.');
  }

  await page.close();
});

test('최근 본 작품_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();

  //order_recent 에서 요소 정보를 element 에 저장
  const element = await page.waitForSelector('#order_recent'); 
  //isVisible_recent 변수에 element 노출 여부 저장 
  const isVisible_recent = await element.isVisible(); 
  //최근 본 작품 영역 노출여부 확인
  expect(isVisible_recent).toBeTruthy; 
  //order_recent의 텍스트를 recent_id애 저장
  const recent_id = await element.evaluate((el) => el.id);
  //최근 본 작품 노출 확인
  expect(recent_id?.trim()).toBe("order_recent"); 
  
  if (isVisible_recent && recent_id) {
    console.log('최근 본 작품 영역이 노출됩니다.');
  } else {
    console.log('최근 본 작품 영역이 노출되지 않습니다.');
  }

  await page.close();
});




test('홈에서 보고 싶은 장르 취향 설정 하기', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('hidelove13@naver.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForTimeout(4000); 

 

  //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  const spanText = await page.$eval('span.style_myGenreSet__btnSubText__hgWM1', (element) => element.textContent);
  // 홈에서 보고 싶은 장르 취향 설정 노출 확인 
  expect(spanText?.trim()).toBe("홈에서 보고 싶은 장르"); 

  if (spanText?.trim() === '홈에서 보고 싶은 장르') {
    console.log('홈에서 보고 싶은 장르가 노출 됩니다.');
  } else {
    console.log('홈에서 보고 싶은 장르가 노출 되지 않습니다.');
  }

  await page.close();
});



test('취향 설정 하기 버튼 노출_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('hidelove13@naver.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForTimeout(4000);
  await page.getByRole('button', { name: '홈에서 보고 싶은 장르 취향 설정 하기' }).click();
  await page.getByRole('button', { name: '취소' }).click();


  //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  const spanText = await page.$eval('span.style_myGenreSet__btnText__LxuAP', (element) => element.textContent); 
  // 취향 설정 하기 노출 확인
  expect(spanText?.trim()).toBe("취향 설정 하기"); 
  
  if (spanText?.trim() === '취향 설정 하기') {
    console.log('취향 설정 하기가 노출 됩니다.');
  } else {
    console.log('취향 설정 하기가 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 설정 하기 버튼 노출_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForTimeout(4000);


  //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  const spanText = await page.$eval('span.style_myGenreSet__btnText__LxuAP', (element) => element.textContent); 
  // 취향 설정 하기 노출 확인
  expect(spanText?.trim()).toBe("好みのジャンルを設定する"); 

  if (spanText?.trim() === '好みのジャンルを設定する') {
    console.log('취향 설정 하기가 노출 됩니다.');
  } else {
    console.log('취향 설정 하기가 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 설정 하기 버튼 노출_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.waitForTimeout(4000);


  //취향 설정하기 버튼의 텍스트 요소 를 spanText에 저장
  const spanText = await page.$eval('span.style_myGenreSet__btnText__LxuAP', (element) => element.textContent); 
  // 취향 설정 하기 노출 확인
  expect(spanText?.trim()).toBe("My Recommendations Settings"); 

  if (spanText?.trim() === 'My Recommendations Settings') {
    console.log('취향 설정 하기가 노출 됩니다.');
  } else {
    console.log('취향 설정 하기가 노출 되지 않습니다.');
  }
  await page.close();
});


test('취향 적용 중_kr', async ({ page }) => {
  await page.goto('https://www.lezhin.com/ko');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('hidelove99@nate.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForTimeout(4000);
  //await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
 


  //취향 적용 중 버튼의 텍스트 요소 를 spanText에 저장
  const spanText = await page.$eval('span.style_myGenreSet__btnText__LxuAP', (element) => element.textContent); 
  // 취향적용 중 노출 확인
  expect(spanText?.trim()).toBe("취향 적용 중"); 

  if (spanText?.trim() === '취향 적용 중') {
    console.log('취향 적용 중이 노출 됩니다.');
  } else {
    console.log('취향 적용 중이 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 적용 중_ja', async ({ page }) => {
  await page.goto('https://www.lezhin.jp/ja');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('hidelove99@nate.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForTimeout(4000);
 


  //취향 적용 중 버튼의 텍스트 요소 를 spanText에 저장
  const spanText = await page.$eval('span.style_myGenreSet__btnText__LxuAP', (element) => element.textContent); 
  // 취향적용 중 노출 확인
  expect(spanText?.trim()).toBe("好みのジャンル設定適用中"); 
  
  if (spanText?.trim() === '好みのジャンル設定適用中') {
    console.log('취향 적용 중이 노출 됩니다.');
  } else {
    console.log('취향 적용 중이 노출 되지 않습니다.');
  }
  await page.close();
});

test('취향 적용 중_us', async ({ page }) => {
  await page.goto('https://www.lezhinus.com/en');
  try {
    // '오늘 하루 안보기' 버튼이 보이는지 확인
    const button = await page.waitForSelector('button[role="button"][class*="style_lzBtn__tyLuS"]', { timeout: 5000 });
    if (button) {
      // 버튼이 보이면 클릭
      await button.click();
    } else {
      console.log('오늘 하루 안보기 버튼이 표시되지 않았습니다.');
    }
  } catch (error) {
    
  }
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('hidelove99@nate.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.waitForTimeout(4000);
 


  //취향 적용 중 버튼의 텍스트 요소 를 spanText에 저장
  const spanText = await page.$eval('span.style_myGenreSet__btnText__LxuAP', (element) => element.textContent); 
  // 취향적용 중 노출 확인
  expect(spanText?.trim()).toBe("My Recommendations On"); 
  
  if (spanText?.trim() === 'My Recommendations On') {
    console.log('취향 적용 중이 노출 됩니다.');
  } else {
    console.log('취향 적용 중이 노출 되지 않습니다.');
  }
  await page.close();
});

