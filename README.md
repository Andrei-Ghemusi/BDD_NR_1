# BDD internet.herokuapp site

This is my first BDD project.

Site tested: https://the-internet.herokuapp.com/

Libraries and packages used:
- selenium;
- behave;
- webdriver_manager;

This project aims to test the:
- Basic Authentication page;
- Checkboxes page;
- Home page;
- Login page;
- and some features regarding the Secure page.

Structure of the project:
- package called "features" in which there is the login.feature file which contains the said feature;
- package called "pages" which contains the: basic_auth_page, checkboxes_page, home_page, login_page, secure_page; files;
- package called "steps";
- behave.ini file;
- environment file;
- 2 behave reports which can be opened in browser.

How to run the project:
- using the command "behave -f html -o behave -report.html" in the terminal will run the entire project. *
*IT IS ESSENTIAL to have the behave.ini file alongside the code written in it, otherwise the command to run the whole project will not work.
