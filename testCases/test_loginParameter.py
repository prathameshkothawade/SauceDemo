from utilities.readproperties import ReadConfig
from PageObjects.LoginPage import Login_Class
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_LoginParamClass:
    LoginUrl = ReadConfig.GetLoginUrl()
    Username = ReadConfig.GetUsername()
    Password = ReadConfig.GetPassword()

    def test_LoginParam(self, setup, getDataForLogin):
        self.driver = setup
        self.driver.get(self.LoginUrl)
        self.pr = Login_Class(self.driver)
        self.pr.Enter_Username(getDataForLogin[0])
        print("Username-->" + getDataForLogin[0])
        self.pr.Enter_Password(getDataForLogin[1])
        print("Password-->" + getDataForLogin[1])
        self.pr.Click_login()
        if self.pr.VerifyTitle() == "Success":
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\LoginPass.png")
                assert True
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\LoginFail1.png")
                assert False
        else:
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\LoginFail2.png")
                assert False
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\LoginFail3.png")
                assert True

            self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\LoginFail4.png")