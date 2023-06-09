from pathlib import Path
import time
from typing import Any
import os
import string
import random

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import MainPageHeaderLocators
from utils import settings


class BasePage:
    """The BasePage class holds all common functionality across the website."""

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, settings.LOAD_DATA_DELAY)
        self.actions = ActionChains(self.driver)

    def click(self, by_locator: tuple) -> None:
        """Performs click on web element whose locator is passed to it."""
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator: tuple, value: Any):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it."""
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def select_element_by_name(
            self, name: Any, by_locator: tuple = None, element: str = "*"
    ) -> None:
        """Performs selection by name from a list received from the endpoint."""
        if by_locator:
            self.click(by_locator)
            time.sleep(settings.SYSTEM_DELAY)
        self.click((By.XPATH, f"//{element}[text()='{name}']"))

    def select_element_by_index(self, by_locator: tuple, index: int) -> None:
        """Performs selection of an item from a list received from endpoint."""
        element = self.driver.find_element(*by_locator)
        self.actions.move_to_element(element)
        self.actions.click()
        for _ in range(index):
            self.actions.send_keys(Keys.DOWN)
        self.actions.send_keys(Keys.ENTER)
        self.actions.perform()

    def get_element_text(self, by_locator: tuple) -> str:
        """Gets the text from the element."""
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)).text
        except TimeoutException:
            return "Not found"

    def get_elements(self, by_locator: tuple) -> list:
        """Gets elements and returns as a list."""
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def get_count(self, by_locator: tuple) -> int:
        """Counts the number of elements."""
        try:
            return len(self.wait.until(EC.presence_of_all_elements_located(by_locator)))
        except TimeoutException:
            return 0

    def clear_text(self, by_locator: tuple) -> None:
        """Clean text field."""
        self.send_keys(by_locator, Keys.CONTROL + "a")
        self.send_keys(by_locator, Keys.BACKSPACE)

    def is_visible(self, by_locator: tuple) -> bool:
        """Checks if the element is visible."""
        try:
            return bool(
                self.wait.until(EC.presence_of_all_elements_located(by_locator))
            )
        except TimeoutException:
            return False

    def is_enabled(self, by_locator: tuple) -> bool:
        """Checks if the element is enabled."""
        return self.wait.until(EC.visibility_of_element_located(by_locator)).is_enabled()

    def move_to_element_by_name(self, name: str) -> None:
        """Moves the mouse to the selected element."""
        element = self.driver.find_element(By.XPATH, f"//*[text()='{name}']")
        self.actions.move_to_element(element)
        self.actions.perform()

    def move_to_element_and_click(self, by_locator: tuple) -> None:
        """Moves the mouse to the element by given locator."""
        element = self.driver.find_element(By.XPATH, by_locator)
        self.actions.move_to_element(element).click().perform()

    def action_chains(self, by_locator: tuple, value: Any = None, value2: Any = None) -> None:
        """It performs more complex actions, like as hover over and click etc."""
        element = self.driver.find_element(*by_locator)
        self.actions.move_to_element(element)
        self.actions.click()
        if value is not None:
            self.actions.send_keys(value)
        if value2 is not None:
            self.actions.send_keys(value2)
        self.actions.perform()

    def get_attribute(self, by_locator: tuple, attribute: str) -> str:
        """Retrieves the value of the attribute."""
        return self.wait.until(
            EC.visibility_of_element_located(by_locator)
        ).get_attribute(attribute)

    def import_file(self, by_locator: tuple, file_path: str) -> None:
        """Retrieves data from a file."""
        self.driver.find_element(*by_locator).send_keys(file_path)

    def select_item(self, name: str) -> None:
        """Selects the network by name."""
        self.send_keys(
            by_locator=MainPageHeaderLocators.SEARCH_BAR_INPUT,
            value=name,
        )
        self.select_element_by_name(name=name)

    def get_current_url(self) -> str:
        """"Gets current page URL"""
        return self.driver.current_url()

    def find_by_name(self, name: str) -> None:
        """"Selects element by name"""
        self.send_keys(MainPageHeaderLocators.SEARCH_BAR_INPUT, name)

    def execute_script(self, by_locator: tuple, script: str) -> None:
        """Executes JS script on element"""
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script(script, element)

    def send_ESC_key(self) -> None:
        """Send ESC key to window application"""
        self.actions.send_keys(Keys.ESCAPE).perform()

    def get_screenshot(self) -> None:
        """Perform screenshot during tests"""
        self.driver.get_screenshot_as_png()
    @staticmethod
    def get_random_string(length: int) -> str:
        """"Generates random string

        :param length: length of randomly generated string
        :return: random generated string
        """
        letters = string.ascii_lowercase
        result_string = ''.join(random.choice(letters) for i in range(length))
        return result_string

    def get_tab_column_content(self, column_index: int) -> list:
        """"Gets text from selected column
        
        :param column_index: index of selected column
        :return: list contains columns content
        """
        column_content = []
        tab_body = self.driver.find_element(By.TAG_NAME, "tbody")
        rows = tab_body.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            col = row.find_elements(By.TAG_NAME, "td")[column_index]
            column_content += col.text
        return column_content

    def ctrl_click(self, tag_name: str) -> None:
        """"Performs left-mouse click while CTRL key is pressed
        
        :param tag_name: web element on which command is performed
        """
        element = self.driver.find_element(By.TAG_NAME, tag_name)
        self.actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    def click_on_coordinates(self, element_xpath: str, x: int, y: int) -> None:
        """"Clicks on given element with OX and OY coordinates
        
        :param element_xpath: XPATH route to web element
        :param x: horizontal coordinate
        :param y: vertical coordinate
        """
        element = self.driver.find_element(By.XPATH, element_xpath)
        self.actions.move_to_element_with_offset(element, x, y).click().perform()
