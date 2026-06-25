import pytest
from pathlib import Path
import requests 
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from utils.config_reader import ConfigReader
from selenium.webdriver.chrome.options import Options
@pytest.fixture
def driver():
    options = Options()
    is_headless = ConfigReader.get_isheadless()
    #print(f"isHeadless = {is_headless}")
    if is_headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
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