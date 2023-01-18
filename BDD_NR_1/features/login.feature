Feature: check that the functionality of certain elements on the-internet.herokuapp page

  Background:
    Given Home Page: I am on the-internet.herokuapp page

  @T1 @Basic_Auth @click_element
  Scenario: Check that you can click on the Basic Auth
    When Home Page: I click on Basic Auth
    Then Basic Auth Page: I am on the Basic Auth page

  @T2 @Checkboxes @click_element
  Scenario: Check that you can click on the Checkboxes
    When Home Page: I click on Checkboxes
    Then Checkboxes: I am on the Checkboxes page

  @T3 @Form_Authentication @click_element
  Scenario: Check that you can click on the Form Authentication
    When Home Page: I click on Form Authentication
    Then Login Page: I am on the Form Authentication

  @T4 @Login_Succes @login_page
  Scenario: From the login page, check that you can login after providing correct username and correct password
    Given Login Page: I am on the login page
    When Login Page: I insert the username "tomsmith" and password "SuperSecretPassword!"
    When Login Page: I click the login button
    Then Secure Page: I am on the secure page and I can see a message

  @T5 @Login_Failed @login_page
  Scenario Outline: From the login page, check that you cannot login after providing incorrect credentials
    Given Login Page: I am on the login page
    When Login Page: I insert the username "<username>" and password "<password>"
    When Login Page: I click the login button
    Then Login Page: I cannot login into the application and I receive error message "<error_message>"
    Examples:
      | username           | password             | error_message               |
      | incorrect_username | incorrect_password   | Your username is invalid!   |
      | incorrect_username | SuperSecretPassword! | Your username is invalid!   |
      | tomsmith           | incorrect_password   | Your password is invalid!   |
      |                    | incorrect_password   | Your username is invalid!   |
      |                    | SuperSecretPassword! | Your username is invalid!   |
      | incorrect_username |                      | Your username is invalid!   |
      | tomsmith           |                      | Your password is invalid!   |

  @T6 @Secure_Page_Logout
  Scenario: From the secure page, check that you can log out
    Given Secure Page: I am logged in on the secure page with username "tomsmith" and password "SuperSecretPassword!"
    When Secure Page: I click on logout
    Then Login Page: I leave the secure page and I am on the login page

