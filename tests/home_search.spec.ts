import { test, expect } from '@playwright/test';

test('전체 삭제', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바툰 ');
  await page.waitForTimeout(4000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.getByRole('link', { name: '레진코믹스' }).click();
  await page.waitForTimeout(4000);
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('button', { name: '전체 삭제' }).click();

  

   //전체 삭제 기능 확인
  const button = await page.getByRole('heading', { name: '최근 검색' });
  const isVisible = await button.isVisible(); 
  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }
});

test('인기 태그 상세 페이지 이동', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('link', { name: '#현대물' }).click();

  
   //전체 삭제 기능 확인
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);
   
   if (text_1.trim() === '#현대물') {
     console.log('#현대물 태그 상세페이지 이동 되었습니다.');
   } else {
     console.log('#현대물 태그 상세페이지 이동 되지 않았습니다.');
   }
});

test('검색 자동 완성', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('일상 ');
  await page.waitForTimeout(1000);

  

   //태그 자동완성 노출
   const element_1 = await page.getByRole('heading', { name: '태그' }); //  텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);
   
   if (text_1.trim() === '태그') {
     console.log('자동완성 태그 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 태그 영역이 노출 되지 않습니다.');
   }

   //작품 자동완성 노출
   
   //await page.getByRole('heading', { name: '작품' });
   const element_2 = await page.getByRole('heading', { name: '작품' });// 텍스트 가져오기
   const text_2 = await element_2.evaluate((el) => el.textContent);
   
   if (text_2.trim() === '작품') {
     console.log('자동완성 작품 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 작품 영역이 노출 되지 않습니다.');
   }
});


test('검색 후 태그 상세 페이지 이동', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('일상 ');
  await page.waitForTimeout(1000);
  
  const element_2 = await page.getByRole('link', { name: '#일상' }); // 텍스트 가져오기
  const text_2 = await element_2.evaluate((el) => el.textContent);
   
   if (text_2.trim() === '#일상') {
     console.log('검색한 태그가 노출 됩니다.');
   } else {
     console.log('검색한 태그가 노출되지 않았습니다.');
   }
   
  
  await page.getByRole('link', { name: '#일상' }).click();
   //태그 상세 페이지 이동 확인
   const element_1 = await page.waitForSelector('#tag-comic-heading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);
   
   if (text_1.trim() === '#일상') {
     console.log('#일상 태그 상세페이지 이동 되었습니다.');
   } else {
     console.log('#일상 태그 상세페이지 이동 되지 않았습니다.');
   }
});


test('최근 검색 태그 비노출', async ({ page }) => {
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


  const button = await page.getByRole('heading', { name: '최근 검색' });
  const isVisible = await button.isVisible(); 
  if (isVisible) {
    console.log('최근 검색이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('최근 검색이 노출 되지 않아 검증이 완료 되었습니다.');
  }
});


test('검색 갯수 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('DCW ');
  await page.waitForTimeout(1000);

  //검색결과 노출 갯수 체크
  const searchListItemsCount = await page.$$eval('.searchList li', (elements) => elements.length);
  console.log('.searchList 클래스에 포함된 li 태그의 개수:', searchListItemsCount);


  if (searchListItemsCount == 8) {
    console.log('검색 최대 갯수가 8개 확인 완료');
  } else if(searchListItemsCount > 8){
    console.log('검색 최대 갯수가 8개를 초과하여 오류 입니다.');
  } else {
    console.log('검색 최대 갯수개 8개 미만입니다 검색어를 확인하세요');
  }
  
});

test('비성인 계정 블라인드 작품', async ({ page }) => {
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


  //블라인드 이미지 노출
  try {
    const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 });
    console.log('블라인드 이미지 노출 확인 완료');
    // 이미지가 화면에 노출되었을 때 추가로 수행할 작업을 여기에 작성합니다.
  } catch (error) {
    console.log('이미지가 화면에 노출되지 않습니다.');
    // 이미지가 화면에 노출되지 않았을 때 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
});

test('비로그인 블라인드 작품', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('불륜  ');
  await page.waitForTimeout(1000);

  //블라인드 이미지 노출
  try {
    const imageElement = await page.waitForSelector('img[src="//ccdn.lezhin.com/files/assets/img/adult_thumbnail.png"]', { timeout: 4000 });
    console.log('블라인드 이미지 노출 확인 완료');
    // 이미지가 화면에 노출되었을 때 추가로 수행할 작업을 여기에 작성합니다.
  } catch (error) {
    console.log('이미지가 화면에 노출되지 않습니다.');
    // 이미지가 화면에 노출되지 않았을 때 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
});

