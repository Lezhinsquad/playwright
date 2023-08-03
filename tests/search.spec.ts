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

test('검색 자동완성', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '검색창 열기' }).click();
  await page.getByRole('link', { name: '일상' }).click();

  
   //전체 삭제 기능 확인
   //태그 자동완성 노출
   const element_1 = await page.waitForSelector('.search__subHeading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);
   
   if (text_1.trim() === '태그') {
     console.log('자동완성 태그 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 태그 영역이 노출 되지 않습니다.');
   }

   //작품 자동완성 노출
   const element_1 = await page.waitForSelector('.search__subHeading'); // 요소 id에서 텍스트 가져오기
   const text_1 = await element_1.evaluate((el) => el.textContent);
   
   if (text_1.trim() === '작품') {
     console.log('자동완성 작품 영역이 노출 됩니다.');
   } else {
     console.log('자동완성 작품  영역이 노출 되지 않습니다.');
   }
});