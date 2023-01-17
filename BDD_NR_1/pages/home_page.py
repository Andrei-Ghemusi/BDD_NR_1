from selenium.webdriver.common.by import By

from steps.browser import Browser


class Home_page(Browser):
    BASIC_AUTH = (By.LINK_TEXT, 'Basic Auth')
    CHECKBOXES = (By.LINK_TEXT, 'Checkboxes')
    FORM_AUTHENTICATION = (By.LINK_TEXT, 'Form Authentication')

    def navigate_to_home_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/')

    def click_on_Basic_Auth(self):
        self.chrome.find_element(*self.BASIC_AUTH).click()

    def click_on_Checkboxes(self):
        self.chrome.find_element(*self.CHECKBOXES).click()

    def click_on_Form_Authentication(self):
        self.chrome.find_element(*self.FORM_AUTHENTICATION).click()