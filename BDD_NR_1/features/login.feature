Feature: check that the functionality of certain elements on the-internet.herokuapp page

  Scenario: Check that you can click on the Basic Auth
    Given Home Page: I am on the-internet.herokuapp page
    When Home Page: I click on Basic Auth
    Then Basic Auth Page: I am on the Basic Auth page

  Scenario: Check that you can click on the Checkboxes
    Given Home Page: I am on the-internet.herokuapp page
    When Home Page: I click on Checkboxes
    Then Checkboxes: I am on the Checkboxes page

  Scenario: Check that you can click on the Form Authentication
    Given Home Page: I am on the-internet.herokuapp page
    When Home Page: I click on Form Authentication
    Then Login Page: I am on the Form Authentication

  Scenario: From the login page, check that you can login after providing correct username and correct password
    Given Login Page: I am on the login page
    When Login Page: I insert the username "tomsmith" and password "SuperSecretPassword!"
    When Login Page: I click the login button
    Then Secure Page: I am on the secure page and I can see a message

  Scenario: From the login page, check that you can login after providing incorrect username and incorrect password
    Given Login Page: I am on the login page
    When Login Page: I insert username "incorrect_username" and password "incorrect password"
    When Login Page: I click the login button
    Then Login Page: I cannot login into the application and I receive error message " Your username is invalid!"

  Scenario: From the secure page, check that you can log out
    Given Secure Page: I am logged in on the secure page with username "tomsmith" and password "SuperSecretPassword!"
    When Secure Page: I click on logout
    Then Login Page: I leave the secure page and I am on the login page

