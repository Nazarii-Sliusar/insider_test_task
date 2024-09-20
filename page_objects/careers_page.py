from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class CareersPage(BasePage):
    _url = 'https://useinsider.com/careers/'
    _section_locations = (By.XPATH, '//section[@id="career-our-location"]')
    _section_teams = (By.XPATH, '//section[@id="career-find-our-calling"]')
    _section_life = (By.XPATH, '//h2[contains(text(), "Life at Insider")]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    def section_locations_is_displayed(self) -> bool:
        return super()._is_displayed(self._section_locations)

    def section_teams_is_displayed(self) -> bool:
        return super()._is_displayed(self._section_teams)

    def section_life_is_displayed(self) -> bool:
        return super()._is_displayed(self._section_life)
