import { test, expect } from '@playwright/test';


test('전체 삭제_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바툰 ');
  await page.waitForTimeout(4000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  //await page.locator('div').filter({ hasText: /^작품레바툰레바닫기$/ }).getByRole('link').first().click();
  //await page.getByRole('button', { name: '검색', exact: true }).click();
  await page.getByRole('link', { name: '레진코믹스' }).click();
  await page.waitForTimeout(4000);
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('button', { name: '전체 삭제' }).click();

  

   //전체 삭제 기능 확인
  const button = await page.getByRole('heading', { name: '최근 검색' }); // 최근 검색 텍스트 노출 저장
  const isVisible = await button.isVisible();  //최근 검색 버튼 노출 유무 저장

  expect(isVisible).toBe(false);  // 최근 검색 영역 노출 유무를 판단
  
  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }


  await page.close();
});


test('전체 삭제_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('悪魔の育児日記 ');
  await page.waitForTimeout(4000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.getByRole('link', { name: 'レジンコミックス' }).click();
  await page.waitForTimeout(4000);
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  await page.getByRole('button', { name: 'すべて削除' }).click();


   //전체 삭제 기능 확인
  const button = await page.getByRole('heading', { name: '最近の検索' }); // 최근 검색 텍스트 노출 저장
  const isVisible = await button.isVisible();  //최근 검색 버튼 노출 유무 저장

  expect(isVisible).toBe(false);  // 최근 검색 영역 노출 유무를 판단
  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
});

test('전체 삭제_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Joseon Attorney ');
  await page.waitForTimeout(2000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(2000);
  await page.getByRole('link', { name: 'Lezhin Comics' }).click();
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  await page.getByRole('button', { name: 'Delete All' }).click();


   //전체 삭제 기능 확인
  const button = await page.getByRole('heading', { name: 'Recent Searches' }); // 최근 검색 텍스트 노출 저장
  const isVisible = await button.isVisible();  //최근 검색 버튼 노출 유무 저장

  expect(isVisible).toBe(false);  // 최근 검색 영역 노출 유무를 판단
  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
});



test('인기 태그 상세 페이지 이동_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('link', { name: '#액션' }).click();

  
   //전체 삭제 기능 확인
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1에서 가져온 텍스트 저장
   expect(text_1).toBe('#액션');  //text_1에 저장된 텍스트와 비교
   
   if (text_1 === '#액션') {
     console.log('#액션 태그 상세페이지 이동 되었습니다.');

   } else {
     console.log('#액션 태그 상세페이지 이동 되지 않았습니다.');
   }
  
   await page.close();

});

test('인기 태그 상세 페이지 이동_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  await page.getByRole('link', { name: '#百合' }).click();

  
   //전체 삭제 기능 확인
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1에서 가져온 텍스트 저장
   expect(text_1).toBe('#百合');  //text_1에 저장된 텍스트와 비교
   
   if (text_1 === '#百合') {
     console.log('#百合 태그 상세페이지 이동 되었습니다.');

   } else {
     console.log('#百合 태그 상세페이지 이동 되지 않았습니다.');
   }
  
   await page.close();

});

test('인기 태그 상세 페이지 이동_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  await page.getByRole('link', { name: '#Drama' }).click();

  
   //전체 삭제 기능 확인
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1에서 가져온 텍스트 저장
   expect(text_1).toBe('#Drama');  //text_1에 저장된 텍스트와 비교
   
   if (text_1 === '#Drama') {
     console.log('#Drama 태그 상세페이지 이동 되었습니다.');

   } else {
     console.log('#Drama 태그 상세페이지 이동 되지 않았습니다.');
   }
  
   await page.close();

});



test('검색 자동 완성_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('일상 ');
  await page.waitForTimeout(1000);

  

   //태그 자동완성 노출
   const element_1 = await page.getByRole('heading', { name: '태그' }); //  텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);//text_1 변수에 element_1에서 가져온 텍스트 저장

   expect(text_1).toBe('태그'); //text_1에 저장된 텍스트와 비교
  
   if (text_1 === '태그') {
     console.log('자동완성 태그 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 태그 영역이 노출 되지 않습니다.');
   }

  //작품 자동완성 노출
   const element_2 = await page.getByRole('heading', { name: '작품' }); // 텍스트 가져오기
   const text_2 = await element_2.evaluate((el) => el.textContent); //text_2 변수에 element_2에서 가져온 텍스트 저장
   expect(text_2).toBe('작품'); //text_2에 저장된 텍스트와 비교
   
   if (text_2 === '작품') {
     console.log('자동완성 작품 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 작품 영역이 노출 되지 않습니다.');
   }

   await page.close();
});

test('검색 자동 완성_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ドラマ ');
  await page.waitForTimeout(1000);

  

   //태그 자동완성 노출
   const element_1 = await page.getByRole('heading', { name: 'タグ' }); //  텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);//text_1 변수에 element_1에서 가져온 텍스트 저장

   expect(text_1).toBe('タグ'); //text_1에 저장된 텍스트와 비교
  
   if (text_1 === 'タグ') {
     console.log('자동완성 태그 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 태그 영역이 노출 되지 않습니다.');
   }

  //작품 자동완성 노출
   const element_2 = await page.getByRole('heading', { name: '作品',exact: true }); // 텍스트 가져오기
   const text_2 = await element_2.evaluate((el) => el.textContent); //text_2 변수에 element_2에서 가져온 텍스트 저장
   expect(text_2).toBe('作品'); //text_2에 저장된 텍스트와 비교
   
   if (text_2 === '作品') {
     console.log('자동완성 작품 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 작품 영역이 노출 되지 않습니다.');
   }

   await page.close();
});

test('검색 자동 완성_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('drama ');
  await page.waitForTimeout(1000);

  

   //태그 자동완성 노출
   const element_1 = await page.getByRole('heading', { name: 'Tag' }); //  텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);//text_1 변수에 element_1에서 가져온 텍스트 저장

   expect(text_1).toBe('Tag'); //text_1에 저장된 텍스트와 비교
  
   if (text_1 === 'Tag') {
     console.log('자동완성 태그 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 태그 영역이 노출 되지 않습니다.');
   }

  //작품 자동완성 노출
   const element_2 = await page.getByRole('heading', { name: 'Title',exact: true }); // 텍스트 가져오기
   const text_2 = await element_2.evaluate((el) => el.textContent); //text_2 변수에 element_2에서 가져온 텍스트 저장
   expect(text_2).toBe('Title'); //text_2에 저장된 텍스트와 비교
   
   if (text_2 === 'Title') {
     console.log('자동완성 작품 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 작품 영역이 노출 되지 않습니다.');
   }

   await page.close();
});



test('검색 후 태그 상세 페이지 이동_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('일상 ');
  await page.waitForTimeout(1000);
  
  const element_2 = await page.getByRole('link', { name: '#일상' }); // 텍스트 가져오기
  const text_2 = await element_2.evaluate((el) => el.textContent);  //text_2 변수에 element_2에서 가져온 텍스트 저장
  expect(text_2?.trim()).toBe('#일상'); //text_2에 저장된 텍스트와 비교

   
   if (text_2?.trim() === '#일상') {
     console.log('검색한 태그가 노출 됩니다.');
   } else {
     console.log('검색한 태그가 노출되지 않았습니다.');
   }
  
  await page.getByRole('link', { name: '#일상' }).click();
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1에서 가져온 텍스트 저장
   expect(text_1).toBe('#일상'); //text_1에 저장된 텍스트와 비교

   if (text_1 === '#일상') {
     console.log('#일상 태그 상세페이지 이동 되었습니다.');
   } else {
     console.log('#일상 태그 상세페이지 이동 되지 않았습니다.');
   }

   await page.close();
});

