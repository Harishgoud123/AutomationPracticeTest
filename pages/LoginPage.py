from selenium.webdriver.common.by import By

from config.config import signup_testdata
from config.locators import login_locators, signup_locators
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        self.do_click(login_locators.Sign_in)
        return self.get_title(title)

    def is_create_account_button_exist(self):
        self.do_click(login_locators.Sign_in)
        return self.is_enabled(self.Create_account_Button)

    def do_login(self, username, password):
        self.do_click(login_locators.Sign_in)
        self.do_send_keys(login_locators.EMAIL, username)
        self.do_send_keys(login_locators.PASSWORD, password)
        self.do_click(login_locators.Login_Button)

    def is_invalid_credentails_displayed(self):
        return self.is_enabled(signup_locators.Login_Invalid_cred)

    def is_Login_Successful(self):
        return self.is_enabled(login_locators.Sign_out)

    def do_logout(self):
        self.do_click(login_locators.Sign_out)
        self.is_enabled(login_locators.Sign_in)
