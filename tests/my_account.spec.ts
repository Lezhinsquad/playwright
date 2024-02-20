import { test, expect } from '@playwright/test';

test('이메일 로그인 정보 필드 확인', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_01@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();

  
  await page.setDefaultTimeout(2000);
  const emailElement = await page.waitForSelector('dd.email');  // 요소를 선택하는 적절한 셀렉터를 사용합니다.
  const emailText = await emailElement.textContent();
  expect(emailText).toBe("squad_01@yopmail.com"); // dtText에 저장된 텍스트 값과 실제 노출되어야할 텍스트 값 비교
  console.log('로그인된 이메일 계정', emailText);
  console.log();

  const AccountManagement = await page.waitForSelector('#change-password-btn'); // 비밀번호 변경 버튼 요소 얻기
  expect(AccountManagement).toBeTruthy; // 비밀번호 변경 버튼 노출 유무 확인


  if (AccountManagement) {
    console.log('비밀번호 변경 버튼이 노출 됩니다.');
  } else {
    console.log('비밀번호 변경 버튼이 노출 되지 않습니다.');
  }
  console.log();

  const Locale_change = await page.waitForSelector('#change-locale-btn'); //언어/국가 변경 버튼 요소 얻기
  expect(Locale_change).toBeTruthy; // 언어/국가 설정 버튼 노출 유무 확인
  if (Locale_change) {
    console.log('언어/국가 변경 버튼이 노출 됩니다.');
  } else {
    console.log('언어/국가 변경 버튼이 노출 되지 않습니다.');
  }

  console.log();
 

});

