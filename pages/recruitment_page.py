import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RecruitmentPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.recruitment_btn = (By.XPATH, '//a[contains(@href,"recruitment")]')
        self.vacancies_btn = (By.LINK_TEXT, "Vacancies")
        self.add_btn = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        self.vacancy_name_field = (By.XPATH, "//label[text()='Vacancy Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.job_title_dropdown = (By.XPATH, "//div[contains(@class,'oxd-select-text')]")
        self.job_title_option = (By.XPATH,"//span[normalize-space()='Automation Tester']")
        self.description_field = (By.XPATH, "//textarea[@placeholder='Type description here']")
        self.hiring_manager_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.hiring_manager_option = (By.XPATH, "//div[@role='option']//span[contains(text(),'Casimir')]")
        self.number_of_positions_field = (By.XPATH, "//label[text()='Number of Positions']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        self.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')
        self.active_checkbox = (By.XPATH, "//div[contains(@class,'orangerhrm-switch-wrapper')]//p[normalize-space()='Active']/following::span[1]")
        self.publish_in_rss_feed_and_web_page = (By.XPATH, "//div[contains(@class,'orangerhrm-switch-wrapper')]//p[normalize-space()='Publish in RSS Feed and Web Page']/following::span[1]")
        self.save_btn = (By.XPATH, '//button[@type="submit"]')
        self.cancel_btn = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--ghost"]')
        self.vacancy_dropdown = (By.XPATH, "//label[normalize-space()='Vacancy']/following::div[contains(@class,'oxd-select-text')][1]")
        self.vancacy_option = (By.XPATH,"//span[normalize-space()='Automation Tester (Closed)']")
        self.hiring_manager_dropdown = (By.XPATH, "//label[normalize-space()='Hiring Manager']/following::div[contains(@class,'oxd-select-text')][1]")
        self.search_btn = (By.XPATH, '//button[@type="submit"]')
    def recruitment(self):
        self.driver.find_element(*self.recruitment_btn).click()
        self.driver.find_element(*self.vacancies_btn).click()
        self.driver.find_element(*self.add_btn).click()
    def add_vacancy(self):
        self.driver.find_element(*self.vacancy_name_field).send_keys('Automation Tester')
        self.driver.find_element(*self.job_title_dropdown).click()
        self.driver.find_element(*self.job_title_option).click()
        self.driver.find_element(*self.description_field).send_keys('Automation test is running')
        self.driver.find_element(*self.hiring_manager_field).send_keys('Casimir Admin')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.hiring_manager_option)).click()
        sleep(3)
        self.driver.find_element(*self.number_of_positions_field).send_keys('1')
        checkbox = self.driver.find_element(*self.active_checkbox)

        if not checkbox.is_selected():
            self.driver.find_element(*self.active_checkbox).click()

        publish_checkbox = self.driver.find_element(*self.publish_in_rss_feed_and_web_page)
        if publish_checkbox.is_selected():
            self.driver.find_element(*self.publish_in_rss_feed_and_web_page).click()
        
        self.driver.find_element(*self.save_btn).click()
    def edit_vacancy(self):
        self.driver.find_element(*self.cancel_btn).click()
    def return_to_recruitment(self):
        self.driver.find_element(*self.job_title_dropdown).click()
        self.driver.find_element(*self.job_title_option).click()
        self.driver.find_element(*self.vacancy_dropdown).click()
        self.driver.find_element(*self.vancacy_option).click()
        self.driver.find_element(*self.hiring_manager_dropdown).click()
        self.driver.find_element(*self.hiring_manager_option).click()
        self.driver.find_element(*self.search_btn).click()

    def is_upgraded_button_displayed(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.upgrade_btn)).is_displayed()