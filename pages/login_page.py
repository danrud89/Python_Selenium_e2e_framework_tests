import time
from pages.base_page import BasePage
from pages.locators import (
    LoginPageLocators,
)
from utils import settings


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_new_user(self, user_name: str, user_password: str) -> None:
        """
        Creates new user with given data.

        :param user_name: Username/login
        :param user_password: User password
        """
        pass
    
    def login(self, login: str, password: str) -> None:
        """
        Logs the user with given credentials

        :param login: User login or email
        :param password: User password
        """
        
        self.fill_login_input(login)
        self.fill_password_input(password)
        self.submit_login_credentials()

    def get_login_error_msg(self) -> str:
        """" Extracts error message from login form
        
        return: error message content
        """
        error_login_message = self.get_element_text(LoginPageLocators.LOGIN_ERROR)
        return error_login_message

    def fill_login_input(self, login: str) -> None:
        """Fills username input with given data
        
        :param login: Username/login/e-mail address
        """
        time.sleep(settings.SYSTEM_DELAY)
        self.click(LoginPageLocators.USERNAME_INPUT)
        time.sleep(settings.SYSTEM_DELAY)
        self.clear_text(LoginPageLocators.USERNAME_INPUT)
        time.sleep(settings.SYSTEM_DELAY)
        self.send_keys(LoginPageLocators.USERNAME_INPUT, login)
        time.sleep(settings.SYSTEM_DELAY)

    def fill_password_input(self, password: str) -> None:
        """Fills password input with given data
        
        :param password: User password
        """
        time.sleep(settings.SYSTEM_DELAY)
        self.click(LoginPageLocators.PASSWORD_INPUT)
        time.sleep(settings.SYSTEM_DELAY)
        self.clear_text(LoginPageLocators.PASSWORD_INPUT)
        time.sleep(settings.SYSTEM_DELAY)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        time.sleep(settings.SYSTEM_DELAY)
    
    def submit_login_credentials(self) -> None:
        """Checks if submit button is enabled and clicks"""
        try:
            enabled_submit_button = self.is_enabled(LoginPageLocators.SUBMIT_BUTTON)
            if enabled_submit_button:
                self.click(LoginPageLocators.SUBMIT_BUTTON)
            time.sleep(settings.SYSTEM_DELAY)
        except AttributeError:
            print('Button is not active !')
    
    def user_logout(self) -> None:
        """" Logs the user out -> redirect to login page"""
        pass
    