test('카카오 SNS 로그인 정보 필드 확인_kr', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.com/ko')
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('button', { name: '카카오로 로그인' }).click();
  //카카오 계정 로그인 
  await page.getByPlaceholder('KakaoMail ID, email, phone number').click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In', exact: true }).click();
  await page.waitForNavigation({ waitUntil: 'load' });
  
  //레진 회원가입 Flow

  await page.getByText('전체동의').click();
  await page.getByText('만 14세 이상입니다.(필수)').click();
  await page.getByRole('button', { name: '동의' }).click();
  await page.getByRole('link', { name: '확인' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  
  const dtText = await page.$eval('dt', (element) => element.textContent);
  expect(dtText).toBe("카카오"); // dtText에 저장된 텍스트 값과 실제 노출되어야할 텍스트 값 비교
  console.log('로그인 된 SNS 계정 타입:', dtText);
  console.log();

  const AccountManagement = await page.waitForSelector('#connect-email-btn'); // 비밀번호 설정 버튼 요소 얻기
  expect(AccountManagement).toBeTruthy; // 비밀번호 설정 버튼 노출 유무 확인


  if (AccountManagement) {
    console.log('비밀번호 설정 버튼이 노출 됩니다.');
  } else {
    console.log('비밀번호 설정 버튼이 노출 되지 않습니다.');
  }
  console.log();

  const Locale_change = await page.waitForSelector('#change-locale-btn'); //언어/국가 변경 버튼 요소 얻기
  expect(Locale_change).toBeTruthy; // 언어/국가 설정 버튼 노출 유무 확인
  if (Locale_change) {
    console.log('언어/국가 변경 버튼이 노출 됩니다.');
  } else {
    console.log('언어/국가 변경 버튼이 노출 되지 않습니다.');
  }

  console.log();

  const phonenumber = await page.getByText('01089917088'); //인증된 번화번호 요소 얻기
  expect(phonenumber).toBeTruthy; //전화번호  노출 유무 확인
  if (phonenumber) {
    console.log('카카오 회원가입 시 인증된 전화번호 01089917088이 정상 노출됩니다.');
  } else {
    console.log('휴대폰 번호가 잘못 노출되거나 노출되지 않습니다.');
  }
  await page.click('#toggle-unregister-form');
  await page.getByText('이용이 불편하고 장애가 많음').click();
  await page.getByRole('button', { name: '탈퇴하기' }).click();
  await page.getByRole('button', { name: '확인' }).click();
  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();

});

test('네이버 SNS 로그인 정보 필드 확인_kr', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.com/ko')
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();

  //네이버 계정 로그인 
  await page.getByRole('button', { name: '네이버로 로그인' }).click();
  await page.getByPlaceholder('Username').click();
  await page.getByPlaceholder('Username').fill('hidelove999');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('cogus7qwe!@#');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.waitForLoadState('load');

  //레진 회원가입 Flow
  await page.getByText('전체동의').click();
  await page.getByText('만 14세 이상입니다.(필수)').click();
  await page.getByRole('button', { name: '동의' }).click();
  await page.getByRole('link', { name: '확인' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  
  const dtText = await page.$eval('dt', (element) => element.textContent);
  expect(dtText).toBe("네이버"); // dtText에 저장된 텍스트 값과 실제 노출되어야할 텍스트 값 비교
  console.log('로그인 된 SNS 계정 타입:', dtText);
  console.log();

  const AccountManagement = await page.waitForSelector('#connect-email-btn'); // 비밀번호 설정 버튼 요소 얻기
  expect(AccountManagement).toBeTruthy; // 비밀번호 설정 버튼 노출 유무 확인


  if (AccountManagement) {
    console.log('비밀번호 설정 버튼이 노출 됩니다.');
  } else {
    console.log('비밀번호 설정 버튼이 노출 되지 않습니다.');
  }
  console.log();

  const Locale_change = await page.waitForSelector('#change-locale-btn'); //언어/국가 변경 버튼 요소 얻기
  expect(Locale_change).toBeTruthy; // 언어/국가 설정 버튼 노출 유무 확인
  if (Locale_change) {
    console.log('언어/국가 변경 버튼이 노출 됩니다.');
  } else {
    console.log('언어/국가 변경 버튼이 노출 되지 않습니다.');
  }

  console.log();


  await page.click('#toggle-unregister-form');
  await page.getByText('이용이 불편하고 장애가 많음').click();
  await page.getByRole('button', { name: '탈퇴하기' }).click();
  await page.getByRole('button', { name: '확인' }).click();
  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();

});



test('라인 SNS 로그인 정보 필드 확인_jp', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('button', { name: 'LINEでログイン' }).click();
  //라인 로그인
  await page.locator('div').filter({ hasText: /^Email address$/ }).click();
  await page.locator('input[name="tid"]').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.locator('input[name="tpasswd"]').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In' }).click();
  await page.waitForLoadState('load');
  //레진 회원가입 Flow
  //await page.getByRole('button', { name: 'Allow' }).click();
  //await page.getByRole('button', { name: 'Back' }).click();
  await page.getByText('全ての規約に同意する').click();
  await page.getByRole('button', { name: '同意' }).click();
  await page.waitForLoadState('load');
  //await page.goto('https://q-www.lezhin.jp/ja/welcome/line?redirect=%2Fja');
  await page.getByRole('link', { name: 'レジンコミックス' }).click();
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();

  const dtText = await page.$eval('dt', (element) => element.textContent);
  expect(dtText).toBe("LINE"); // dtText에 저장된 텍스트 값과 실제 노출되어야할 텍스트 값 비교
  console.log('로그인 된 SNS 계정 타입:', dtText);
  console.log();

  const AccountManagement = await page.waitForSelector('#connect-email-btn'); // 비밀번호 설정 버튼 요소 얻기
  expect(AccountManagement).toBeTruthy; // 비밀번호 설정 버튼 노출 유무 확인


  if (AccountManagement) {
    console.log('비밀번호 설정 버튼이 노출 됩니다.');
  } else {
    console.log('비밀번호 설정 버튼이 노출 되지 않습니다.');
  }
  console.log();

  const Locale_change = await page.waitForSelector('#change-locale-btn'); //언어/국가 변경 버튼 요소 얻기
  expect(Locale_change).toBeTruthy; // 언어/국가 설정 버튼 노출 유무 확인
  if (Locale_change) {
    console.log('언어/국가 변경 버튼이 노출 됩니다.');
  } else {
    console.log('언어/국가 변경 버튼이 노출 되지 않습니다.');
  }
  console.log();
  await page.click('#toggle-unregister-form');
  await page.getByText('使い勝手が悪く障害が多いため').click();
  await page.getByRole('button', { name: '退会する' }).click();
  await page.getByRole('button', { name: '確認' }).click();

  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();

});

/*test('야후 SNS 로그인 정보 필드 확인_jp', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('button', { name: 'Yahoo!でログイン' }).click();
  //야후 로그인
  await page.waitForLoadState('load');
  const handleInput = await page.waitForSelector('#login_handle');
  await handleInput.type('hidelove9999');
  // 버튼이 나타날 때까지 대기
  const nextButton = await page.waitForSelector('.ar-button_button_J2jv2 button');
  // 버튼 클릭
  await nextButton.click();
  const passwordInputSelector = 'input#password';  // 적절한 셀렉터로 수정하세요
  const passwordInput = await page.waitForSelector(passwordInputSelector);
  // 텍스트 입력
  await passwordInput.type('wlscogus7!@#'); // 'YourPassword'에는 실제 비밀번호를 입력하세요
  
  const loginButtonSelector = 'button[type="submit"]';
  const loginButton = await page.waitForSelector(loginButtonSelector);
  // 버튼 클릭
  await loginButton.click();



  /*
  await page.getByPlaceholder('ID/携帯電話番号/メールアドレス').click();
  await page.getByPlaceholder('ID/携帯電話番号/メールアドレス').fill('hidelove9999');
  await page.getByRole('button', { name: '次へ' }).click();
  await page.waitForLoadState('load');
  await page.getByPlaceholder('パスワード').click();
  await page.getByPlaceholder('パスワード').fill('wlscogus7!@#');
  await page.getByRole('button', { name: 'ログイン', exact: true }).click();
  //레진 회원가입 Flow
  await page.getByText('全ての規約に同意する').click();
  await page.getByRole('button', { name: '同意' }).click();
  await page.waitForLoadState('load');
  //await page.goto('https://q-www.lezhin.jp/ja/welcome/line?redirect=%2Fja');
  await page.getByRole('link', { name: 'レジンコミックス' }).click();
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();

  const dtText = await page.$eval('dt', (element) => element.textContent);
  expect(dtText).toBe("Yahoo"); // dtText에 저장된 텍스트 값과 실제 노출되어야할 텍스트 값 비교
  console.log('로그인 된 SNS 계정 타입:', dtText);
  console.log();

  const AccountManagement = await page.waitForSelector('#connect-email-btn'); // 비밀번호 설정 버튼 요소 얻기
  expect(AccountManagement).toBeTruthy; // 비밀번호 설정 버튼 노출 유무 확인


  if (AccountManagement) {
    console.log('비밀번호 설정 버튼이 노출 됩니다.');
  } else {
    console.log('비밀번호 설정 버튼이 노출 되지 않습니다.');
  }
  console.log();

  const Locale_change = await page.waitForSelector('#change-locale-btn'); //언어/국가 변경 버튼 요소 얻기
  expect(Locale_change).toBeTruthy; // 언어/국가 설정 버튼 노출 유무 확인
  if (Locale_change) {
    console.log('언어/국가 변경 버튼이 노출 됩니다.');
  } else {
    console.log('언어/국가 변경 버튼이 노출 되지 않습니다.');
  }
  console.log();

  await page.click('#toggle-unregister-form');
  await page.getByText('使い勝手が悪く障害が多いため').click();
  await page.getByRole('button', { name: '退会する' }).click();
  await page.getByRole('button', { name: '確認' }).click();

  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();

});
*/



test('페이스북 SNS 로그인 정보 필드 확인_US', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhinus.com/en')
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('button', { name: 'Login with Facebook' }).click();
  //페이스북 로그인
  await page.getByPlaceholder('Email or phone number').click();
  await page.getByPlaceholder('Email or phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7!@#');
  await page.getByRole('button', { name: 'Log In' }).click();
  await page.waitForLoadState('load');
  //레진 회원가입 Flow 
  await page.getByText('Agree to the Lezhin Comics Terms of Use(required)').click();
  await page.getByRole('button', { name: 'Confirm' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('link', { name: 'OK' }).click();
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'My Account' }).click();
  

  const dtText = await page.$eval('dt', (element) => element.textContent);
  expect(dtText).toBe("Facebook"); // dtText에 저장된 텍스트 값과 실제 노출되어야할 텍스트 값 비교
  console.log('로그인 된 SNS 계정 타입:', dtText);
  console.log();

  const AccountManagement = await page.waitForSelector('#connect-email-btn'); // 비밀번호 설정 버튼 요소 얻기
  expect(AccountManagement).toBeTruthy; // 비밀번호 설정 버튼 노출 유무 확인

  if (AccountManagement) {
    console.log('비밀번호 설정 버튼이 노출 됩니다.');
  } else {
    console.log('비밀번호 설정 버튼이 노출 되지 않습니다.');
  }
  console.log();

  const Locale_change = await page.waitForSelector('#change-locale-btn'); //언어/국가 변경 버튼 요소 얻기
  expect(Locale_change).toBeTruthy; // 언어/국가 설정 버튼 노출 유무 확인
  if (Locale_change) {
    console.log('언어/국가 변경 버튼이 노출 됩니다.');
  } else {
    console.log('언어/국가 변경 버튼이 노출 되지 않습니다.');
  }
  console.log();

  await page.click('#toggle-unregister-form');
 await page.getByText('Difficult to use and too many errors').click();
 await page.getByRole('button', { name: 'Deactivate', exact: true }).click();
 await page.getByRole('button', { name: 'OK' }).click();
 await page.getByRole('link', { name: 'Home' }).click();

 await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();

});


