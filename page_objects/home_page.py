from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class HomePage(BasePage):
    __url = 'https://useinsider.com/'
    __nav_company_dropdown = (By.XPATH, '/html/body/nav/div[2]/div/ul[1]/li[6]/a')
    __nav_company_careers_list = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]/div/div[2]/a[2]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._driver.get(self.__url)

    def page_is_loaded(self):
        return super()._page_is_loaded()

    def click_company(self):
        super()._click(self.__nav_company_dropdown)

    def click_careers(self):
        super()._click(self.__nav_company_careers_list)
