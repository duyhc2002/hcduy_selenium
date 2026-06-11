import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver

        self.recruitment_btn = (By.XPATH, '//a[contains(@href,"recruitment")]')
        self.vacancies_btn = (By.LINK_TEXT, "Vacancies")
        self.job_title = (By.XPATH, "//div[@role='option' and normalize-space()='Database Administrator']")
        self.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')
    def recruitment(self):
        self.driver.find_element(*self.recruitment_btn).click()
        self.driver.find_element(*self.vacancies_btn).click()
        self.driver.find_element(*self.job_title).click()
    def is_upgraded_button_displayed(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.upgrade_btn)).is_displayed()