test('트위터 SNS 로그인 정보 필드 확인_US', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhinus.com/en')
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('button', { name: 'Login with Twitter' }).click();
  //페이스북 로그인
  await page.getByPlaceholder('Username or email').click();
  await page.getByPlaceholder('Username or email').fill('hidelove999');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await page.waitForLoadState('load');
  /*
  await page.getByLabel('Phone, email, or username').click();
  await page.getByLabel('Phone, email, or username').fill('hidelove999@daum.net');
  await page.getByRole('button', { name: 'Next' }).click();
  await page.locator('label div').nth(3).click();
  await page.getByTestId('ocfEnterTextTextInput').fill('hidelove999');
  await page.getByTestId('ocfEnterTextNextButton').click();
  await page.getByLabel('Password', { exact: true }).click();
  await page.getByLabel('Password', { exact: true }).fill('wlscogus7!');
  await page.getByTestId('LoginForm_Login_Button').click();
  */
  //레진 회원가입 Flow 
  await page.getByText('Agree to the Lezhin Comics Terms of Use(required)').click();
  await page.getByRole('button', { name: 'Confirm' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('link', { name: 'OK' }).click();
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'My Account' }).click();
  

  const dtText = await page.$eval('dt', (element) => element.textContent);
  expect(dtText).toBe("Twitter"); // dtText에 저장된 텍스트 값과 실제 노출되어야할 텍스트 값 비교
  console.log('로그인 된 SNS 계정 타입:', dtText);
  console.log();

  const AccountManagement = await page.waitForSelector('#connect-email-btn'); // 비밀번호 설정 버튼 요소 얻기
  expect(AccountManagement).toBeTruthy; // 비밀번호 설정 버튼 노출 유무 확인

  if (AccountManagement) {
    console.log('비밀번호 설정 버튼이 노출 됩니다.');
  } else {
    console.log('비밀번호 설정 버튼이 노출 되지 않습니다.');
  }
  console.log();

  const Locale_change = await page.waitForSelector('#change-locale-btn'); //언어/국가 변경 버튼 요소 얻기
  expect(Locale_change).toBeTruthy; // 언어/국가 설정 버튼 노출 유무 확인
  if (Locale_change) {
    console.log('언어/국가 변경 버튼이 노출 됩니다.');
  } else {
    console.log('언어/국가 변경 버튼이 노출 되지 않습니다.');
  }
  console.log();
  await page.click('#toggle-unregister-form');
 await page.getByText('Difficult to use and too many errors').click();
 await page.getByRole('button', { name: 'Deactivate', exact: true }).click();
 await page.getByRole('button', { name: 'OK' }).click();
 await page.getByRole('link', { name: 'Home' }).click();

 await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');

  await page.close();

});






