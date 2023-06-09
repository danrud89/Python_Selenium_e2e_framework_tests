import time

import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.driver_factory import DriverFactory
from utils import settings


@pytest.fixture(scope="class")
def driver(request):
    driver = DriverFactory.get_driver('firefox')
    driver.get(settings.URL)
    request.cls.login_page = LoginPage(driver)
    request.cls.main_page = MainPage(driver)
    #Here you can add more pages
    yield driver
    driver.quit()
    time.sleep(2)
