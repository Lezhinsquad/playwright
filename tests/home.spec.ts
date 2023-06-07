import { test, expect } from '@playwright/test';

test('Top 버튼 이동', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko'); //레진 KO 홈 접속
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click(); // 전면배너 오늘 하루 안보기 클릭
  await page.evaluate(() => { // Top 이동 버튼 노출 되는 위치로 스크롤 내리기
      window.scrollBy(0, 1000);
    });
  await page.getByRole('button', { name: '맨 위로' }).click(); //탑 이동 버튼 클릭
});