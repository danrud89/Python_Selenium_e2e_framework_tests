from selenium.webdriver.common.by import By


# TU WPISUJESZ WSZSYTKIE LOCATORY NA ZE STRONY Z PODZIAŁEM NA KLASY ZE WZGLĘDU NA UMIEJSCOWIENIE/MODALE/STOPKI itp
class LoginPageLocators:
    APP_TITLE = (
        By.ID,
        'kc-header',
    )
    LOGIN_HEADER = (
        By.ID,
        'kc-page-title',
    )
    USERNAME_INPUT = (
        By.ID,
        'username',
    )
    PASSWORD_INPUT = (
        By.ID,
        'password',
    )
    SUBMIT_BUTTON = (
        By.ID,
        'kc-form-buttons',
    )
    LOGIN_ERROR = (
        By.ID,
        'input-error',
    )


class MainPageHeaderLocators:
    APP_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'site-title')]"
    )
    MY_ACCOUNT_BUTTON = (
        By.XPATH,
        "//li[contains(@class, 'page_item page-item-9')]"
    )
    ADD_ALBUM_TO_CART_BTN = (
        By.CSS_SELECTOR,
        'ul.products li:nth-child(3) .button'
    )
    CART_ICON = (
        By.ID,
        '#site-header-cart li .cart-contents'
    )
    SEARCH_BAR_INPUT = (
        By.ID,
        '#woocommerce-product-search-field-0'
    )


class CartLocators:
    PRODUCT_REMOVE = (
        By.XPATH,
        "//td[contains(@class, 'product-remove')]"
    )

class MyAccountPageLocators:
    MY_ACCOUNT_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'entry-title')]"
    )
