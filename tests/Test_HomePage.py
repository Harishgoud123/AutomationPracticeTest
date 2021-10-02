import pytest
from config.config import TestData
from tests.Test_base import BaseTest
from pages.HomePage import HomePage


class Test_HomePage(BaseTest):

    """Test is validate if the homepage title is correct"""
    @pytest.mark.positive
    def test_homepage_title(self):
        self.homepage = HomePage(self.driver)
        title = self.homepage.get_home_page_title(TestData.Home_Page_Title)
        assert title == self.homepage.get_home_page_title(TestData.Home_Page_Title)