test('카카오 SNS 비밀번호 등록 과 연결해제, 로그인_kr', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.com/ko')
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('button', { name: '카카오로 로그인' }).click();
  // 카카오 로그인
  await page.getByPlaceholder('KakaoMail ID, email, phone number').click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In', exact: true }).click();
  //레진 회원가입 Flow  
  await page.waitForLoadState('load');
  await page.getByText('전체동의').click();
  await page.getByText('만 14세 이상입니다.(필수)').click();
  await page.getByRole('button', { name: '동의' }).click();
  await page.getByRole('link', { name: '확인' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  
  await page.getByRole('button', { name: '비밀번호 설정' }).click();
  await page.getByLabel('새 비밀번호', { exact: true }).click();
  await page.getByLabel('새 비밀번호', { exact: true }).fill('wlscogus7!');
  await page.getByLabel('새 비밀번호 재입력').click();
  await page.getByLabel('새 비밀번호 재입력').fill('wlscogus7!');
  await page.getByRole('button', { name: '저장' }).click();

  const email = await page.getByRole('tabpanel', { name: '계정 관리' }).getByText('hidelove999@naver.com'); //계정관리의 이메일 텍스트 요소 얻기
  expect(email).toBeTruthy; //연결된 이메일  노출 유무 확인
  //const button = await page.getByRole('link', { name: '내 정보' }).click();

  if (email) {
    console.log('SNS 계정 비밀번호 등록이 완료 되어 이메일로 로그인 가능합니다.');
  } else {
    console.log('SNS 계정 비밀번호 등록이 완료 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '연결 해제' }).click();
  await page.waitForLoadState('load');

  
  const kakao_link = await page.locator('div').filter({ hasText: '카카오 연결' }).getByRole('link', { name: '연결' });//카카오 연결하기 이메일 텍스트 요소 얻기
  expect(kakao_link).toBeTruthy; //카카오 연결 텍스트 노출 확인

  if (kakao_link) {
    console.log('카카오 연결이 해제 되었습니다.');
  } else {
    console.log('카카오 연결이 해제  되지 않았습니다.');
  }
  console.log();

  await page.waitForTimeout(2000);

  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '로그아웃' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('hidelove999@naver.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();

  const Locale_change = await page.waitForSelector('.userInfo__email'); //로그인된 이메일 주소 요소 얻기
  const text = await Locale_change.evaluate((el) => el.textContent); //Locale_change에서 설정된 텍스트 얻기
  expect(text).toBe("hidelove999@naver.com"); //카카오 연결 텍스트 노출 확인

  if (text === 'hidelove999@naver.com') {
    console.log('이메일 로그인이 완료 되었습니다.');
  } else {
    console.log('이메일 로그인이 완료  되지 않았습니다.');
  }
  console.log();
  await page.click('#toggle-unregister-form');
  await page.getByText('이용이 불편하고 장애가 많음').click();
  await page.getByPlaceholder('비밀번호를 입력해 주세요.').click();
  await page.getByPlaceholder('비밀번호를 입력해 주세요.').fill('wlscogus7!');
  await page.getByRole('button', { name: '탈퇴하기' }).click();
  await page.getByRole('button', { name: '확인' }).click();
  await page.waitForLoadState('load');
  
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();
});


test('네이버 SNS 비밀번호 등록 과 연결해제, 로그인_kr', async ({ page }) => {
  await page.setDefaultTimeout(120000);
  await page.goto('https://q-www.lezhin.com/ko')
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  //네이버 로그인
  await page.getByRole('button', { name: '네이버로 로그인' }).click();
  await page.getByPlaceholder('Username').click();
  await page.getByPlaceholder('Username').fill('hidelove999');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('cogus7qwe!@#');
  await page.getByRole('button', { name: 'Sign in' }).click();
  //레진 회원가입 Flow  
  await page.waitForLoadState('load');
  await page.getByText('전체동의').click();
  await page.getByText('만 14세 이상입니다.(필수)').click();
  await page.getByRole('button', { name: '동의' }).click();
  await page.getByRole('link', { name: '확인' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  
  await page.getByRole('button', { name: '비밀번호 설정' }).click();
  await page.getByLabel('새 비밀번호', { exact: true }).click();
  await page.getByLabel('새 비밀번호', { exact: true }).fill('wlscogus7!');
  await page.getByLabel('새 비밀번호 재입력').click();
  await page.getByLabel('새 비밀번호 재입력').fill('wlscogus7!');
  await page.getByRole('button', { name: '저장' }).click();

  const email = await page.getByRole('tabpanel', { name: '계정 관리' }).getByText('hidelove999@naver.com'); //계정관리의 이메일 텍스트 요소 얻기
  expect(email).toBeTruthy; //연결된 이메일  노출 유무 확인
  //const button = await page.getByRole('link', { name: '내 정보' }).click();

  if (email) {
    console.log('SNS 계정 비밀번호 등록이 완료 되어 이메일로 로그인 가능합니다.');
  } else {
    console.log('SNS 계정 비밀번호 등록이 완료 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '연결 해제' }).click();
  await page.waitForLoadState('load');

  
  const kakao_link = await page.locator('div').filter({ hasText: '네이버 연결' }).getByRole('link', { name: '연결' });//카카오 연결하기 이메일 텍스트 요소 얻기
  expect(kakao_link).toBeTruthy; //카카오 연결 텍스트 노출 확인

  if (kakao_link) {
    console.log('네이버 연결이 해제 되었습니다.');
  } else {
    console.log('네이버 연결이 해제  되지 않았습니다.');
  }
  console.log();
  await page.waitForTimeout(2000);

  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '로그아웃' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('hidelove999@naver.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();

  const Locale_change = await page.waitForSelector('.userInfo__email'); //로그인된 이메일 주소 요소 얻기
  const text = await Locale_change.evaluate((el) => el.textContent); //Locale_change에서 설정된 텍스트 얻기
  expect(text).toBe("hidelove999@naver.com"); //카카오 연결 텍스트 노출 확인

  if (text === 'hidelove999@naver.com') {
    console.log('이메일 로그인이 완료 되었습니다.');
  } else {
    console.log('이메일 로그인이 완료  되지 않았습니다.');
  }
  console.log();

  await page.click('#toggle-unregister-form');
  await page.getByText('이용이 불편하고 장애가 많음').click();
  await page.getByPlaceholder('비밀번호를 입력해 주세요.').click();
  await page.getByPlaceholder('비밀번호를 입력해 주세요.').fill('wlscogus7!');
  await page.getByRole('button', { name: '탈퇴하기' }).click();
  await page.getByRole('button', { name: '확인' }).click();
  
  //await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();
});





test('라인 SNS 비밀번호 등록 과 연결해제, 로그인_jp', async ({ page }) => {
  await page.setDefaultTimeout(80000);
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('button', { name: 'LINEでログイン' }).click();
  // 라인 로그인
  await page.locator('div').filter({ hasText: /^Email address$/ }).click();
  await page.locator('input[name="tid"]').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.locator('input[name="tpasswd"]').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In' }).click();
  //레진 회원가입 Flow  
  await page.getByText('全ての規約に同意する').click();
  await page.getByRole('button', { name: '同意' }).click();
  await page.waitForTimeout(3000);
  //await page.goto('https://q-www.lezhin.jp/ja/welcome/line?redirect=%2Fja');
  await page.getByRole('link', { name: '確認' }).click();
  await page.getByRole('link', { name: 'レジンコミックス' }).click();
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();
  await page.getByRole('button', { name: 'パスワード設定' }).click();
  await page.getByLabel('新しいパスワード', { exact: true }).click();
  await page.getByLabel('新しいパスワード', { exact: true }).fill('wlscogus7!');
  await page.getByLabel('新しいパスワード再入力').click();
  await page.getByLabel('新しいパスワード再入力').fill('wlscogus7!');
  await page.waitForTimeout(3000);
  await page.getByRole('button', { name: '保存' }).click();
  await page.waitForTimeout(3000);

  const email = await page.getByRole('tabpanel', { name: '会員情報' }).getByText('hidelove999@naver.com'); //계정관리의 이메일 텍스트 요소 얻기
  expect(email).toBeTruthy; //연결된 이메일  노출 유무 확인
  //const button = await page.getByRole('link', { name: '내 정보' }).click();

  if (email) {
    console.log('SNS 계정 비밀번호 등록이 완료 되어 이메일로 로그인 가능합니다.');
  } else {
    console.log('SNS 계정 비밀번호 등록이 완료 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '解除する' }).click();
  await page.waitForTimeout(3000);

  
  const kakao_link = await page.locator('div').filter({ hasText: 'LINE 連携する' }).getByRole('link', { name: '連携する' });//카카오 연결하기 이메일 텍스트 요소 얻기
  expect(kakao_link).toBeTruthy; //카카오 연결 텍스트 노출 확인

  if (kakao_link) {
    console.log('라인 연결이 해제 되었습니다.');
  } else {
    console.log('라인 연결이 해제  되지 않았습니다.');
  }
  console.log();

  //await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  //await page.getByRole('link', { name: 'ログアウト' }).click();
  await page.getByRole('button', { name: 'アカウントメニュー 10' }).click();
  await page.getByRole('link', { name: 'ログアウト' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('hidelove999@naver.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();

  const Locale_change = await page.waitForSelector('.userInfo__email'); //로그인된 이메일 주소 요소 얻기
  const text = await Locale_change.evaluate((el) => el.textContent); //Locale_change에서 설정된 텍스트 얻기
  expect(text).toBe("hidelove999@naver.com"); //라인 연결 텍스트 노출 확인

  if (text === 'hidelove999@naver.com') {
    console.log('이메일 로그인이 완료 되었습니다.');
  } else {
    console.log('이메일 로그인이 완료  되지 않았습니다.');
  }
  console.log();

  await page.click('#toggle-unregister-form');
  await page.getByText('使い勝手が悪く障害が多いため').click();
  await page.getByPlaceholder('パスワードを入力してください').click();
  await page.getByPlaceholder('パスワードを入力してください').fill('wlscogus7!');
  await page.getByRole('button', { name: '退会する' }).click();
  await page.getByRole('button', { name: '確認' }).click();
  await page.getByRole('link', { name: 'ホームに戻る' }).click();

  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();
});

/*test('야후 SNS 비밀번호 등록 과 연결해제, 로그인_jp', async ({ page }) => {
  await page.setDefaultTimeout(120000);
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('button', { name: 'Yahoo!でログイン' }).click();
  await page.waitForLoadState('load');
  //야후 로그인
  await page.getByPlaceholder('ID/携帯電話番号/メールアドレス').click();
  await page.getByPlaceholder('ID/携帯電話番号/メールアドレス').fill('hidelove9999');
  await page.getByRole('button', { name: '次へ' }).click();
  await page.waitForLoadState('load');
  await page.getByPlaceholder('パスワード').click();
  await page.getByPlaceholder('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'ログイン', exact: true }).click();
  //레진 회원가입 Flow  
  await page.getByText('全ての規約に同意する').click();
  await page.getByRole('button', { name: '同意' }).click();
  await page.waitForLoadState('load');
  //await page.goto('https://q-www.lezhin.jp/ja/welcome/line?redirect=%2Fja');
  await page.getByRole('link', { name: 'レジンコミックス' }).click();
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();
  await page.getByRole('button', { name: 'パスワード設定' }).click();
  await page.getByLabel('新しいパスワード', { exact: true }).click();
  await page.getByLabel('新しいパスワード', { exact: true }).fill('wlscogus7!');
  await page.getByLabel('新しいパスワード再入力').click();
  await page.getByLabel('新しいパスワード再入力').fill('wlscogus7!');
  await page.getByRole('button', { name: '保存' }).click();

  const email = await page.getByRole('tabpanel', { name: '会員情報' }).getByText('hidelove9999@yahoo.co.jp'); //계정관리의 이메일 텍스트 요소 얻기
  expect(email).toBeTruthy; //연결된 이메일  노출 유무 확인
  //const button = await page.getByRole('link', { name: '내 정보' }).click();

  if (email) {
    console.log('SNS 계정 비밀번호 등록이 완료 되어 이메일로 로그인 가능합니다.');
  } else {
    console.log('SNS 계정 비밀번호 등록이 완료 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '解除する' }).click();
  await page.waitForLoadState('load');

  
  const kakao_link = await page.locator('div').filter({ hasText: 'Yahoo 連携する' }).getByRole('link', { name: '連携する' });//카카오 연결하기 이메일 텍스트 요소 얻기
  expect(kakao_link).toBeTruthy; //카카오 연결 텍스트 노출 확인

  if (kakao_link) {
    console.log('야후 연결이 해제 되었습니다.');
  } else {
    console.log('야후 연결이 해제  되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'ログアウト' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('hidelove9999@yahoo.co.jp');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();

  const Locale_change = await page.waitForSelector('.userInfo__email'); //로그인된 이메일 주소 요소 얻기
  const text = await Locale_change.evaluate((el) => el.textContent); //Locale_change에서 설정된 텍스트 얻기
  expect(text).toBe("hidelove9999@yahoo.co.jp"); //라인 연결 텍스트 노출 확인

  if (text === 'hidelove9999@yahoo.co.jp') {
    console.log('이메일 로그인이 완료 되었습니다.');
  } else {
    console.log('이메일 로그인이 완료  되지 않았습니다.');
  }
  console.log();

  await page.click('#toggle-unregister-form');
  await page.getByText('使い勝手が悪く障害が多いため').click();
  await page.getByPlaceholder('パスワードを入力してください').click();
  await page.getByPlaceholder('パスワードを入力してください').fill('wlscogus7!');
  await page.getByRole('button', { name: '退会する' }).click();
  await page.getByRole('button', { name: '確認' }).click();
  await page.getByRole('link', { name: 'ホームに戻る' }).click();
  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();
});
*/



test('페이스북 SNS 비밀번호 등록 과 연결해제, 로그인_us', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('button', { name: 'Login with Facebook' }).click();
  //페이스북 로그인
  await page.getByPlaceholder('Email or phone number').click();
  await page.getByPlaceholder('Email or phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7!@#');
  await page.getByRole('button', { name: 'Log In' }).click();
  //레진 회원가입 Flow
  await page.getByText('Agree to the Lezhin Comics Terms of Use(required)').click();
  await page.getByRole('button', { name: 'Confirm' }).click();
  await page.getByRole('link', { name: 'OK' }).click();
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'My Account' }).click();
  await page.getByRole('button', { name: 'Password setting' }).click();
  await page.getByLabel('New password', { exact: true }).click();
  await page.getByLabel('New password', { exact: true }).fill('wlscogus7!');
  await page.getByLabel('Re-enter your password').click();
  await page.getByLabel('Re-enter your password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Save' }).click();

  const email = await page.getByRole('tabpanel', { name: 'My Account' }).getByText('hidelove999@naver.com'); //계정관리의 이메일 텍스트 요소 얻기
  expect(email).toBeTruthy; //연결된 이메일  노출 유무 확인
  //const button = await page.getByRole('link', { name: '내 정보' }).click();

  if (email) {
    console.log('SNS 계정 비밀번호 등록이 완료 되어 이메일로 로그인 가능합니다.');
  } else {
    console.log('SNS 계정 비밀번호 등록이 완료 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: 'Disconnect Account' }).click();
  await page.waitForLoadState('load');

  
  const kakao_link = await page.locator('div').filter({ hasText: 'Facebook Connect Account' }).getByRole('link', { name: 'Connect Account' });//페이스북  연결하기  텍스트 요소 얻기
  expect(kakao_link).toBeTruthy; //페이스북 연결 텍스트 노출 확인

  if (kakao_link) {
    console.log('페이스북 연결이 해제 되었습니다.');
  } else {
    console.log('페이스북 연결이 해제  되지 않았습니다.');
  }
  console.log();
  await page.waitForTimeout(2000);

  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Logout' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('hidelove999@naver.com');
  await page.getByLabel('Password').click();
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.getByRole('button', { name: 'Account Menu' }).click();

  const Locale_change = await page.waitForSelector('.userInfo__email'); //로그인된 이메일 주소 요소 얻기
  const text = await Locale_change.evaluate((el) => el.textContent); //Locale_change에서 설정된 텍스트 얻기
  expect(text).toBe("hidelove999@naver.com"); //라인 연결 텍스트 노출 확인

  if (text === 'hidelove999@naver.com') {
    console.log('이메일 로그인이 완료 되었습니다.');
  } else {
    console.log('이메일 로그인이 완료  되지 않았습니다.');
  }
  console.log();
  await page.click('#toggle-unregister-form');
  await page.getByText('Difficult to use and too many errors').click();
  await page.getByPlaceholder('Please enter your password').click();
  await page.getByPlaceholder('Please enter your password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Deactivate', exact: true }).click();
  await page.getByRole('button', { name: 'OK' }).click();
  await page.getByRole('link', { name: 'Home' }).click();

  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();
});

test('트위터 SNS 비밀번호 등록 과 연결해제, 로그인_us', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('button', { name: 'Login with Twitter' }).click();
  //트위터 로그인
  await page.getByPlaceholder('Username or email').click();
  await page.getByPlaceholder('Username or email').fill('hidelove999');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await page.waitForLoadState('load');

  
  /*
  await page.getByLabel('Phone, email, or username').click();
  await page.getByLabel('Phone, email, or username').fill('hidelove999@daum.net');
  await page.getByRole('button', { name: 'Next' }).click();
  await page.locator('label div').nth(3).click();
  await page.getByTestId('ocfEnterTextTextInput').fill('hidelove999');
  await page.getByTestId('ocfEnterTextNextButton').click();
  await page.getByLabel('Password', { exact: true }).click();
  await page.getByLabel('Password', { exact: true }).fill('wlscogus7!');
  await page.getByTestId('LoginForm_Login_Button').click();
  */
  //레진 회원가입 Flow  
  await page.getByText('Agree to the Lezhin Comics Terms of Use(required)').click();
  await page.getByRole('button', { name: 'Confirm' }).click();
  await page.getByRole('link', { name: 'OK' }).click();
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'My Account' }).click();


  await page.getByRole('button', { name: 'Password setting' }).click();
  await page.getByLabel('New password', { exact: true }).click();
  await page.getByLabel('New password', { exact: true }).fill('wlscogus7!');
  await page.getByLabel('Re-enter your password').click();
  await page.getByLabel('Re-enter your password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Save' }).click();

  const email = await page.getByRole('tabpanel', { name: 'My Account' }).getByText('hidelove999@daum.net'); //계정관리의 이메일 텍스트 요소 얻기
  expect(email).toBeTruthy; //연결된 이메일  노출 유무 확인
  //const button = await page.getByRole('link', { name: '내 정보' }).click();

  if (email) {
    console.log('SNS 계정 비밀번호 등록이 완료 되어 이메일로 로그인 가능합니다.');
  } else {
    console.log('SNS 계정 비밀번호 등록이 완료 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: 'Disconnect Account' }).click();
  await page.waitForLoadState('load');

  
  const kakao_link = await page.locator('div').filter({ hasText: 'Twitter Connect Account' }).getByRole('link', { name: 'Connect Account' });//페이스북  연결하기  텍스트 요소 얻기
  expect(kakao_link).toBeTruthy; //페이스북 연결 텍스트 노출 확인

  if (kakao_link) {
    console.log('트위터 연결이 해제 되었습니다.');
  } else {
    console.log('트위터 연결이 해제  되지 않았습니다.');
  }
  console.log();
  await page.waitForTimeout(2000);

  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Logout' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('hidelove999@daum.net');
  await page.getByLabel('Password').click();
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.getByRole('button', { name: 'Account Menu' }).click();

  const Locale_change = await page.waitForSelector('.userInfo__email'); //로그인된 이메일 주소 요소 얻기
  const text = await Locale_change.evaluate((el) => el.textContent); //Locale_change에서 설정된 텍스트 얻기
  expect(text).toBe("hidelove999@daum.net"); //라인 연결 텍스트 노출 확인

  if (text === 'hidelove999@daum.net') {
    console.log('이메일 로그인이 완료 되었습니다.');
  } else {
    console.log('이메일 로그인이 완료  되지 않았습니다.');
  }
  console.log();
  await page.click('#toggle-unregister-form');
  await page.getByText('Difficult to use and too many errors').click();
  await page.getByPlaceholder('Please enter your password').click();
  await page.getByPlaceholder('Please enter your password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Deactivate', exact: true }).click();
  await page.getByRole('button', { name: 'OK' }).click();
  await page.getByRole('link', { name: 'Home' }).click();

  await page.waitForLoadState('load');
  console.log('회원탈퇴가 완료 되었습니다.');
  await page.close();
});





//TC 133 , 146 수행 케이스
test('이메일 계정 로그인 , 카카오 연결,연결 해제_kr', async ({ page }) => {
   await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_01@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  //await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  await page.locator('div').filter({ hasText: '카카오 연결' }).getByRole('link', { name: '연결' }).click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In', exact: true }).click();
  await page.waitForLoadState('load');

  const kakao_connect = await page.waitForSelector('.oauth--disconnect');  //카카오 연결 끊기 버튼 요소 얻기
  const isVisible = await kakao_connect.isVisible(); //카카오 연결 끊기 노출 값 저장
  expect(isVisible).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible) {
    console.log('카카오 계정이 연결 되었습니다.');
  } else {
    console.log('카카오 계정이 연결 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '연결 해제' }).click();
  await page.waitForLoadState('load');

  const kakao_disconnect = await page.$('.myAccount__section'); //카카오 연결 버튼 요소 얻기
  const isVisible_2 = await kakao_disconnect?.isVisible(); //카카오 연결 노출 값 저장
  expect(isVisible_2).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible_2) {
    console.log('카카오 계정이 연결해제 되었습니다.');
  } else {
    console.log('카카오 계정이 연결해제 되지 않았습니다.');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();

});

test('이메일 계정 로그인 , 네이버 연결,연결 해제_kr', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_01@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  await page.locator('div').filter({ hasText: '네이버 연결' }).getByRole('link', { name: '연결' }).click();
  await page.getByPlaceholder('Username').click();
  await page.getByPlaceholder('Username').fill('hidelove999');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('cogus7qwe!@#');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.waitForLoadState('load');

  const kakao_connect = await page.waitForSelector('.oauth--disconnect');  //카카오 연결 끊기 버튼 요소 얻기
  const isVisible = await kakao_connect.isVisible(); //카카오 연결 끊기 노출 값 저장
  expect(isVisible).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible) {
    console.log('네이버 계정이 연결 되었습니다.');
  } else {
    console.log('네이버 계정이 연결 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '연결 해제' }).click();
  await page.waitForLoadState('load');

  const kakao_disconnect = await page.$('.myAccount__section'); //카카오 연결 버튼 요소 얻기
  const isVisible_2 = await kakao_disconnect?.isVisible(); //카카오 연결 노출 값 저장
  expect(isVisible_2).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible_2) {
    console.log('네이버 계정이 연결해제 되었습니다.');
  } else {
    console.log('네이버 계정이 연결해제 되지 않았습니다.');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();

});


test('이메일 계정 로그인 , 페이스북 연결,연결 해제_kr', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.com/ko');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '이메일로 로그인' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('squad_01@yopmail.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  await page.locator('div').filter({ hasText: '페이스북 연결' }).getByRole('link', { name: '연결' }).click();
  await page.getByPlaceholder('Email or phone number').click();
  await page.getByPlaceholder('Email or phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7!@#');
  await page.getByRole('button', { name: 'Log In' }).click();
  await page.waitForLoadState('load');

  const kakao_connect = await page.waitForSelector('.oauth--disconnect');  //카카오 연결 끊기 버튼 요소 얻기
  const isVisible = await kakao_connect.isVisible(); //카카오 연결 끊기 노출 값 저장
  expect(isVisible).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible) {
    console.log('페이스북 계정이 연결 되었습니다.');
  } else {
    console.log('페이스북 계정이 연결 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '연결 해제' }).click();
  await page.waitForLoadState('load');

  const kakao_disconnect = await page.$('.myAccount__section'); //카카오 연결 버튼 요소 얻기
  const isVisible_2 = await kakao_disconnect?.isVisible(); //카카오 연결 노출 값 저장
  expect(isVisible_2).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible_2) {
    console.log('페이스북 계정이 연결해제 되었습니다.');
  } else {
    console.log('페이스북 계정이 연결해제 되지 않았습니다.');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();

});



test('이메일 계정 로그인 , 라인 연결,연결 해제_ja', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad_01@yopmail.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();
  await page.locator('div').filter({ hasText: 'LINE 連携する' }).getByRole('link', { name: '連携する' }).click();
  await page.locator('div').filter({ hasText: /^Email address$/ }).click();
  await page.locator('input[name="tid"]').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.locator('input[name="tpasswd"]').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In' }).click();
  //await page.waitForLoadState('load');

  const kakao_connect = await page.waitForSelector('.oauth--disconnect');  //라인 연결 끊기 버튼 요소 얻기
  const isVisible = await kakao_connect.isVisible(); //라인 연결 끊기 노출 값 저장
  expect(isVisible).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible) {
    console.log('라인 계정이 연결 되었습니다.');
  } else {
    console.log('라인 계정이 연결 되지 않았습니다.');
  }
  console.log();
  await page.waitForTimeout(2000);

  await page.getByRole('button', { name: '解除する' }).click();
  //await page.waitForLoadState('load');

  const kakao_disconnect = await page.$('.myAccount__section'); //라인 연결 버튼 요소 얻기
  const isVisible_2 = await kakao_disconnect?.isVisible(); //라인 연결 노출 값 저장
  expect(isVisible_2).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible_2) {
    console.log('라인 계정이 연결해제 되었습니다.');
  } else {
    console.log('라인 계정이 연결해제 되지 않았습니다.');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();

});

/*test('이메일 계정 로그인 , 야후 연결,연결 해제_ja', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad_01@yopmail.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();
  await page.locator('div').filter({ hasText: 'Yahoo 連携する' }).getByRole('link', { name: '連携する' }).click();
  await page.waitForLoadState('load');
  await page.getByPlaceholder('ID/携帯電話番号/メールアドレス').click();
  await page.getByPlaceholder('ID/携帯電話番号/メールアドレス').fill('hidelove9999');
  await page.getByRole('button', { name: '次へ' }).click();
  await page.waitForLoadState('load');
  await page.getByPlaceholder('パスワード').click();
  await page.getByPlaceholder('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'ログイン', exact: true }).click();
  await page.waitForLoadState('load');

  const kakao_connect = await page.waitForSelector('.oauth--disconnect');  //라인 연결 끊기 버튼 요소 얻기
  const isVisible = await kakao_connect.isVisible(); //라인 연결 끊기 노출 값 저장
  expect(isVisible).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible) {
    console.log('야후 계정이 연결 되었습니다.');
  } else {
    console.log('야후 계정이 연결 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '解除する' }).click();
  await page.waitForLoadState('load');

  const kakao_disconnect = await page.$('.myAccount__section'); //라인 연결 버튼 요소 얻기
  const isVisible_2 = await kakao_disconnect?.isVisible(); //라인 연결 노출 값 저장
  expect(isVisible_2).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible_2) {
    console.log('야후 계정이 연결해제 되었습니다.');
  } else {
    console.log('야후 계정이 연결해제 되지 않았습니다.');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();

});
*/

test('이메일 계정 로그인 , 트위터 연결,연결 해제_us', async ({ page }) => {
  await page.setDefaultTimeout(60000);
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad_01@yopmail.com');
  await page.getByLabel('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.waitForLoadState('load');

  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'My Account' }).click();

  await page.locator('div').filter({ hasText: 'Twitter Connect Account' }).getByRole('link', { name: 'Connect Account' }).click();
  await page.getByPlaceholder('Username or email').click();
  await page.getByPlaceholder('Username or email').fill('hidelove999');
  
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7!');
  await page.getByRole('button', { name: 'Sign In' }).click();
  await page.waitForLoadState('load');
  /*
  await page.getByLabel('Phone, email, or username').click();
  await page.getByLabel('Phone, email, or username').fill('hidelove999@daum.net');
  await page.getByRole('button', { name: 'Next' }).click();
  await page.locator('label div').nth(3).click();
  await page.getByTestId('ocfEnterTextTextInput').fill('hidelove999');
  await page.getByTestId('ocfEnterTextNextButton').click();
  await page.getByLabel('Password', { exact: true }).click();
  await page.getByLabel('Password', { exact: true }).fill('wlscogus7!');
  await page.getByTestId('LoginForm_Login_Button').click();
  await page.waitForTimeout(7000);
  */
  const kakao_connect = await page.waitForSelector('.oauth--disconnect');  //라인 연결 끊기 버튼 요소 얻기
  const isVisible = await kakao_connect.isVisible(); //라인 연결 끊기 노출 값 저장
  expect(isVisible).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible) {
    console.log('트위터 계정이 연결 되었습니다.');
  } else {
    console.log('트위터 계정이 연결 되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: 'Disconnect Account' }).click();
  await page.waitForLoadState('load');

  const kakao_disconnect = await page.$('.myAccount__section'); //라인 연결 버튼 요소 얻기
  const isVisible_2 = await kakao_disconnect?.isVisible(); //라인 연결 노출 값 저장
  expect(isVisible_2).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible_2) {
    console.log('트위터 계정이 연결해제 되었습니다.');
  } else {
    console.log('트위터 계정이 연결해제 되지 않았습니다.');
  }
  console.log();
  await page.waitForLoadState('load');
  
  await page.close();

});




test('내정보 > 생년월일 입력하기_kr', async ({ page }) => {
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
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '정보입력' }).click();
  await page.getByRole('combobox', { name: '년' }).selectOption('1983');
  await page.getByRole('combobox', { name: '월' }).selectOption('12');
  await page.getByRole('combobox', { name: '일' }).selectOption('20');
  await page.getByRole('button', { name: '저장' }).click();

  const birth_snackbar = await page.waitForSelector('.lzSnackbar'); //생년월일 입력후 노출되는 스낵바 요소 얻기
  const isVisible = await birth_snackbar.isVisible(); //생년월일 입력 스낵바 노출 값 저장
  expect(isVisible).toBeTruthy; //생년월일 스낵바 노출 검증


  if (isVisible) {
    console.log('생년월일이 저장 되었습니다.');
  } else {
    console.log('생년월일이 저장 되지 않았습니다.');
  }
  console.log();


  await page.getByRole('button', { name: '정보변경' }).click();
  await page.getByText('(선택) 개인정보 수집 및 이용동의 상세보기').click();
  await page.getByRole('button', { name: '저장' }).click();
  console.log('생년월일이 초기화 되었습니다.');
  await page.waitForLoadState('load');
  await page.close();

});

test('내정보 > 생년월일 입력하기_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '情報入力' }).click();
  await page.getByRole('combobox', { name: '年' }).selectOption('1983');
  await page.getByRole('combobox', { name: '月' }).selectOption('12');
  await page.getByRole('combobox', { name: '日' }).selectOption('20');
  await page.getByRole('button', { name: '保存' }).click();

  const birth_snackbar = await page.waitForSelector('.lzSnackbar'); //생년월일 입력후 노출되는 스낵바 요소 얻기
  const isVisible = await birth_snackbar.isVisible(); //생년월일 입력 스낵바 노출 값 저장
  expect(isVisible).toBeTruthy; //생년월일 스낵바 노출 검증


  if (isVisible) {
    console.log('생년월일이 저장 되었습니다.');
  } else {
    console.log('생년월일이 저장 되지 않았습니다.');
  }
  console.log();


  await page.getByRole('button', { name: '情報変更' }).click();
  await page.getByText('(選択)個人情報取扱い同意 確認').click();
  await page.getByRole('button', { name: '保存' }).click();
  console.log('생년월일이 초기화 되었습니다.');
  await page.waitForLoadState('load');
  await page.close();

});

test('내정보 > 생년월일 입력하기_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'My Account' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'Enter Information' }).click();
  await page.getByRole('combobox', { name: 'Year' }).selectOption('1983');
  await page.getByRole('combobox', { name: 'Month' }).selectOption('12');
  await page.getByRole('combobox', { name: 'Day' }).selectOption('20');
  await page.getByRole('button', { name: 'Save' }).click();

  const birth_snackbar = await page.waitForSelector('.lzSnackbar'); //생년월일 입력후 노출되는 스낵바 요소 얻기
  const isVisible = await birth_snackbar.isVisible(); //생년월일 입력 스낵바 노출 값 저장
  expect(isVisible).toBeTruthy; //생년월일 스낵바 노출 검증


  if (isVisible) {
    console.log('생년월일이 저장 되었습니다.');
  } else {
    console.log('생년월일이 저장 되지 않았습니다.');
  }
  console.log();


  await page.getByRole('button', { name: 'Change Information' }).click();
  await page.getByText('(optional) Agree to the Collection and Use of Personal Information').click();
  await page.getByRole('button', { name: 'Save' }).click();
  console.log('생년월일이 초기화 되었습니다.');
  await page.waitForLoadState('load');
  await page.close();

});






test('내정보 > 기기초기화 3개월 이내_kr', async ({ page }) => {
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
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '기기 초기화' }).click();
  await page.getByRole('button', { name: '확인' }).click();




  const mobile_snackbar = await page.waitForSelector('.lzSnackbar'); //초기화 실패 스낵바 요소 얻기
  const isVisible = await mobile_snackbar.isVisible(); //초기화 실패 스낵바 노출 값 저장
  expect(isVisible).toBeTruthy; //초기화 실패 스낵바 노출 검증


  if (isVisible) {
    console.log('최근에 디바이스 연결 해제를 이미 하였습니다. 확인완료');
  } else {
    console.log('최근에 디바이스 연결 해제를 이미 하였습니다. 실패');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();


});

test('내정보 > 기기초기화 3개월 이내_ja', async ({ page }) => {
  await page.goto('https://q-www.lezhin.jp/ja');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: 'メールアドレスでログイン' }).click();
  await page.getByLabel('メールアドレス').click();
  await page.getByLabel('メールアドレス').fill('squad@lezhin.com');
  await page.getByLabel('パスワード').click();
  await page.getByLabel('パスワード').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'メールアドレスでログイン' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'アカウントメニュー' }).click();
  await page.getByRole('link', { name: '会員情報' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: '端末の初期化' }).click();
  await page.getByRole('button', { name: '確認' }).click();

  const mobile_snackbar = await page.waitForSelector('.lzSnackbar'); //초기화 실패 스낵바 요소 얻기
  const isVisible = await mobile_snackbar.isVisible(); //초기화 실패 스낵바 노출 값 저장
  expect(isVisible).toBeTruthy; //초기화 실패 스낵바 노출 검증


  if (isVisible) {
    console.log('최근에 디바이스 연결 해제를 이미 하였습니다. 확인완료');
  } else {
    console.log('최근에 디바이스 연결 해제를 이미 하였습니다. 실패');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();


});

