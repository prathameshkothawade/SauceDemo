from utilities.readproperties import ReadConfig
from PageObjects.LoginPage import Login_Class
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_LoginClass:

    LoginUrl = ReadConfig.GetLoginUrl()
    Username = ReadConfig.GetUsername()
    Password = ReadConfig.GetPassword()

    def test_Login(self, setup):
        self.driver = setup
        self.LC = Login_Class(self.driver)

        self.driver.get(self.LoginUrl)
        self.LC.Enter_Username(self.Username)
        self.LC.Enter_Password(self.Password)
        self.LC.Click_login()
        if self.LC.VerifyTitle() == "Success":
            print("Success")
            assert True
        else:
            print("Fail")
            assert False

