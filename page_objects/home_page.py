from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class HomePage(BasePage):
    _url = 'https://useinsider.com/'
    _nav_company_dropdown = (By.XPATH, '//a[contains(text(), "Company")]')
    _nav_company_careers_list = (By.XPATH, '//a[contains(text(), "Careers")]')
    _login_button = (By.XPATH, '//a[contains(text(), "Login")]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._driver.get(self._url)

    def page_is_loaded(self):
        try:
            super()._wait_until_element_is_visible(self._login_button)
            return True
        except TimeoutException:
            return False

    def click_company(self):
        super()._click(self._nav_company_dropdown)

    def click_careers(self):
        super()._click(self._nav_company_careers_list)
