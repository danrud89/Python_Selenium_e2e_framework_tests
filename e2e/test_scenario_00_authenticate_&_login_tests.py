# najpierw biblioteki Python
import time

#Potem biblioteki zewnętrzne
import pytest
from faker import Faker

#Na końcu importy własne
from e2e.test_base import BaseTest
from pages.locators import (
   LoginPageLocators, MainPageHeaderLocators
)
from utils import settings

fake = Faker("pl_PL")


class TestAuthenticateAndLogin(BaseTest):

    login_header = 'Sign in'

    def test_create_user_account(self):
        pass

    @pytest.mark.parametrize("login, password",
        [
            ('invalid_login', 'test1234'),
            ('test1', 'invalid_password'),
            ('invalid_login', 'invalid_password'),
            (' ', ' ',),
        ]
        )
    def test_login_with_invalid_credentials(self, login, password):
        self.login_page.login(login, password)
        time.sleep(1)
        get_error_content = self.get_element_text(LoginPageLocators.LOGIN_ERROR)
        time.sleep(1)
        assert get_error_content == error_messages.LOGIN_ERROR
        
    def test_login_success(self):
        self.login_page.login(settings.USER_LOGIN, settings.USER_PASSWORD)
        home_page_logo = self.is_visible(MainPageHeaderLocators.APP_TITLE)
        assert home_page_logo is True
    
    def test_logout_success(self):
        self.login_page.user_logout()
        login_page_header = self.get_element_text(LoginPageLocators.LOGIN_HEADER)
        assert login_page_header == self.login_header
