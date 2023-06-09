import time

import pytest
from faker import Faker

from e2e.test_base import BaseTest
from pages.locators import CartLocators, MyAccountPageLocators


class TestOpenApp(BaseTest):
    app_title = 'Demo Store'
    my_account = 'My account'

    def test_open_app_success(self):
        time.sleep(3)
        app_title = self.main_page.get_header_text()
        assert app_title == self.app_title

    def test_open_my_account(self):
        self.main_page.open_my_account()
        time.sleep(2)
        assert self.main_page.get_element_text(
            MyAccountPageLocators.MY_ACCOUNT_TITLE
        ) == self.my_account
        time.sleep(2)

    def test_back_to_home_page(self):
        time.sleep(2)
        self.main_page.back_to_home_page()
        time.sleep(2)
        app_title = self.main_page.get_header_text()
        assert app_title == self.app_title

    def test_add_item_to_cart(self):
        self.main_page.add_album_to_cart()
        time.sleep(2)
        self.main_page.open_shopping_cart()
        time.sleep(2)
        assert self.main_page.get_count(
            CartLocators.PRODUCT_REMOVE
        ) > 0