test('성인 계정 성인작품 노출 19on', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_01@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  try {
    await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  } catch (error) {
    console.log('오늘 하루 안보기 버튼을 찾지 못하여 다음 스크립트를 실행합니다.');
  }
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('불륜  ');
  await page.waitForTimeout(1000);


  //블라인드 이미지 노출
  try {
    const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/5074329736642560/images/thumbnail.webp?updated=1690937569833&width=100"]', { timeout: 4000 });
    console.log('성인작품 이미지 노출 확인 완료');
    // 이미지가 화면에 노출되었을 때 추가로 수행할 작업을 여기에 작성합니다.
  } catch (error) {
    console.log('잘못된 이미지가 노출 됩니다.');
    // 이미지가 화면에 노출되지 않았을 때 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
});

test('성인 계정 성인작품 노출 19 Off', async ({ page }) => {
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

  try {
    await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  } catch (error) {
    console.log('오늘 하루 안보기 버튼을 찾지 못하여 다음 스크립트를 실행합니다.');
  }
 
  await page.waitForTimeout(2000);
  await page.getByRole('link', { name: '전연령으로 이동' }).click();
  await page.waitForTimeout(2000);
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('어쩌라go ');
  await page.waitForTimeout(1000);


  //블라인드 이미지 노출
  try {
    const imageElement = await page.waitForSelector('img[src="https://q-ccdn.lezhin.com/v2/comics/6207797588393984/images/thumbnail.webp?updated=1624598074730&width=100"]', { timeout: 4000 });
    console.log('성인작품 이미지 노출 확인 완료');
    // 이미지가 화면에 노출되었을 때 추가로 수행할 작업을 여기에 작성합니다.
  } catch (error) {
    console.log('잘못된 이미지가 노출 됩니다.');
    // 이미지가 화면에 노출되지 않았을 때 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
});

test('검색 > 에피소드 목록 이동', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('귀멸의 칼날  ');
  await page.waitForTimeout(1000);
  await page.getByRole('link', { name: '귀멸의 칼날 고토게 코요하루 / DCW' }).click();
  //await page.getByRole('button', { name: '변경하기' }).click();
  //블라인드 이미지 노출

  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.comicInfo__title'); // 요소 클래스에서 텍스트 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent);
  
  if (text_1.trim() === '귀멸의 칼날') {
    console.log('귀멸의 칼날 에피소드 목록으로 이동 되었습니다.');
  } else {
    console.log('귀멸의 칼날 에피소드 목록으로 이동 되지 않았습니다.');
  }
  
});

test('검색상세 작가리스트 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('망자카페 ');
  await page.waitForTimeout(1000);


  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.searchList__author'); // 요소 클래스에서 텍스트 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent);
  
  if (text_1.trim() === '베르디, 가나다, 라마바, 사아자, 하하하') {
    console.log('작가(글,그림,작가,원작,모델)이 노출됩니다.');
  } else {
    console.log('작가(글,그림,작가,원작,모델)이 노출되지 않습니다.');
  }
  
});

test('검색상세 출판사 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('망자카페 ');
  await page.waitForTimeout(1000);

  //에피소드 목록진입
  const element_1 = await page.waitForSelector('.searchList__publisher'); // 요소 클래스에서 텍스트 가져오기
  const text_1 = await element_1.evaluate((el) => el.textContent);
  
  if (text_1.trim() === '출판사1, 출판사2, 레이블') {
    console.log('출판사1, 출판사2, 레이블이 노출됩니다.');
  } else {
    console.log('출판사1, 출판사2, 레이블이 노출되지 않습니다.');
  }
  
});

