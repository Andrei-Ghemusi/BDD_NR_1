from behave import *

@given("Login Page: I am on the login page")
def steps_impl(context):
    context.login_page_object.navigate_to_login_page()

@when('Login Page: I insert the username "{username}" and password "{password}"')
def steps_impl(context, username, password):
    context.login_page_object.insert_username(username)
    context.login_page_object.insert_password(password)

@when("Login Page: I click the login button")
def step_impl(context):
    context.login_page_object.click_on_login()

@then("Secure Page: I am on the secure page and I can see a message")
def step_impl(context):
    context.secure_page_object.check_succes_message()

@then('Login Page: I cannot login into the application and I receive error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page_object.check_login_error_message(error_message)

