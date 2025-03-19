import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@name = 'user-name']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)
# Dropdown
dp = Select (driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
#dp.select_by_index(2)
dp.select_by_index(0)
time.sleep(5)