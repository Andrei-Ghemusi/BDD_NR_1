from pages.basic_auth_page import Basic_Auth
from pages.checkboxes_page import Checkboxes
from pages.home_page import Home_page
from pages.login_page import Login_page
from pages.secure_page import Secure_page
from steps.browser import Browser


def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.login_page_object = Login_page()
    context.basic_auth_page_object = Basic_Auth()
    context.checkboxes_page_object = Checkboxes()
    context.secure_page_object = Secure_page()

def after_all(context):
    context.browser.quit()