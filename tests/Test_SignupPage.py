import pytest
from config.config import TestData
from pages.SingupPage import SignupPage
from tests.Test_base import BaseTest


class Test_Signup_Page(BaseTest):

    @pytest.mark.positive
    def test_create_account(self):
        self.signup = SignupPage(self.driver)
        self.signup.create_account()
        assert self.signup.is_registration_Successful()