test('검색 후 태그 상세 페이지 이동_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ドラマ ');
  await page.waitForTimeout(1000);
  
  const element_2 = await page.getByRole('link', { name: '#ドラマ' }); // 텍스트 가져오기
  const text_2 = await element_2.evaluate((el) => el.textContent);  //text_2 변수에 element_2에서 가져온 텍스트 저장
  expect(text_2?.trim()).toBe('#ドラマ'); //text_2에 저장된 텍스트와 비교

   
   if (text_2?.trim() === '#ドラマ') {
     console.log('검색한 태그가 노출 됩니다.');
   } else {
     console.log('검색한 태그가 노출되지 않았습니다.');
   }
  
  await page.getByRole('link', { name: '#ドラマ' }).click();
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1에서 가져온 텍스트 저장
   expect(text_1).toBe('#ドラマ'); //text_1에 저장된 텍스트와 비교

   if (text_1 === '#ドラマ') {
     console.log('#ドラマ 태그 상세페이지 이동 되었습니다.');
   } else {
     console.log('#ドラマ 태그 상세페이지 이동 되지 않았습니다.');
   }

   await page.close();
});

test('검색 후 태그 상세 페이지 이동_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('drama ');
  await page.waitForTimeout(1000);
  
  const element_2 = await page.getByRole('link', { name: '#drama' }); // 텍스트 가져오기
  const text_2 = await element_2.evaluate((el) => el.textContent);  //text_2 변수에 element_2에서 가져온 텍스트 저장
  expect(text_2?.trim()).toBe('#Drama'); //text_2에 저장된 텍스트와 비교

   
   if (text_2?.trim() === '#Drama') {
     console.log('검색한 태그가 노출 됩니다.');
   } else {
     console.log('검색한 태그가 노출되지 않았습니다.');
   }
  
  await page.getByRole('link', { name: '#Drama' }).click();
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1에서 가져온 텍스트 저장
   expect(text_1).toBe('#Drama'); //text_1에 저장된 텍스트와 비교

   if (text_1 === '#Drama') {
     console.log('#drama 태그 상세페이지 이동 되었습니다.');
   } else {
     console.log('#drama 태그 상세페이지 이동 되지 않았습니다.');
   }

   await page.close();
});


test('최근 검색 태그 비노출_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('일상 ');
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '#일상' }).click();
  await page.getByRole('link', { name: '레진코믹스' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.waitForTimeout(1000);


  const button = await page.getByRole('heading', { name: '최근 검색' }); //button 변수에최근 검색 헤더 텍스트 지정
  const isVisible = await button.isVisible(); //isVisible 변수에 버튼 노출 값 저장  
  expect(isVisible).toBe(false); //최근 검색 버튼이 비노출 되는지 체크

  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
});

test('최근 검색 태그 비노출_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ドラマ ');
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '#ドラマ' }).click();
  await page.getByRole('link', { name: 'レジンコミックス' }).click();
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  await page.waitForTimeout(1000);


  const button = await page.getByRole('heading', { name: '最近の検索' }); //button 변수에최근 검색 헤더 텍스트 지정
  const isVisible = await button.isVisible(); //isVisible 변수에 버튼 노출 값 저장  
  expect(isVisible).toBe(false); //최근 검색 버튼이 비노출 되는지 체크

  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
});

test('최근 검색 태그 비노출_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Drama ');
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '#Drama' }).click();
  await page.getByRole('link', { name: 'Lezhin Comics' }).click();
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  await page.waitForTimeout(1000);


  const button = await page.getByRole('heading', { name: 'Recent Searches' }); //button 변수에최근 검색 헤더 텍스트 지정
  const isVisible = await button.isVisible(); //isVisible 변수에 버튼 노출 값 저장  
  expect(isVisible).toBe(false); //최근 검색 버튼이 비노출 되는지 체크

  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  await page.close();
});


test('검색 갯수 최대 노출_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('DCW ');
  await page.waitForTimeout(1000);

  //검색결과 노출 갯수 체크
  const searchListItemsCount = await page.$$eval('.hy__listItem', (elements) => elements.length); //searchListItemsCount에 searchList에 포함된 li 태그 갯수를 저장
  expect(searchListItemsCount).toBe(8); //searchListItemsCount에 저장된 li 태그 갯수와 8개 숫자를 비교
  console.log('.hy__listItem li 태그의 개수:', searchListItemsCount);


  if (searchListItemsCount == 8) {
    console.log('검색 최대 갯수가 8개 확인 완료');
  } else if(searchListItemsCount > 8){
    console.log('검색 최대 갯수가 8개를 초과하여 오류 입니다.');
  } else {
    console.log('검색 최대 갯수개 8개 미만입니다 검색어를 확인하세요');
  }

  await page.close();
  
});

test('검색 갯수 최대 노출_jp', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('日常 ');
  await page.waitForTimeout(1000);

  //검색결과 노출 갯수 체크
  const searchListItemsCount = await page.$$eval('.hy__listItem', (elements) => elements.length); //searchListItemsCount에 searchList에 포함된 li 태그 갯수를 저장
  expect(searchListItemsCount).toBe(8); //searchListItemsCount에 저장된 li 태그 갯수와 8개 숫자를 비교
  console.log('.hy__listItem li 태그의 개수:', searchListItemsCount);


  if (searchListItemsCount == 8) {
    console.log('검색 최대 갯수가 8개 확인 완료');
  } else if(searchListItemsCount > 8){
    console.log('검색 최대 갯수가 8개를 초과하여 오류 입니다.');
  } else {
    console.log('검색 최대 갯수개 8개 미만입니다 검색어를 확인하세요');
  }

  await page.close();
  
});

test('검색 갯수 최대 노출_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Drama ');
  await page.waitForTimeout(1000);

  //검색결과 노출 갯수 체크
  const searchListItemsCount = await page.$$eval('.hy__listItem', (elements) => elements.length); //searchListItemsCount에 searchList에 포함된 li 태그 갯수를 저장
  expect(searchListItemsCount).toBe(8); //searchListItemsCount에 저장된 li 태그 갯수와 8개 숫자를 비교
  console.log('.hy__listItem li 태그의 개수:', searchListItemsCount);


  if (searchListItemsCount == 8) {
    console.log('검색 최대 갯수가 8개 확인 완료');
  } else if(searchListItemsCount > 8){
    console.log('검색 최대 갯수가 8개를 초과하여 오류 입니다.');
  } else {
    console.log('검색 최대 갯수개 8개 미만입니다 검색어를 확인하세요');
  }

  await page.close();
  
});



test('비성인 계정 블라인드 작품_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_04@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('불륜  ');
  await page.waitForTimeout(1000);

  const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 }); //블라인드 이미지 URL주소를 저장한다.
  
  expect(imageElement).toBeTruthy(); //현재 페이지에서 imageElement 에 저장된 이미지 url 주소가 실제 노출되는지 확인
  console.log('블라인드 이미지 노출 확인 완료');
  await page.close();
  
});

