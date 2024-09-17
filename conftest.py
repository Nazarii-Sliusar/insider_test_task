import pytest
from selenium import webdriver
import os


@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    if browser == 'chrome':
        my_driver = webdriver.Chrome()
    elif browser == 'firefox':
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
    yield my_driver
    my_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            screenshot_path = f'screenshots/{item.name}.png'
            driver.save_screenshot(screenshot_path)
