# Login Page Class

# Responsibility of this class:
# get username and send keys - email
# # get password and send keys - email
# # click the submit button and navigate to dashboard Page
# Invalid -> error message
# Forgot password

# Page Class
# 1. Page Locators
# 2. Page Actions
# 3. Web driver Initialization
# 4. Custom Functions
# 5. No Assertions in Page Object Class

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators -> test case already created - just creating page model. test case reference ->Py2xAutomationProgramSelenium -> 24Apr2024
    email = (By.ID, "login-username")
    password = (By.NAME, "password")
    signin_button = (By.XPATH, "//button[@id='js-login-btn']")
    #forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.ID, "js-notification-box-msg")

    #free_trail = (By.XPATH, "//a[normalize-space()='Start a free trail']")
    #sso_login = (By.XPATH, "//a[normalize-space()='Sign in using SSO']")
    #remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")

    # Page Actions
    def get_email(self):
        return self.driver.find_element(*LoginPage.email)  # * means current class

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_signin_button(self):
        return self.driver.find_element(*LoginPage.signin_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trail(self):
        return self.driver.find_element(*LoginPage.free_trail)

    # In POM don't add functions if we are not using

    # Page Actions -> Main Action

    def login_to_vwo(self, email, password):
        self.get_email().send_keys(email)
        self.get_password().send_keys(password)
        self.get_signin_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    #def click_free_trail(self):
    #self.get_free_trail().click()
