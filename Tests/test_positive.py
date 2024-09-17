from page_objects.home_page import HomePage
from page_objects.careers_page import CareersPage
from page_objects.quality_assurance_page import QualityAssurancePage


class TestScenario:
    def test_insider_homepage(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.page_is_loaded(), 'Page is not loaded'

    def test_careers_page(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.click_company()
        home_page.click_careers()
        careers_page = CareersPage(driver)
        assert careers_page.current_url == careers_page.expected_url, 'Expected page is not opened'
        assert careers_page.section_locations_is_displayed(), 'Section "Locations" is not displayed'
        assert careers_page.section_teams_is_displayed(), 'Section "Teams" is not displayed'
        assert careers_page.section_life_is_displayed(), 'Section "Life" is not displayed'
        quality_assurance_page = QualityAssurancePage(driver)
        quality_assurance_page.open()
        quality_assurance_page.click_see_all_jobs()
        quality_assurance_page.filter_by_location("Istanbul, Turkey")
        quality_assurance_page.filter_by_department("Quality Assurance")
        assert quality_assurance_page.job_list_is_displayed(), 'Job list is not displayed'

    def test_job_list(self, driver):
        quality_assurance_page = QualityAssurancePage(driver)
        quality_assurance_page.open()
        quality_assurance_page.click_see_all_jobs()
        quality_assurance_page.filter_by_location("Istanbul, Turkey")
        quality_assurance_page.filter_by_department("Quality Assurance")
        assert quality_assurance_page.job_list_is_displayed(), 'Job list is not displayed'
        jobs = quality_assurance_page.get_all_jobs()
        for job in jobs:
            assert 'Quality Assurance' in job['title'], 'Job title does not contain "Quality Assurance"'
            assert 'Quality Assurance' in job['department'], 'Department is not "Quality Assurance"'
            assert 'Istanbul, Turkey' in job['location'], 'Location is not "Istanbul, Turkey"'

    def test_view_role_redirect(self, driver):
        quality_assurance_page = QualityAssurancePage(driver)
        quality_assurance_page.open()
        quality_assurance_page.click_see_all_jobs()
        quality_assurance_page.filter_by_location("Istanbul, Turkey")
        quality_assurance_page.filter_by_department("Quality Assurance")
        quality_assurance_page.click_view_role_button()
        quality_assurance_page.switch_to_new_window()
        assert 'https://jobs.lever.co/' in quality_assurance_page.current_url