test('검색 결과 페이지 전체탭 선택과 결과', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();

  const selectedElement = await page.waitForSelector('[aria-selected="true"]'); // aria-selected="true 속성 가져오기 (전체 탭 강조효과 처리)
  
  if (selectedElement) {
    console.log('전체탭이 선택되어 노출 됩니다.');
  } else {
    console.log('전체탭이 선택되지 않았습니다.');
  }

  const title = await page.waitForSelector('.lzComic__title'); // 요소 클래스에서 텍스트 가져오기
  const text_1 = await title.evaluate((el) => el.textContent);
  
  if (text_1.trim() === '레바툰') {
    console.log('작품 레바툰이 노출 됩니다.');
  } else {
    console.log('작품 레바툰이 노출되지 않습니다.');
  }

  const artist = await page.waitForSelector('.lzComic__artist'); // 요소 클래스에서 텍스트 가져오기
  const text_2 = await artist.evaluate((el) => el.textContent);
  
  if (text_2.trim() === '레바') {
    console.log('작가 레바가 노출 됩니다.');
  } else {
    console.log('작가 레바가 노출되지 않습니다.');
  }

  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByPlaceholder('작품, 작가, 출판사, 태그 검색').click();
  await page.getByPlaceholder('작품, 작가, 출판사, 태그 검색').fill('');
  const searchInput2 = await page.waitForSelector('#search-input');
  await searchInput2.type('일상 ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();

  const tag = await page.waitForSelector('.lzComic__tags'); // 요소 클래스에서 텍스트 가져오기
  const text_3 = await tag.evaluate((el) => el.textContent);
  
  if (text_3.trim() === '#일상 #드라마1 #음식') {
    console.log('태그 일상이 노출 됩니다.');
  } else {
    console.log('태그 일상이 노출되지 않습니다.');
  }

  const text_5 = await page.$eval('li.lzComic__item[data-id="161"] .lzComic__genre', (element) => element.textContent);
  
  if (text_5.trim() === '일상') {
    console.log('일상 장르가 노출 됩니다.');
  } else {
    console.log('일상 장르가 노출 노출되지 않습니다.');
  }

});

