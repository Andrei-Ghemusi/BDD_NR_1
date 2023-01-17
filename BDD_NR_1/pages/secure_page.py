from selenium.webdriver.common.by import By
import unittest
from steps.base_page import Base_page


class Secure_page(Base_page):
    SECURE_AREA_MESSAGE = (By.XPATH, '//*[@id="flash"]')
    LOGOUT = (By.XPATH, '//*[@id="content"]/div/a/i')

    def is_succes_message_displayed(self):
        is_message_displayed = self.chrome.find_element(*self.SECURE_AREA_MESSAGE).is_displayed()
        assert (is_message_displayed == True, 'Error, message is not displayed')

    def check_succes_message(self):
        expected_message = 'You logged into a secure area!'
        actual_message = self.chrome.find_element(*self.SECURE_AREA_MESSAGE).text
        assert(expected_message in actual_message,f'Error, expected {expected_message} message, but got {actual_message} instead')

    def is_logout_button_displayed(self):
        is_button_displayed = self.chrome.find_element(*self.LOGOUT).is_displayed()
        assert (is_button_displayed == True, 'Error, button is not displayed')

    def click_on_logout(self):
        self.chrome.find_element(*self.LOGOUT).click()
