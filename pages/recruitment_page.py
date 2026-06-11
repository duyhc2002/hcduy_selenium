import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        self.click_btn = (By.XPATH, '//button[@type="submit"]')
        self.recruitment_btn = (By.XPATH, '//a[contains(@href,"recruitment")]')
        self.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')
    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys('Admin')
        self.driver.find_element(*self.password_field).send_keys('admin123')
        self.driver.find_element(*self.click_btn).click()
        self.driver.find_element(*self.recruitment_btn).click()
    def is_upgraded_button_displayed(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.upgrade_btn)).is_displayed()