test('내정보 > 기기초기화 3개월 이내_us', async ({ page }) => {
  await page.goto('https://q-www.lezhinus.com/en');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'Login with email' }).click();
  await page.getByLabel('Email').click();
  await page.getByLabel('Email').fill('squad@lezhin.com');
  await page.getByLabel('Password').fill('wlscogus7!@');
  await page.getByRole('button', { name: 'Login with email' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'Account Menu' }).click();
  await page.getByRole('link', { name: 'My Account' }).click();
  await page.waitForLoadState('load');
  await page.getByRole('button', { name: 'Device Reset' }).click();
  await page.getByRole('button', { name: 'OK' }).click();

  const mobile_snackbar = await page.waitForSelector('.lzSnackbar'); //초기화 실패 스낵바 요소 얻기
  const isVisible = await mobile_snackbar.isVisible(); //초기화 실패 스낵바 노출 값 저장
  expect(isVisible).toBeTruthy; //초기화 실패 스낵바 노출 검증


  if (isVisible) {
    console.log('최근에 디바이스 연결 해제를 이미 하였습니다. 확인완료');
  } else {
    console.log('최근에 디바이스 연결 해제를 이미 하였습니다. 실패');
  }
  console.log();
  await page.waitForLoadState('load');
  await page.close();


});



  

  








