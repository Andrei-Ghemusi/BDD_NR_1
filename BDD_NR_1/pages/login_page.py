from steps.browser import Browser
import unittest

class Login_page(Browser, unittest):
    USERNAME = ()
    PASSWORD = ()
    LOGIN_BUTTON = ()
    ERROR_MESSAGE_LOGIN = ()

    def check_current_url(self):
        expected_url = 'https://the-internet.herokuapp.com/login'
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, f'Error, expected {expected_url} but got {actual_url} instead'

    def navigate_to_login_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/login')

    def insert_username(self, username):
        self.chrome.find_element(*self.USERNAME).send_keys(username)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def click_on_login(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def check_login_error_message(self, expected_error_message):
        self.check_error_message(*self.ERROR_MESSAGE_LOGIN,expected_error_message)