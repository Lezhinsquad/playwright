import { test, expect } from '@playwright/test';

test('Top 버튼 이동', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko'); //레진 KO 홈 접속
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click(); // 전면배너 오늘 하루 안보기 클릭
  await page.evaluate(() => { // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
      window.scrollBy(0, 1000);
    });
  
 /* await page.getByRole('button', { name: '맨 위로' }).click(); //탑 이동 버튼 클릭*/
  
  // 최상단으로 이동하여 노출되는 컴포넌트 취향 설정 하기 확인
  const titleElement = await page.getByRole('button', { name: '취향 설정 하기' }); // 취향설정하기 텍스트를 포함하고있는 p 태그 확인
  if (titleElement) {
    const titleText = await titleElement.innerText(); // 
    if (titleText === '취향 설정 하기') {
      console.log('취향 설정 하기 텍스트를 찾을 수 없습니다. 스크립트를 확인하세요');
    } else {
      console.log('취향 설정 하기 텍스트를 찾아 검증이 완료 되었습니다.');
    }
  } else {
    console.log('취향 설정하기 텍스트 요소가 없습니다.');
  }
 
  /*
  //화면 최상단으로 이동하여 Top 이동 버튼 비노출 검증
  const button = await page.getByRole('button', { name: '맨 위로' });
  if (button) {
    button.isVisible;
    console.log('버튼이 노출 되지 않아 검증이 완료 되었습니다.');
  } else {
    console.log('top 이동 버튼이 노출 됩니다. 스크립트를 확인하세요');

  }
*/
  
});