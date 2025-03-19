import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@name = 'user-name']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
try:
    driver.find_element(By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
    print("True")
    assert True
except:
    print("False")
    assert False
