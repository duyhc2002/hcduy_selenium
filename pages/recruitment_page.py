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
        self.job_title_dropdown = (By.XPATH, "//div[contains(@class,'oxd-select-text')]")
        self.job_title_option = (By.XPATH,"//span[normalize-space()='Automaton Tester']")
        self.vancacy_dropdown = (By.XPATH, "//label[normalize-space()='Vacancy']/following::div[contains(@class,'oxd-select-text')][1]")
        self.vancacy_option = (By.XPATH,"//span[normalize-space()='Automation Tester For 13/06/2026']")
        self.hiring_manager_dropdown = (By.XPATH, "//label[normalize-space()='Hiring Manager']/following::div[contains(@class,'oxd-select-text')][1]")
        self.hiring_manager_option = (By.XPATH,"//span[normalize-space()='Rahul Patil']")
        self.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')
    def recruitment(self):
        self.driver.find_element(*self.recruitment_btn).click()
        self.driver.find_element(*self.vacancies_btn).click()
        self.driver.find_element(*self.job_title_dropdown).click()
        self.driver.find_element(*self.job_title_option).click()
        self.driver.find_element(*self.vancacy_dropdown).click()
        self.driver.find_element(*self.vancacy_option).click()
        self.driver.find_element(*self.hiring_manager_dropdown).click()
        self.driver.find_element(*self.hiring_manager_option).click()
    def is_upgraded_button_displayed(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.upgrade_btn)).is_displayed()