test('비성인 계정 블라인드 작품_jp', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad_04@yopmail.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('百合  ');
  await page.waitForTimeout(1000);

  const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 }); //블라인드 이미지 URL주소를 저장한다.
  
  expect(imageElement).toBeTruthy(); //현재 페이지에서 imageElement 에 저장된 이미지 url 주소가 실제 노출되는지 확인
  console.log('블라인드 이미지 노출 확인 완료');
  await page.close();
  
});

test('비성인 계정 블라인드 작품_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad_04@yopmail.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('wife  ');
  await page.waitForTimeout(1000);

  const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 }); //블라인드 이미지 URL주소를 저장한다.
  
  expect(imageElement).toBeTruthy(); //현재 페이지에서 imageElement 에 저장된 이미지 url 주소가 실제 노출되는지 확인
  console.log('블라인드 이미지 노출 확인 완료');
  await page.close();
  
});




test('비로그인 블라인드 작품_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('불륜  ');
  await page.waitForTimeout(1000);

  const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 }); //블라인드 이미지의 URL주소를 저장한다.
  
  // 이미지가 화면에 노출되었을 때 추가로 수행할 작업을 여기에 작성합니다.
  expect(imageElement).toBeTruthy();//현재 페이지에서 imageElement 에 저장된 이미지 url 주소가 실제 노출되는지 확인
  console.log('블라인드 이미지 노출 확인 완료');
  await page.close();
  
});

test('비로그인 블라인드 작품_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('百合  ');
  await page.waitForTimeout(1000);

  const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 }); //블라인드 이미지의 URL주소를 저장한다.
  
  // 이미지가 화면에 노출되었을 때 추가로 수행할 작업을 여기에 작성합니다.
  expect(imageElement).toBeTruthy();//현재 페이지에서 imageElement 에 저장된 이미지 url 주소가 실제 노출되는지 확인
  console.log('블라인드 이미지 노출 확인 완료');
  await page.close();
  
});

test('비로그인 블라인드 작품_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('wife  ');
  await page.waitForTimeout(1000);

  const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 }); //블라인드 이미지의 URL주소를 저장한다.
  
  // 이미지가 화면에 노출되었을 때 추가로 수행할 작업을 여기에 작성합니다.
  expect(imageElement).toBeTruthy();//현재 페이지에서 imageElement 에 저장된 이미지 url 주소가 실제 노출되는지 확인
  console.log('블라인드 이미지 노출 확인 완료');
  await page.close();
  
});



test('성인 계정 성인작품 노출 19on_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_01@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();

  /*
  try {
    await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  } catch (error) {
    console.log('오늘 하루 안보기 버튼을 찾지 못하여 다음 스크립트를 실행합니다.');
  }*/

  if (!page.isClosed()) {
    await page.waitForTimeout(2000);
  }

  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('어쩌라GO  ');
  await page.waitForTimeout(1000);

//정상 성인 이미지 노출
const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/6207797588393984/images/thumbnail.webp?updated=1624598074730&width=100"]'); // 이미지 요소를 선택
const srcValue = await imageElement.evaluate(element => element.getAttribute('src'));// 이미지 요소의 url을 srcValue 변수에 저장

expect(srcValue).toBe("https://q-ccdn.lezhin.com/v2/comics/6207797588393984/images/thumbnail.webp?updated=1624598074730&width=100"); //srcAttribute에 저장된 srcValue 링크 url과 실제 url을 비교
console.log('성인작품 이미지 정상 노출 확인 완료');
await page.close();
  
});

test('성인 계정 성인작품 노출 19on_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad_01@yopmail.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('BAD THINKING DIARY  ');
  await page.waitForTimeout(1000);


//정상 성인 이미지 노출
const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/4626270150000640/images/thumbnail.webp?updated=1691926581430&width=100"]'); // 이미지 요소를 선택
const srcValue = await imageElement.evaluate(element => element.getAttribute('src'));// 이미지 요소의 url을 srcValue 변수에 저장

expect(srcValue).toBe("https://q-ccdn.lezhin.com/v2/comics/4626270150000640/images/thumbnail.webp?updated=1691926581430&width=100"); //srcAttribute에 저장된 src 링크 url과 실제 url을 비교
console.log('성인작품 이미지 정상 노출 확인 완료');
await page.close();
  
});


test('성인 계정 성인작품 노출 19on_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad_01@yopmail.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Like Fine Wine  ');
  await page.waitForTimeout(1000);

//정상 성인 이미지 노출
const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/4953128406155264/images/thumbnail.webp?updated=1703062255856&width=100"]'); // 이미지 요소를 선택
const srcValue = await imageElement.evaluate(element => element.getAttribute('src'));// 이미지 요소의 url을 srcValue 변수에 저장

expect(srcValue).toBe("https://q-ccdn.lezhin.com/v2/comics/4953128406155264/images/thumbnail.webp?updated=1703062255856&width=100"); //srcAttribute에 저장된 src 링크 url과 실제 url을 비교
console.log('성인작품 이미지 정상 노출 확인 완료');
await page.close();
  
});






test('성인 계정 성인작품 노출 19 Off_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad@lezhin.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!@');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForTimeout(2000);
  /*
  try {
    await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  } catch (error) {
    console.log('오늘 하루 안보기 버튼을 찾지 못하여 다음 스크립트를 실행합니다.');
  }*/
  await page.getByRole('button', { name: '전연령으로 이동' }).click();
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('어쩌라go ');
  await page.waitForTimeout(1000);


//정상 성인 이미지 노출
const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/6207797588393984/images/thumbnail.webp?updated=1624598074730&width=100"]'); // 이미지 요소를 선택
const srcValue = await imageElement.evaluate(element => element.getAttribute('src'));// 이미지 요소의 url을 srcValue 변수에 저장

expect(srcValue).toBe("https://q-ccdn.lezhin.com/v2/comics/6207797588393984/images/thumbnail.webp?updated=1624598074730&width=100"); //srcAttribute에 저장된 src 링크 url과 실제 url을 비교
console.log('성인작품 이미지 정상 노출 확인 완료');
await page.close();

});

test('성인 계정 성인작품 노출 19 Off_jp', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForTimeout(2000);

 
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '全年齢に移動' }).click();
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('BAD THINKING DIARY ');
  await page.waitForTimeout(1000);


//정상 성인 이미지 노출
const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/4626270150000640/images/thumbnail.webp?updated=1691926581430&width=100"]'); // 이미지 요소를 선택
const srcValue = await imageElement.evaluate(element => element.getAttribute('src'));// 이미지 요소의 url을 srcValue 변수에 저장

expect(srcValue).toBe("https://q-ccdn.lezhin.com/v2/comics/4626270150000640/images/thumbnail.webp?updated=1691926581430&width=100"); //srcAttribute에 저장된 src 링크 url과 실제 url을 비교
console.log('성인작품 이미지 정상 노출 확인 완료');
await page.close();

});


test('성인 계정 성인작품 노출 19 Off_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'Login with email' }).click();

 
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: 'Go to All-Ages' }).click();
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Like Fine Wine  ');
  await page.waitForTimeout(1000);


//정상 성인 이미지 노출
const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/4953128406155264/images/thumbnail.webp?updated=1703062255856&width=100"]'); // 이미지 요소를 선택
const srcValue = await imageElement.evaluate(element => element.getAttribute('src'));// 이미지 요소의 url을 srcValue 변수에 저장

