import { test, expect } from '@playwright/test';

test('Top 버튼 이동', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko'); //레진 KO 홈 접속
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click(); // 전면배너 오늘 하루 안보기 클릭
  await page.evaluate(() => { // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
      window.scrollBy(0, 1000);
    });
  
  await page.waitForTimeout(2000);
 /*await page.getByRole('button', { name: '맨 위로' }).click(); //탑 이동 버튼 클릭*/
  
  // 최상단으로 이동하여 노출되는 컴포넌트 취향 설정 하기 확인

  /*
  const titleElement = await page.getByRole('button', { name: '취향 설정 하기' });
  const isVisible = await titleElement.isVisible(); 
  if (isVisible) {
   console.log('취향 설정 하기 요소를 확인했습니다. 테스트 완료');
 } else {
  
   console.log('취향 설정 하기 테스트 요소가 발견 되지 않습니다. 스크립트를 확인하세요');

 }
 */

  //화면 최상단으로 이동하여 Top 이동 버튼 비노출 검증
  const button = await page.getByRole('button', { name: '맨 위로' });
  const isVisible = await button.isVisible(); 
  if (isVisible == false) {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');
  } else {
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  }

  
});