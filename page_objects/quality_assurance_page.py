from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from page_objects.base_page import BasePage


class QualityAssurancePage(BasePage):
    __url = 'https://useinsider.com/careers/quality-assurance/'
    __link_see_all_jobs = (By.LINK_TEXT, 'See all QA jobs')
    __job_list = (By.XPATH, '//div[@id="jobs-list"]')
    __dropdown_filter_by_location = (By.XPATH, '//select[@id="filter-by-location"]')
    __dropdown_filter_by_location_option = (By.XPATH, '//*[@id="filter-by-location"]/option[2]')
    __dropdown_filter_by_department = (By.XPATH, '//select[@id="filter-by-department"]')
    __dropdown_filter_by_department_option = (By.XPATH, '//*[@id="filter-by-location"]/option[2]')
    __job_items = (By.CSS_SELECTOR, '#jobs-list .position-list-item')
    __position_title = (By.CSS_SELECTOR, '.position-title')
    __position_department = (By.CSS_SELECTOR, '.position-department')
    __position_location = (By.CSS_SELECTOR, '.position-location')
    __button_view_role = (By.XPATH, '//*[@id="jobs-list"]/div/div/a')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._driver.get(self.__url)

    def click_see_all_jobs(self):
        super()._close_cookie_consent()
        super()._click(self.__link_see_all_jobs)

    def job_list_is_displayed(self) -> bool:
        return super()._is_displayed(self.__job_list)

    def filter_by_location(self, option: str):
        select_element = super()._find(self.__dropdown_filter_by_location)
        select = Select(select_element)
        super()._wait_until_element_is_visible(self.__dropdown_filter_by_location_option)
        select.select_by_visible_text(option)

    def filter_by_department(self, option: str):
        select_element = super()._find(self.__dropdown_filter_by_department)
        select = Select(select_element)
        super()._wait_until_element_is_visible(self.__dropdown_filter_by_department_option)
        select.select_by_visible_text(option)

    def get_all_jobs(self):
        self._driver.execute_script('window.scrollBy(0, 600);')
        job_elements = super()._find_elements(self.__job_items)
        jobs = []
        for job_element in job_elements:
            title = job_element.find_element(*self.__position_title).text
            department = job_element.find_element(*self.__position_department).text
            location = job_element.find_element(*self.__position_location).text
            jobs.append({
                'title': title,
                'department': department,
                'location': location
            })
        return jobs

    def click_view_role_button(self):
        super()._close_cookie_consent()
        super()._hover(self.__position_title)
        super()._click(self.__button_view_role)

    def switch_to_new_window(self):
        window_handles = self._driver.window_handles
        new_window = window_handles[-1]
        self._driver.switch_to.window(new_window)
