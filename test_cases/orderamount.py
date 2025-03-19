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

l = len(driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/div/div"))
print(l)

Price_List = []
for r in range(1,l+1):
    Var = driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
    Product_Price = (Var[1:])
    Price_List.append(float(Product_Price))

    Var2 = sum(Price_List)
    Sub_Total = round(Var2,2)
    print(Sub_Total)
    Exp_Tax = round((Sub_Total * 3.20),2)
    print(Exp_Tax)