expect(srcValue).toBe("https://q-ccdn.lezhin.com/v2/comics/4953128406155264/images/thumbnail.webp?updated=1703062255856&width=100"); //srcAttribute에 저장된 src 링크 url과 실제 url을 비교
console.log('성인작품 이미지 정상 노출 확인 완료');
await page.close();

});



test('검색 > 에피소드 목록 이동_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('귀멸의 칼날  ');
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '귀멸의 칼날 고토게 코요하루 / DCW' }).click();

  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.comicInfo__title'); // 요소 클래스에서 에피소드 목록 타이틀 요소 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1 저장된 텍스트를 저장

  expect(text_1).toBe("귀멸의 칼날"); //text_1에 저장된 텍스트와 실제 텍스트를 비교
  
  if (text_1 === '귀멸의 칼날') {
    console.log('귀멸의 칼날 에피소드 목록으로 이동 되었습니다.');
  } else {
    console.log('귀멸의 칼날 에피소드 목록으로 이동 되지 않았습니다.');
  }

  await page.close();
});

test('검색 > 성인 작품 에피소드 목록 이동_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('BAD THINKING DIARY  ');
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '18 BAD THINKING DIARY：バット・シンキング・ダイアリー ホダン, ランラリー' }).click();

  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.comicInfo__title'); // 요소 클래스에서 에피소드 목록 타이틀 요소 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1 저장된 텍스트를 저장

  expect(text_1).toBe("BAD THINKING DIARY：バット・シンキング・ダイアリー"); //text_1에 저장된 텍스트와 실제 텍스트를 비교
  
  if (text_1 === 'BAD THINKING DIARY：バット・シンキング・ダイアリー') {
    console.log('BAD THINKING DIARY：バット・シンキング・ダイアリー 에피소드 목록으로 이동 되었습니다.');
  } else {
    console.log('BAD THINKING DIARY：バット・シンキング・ダイアリー 에피소드 목록으로 이동 되지 않았습니다.');
  }

  await page.close();
});

test('검색 > 에피소드 목록 이동_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('4cut  ');
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '4 Cut Hero Gojira-kun', exact: true }).click();


  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.comicInfo__title'); // 요소 클래스에서 에피소드 목록 타이틀 요소 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1 저장된 텍스트를 저장

  expect(text_1).toBe("4 Cut Hero"); //text_1에 저장된 텍스트와 실제 텍스트를 비교
  
  if (text_1 === '4 Cut Hero') {
    console.log('4 Cut Hero 에피소드 목록으로 이동 되었습니다.');
  } else {
    console.log('4 Cut Hero 에피소드 목록으로 이동 되지 않았습니다.');
  }

  await page.close();
});




test('검색상세 작가/출판사 리스트 노출_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('망자카페 ');
  await page.waitForTimeout(1000);


  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.hy__infoMeta'); // 클래스에서 작가(글,그림,작가,원작,모델) 요소 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1 저장된 텍스트를 저장

  expect(text_1?.trim()).toBe("베르디, 가나다, 라마바, 사아자, 하하하/출판사1, 출판사2, 레이블"); //text_1에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  
  if (text_1?.trim() === '베르디, 가나다, 라마바, 사아자, 하하하/출판사1, 출판사2, 레이블') {
    console.log('작가(글,그림,작가,원작,모델)이 노출됩니다.');
  } else {
    console.log('작가(글,그림,작가,원작,모델)이 노출되지 않습니다.');
  }
  await page.close();
});

test('검색상세 작가/출판사 리스트 노출_jp', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('男主人公は丁重にお断りします！ ');
  await page.waitForTimeout(1000);



  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.hy__infoMeta'); // 클래스에서 작가(글,그림,작가,원작,모델) 요소 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1 저장된 텍스트를 저장

  expect(text_1?.trim()).toBe("SALAMAN, YEHWON/Kidari Studio, Kidari Studio"); //text_1에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  
  if (text_1?.trim() === 'SALAMAN, YEHWON/Kidari Studio, Kidari Studio') {
    console.log('작가 영역이 노출됩니다.');
  } else {
    console.log('작가 영역이 노출되지 않습니다.');
  }
  await page.close();
});

test('검색상세 작가/출판사 리스트 노출_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Behind Story ');
  await page.waitForTimeout(1000);


  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.hy__infoMeta'); // 클래스에서 작가(글,그림,작가,원작,모델) 요소 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent); //text_1 변수에 element_1 저장된 텍스트를 저장

  expect(text_1?.trim()).toBe("Narae Ahn/NETCOMICS, 레이블"); //text_1에 저장된 텍스트와 실제 노출되어야할 텍스트 비교
  
  if (text_1?.trim() === 'Narae Ahn') {
    console.log('작가 영역이 노출됩니다.');
  } else {
    console.log('작가 영역이 노출되지 않습니다.');
  }
  await page.close();
});





test('검색 결과 페이지 전체탭 선택과 결과_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');

  const buttonElement = await page.waitForSelector('button[data-search-type="all"][aria-selected="true"]');  // 버튼 요소를 선택

  const ariaSelectedValue = await buttonElement.getAttribute('aria-selected');// 버튼 요소의 aria-selected 속성 값을 가져옴
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('전체탭이 선택되어 노출 됩니다.');
  } else {
    console.log('전체탭이 선택되지 않았습니다.');
  }

  const title = await page.waitForSelector('.lzComic__title'); //클래스에서 요소 가져오기
  const text_1 = await title.evaluate((el) => el.textContent); // 요소에 저장된 텍스트를 text_1 변수에 저장
  expect(text_1?.trim()).toBe("레바툰");  // text_1 변수에 저장된 텍스트와 노출되어야할 텍스트르 비교

  if (text_1?.trim() === '레바툰') {
    console.log('작품 레바툰이 노출 됩니다.');
  } else {
    console.log('작품 레바툰이 노출되지 않습니다.');
  }

  const artist = await page.waitForSelector('.lzComic__artist'); //클래스에서 요소 가져오기
  const text_2 = await artist.evaluate((el) => el.textContent);// 요소에 저장된 텍스트를 text_2 변수에 저장
  expect(text_2?.trim()).toBe("레바"); // text_2 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교


  if (text_2?.trim() === '레바') {
    console.log('작가 레바가 노출 됩니다.');
  } else {
    console.log('작가 레바가 노출되지 않습니다.');
  }

  const tag = await page.waitForSelector('.lzComic__tags'); //클래스에서 요소 가져오기
  const text_3 = await tag.evaluate((el) => el.textContent); // 요소에 저장된 텍스트를 text_3 변수에 저장
  expect(text_3?.trim()).toBe("#일상 #병맛 #코믹"); //text_3 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교
  
  if (text_3?.trim() === '#일상 #병맛 #코믹') {
    console.log('태그 일상이 노출 됩니다.');
  } else {
    console.log('태그 일상이 노출되지 않습니다.');
  }

  const text_5 = await page.$eval('li.lzComic__item[data-id="260"] .lzComic__genre', (element) => element.textContent); //작품에 저장된 장르값을 text_5 변수에 저장
  expect(text_5?.trim()).toBe("일상"); //text_5 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교

  if (text_5?.trim() === '일상') {
    console.log('일상 장르가 노출 됩니다.');
  } else {
    console.log('일상 장르가 노출 노출되지 않습니다.');
  }

  await page.close();

});

