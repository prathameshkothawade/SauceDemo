from selenium.webdriver.common.by import By


class Login_Class:
    Text_Name_Xpath = (By.XPATH, "//input[@name = 'user-name']")
    Text_Password_Css = (By.CSS_SELECTOR, "input[type='password']")
    Click_Login_ID = (By.ID, "login-button")
    Verify_Title_Xpath = (By.XPATH, "//div[@class='app_logo']")
    Click_Menu_Xpath = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    Click_Logout_Xpath = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Username(self, name):
        self.driver.find_element(*Login_Class.Text_Name_Xpath).send_keys(name)

    def Enter_Password(self, password):
        self.driver.find_element(*Login_Class.Text_Password_Css).send_keys(password)

    def Click_login(self):
        self.driver.find_element(*Login_Class.Click_Login_ID).click()

    def Click_Menu(self):
        self.driver.find_element(*Login_Class.Click_Menu_Xpath).click()

    def Click_Logout(self):
        self.driver.find_element(*Login_Class.Click_Logout_Xpath).click()

    def VerifyTitle(self):
        try:
            self.driver.find_element(*Login_Class.Verify_Title_Xpath)
            print("Success")
            return "Success"
        except:
            print("False")
            return "False"
