from behave import *

@given("Home Page: I am on the-internet.herokuapp page")
def step_impl(context):
    context.home_page_object.navigate_to_home_page()

@when("Home Page: I click on Basic Auth")
def step_impl(context):
    context.home_page_object.click_on_Basic_Auth()

@then("Basic Auth Page: I am on the Basic Auth page")
def step_impt(context):
    context.basic_auth_page_object.check_current_url()

@when("Home Page: I click on Checkboxes")
def step_impl(context):
    context.home_page_object.click_on_Checkboxes()

@then("Checkboxes: I am on the Checkboxes page")
def step_impl(context):
    context.checkboxes_page_object.check_current_url()

@when("Home Page: I click on Form Authentication")
def step_impl(context):
    context.home_page_object.click_on_Form_Authentication()

@then("Login Page: I am on the Form Authentication")
def step_impl(context):
    context.login_page_object.check_current_url()