test('검색 결과 페이지 전체탭 선택과 결과_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('男主人公は丁重にお断りします！ ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);

  const buttonElement = await page.waitForSelector('button[data-search-type="all"][aria-selected="true"]');  // 버튼 요소를 선택

  const ariaSelectedValue = await buttonElement.getAttribute('aria-selected');// 버튼 요소의 aria-selected 속성 값을 가져옴
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('전체탭이 선택되어 노출 됩니다.');
  } else {
    console.log('전체탭이 선택되지 않았습니다.');
  }

  const title = await page.waitForSelector('.lzComic__title'); //클래스에서 요소 가져오기
  const text_1 = await title.evaluate((el) => el.textContent); // 요소에 저장된 텍스트를 text_1 변수에 저장
  expect(text_1?.trim()).toBe("男主人公は丁重にお断りします！【連載】");  // text_1 변수에 저장된 텍스트와 노출되어야할 텍스트르 비교

  if (text_1?.trim() === '男主人公は丁重にお断りします！') {
    console.log('작품 男主人公は丁重にお断りします！이 노출 됩니다.');
  } else {
    console.log('작품 男主人公は丁重にお断りします！이 노출되지 않습니다.');
  }

  const artist = await page.waitForSelector('.lzComic__artist'); //클래스에서 요소 가져오기
  const text_2 = await artist.evaluate((el) => el.textContent);// 요소에 저장된 텍스트를 text_2 변수에 저장
  expect(text_2?.trim()).toBe("SALAMAN, YEHWON"); // text_2 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교


  if (text_2?.trim() === 'SALAMAN, YEHWON') {
    console.log('작가 SALAMAN, YEHWON가 노출 됩니다.');
  } else {
    console.log('작가 SALAMAN, YEHWON가 노출되지 않습니다.');
  }


  const tag = await page.waitForSelector('.lzComic__tags'); //클래스에서 요소 가져오기
  const text_3 = await tag.evaluate((el) => el.textContent); // 요소에 저장된 텍스트를 text_3 변수에 저장
  expect(text_3?.trim()).toBe("#転生 #恋愛 #ロマンス"); //text_3 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교
  
  if (text_3?.trim() === '#転生 #恋愛 #ロマンス') {
    console.log('태그 일상이 노출 됩니다.');
  } else {
    console.log('태그 일상이 노출되지 않습니다.');
  }

  const text_5 = await page.$eval('li.lzComic__item[data-id="4897286449856512"] .lzComic__genre', (element) => element.textContent); //작품에 저장된 장르값을 text_5 변수에 저장
  expect(text_5?.trim()).toBe("ロマンス"); //text_5 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교

  if (text_5?.trim() === 'ロマンス') {
    console.log('ロマンス 장르가 노출 됩니다.');
  } else {
    console.log('ロマンス 장르가 노출 노출되지 않습니다.');
  }

  await page.close();
});

test('검색 결과 페이지 전체탭 선택과 결과_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Joseon Attorney ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);


  const buttonElement = await page.waitForSelector('button[data-search-type="all"][aria-selected="true"]');  // 버튼 요소를 선택

  const ariaSelectedValue = await buttonElement.getAttribute('aria-selected');// 버튼 요소의 aria-selected 속성 값을 가져옴
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('전체탭이 선택되어 노출 됩니다.');
  } else {
    console.log('전체탭이 선택되지 않았습니다.');
  }

  const title = await page.waitForSelector('.lzComic__title'); //클래스에서 요소 가져오기
  const text_1 = await title.evaluate((el) => el.textContent); // 요소에 저장된 텍스트를 text_1 변수에 저장
  expect(text_1?.trim()).toBe("Joseon Attorney");  // text_1 변수에 저장된 텍스트와 노출되어야할 텍스트르 비교

  if (text_1?.trim() === 'Joseon Attorney') {
    console.log('작품 Joseon Attorney이 노출 됩니다.');
  } else {
    console.log('작품 Joseon Attorney이 노출되지 않습니다.');
  }

  const artist = await page.waitForSelector('.lzComic__artist'); //클래스에서 요소 가져오기
  const text_2 = await artist.evaluate((el) => el.textContent);// 요소에 저장된 텍스트를 text_2 변수에 저장
  expect(text_2?.trim()).toBe("JeongHolak, SIMGUN"); // text_2 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교


  if (text_2?.trim() === 'JeongHolak, SIMGUN') {
    console.log('작가 JeongHolak, SIMGUN가 노출 됩니다.');
  } else {
    console.log('작가 JeongHolak, SIMGUN가 노출되지 않습니다.');
  }


  const tag = await page.waitForSelector('.lzComic__tags'); //클래스에서 요소 가져오기
  const text_3 = await tag.evaluate((el) => el.textContent); // 요소에 저장된 텍스트를 text_3 변수에 저장
  expect(text_3?.trim()).toBe("#FarEast #Historical #Drama"); //text_3 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교
  
  if (text_3?.trim() === '#FarEast #Historical #Drama') {
    console.log('태그 일상이 노출 됩니다.');
  } else {
    console.log('태그 일상이 노출되지 않습니다.');
  }

  const text_5 = await page.$eval('li.lzComic__item[data-id="5656291320856576"] .lzComic__genre', (element) => element.textContent); //작품에 저장된 장르값을 text_5 변수에 저장
  expect(text_5?.trim()).toBe("Drama"); //text_5 변수에 저장된 텍스트와 노출되어야할 텍스트를 비교

  if (text_5?.trim() === 'Drama') {
    console.log('Drama 장르가 노출 됩니다.');
  } else {
    console.log('Drama 장르가 노출 노출되지 않습니다.');
  }

  await page.close();
});

