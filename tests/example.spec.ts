import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/레진코믹스/);
});

test('get started link', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  // Click the get started link.
  await page.getByRole('link', { name: 'Get started' }).click();

  // Expects the URL to contain intro.
  await expect(page).toHaveURL(/.*intro/);
});

test('연습하기', async ({ page }) => {
  
  await page.goto('https://example.com');

  // 버튼 요소 존재 여부 확인
  const button = await page.$('#myButton');
  if (!button) {
    console.log('Button is not found.');
  } else {
    // 버튼 요소의 속성 검증
    const isHidden = await page.evaluate((btn) => {
      const styles = getComputedStyle(btn);
      return styles.display === 'none' || styles.visibility === 'hidden' || styles.opacity === '0';
    }, button);

    if (isHidden) {
      console.log('Button is not visible.');
    } else {
      console.log('Button is visible.');
    }
  }

  



});
