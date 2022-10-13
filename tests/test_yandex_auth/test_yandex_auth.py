import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from tests.fixtures_yandex_auth import (
    FIXTURES_BAD_PASSWD,
    FIXTURES_BAD_LOGIN,
    FIXTURES_CORRECT_LOGIN_AND_PASSWD
)


class TestYandexAuth:
    url = 'https://passport.yandex.ru/auth/'
    input_login = 'login'
    input_passwd = 'passwd'
    btn_login = 'passp:sign-in'

    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def teardown(self):
        self.driver.close()

    def _send_email(self, driver, login):
        driver.find_element(By.NAME, self.input_login).send_keys(login)
        driver.find_element(By.ID, self.btn_login).click()
        time.sleep(.5)

    def _send_passwd(self, driver, passwd):
        driver.find_element(By.NAME, self.input_passwd).send_keys(passwd)
        driver.find_element(By.ID, self.btn_login).click()
        time.sleep(.5)

    @pytest.mark.parametrize('login, passwd, exp_result', FIXTURES_BAD_PASSWD)
    def test_bad_passwd(self, login, passwd, exp_result):
        driver = self.driver
        driver.get(self.url)
        time.sleep(.5)
        self._send_email(driver, login)
        assert driver.find_element(By.CLASS_NAME, 'CurrentAccount-displayName').text == login
        self._send_passwd(driver, passwd)
        assert driver.find_element(By.CLASS_NAME, 'Textinput-Hint_state_error').text == exp_result

    @pytest.mark.parametrize('login, exp_result', FIXTURES_BAD_LOGIN)
    def test_bad_login(self, login, exp_result):
        driver = self.driver
        driver.get(self.url)
        time.sleep(.5)
        self._send_email(driver, login)
        assert driver.find_element(By.CLASS_NAME, 'Textinput-Hint_state_error').text == exp_result
    
    @pytest.mark.parametrize('login, passwd, exp_result', FIXTURES_CORRECT_LOGIN_AND_PASSWD)
    def test_correct_login_and_passwd(self, login, passwd, exp_result):
        driver = self.driver
        driver.get(self.url)
        time.sleep(.5)
        self._send_email(driver, login)
        assert driver.find_element(By.CLASS_NAME, 'CurrentAccount-displayName').text == login
        self._send_passwd(driver, passwd)
        assert driver.current_url == exp_result       