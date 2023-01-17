from behave import *

@given('Secure Page: I am logged in on the secure page with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page_object.navigate_to_login_page()
    context.login_page_object.insert_username(username)
    context.login_page_object.insert_password(password)
    context.login_page_object.click_on_login()

@when('Secure Page: I click on logout')
def step_impl(context):
    context.secure_page_object.click_on_logout()

@then('Login Page: I leave the secure page and I am on the login page')
def step_impl(context):
    context.login_page_object.check_current_url()