test('검색 결과 페이지 작품탭 결과', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작품' }).click();


  const selectedElement = await page.waitForSelector('[aria-selected="true"]'); // aria-selected="true 속성 가져오기 전체탭 강조효과
  
  if (selectedElement) {
    console.log('작품탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작품탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-title'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em');

  if (emElement) {
    console.log('레바 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('레바 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

});

test('검색 결과 페이지 작가탭 결과 및 더보기 클릭', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작가' }).click();


  const selectedElement = await page.waitForSelector('[aria-selected="true"]'); // aria-selected="true 속성 가져오기 전체탭 강조효과
  
  if (selectedElement) {
    console.log('작가탭이 선택되어 노출 됩니다.');
  } else {
    console.log('작가탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-artist'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em');

  if (emElement) {
    console.log('레바 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('레바 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');

  await lzComicMoreElement.click();
  
  const artist = await page.waitForSelector('#artist-heading'); // 요소 클래스에서 텍스트 가져오기
  const text = await artist.evaluate((el) => el.textContent);
  
  if (text.trim() === '레바님의 작품') {
    console.log('더보기를 클릭하여 레바 작가 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 레바 작가 페이지로 이동 되지 않았습니다.');
  }
});
test('검색 결과 페이지 출판사 결과 및 더보기 클릭', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('DCW ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '출판사' }).click();


  const selectedElement = await page.waitForSelector('[aria-selected="true"]'); // aria-selected="true 속성 가져오기 전체탭 강조효과
  
  if (selectedElement) {
    console.log('출판사탭이 선택되어 노출 됩니다.');
  } else {
    console.log('출판사탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-publisher'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em');

  if (emElement) {
    console.log('DCW 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('DCW 키워드에 강조효과가 적용되어 있지 않습니다.');
    await page.goto('https://q-www.lezhin.com/ko/search?t=publisher&q=DCW');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }

  const publisherElement = await page.waitForSelector('#search-section-publisher');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');

  // 클릭하여 동작 수행
  await lzComicMoreElement.click();

  const artist = await page.waitForSelector('#artist-heading'); // 요소 클래스에서 텍스트 가져오기
  const text = await artist.evaluate((el) => el.textContent);
  
  if (text.trim() === 'DCW님의 작품') {
    console.log('더보기를 클릭하여 DCW 출판사 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 DCW 출판사 상세 페이지로 이동 되지 않았습니다.');
  }
});

test('검색 결과 페이지 태그 결과 및 더보기 클릭', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('일상 ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '태그' }).click();


  const selectedElement = await page.waitForSelector('[aria-selected="true"]'); // aria-selected="true 속성 가져오기 전체탭 강조효과
  
  if (selectedElement) {
    console.log('태그탭이 선택되어 노출 됩니다.');
  } else {
    console.log('태그탭이 선택되지 않았습니다.');
  }

  const titleElement = await page.waitForSelector('#search-section-tag'); // 검사하려는 특정 요소의 선택자를 사용합니다.
  const emElement = await titleElement.$('em');

  if (emElement) {
    console.log('일상 키워드에 강조효과가 적용되어 노출 됩니다.');
    // 특정 텍스트에 em 태그가 적용된 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('일상 키워드에 강조효과가 적용되어 있지 않습니다.');
    // 특정 텍스트에 em 태그가 적용되지 않은 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
  
  await page.locator('div').filter({ hasText: '#일상 422 매일매일무료 솔로가 하는 연애 신매 로맨스 #일상 #옴니버스 #썸 먹는 존재 들개이빨 일상 #일상 #드라마화 #우정 34세 무직씨' }).getByRole('link', { name: '더보기' }).click();

  const artist = await page.waitForSelector('#tag-comic-heading'); // 요소 클래스에서 텍스트 가져오기
  const text = await artist.evaluate((el) => el.textContent);
  
  if (text.trim() === '#일상') {
    console.log('더보기를 클릭하여 일상 태그 상세 페이지로 이동 되었습니다.');
  } else {
    console.log('더보기를 클릭하여 일상 태그 상세 페이지로 이동 되지 않았습니다.');
  }
});

test('탭 별 검색결과 없음과 신작랭킹 페이지 노출', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('ㅁㄴㅇ ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.waitForTimeout(1000);

  const empty_1 = await page.waitForSelector('.result__countAll'); // 요소 클래스에서 텍스트 가져오기
  const text_1 = await empty_1.evaluate((el) => el.textContent);
  const empty_2 = await page.waitForSelector('.result__emptyMsg1'); // 요소 클래스에서 텍스트 가져오기
  const text_2 = await empty_2.evaluate((el) => el.textContent);
  const empty_3 = await page.waitForSelector('.result__emptyMsg2'); // 요소 클래스에서 텍스트 가져오기
  const text_3 = await empty_3.evaluate((el) => el.textContent);

  console.log('전체 탭 검색결과 없음 UI 확인 결과'); 
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '작품' }).click();

  console.log('작품 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '작가' }).click();

  console.log('작가 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '출판사' }).click();

  console.log('출판사 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  await page.waitForTimeout(1000);

  await page.getByRole('tab', { name: '태그' }).click();

  console.log('태그 탭 검색결과 없음 UI 확인 결과');
  console.log('검색건수 : ',text_1);
  console.log('안내문구 1 : ',text_2);
  console.log('안내문구 2 : ',text_3);
  console.log();

  const new_ranking = await page.waitForSelector('#rank-new'); // 요소 클래스에서 텍스트 가져오기
  const isVisible = await new_ranking.isVisible(); 

  if (isVisible) {
    console.log('신작 랭킹이 노출 됩니다.');
  } else {
    console.log('신작 랭킹이 노출 되지 않습니다.');
  }

  console.log();
  const searchListItemsCount = await page.$$eval('.lzComic__list li', (elements) => elements.length);
  console.log('신작랭킹 작품 갯수 :', searchListItemsCount);
  console.log();


  if (searchListItemsCount == 6) {
    console.log('신작랭킹 작품 갯수 6 개 확인 완료');
  } else {
    console.log('작품 갯수에 오류가 있습니다.');
  }

});

test('작가페이지를 통한 첫화보기 실행', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작가' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement.click();
  await page.waitForTimeout(1000);
  await page.locator('section').filter({ hasText: '던전 속 사정[개정판] 판타지 [개정판] 해당 작품은 <던전 속 사정> 성인 버전의 일부 장면을 수정한 개정판입니다. 마물을 물리치고 얻게 되는' }).getByRole('link', { name: '첫 화 보기' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url();
  if (currentUrl === 'https://q-www.lezhin.com/ko/comic/dungeon_15/1') {
    console.log('던전속 사정 첫화로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
 
});

test('작가페이지를 통한 전체 목록 보기 실행', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  const searchInput = await page.waitForSelector('#search-input');
  await searchInput.type('레바 ');
  await page.waitForTimeout(1000);
  await page.getByRole('button', { name: '검색하기' }).click();
  await page.waitForTimeout(1000);
  await page.getByRole('tab', { name: '작가' }).click();
  const publisherElement = await page.waitForSelector('#search-section-artist');
  const lzComicMoreElement = await publisherElement.$('.lzComic__more');
  await lzComicMoreElement.click();
  await page.waitForTimeout(1000);
  await page.locator('section').filter({ hasText: '던전 속 사정[개정판] 판타지 [개정판] 해당 작품은 <던전 속 사정> 성인 버전의 일부 장면을 수정한 개정판입니다. 마물을 물리치고 얻게 되는' }).getByRole('link', { name: '전체 목록 보기' }).click();
  await page.waitForTimeout(1000);
  
  const currentUrl = await page.url();
  if (currentUrl === 'https://q-www.lezhin.com/ko/comic/dungeon_15') {
    console.log('던전속 사정 에피소드 목록으로 이동되었습니다.');
    // URL이 일치하는 경우 추가로 수행할 작업을 여기에 작성합니다.
  } else {
    console.log('오류 입니다.');
    // URL이 일치하지 않는 경우 다른 동작을 수행할 작업을 여기에 작성합니다.
  }
 
});