test('검색 결과 페이지 작품탭 결과_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작품' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="title"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작품탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('작품탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작품탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-title'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증


  if (emElement) {
    console.log('레바 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('레바 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();

});

test('검색 결과 페이지 작품탭 결과_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('男主人公は丁重にお断りします！ ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '作品' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="title"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작품탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('작품탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작품탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-title'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증


  if (emElement) {
    console.log('男主人公は丁重にお断りします 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('男主人公は丁重にお断りします 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();

});

test('검색 결과 페이지 작품탭 결과_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Joseon Attorney ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: 'Title' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="title"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작품탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('작품탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작품탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-title'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증


  if (emElement) {
    console.log('Joseon Attorney 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('Joseon Attorney 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();

});


test('검색 결과 페이지 작가탭 결과 및 더보기 클릭_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작가' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="artist"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (selectedElement) {
    console.log('작가탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작가탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-artist'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('레바 키워드에 강조효과가 적용되어 노출 됩니다.'); // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('레바 키워드에 강조효과가 적용되어 있지 않습니다.'); // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  const publisherElement = await page.waitForSelector('#search-section-artist'); 
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');

  await lzComicMoreElement?.click(); //더보기 버튼 클릭
  
  const artist = await page.waitForSelector('#artist-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); // 요소에서 가져온 텍스트를 text 변수에 저장
  expect(text?.trim()).toBe("레바님의 작품");   // text 변수에 저장된 텍스트와 실제 텍스트를 비교
  
  if (text?.trim() === '레바님의 작품') {
    console.log('더보기를 클릭하여 레바 작가 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 레바 작가 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});

test('검색 결과 페이지 작가탭 결과 및 더보기 클릭_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('YEHWON ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '作家' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="artist"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (selectedElement) {
    console.log('작가탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작가탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-artist'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('레바 키워드에 강조효과가 적용되어 노출 됩니다.'); // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('레바 키워드에 강조효과가 적용되어 있지 않습니다.'); // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  const publisherElement = await page.waitForSelector('#search-section-artist'); 
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');

  await lzComicMoreElement?.click(); //더보기 버튼 클릭
  
  const artist = await page.waitForSelector('#artist-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); // 요소에서 가져온 텍스트를 text 변수에 저장
  expect(text?.trim()).toBe("YEHWONの作品");   // text 변수에 저장된 텍스트와 실제 텍스트를 비교
  
  if (text?.trim() === 'YEHWONの作品') {
    console.log('더보기를 클릭하여 레바 작가 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 레바 작가 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});

test('검색 결과 페이지 작가탭 결과 및 더보기 클릭_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('SIMGUN ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: 'Writer' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="artist"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (selectedElement) {
    console.log('작가탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작가탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-artist'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('SIMGUN 키워드에 강조효과가 적용되어 노출 됩니다.'); // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('SIMGUN 키워드에 강조효과가 적용되어 있지 않습니다.'); // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  const publisherElement = await page.waitForSelector('#search-section-artist'); 
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');

  await lzComicMoreElement?.click(); //더보기 버튼 클릭
  
  const artist = await page.waitForSelector('#artist-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); // 요소에서 가져온 텍스트를 text 변수에 저장
  expect(text?.trim()).toBe("SIMGUN's Titles"); // text 변수에 저장된 텍스트와 실제 텍스트를 비교
  
  const url = page.url();
  if (url === 'https://q-www.lezhinus.com/en/artist/simgun?page=0') {
    console.log('더보기를 클릭하여 SIMGUN 작가 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 SIMGUN 작가 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});


test('검색 결과 페이지 출판사 결과 및 더보기 클릭_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('DCW ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');;
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '출판사' }).click();

  const selectedElement = await page.waitForSelector('button[data-search-type="publisher"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 출판사탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('출판사탭이 선택되어 노출 됩니다.');
  } else {
    console.log('출판사탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-publisher'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('DCW 키워드에 강조효과가 적용되어 노출 됩니다.'); // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('DCW 키워드에 강조효과가 적용되어 있지 않습니다.');
    await page.goto('https://q-www.lezhin.com/ko/search?t=publisher&q=DCW'); // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  const publisherElement = await page.waitForSelector('#search-section-publisher');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click(); // 클릭하여 동작 수행

  const artist = await page.waitForSelector('#artist-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); //요소에 저장된 텍스트를 text 변수에 저장

  expect(text?.trim()).toBe("DCW님의 작품");  //text 변수에 저장된 값과 실제 노출되어야하는 값을 비교
  
  if (text?.trim() === 'DCW님의 작품') {
    console.log('더보기를 클릭하여 DCW 출판사 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 DCW 출판사 상세 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});

test('검색 결과 페이지 출판사 결과 및 더보기 클릭_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Kidari ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '出版社' }).click();

  const selectedElement = await page.waitForSelector('button[data-search-type="publisher"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 출판사탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('출판사탭이 선택되어 노출 됩니다.');
  } else {
    console.log('출판사탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-publisher'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('DCW 키워드에 강조효과가 적용되어 노출 됩니다.'); // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('DCW 키워드에 강조효과가 적용되어 있지 않습니다.');
    await page.goto('https://q-www.lezhin.jp/ja/search?t=publisher&q=kidari'); // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  const publisherElement = await page.waitForSelector('#search-section-publisher');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click(); // 클릭하여 동작 수행

  const artist = await page.waitForSelector('#artist-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); //요소에 저장된 텍스트를 text 변수에 저장

  expect(text?.trim()).toBe("Kidari Studioの作品");  //text 변수에 저장된 값과 실제 노출되어야하는 값을 비교
  
  if (text?.trim() === 'Kidari Studioの作品') {
    console.log('더보기를 클릭하여 Kidari Studio 출판사 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 Kidari Studio 출판사 상세 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});

test('검색 결과 페이지 출판사 결과 및 더보기 클릭_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('NETCOMICS ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: 'Publisher' }).click();

  const selectedElement = await page.waitForSelector('button[data-search-type="publisher"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 출판사탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true");  //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('출판사탭이 선택되어 노출 됩니다.');
  } else {
    console.log('출판사탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-publisher'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('NETCOMICS 키워드에 강조효과가 적용되어 노출 됩니다.'); // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('NETCOMICS 키워드에 강조효과가 적용되어 있지 않습니다.');
    await page.goto('https://q-www.lezhinus.com/en/search?t=publisher&q=NETCOMICS'); // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  const publisherElement = await page.waitForSelector('#search-section-publisher');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click(); // 클릭하여 동작 수행

  const artist = await page.waitForSelector('#artist-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); //요소에 저장된 텍스트를 text 변수에 저장
  expect(text?.trim()).toBe("NETCOMICS's Titles");  //text 변수에 저장된 값과 실제 노출되어야하는 값을 비교
  
  const url = page.url();
  if (text?.trim() === 'https://q-www.lezhinus.com/en/artist/netcomics?page=0') {
    console.log('더보기를 클릭하여 NETCOMICS 출판사 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 NETCOMICS 출판사 상세 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});




test('검색 결과 페이지 태그 결과 및 더보기 클릭_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('일상 ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '태그' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="tag"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 태그 탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected');//ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('태그탭이 선택되어 노출 됩니다.');
  } else {
    console.log('태그탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-tag'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('일상 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('일상 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
  const moreLink = await page.waitForSelector('a.lzComic__more'); // 더보기 버튼 요소 선택
  await moreLink.click(); // 태그 더보기 버튼 클릭

  const artist = await page.waitForSelector('#tag-comic-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); // artist 변수의 요소에서 텍스트를 text변수에 저장
  expect(text?.trim()).toBe("#일상"); //text 변수에 저장된 값과 실제 노출되어야할 값을 비교
  
  if (text?.trim() === '#일상') {
    console.log('더보기를 클릭하여 일상 태그 상세 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 일상 태그 상세 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});


test('검색 결과 페이지 태그 결과 및 더보기 클릭_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ドラマ ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: 'タグ' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="tag"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 태그 탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected');//ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('태그탭이 선택되어 노출 됩니다.');
  } else {
    console.log('태그탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-tag'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('ドラマ 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('ドラマ 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
  const moreLink = await page.waitForSelector('a.lzComic__more'); // 더보기 버튼 요소 선택
  await moreLink.click(); // 태그 더보기 버튼 클릭


  const artist = await page.waitForSelector('#tag-comic-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); // artist 변수의 요소에서 텍스트를 text변수에 저장
  expect(text?.trim()).toBe("#ドラマ"); //text 변수에 저장된 값과 실제 노출되어야할 값을 비교
  
  if (text?.trim() === '#ドラマ') {
    console.log('더보기를 클릭하여 ドラマ 태그 상세 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 ドラマ 태그 상세 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});


test('검색 결과 페이지 태그 결과 및 더보기 클릭_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('Drama ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: 'Tag' }).click();


  const selectedElement = await page.waitForSelector('button[data-search-type="tag"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 태그 탭 강조효과
  const ariaSelectedValue = await selectedElement.getAttribute('aria-selected');//ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교
  
  if (ariaSelectedValue) {
    console.log('태그탭이 선택되어 노출 됩니다.');
  } else {
    console.log('태그탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-tag'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em'); //emElement 변수에 titleElement 요소 값 저장
  expect(emElement).toBeTruthy(); //em 태그가 존재 하는지 검증

  if (emElement) {
    console.log('Drama 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('Drama 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
  const moreLink = await page.waitForSelector('a.lzComic__more'); // 더보기 버튼 요소 선택
  await moreLink.click(); // 태그 더보기 버튼 클릭


  const artist = await page.waitForSelector('#tag-comic-heading'); //  클래스에서 요소 가져오기
  const text = await artist.evaluate((el) => el.textContent); // artist 변수의 요소에서 텍스트를 text변수에 저장
  expect(text?.trim()).toBe("#Drama"); //text 변수에 저장된 값과 실제 노출되어야할 값을 비교
  
  if (text?.trim() === '#Drama') {
    console.log('더보기를 클릭하여 Drama 태그 상세 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 Drama 태그 상세 페이지로 이동 되지 않았습니다.');
  }

  await page.close();
});


test('탭 별 검색결과 없음과 신작랭킹 페이지 노출_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ㅁㄴㅇ ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);

  const empty_1 = await page.waitForSelector('.result__countAll'); //  클래스에서 요소 가져오기
  const text_1 = await empty_1.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_1 변수에 저장
  expect(text_1).toBe("0건"); //text_1에 저장된 텍스트와 실제 노출 문구 비교
  const empty_2 = await page.waitForSelector('.result__emptyMsg1'); //  클래스에서 요소 가져오기
  const text_2 = await empty_2.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_2 변수에 저장
  expect(text_2).toBe("검색결과가 없습니다."); 
  const empty_3 = await page.waitForSelector('.result__emptyMsg2'); //  클래스에서 요소 가져오기
  const text_3 = await empty_3.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_3 변수에 저장
  expect(text_3).toBe("검색어가 정확한지 다시 한 번 확인해주세요."); 

  const selectedElement_all = await page.waitForSelector('button[data-search-type="all"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 전체탭 강조효과
  const ariaSelectedValue_all = await selectedElement_all.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_all).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('전체 탭 검색결과 없음 UI 확인 결과'); 
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '작품' }).click();
  const selectedElement_title = await page.waitForSelector('button[data-search-type="title"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue_title = await selectedElement_title.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_title).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('작품 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '작가' }).click();
  const selectedElement_artist = await page.waitForSelector('button[data-search-type="artist"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue_artist = await selectedElement_artist.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_artist).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교
  

  console.log('작가 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '출판사' }).click();
  const selectedElement_publisher = await page.waitForSelector('button[data-search-type="publisher"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 출판사탭 강조효과
  const ariaSelectedValue_publisher = await selectedElement_publisher.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_publisher).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('출판사 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '태그' }).click();
  const selectedElement_tag = await page.waitForSelector('button[data-search-type="tag"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 태그탭 강조효과
  const ariaSelectedValue_tag = await selectedElement_tag.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_tag).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('태그 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  const new_ranking = await page.waitForSelector('#rank-new'); //  클래스에서 요소 가져오기
  const isVisible = await new_ranking.isVisible(); //해당 요소의 노출 값을 isVisible에 저장
  expect(isVisible).toBe(true); // 신작 랭킹 요소가 노출되는지 검증

  if (isVisible) {
    console.log('신작 랭킹이 노출 됩니다.');
  } else {
    console.log('신작 랭킹이 노출 되지 않습니다.');
  }

  console.log();
  const searchListItemsCount = await page.$$eval('.lzComic__list li', (elements) => elements.length); //신작 랭킹 작품 갯수를 searchListItemsCount에 저장
  expect(searchListItemsCount).toBe(6); //searchListItemsCount과 실제 노출되어야할 작품 갯수 비교
  console.log('신작랭킹 작품 갯수 :', searchListItemsCount);
  console.log();


  if (searchListItemsCount == 6) {
    console.log('신작랭킹 작품 갯수 6 개 확인 완료');
  } else {
    console.log('작품 갯수에 오류가 있습니다.');
  }

  await page.close();

});

test('탭 별 검색결과 없음과 신작랭킹 페이지 노출_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ㅁㄴㅇ ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);

  const empty_1 = await page.waitForSelector('.result__countAll'); //  클래스에서 요소 가져오기
  const text_1 = await empty_1.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_1 변수에 저장
  expect(text_1).toBe("0件"); //text_1에 저장된 텍스트와 실제 노출 문구 비교
  const empty_2 = await page.waitForSelector('.result__emptyMsg1'); //  클래스에서 요소 가져오기
  const text_2 = await empty_2.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_2 변수에 저장
  expect(text_2).toBe("検索結果がありません。"); 
  const empty_3 = await page.waitForSelector('.result__emptyMsg2'); //  클래스에서 요소 가져오기
  const text_3 = await empty_3.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_3 변수에 저장
  expect(text_3).toBe("入力情報をご確認のうえ、もう一度お試しください。"); 

  const selectedElement_all = await page.waitForSelector('button[data-search-type="all"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 전체탭 강조효과
  const ariaSelectedValue_all = await selectedElement_all.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_all).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('전체 탭 검색결과 없음 UI 확인 결과'); 
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '作品' }).click();
  const selectedElement_title = await page.waitForSelector('button[data-search-type="title"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue_title = await selectedElement_title.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_title).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('작품 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '作家' }).click();
  const selectedElement_artist = await page.waitForSelector('button[data-search-type="artist"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue_artist = await selectedElement_artist.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_artist).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교
  

  console.log('작가 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '出版社' }).click();
  const selectedElement_publisher = await page.waitForSelector('button[data-search-type="publisher"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 출판사탭 강조효과
  const ariaSelectedValue_publisher = await selectedElement_publisher.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_publisher).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('출판사 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: 'タグ' }).click();
  const selectedElement_tag = await page.waitForSelector('button[data-search-type="tag"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 태그탭 강조효과
  const ariaSelectedValue_tag = await selectedElement_tag.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_tag).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('태그 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  const new_ranking = await page.waitForSelector('#rank-new'); //  클래스에서 요소 가져오기
  const isVisible = await new_ranking.isVisible(); //해당 요소의 노출 값을 isVisible에 저장
  expect(isVisible).toBe(true); // 신작 랭킹 요소가 노출되는지 검증

  if (isVisible) {
    console.log('신작 랭킹이 노출 됩니다.');
  } else {
    console.log('신작 랭킹이 노출 되지 않습니다.');
  }

  console.log();
  const searchListItemsCount = await page.$$eval('.lzComic__list li', (elements) => elements.length); //신작 랭킹 작품 갯수를 searchListItemsCount에 저장
  expect(searchListItemsCount).toBe(6); //searchListItemsCount과 실제 노출되어야할 작품 갯수 비교
  console.log('신작랭킹 작품 갯수 :', searchListItemsCount);
  console.log();


  if (searchListItemsCount == 6) {
    console.log('신작랭킹 작품 갯수 6 개 확인 완료');
  } else {
    console.log('작품 갯수에 오류가 있습니다.');
  }

  await page.close();

});


test('탭 별 검색결과 없음과 신작랭킹 페이지 노출_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ㅁㄴㅇ ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);

  const empty_1 = await page.waitForSelector('.result__countAll'); //  클래스에서 요소 가져오기
  const text_1 = await empty_1.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_1 변수에 저장
  expect(text_1).toBe("0 Result"); //text_1에 저장된 텍스트와 실제 노출 문구 비교
  const empty_2 = await page.waitForSelector('.result__emptyMsg1'); //  클래스에서 요소 가져오기
  const text_2 = await empty_2.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_2 변수에 저장
  expect(text_2).toBe("No Results Found."); 
  const empty_3 = await page.waitForSelector('.result__emptyMsg2'); //  클래스에서 요소 가져오기
  const text_3 = await empty_3.evaluate((el) => el.textContent); //검색결과 없음 텍스트 문구를 text_3 변수에 저장
  expect(text_3).toBe("Please double-check if the search term is correct."); 

  const selectedElement_all = await page.waitForSelector('button[data-search-type="all"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 전체탭 강조효과
  const ariaSelectedValue_all = await selectedElement_all.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_all).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('전체 탭 검색결과 없음 UI 확인 결과'); 
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: 'Title' }).click();
  const selectedElement_title = await page.waitForSelector('button[data-search-type="title"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue_title = await selectedElement_title.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_title).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('작품 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: 'Writer' }).click();
  const selectedElement_artist = await page.waitForSelector('button[data-search-type="artist"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 작가탭 강조효과
  const ariaSelectedValue_artist = await selectedElement_artist.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_artist).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교
  

  console.log('작가 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: 'Publisher' }).click();
  const selectedElement_publisher = await page.waitForSelector('button[data-search-type="publisher"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 출판사탭 강조효과
  const ariaSelectedValue_publisher = await selectedElement_publisher.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_publisher).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('출판사 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: 'Tag' }).click();
  const selectedElement_tag = await page.waitForSelector('button[data-search-type="tag"][aria-selected="true"]'); // aria-selected="true 속성 가져오기 태그탭 강조효과
  const ariaSelectedValue_tag = await selectedElement_tag.getAttribute('aria-selected'); //ariaSelectedValue 변수에  aria-selected의 속성값 저장
  expect(ariaSelectedValue_tag).toBe("true"); //강조효과인 aria-selected의 속성값이 true인지 비교

  console.log('태그 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  const new_ranking = await page.waitForSelector('#rank-new'); //  클래스에서 요소 가져오기
  const isVisible = await new_ranking.isVisible(); //해당 요소의 노출 값을 isVisible에 저장
  expect(isVisible).toBe(true); // 신작 랭킹 요소가 노출되는지 검증

  if (isVisible) {
    console.log('신작 랭킹이 노출 됩니다.');
  } else {
    console.log('신작 랭킹이 노출 되지 않습니다.');
  }

  console.log();
  const searchListItemsCount = await page.$$eval('.lzComic__list li', (elements) => elements.length); //신작 랭킹 작품 갯수를 searchListItemsCount에 저장
  expect(searchListItemsCount).toBe(6); //searchListItemsCount과 실제 노출되어야할 작품 갯수 비교
  console.log('신작랭킹 작품 갯수 :', searchListItemsCount);
  console.log();


  if (searchListItemsCount == 6) {
    console.log('신작랭킹 작품 갯수 6 개 확인 완료');
  } else {
    console.log('작품 갯수에 오류가 있습니다.');
  }

  await page.close();

});

test('작가페이지를 통한 첫화보기 실행_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작가' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click();
  await page.waitForTimeout(1000);
  await page.locator('section').filter({ hasText: '던전 속 사정[개정판] [개정판] 해당 작품은 <던전 속 사정> 성인 버전의 일부 장면을 수정한 개정판입니다. 마물을 물리치고 얻게 되는 전리품' }).getByRole('link', { name: '첫 화 보기' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url(); //현재 접속 url을 currentUrl 저장
  expect(currentUrl).toBe("https://q-www.lezhin.com/ko/comic/dungeon_15/1"); // currentUrl에 저장된 url값과 실제 노출되어야할 url 값 비교
  if (currentUrl === 'https://q-www.lezhin.com/ko/comic/dungeon_15/1') {
    console.log('던전속 사정 첫화로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();
 
});

test('작가페이지를 통한 첫화보기 실행_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('YEHWON ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '作家' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click();
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '全体リスト表示' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url(); //현재 접속 url을 currentUrl 저장
  expect(currentUrl).toBe("https://q-www.lezhin.jp/ja/comic/okotowari"); // currentUrl에 저장된 url값과 실제 노출되어야할 url 값 비교
  if (currentUrl === 'https://q-www.lezhin.jp/ja/comic/okotowari') {
    console.log('男主人公は丁重にお断りします 첫화로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();
 
});

test('작가페이지를 통한 첫화보기 실행_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('SIMGUN ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: 'Writer' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click();
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: 'Start Reading' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url(); //현재 접속 url을 currentUrl 저장
  expect(currentUrl).toBe("https://q-www.lezhinus.com/en/comic/joseon_attorney/1"); // currentUrl에 저장된 url값과 실제 노출되어야할 url 값 비교
  if (currentUrl === 'https://q-www.lezhinus.com/en/comic/joseon_attorney/1') {
    console.log('Joseon Attorney 첫화로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();
 
});

test('작가페이지를 통한 전체 목록 보기 실행_kr', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작가' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click();
  await page.waitForTimeout(1000);
  await page.locator('section').filter({ hasText: '던전 속 사정[개정판] [개정판] 해당 작품은 <던전 속 사정> 성인 버전의 일부 장면을 수정한 개정판입니다. 마물을 물리치고 얻게 되는 전리품' }).getByRole('link', { name: '전체 목록 보기' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url(); //현재 접속 url을 currentUrl 저장
  expect(currentUrl).toBe("https://q-www.lezhin.com/ko/comic/dungeon_15"); // currentUrl에 저장된 url값과 실제 노출되어야할 url 값 비교
  if (currentUrl === 'https://q-www.lezhin.com/ko/comic/dungeon_15') {
    console.log('던전속 사정 에피소드 목록으로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();
 
});

test('작가페이지를 통한 전체 목록 보기 실행_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: '検索窓を開く' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('YEHWON ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '作家' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click();
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '全体リスト表示' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url(); //현재 접속 url을 currentUrl 저장
  expect(currentUrl).toBe("https://q-www.lezhin.jp/ja/comic/okotowari"); // currentUrl에 저장된 url값과 실제 노출되어야할 url 값 비교
  if (currentUrl === 'https://q-www.lezhin.jp/ja/comic/okotowari') {
    console.log('男主人公は丁重にお断りします 에피소드 목록으로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();
 
});

test('작가페이지를 통한 전체 목록 보기 실행_en', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Open Search Window' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('SIMGUN ');
  await page.waitForTimeout(1000);
  await page.click('.style_gnbSearch__inputGotoDetail__VeIbG');
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: 'Writer' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement?.click();
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: 'Episode List' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url(); //현재 접속 url을 currentUrl 저장
  expect(currentUrl).toBe("https://q-www.lezhinus.com/en/comic/joseon_attorney"); // currentUrl에 저장된 url값과 실제 노출되어야할 url 값 비교
  if (currentUrl === 'https://q-www.lezhinus.com/en/comic/joseon_attorney') {
    console.log('Joseon Attorney 에피소드 목록으로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  await page.close();
 
});