import { test, expect } from '@playwright/test';

test('카카오 SNS 로그인 정보 필드 확인', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko')
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('button', { name: '카카오로 로그인' }).click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In', exact: true }).click();
  await page.waitForTimeout(3000);
  await page.getByText('전체동의').click();
  await page.getByText('만 14세 이상입니다.(필수)').click();
  await page.getByRole('button', { name: '동의' }).click();
  await page.getByRole('link', { name: '확인' }).click();
  await page.waitForTimeout(3000);
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

  await page.getByRole('button', { name: '회원을 탈퇴하시겠습니까?' }).click();
  await page.getByText('이용이 불편하고 장애가 많음').click();
  await page.getByRole('button', { name: '탈퇴하기' }).click();
  await page.getByRole('button', { name: '확인' }).click();

  console.log('회원탈퇴가 완료 되었습니다.');

  await page.close();

});


test('카카오 SNS 비밀번호 등록 과 연결해제, 로그인', async ({ page }) => {
  await page.goto('https://q-www.lezhin.com/ko')
  await page.getByRole('button', { name: '오늘 하루 안보기' }).click();
  await page.getByRole('button', { name: '계정 메뉴' }).click();
  await page.getByRole('button', { name: '카카오로 로그인' }).click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In', exact: true }).click();
  await page.waitForTimeout(3000);
  await page.getByText('전체동의').click();
  await page.getByText('만 14세 이상입니다.(필수)').click();
  await page.getByRole('button', { name: '동의' }).click();
  await page.getByRole('link', { name: '확인' }).click();
  await page.waitForTimeout(3000);
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
  await page.waitForTimeout(3000);

  
  const kakao_link = await page.locator('div').filter({ hasText: '카카오 연결' }).getByRole('link', { name: '연결' });//카카오 연결하기 이메일 텍스트 요소 얻기
  expect(kakao_link).toBeTruthy; //카카오 연결 텍스트 노출 확인

  if (kakao_link) {
    console.log('카카오 연결이 해제 되었습니다.');
  } else {
    console.log('카카오 연결이 해제  되지 않았습니다.');
  }
  console.log();

  await page.getByRole('button', { name: '계정 메뉴 30' }).click();
  await page.getByRole('link', { name: '로그아웃' }).click();
  await page.getByLabel('이메일').click();
  await page.getByLabel('이메일').fill('hidelove999@naver.com');
  await page.getByLabel('비밀번호').click();
  await page.getByLabel('비밀번호').fill('wlscogus7!');
  await page.getByRole('button', { name: '이메일로 로그인' }).click();
  await page.getByRole('button', { name: '계정 메뉴 30' }).click();

  const Locale_change = await page.waitForSelector('.userInfo__email'); //로그인된 이메일 주소 요소 얻기
  const text = await Locale_change.evaluate((el) => el.textContent); //Locale_change에서 설정된 텍스트 얻기
  expect(text).toBe("hidelove999@naver.com"); //카카오 연결 텍스트 노출 확인

  if (text === 'hidelove999@naver.com') {
    console.log('이메일 로그인이 완료 되었습니다.');
  } else {
    console.log('이메일 로그인이 완료  되지 않았습니다.');
  }
  console.log();
  await page.getByRole('button', { name: '회원을 탈퇴하시겠습니까?' }).click();
  await page.getByText('이용이 불편하고 장애가 많음').click();
  await page.getByPlaceholder('비밀번호를 입력해 주세요.').click();
  await page.getByPlaceholder('비밀번호를 입력해 주세요.').fill('wlscogus7!');
  await page.getByRole('button', { name: '탈퇴하기' }).click();
  await page.getByRole('button', { name: '확인' }).click();
  console.log('회원탈퇴가 완료 되었습니다.');
  
  await page.close();
});

//TC 133 , 146 수행 케이스
test('이메일 계정 로그인 , SNS 연결,연결 해제', async ({ page }) => {
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
  await page.getByRole('button', { name: '계정 메뉴 21' }).click();
  await page.getByRole('link', { name: '내 정보' }).click();
  await page.locator('div').filter({ hasText: '카카오 연결' }).getByRole('link', { name: '연결' }).click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').click();
  await page.getByPlaceholder('KakaoMail ID, email, phone number').fill('hidelove999@naver.com');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('wlscogus7');
  await page.getByRole('button', { name: 'Log In', exact: true }).click();
  await page.waitForTimeout(3000);

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
  await page.waitForTimeout(3000);

  const kakao_disconnect = await page.$('.myAccount__section'); //카카오 연결 버튼 요소 얻기
  const isVisible_2 = await kakao_disconnect?.isVisible(); //카카오 연결 노출 값 저장
  expect(isVisible_2).toBeTruthy; //버튼 노츌 유무 확인

  if (isVisible_2) {
    console.log('카카오 계정이 연결해제 되었습니다.');
  } else {
    console.log('카카오 계정이 연결해제 되지 않았습니다.');
  }
  console.log();

  await page.close();

});

test('내정보 > 생년월일 입력하기', async ({ page }) => {
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
  await page.waitForTimeout(3000);
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
  await page.close();

});


test('내정보 > 기기초기화 3개월 이내', async ({ page }) => {
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
  await page.waitForTimeout(3000);
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
  await page.close();


});


  

  








