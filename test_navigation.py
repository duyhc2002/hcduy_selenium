from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
sleep(7)
driver.get("https://www.google.com/")
print(driver.title)
sleep(7)

driver.back()
print(driver.title)