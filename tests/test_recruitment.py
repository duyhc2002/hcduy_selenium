import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage

def test_recruitment(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    sleep(3)
    recruitment_page = RecruitmentPage(driver)
    recruitment_page.recruitment()
    sleep(3)
    recruitment_page.add_vacancy()
    sleep(3)
    recruitment_page.edit_vacancy()
    sleep(3)
    recruitment_page.return_to_recruitment()
    sleep(3)
    recruitment_page.is_upgraded_button_displayed()
