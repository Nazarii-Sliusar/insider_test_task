from typing import List
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> List[WebElement]:
        self._wait_until_element_is_visible(locator)
        return self._driver.find_elements(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, tim: int = 10):
        wait = WebDriverWait(self._driver, tim)
        wait.until(EC.visibility_of_element_located(locator))

    def _click(self, locator: tuple, tim: int = 10):
        self._wait_until_element_is_visible(locator, tim)
        self._find(locator).click()

    def _page_is_loaded(self):
        WebDriverWait(self._driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
        return self._driver.execute_script('return document.readyState') == 'complete'

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _close_cookie_consent(self):
        cookie_consent = (By.ID, "cookie-law-info-bar")
        try:
            if self._is_displayed(cookie_consent):
                accept_button = (By.CSS_SELECTOR, "#wt-cli-accept-all-btn")
                self._click(accept_button)
        except NoSuchElementException:
            pass

    def _hover(self, locator: tuple) -> None:
        self._driver.execute_script('window.scrollBy(0, 600);')
        time.sleep(1)
        element_to_hover = self._find(locator)
        actions = ActionChains(self._driver)
        actions.move_to_element(element_to_hover).perform()
