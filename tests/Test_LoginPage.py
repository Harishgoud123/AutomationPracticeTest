import pytest
from config.config import TestData
from tests.Test_base import BaseTest
from pages.LoginPage import LoginPage
from config.config import Invalid_Credentials


class TestLogin(BaseTest):

    """ Testing if the create account button is available on page"""
    @pytest.mark.positive
    def test_create_account_button(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_create_account_button_exist()
        assert flag

    """Test if the Login page title is correct"""
    @pytest.mark.positive
    def test_title(self):
        self.login = LoginPage(self.driver)
        title = self.login.get_title(TestData.Login_Page_Title)
        assert title == TestData.Login_Page_Title

    """Test is to check the login scenario with different invalid credentials"""
    @pytest.mark.negative
    def test_invalid_login(self):
        self.login = LoginPage(self.driver)
        for user in Invalid_Credentials.userpass:
            self.login.do_login(user,Invalid_Credentials.userpass[user])
            flag = self.login.is_invalid_credentails_displayed()
            assert flag

    """Test is to validate the login with right credentials"""
    @pytest.mark.positive
    def test_login(self):
        self.login = LoginPage(self.driver)
        self.login.do_login(TestData.username, TestData.password)
        assert self.login.is_Login_Successful()


    """Test is signing out"""
    def test_signout(self):
        self.login = LoginPage(self.driver)
        self.login.do_logout()
        assert True


