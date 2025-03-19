import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Login
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@name = 'user-name']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
# Add products
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
# Click on cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# Click on checkout
driver.find_element(By.NAME, "checkout").click()
# Enter details
driver.find_element(By.ID, "first-name").send_keys("pratham")
driver.find_element(By.ID, "last-name").send_keys("sk")
driver.find_element(By.ID, "postal-code").send_keys("411011")
time.sleep(5)
# Click on finish
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
try:
    driver.find_element(By.XPATH, "//h2[@class='complete-header']")
    print("Success")
    assert True
except:
    print("Failed")
    assert False
