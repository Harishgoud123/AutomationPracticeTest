import pytest
from tests.Test_base import BaseTest
from pages.DressesPage import DressesPage


class TestDressesPage(BaseTest):

    """test is to add all the summer items to the cart and validate added and available cart items are same"""
    @pytest.mark.positive
    def test_add_summer_dresses_to_cart(self):
        self.dresspage = DressesPage(self.driver)
        print('this is harish')
        items_in_cart = self.dresspage.add_summer_dresses_to_cart_and_return_number_of_items()
        print(items_in_cart)
        assert items_in_cart, self.dresspage.get_cart_quantity()
