import pytest
from pathlib import Path
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=10)
    driver.get('https://opensource-demo.orangehrmlive.com/')
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(), 
                name="Failure Screenshot", 
                attachment_type=AttachmentType.PNG
            )