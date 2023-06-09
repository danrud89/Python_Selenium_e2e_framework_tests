from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from utils.settings import HEADLESS, WINDOW_SIZE


class DriverFactory:
    @staticmethod
    def get_driver(browser):
        try:
            if browser == "chrome":
                chrome_options = ChromeOptions()
                chrome_options.headless = HEADLESS
                chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")
                return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
            elif browser == "firefox":
            
                #Watch out if using Linux OS -> may require manually download latest version of GeckoDriverManager
                
                firefox_options = FirefoxOptions()
                firefox_options.headless = HEADLESS
                firefox_options.add_argument(f"--window-size={WINDOW_SIZE}")
                return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        except AttributeError:
            print('Provide valid web-driver name')

