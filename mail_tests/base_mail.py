from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import url


class base:
    def __init__(self, driver):
        self.driver = driver
        self.url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locator))
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator))
        )

    def select(self, locator, text):
        return Select(self.driver.find_element_by_css_selector(locator)).select_by_visible_text(text)

    def get_site(self):
        return self.driver.get(self.url)

    def find_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator)
