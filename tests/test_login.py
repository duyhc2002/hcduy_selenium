import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
    sleep(3)
    login_page.is_upgraded_button_displayed()
