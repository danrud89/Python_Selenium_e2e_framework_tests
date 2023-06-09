from pages.base_page import BasePage
from pages.locators import MainPageHeaderLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self) -> str:
        header_element = self.get_element_text(MainPageHeaderLocators.APP_TITLE)
        return header_element

    def open_my_account(self):
        self.click(MainPageHeaderLocators.MY_ACCOUNT_BUTTON)

    def add_album_to_cart(self):
        self.click(MainPageHeaderLocators.ADD_ALBUM_TO_CART_BTN)

    def open_shopping_cart(self):
        self.click(MainPageHeaderLocators.CART_ICON)

    def enter_value_into_search_bar(self):
        self.send_keys(MainPageHeaderLocators.SEARCH_BAR_INPUT, 'Cap')

    def back_to_home_page(self):
        self.click(MainPageHeaderLocators.APP_TITLE)

