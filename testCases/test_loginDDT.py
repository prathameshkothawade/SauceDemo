from utilities import XLutils
from PageObjects.LoginPage import Login_Class
from selenium import webdriver


class Test_DDTparam_Class:
    xlPath = "G:\\Sauce_demo_Automation_pract\\testData\\ddt.xlsx"

    def test_ddt_login(self, setup):
        self.driver = setup
        self.ln = Login_Class(self.driver)

        self.row = XLutils.RowCount(self.xlPath, "Sheet1")
        print("Number of rows in excel is ->" + str(self.row))

        Login_Status_List = []
        for r in range(2, self.row + 1):
            self.name = XLutils.ReadData(self.xlPath, "Sheet1", r, 2)
            self.password = XLutils.ReadData(self.xlPath, "Sheet1", r, 3)
            self.exp_result = XLutils.ReadData(self.xlPath, "Sheet1", r, 4)
            self.driver.get("https://www.saucedemo.com/")
            self.ln.Enter_Username(self.name)
            self.ln.Enter_Password(self.password)
            self.ln.Click_login()
            if self.ln.VerifyTitle == "Success":
                if self.exp_result == "Pass":
                    Login_Status_List.append("Pass")
                    self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\Loginpass1.png")
                    self.ln.Click_Menu()
                    self.ln.Click_Logout()
                    XLutils.WriteData(self.xlPath, "Sheet1", r, 5, "Pass")
                elif self.exp_result == "Fail":
                    Login_Status_List.append("Fail")
                    self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\Loginfail1.png")
                    self.ln.Click_Menu()
                    self.ln.Click_Logout()
                    XLutils.WriteData(self.xlPath, "Sheet1", r, 5, "Fail")
            if self.ln.VerifyTitle() == "False":
                if self.exp_result == "Pass":
                    Login_Status_List.append("Fail")
                    self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\Loginfail2.png")
                    XLutils.WriteData(self.xlPath, "Sheet1", r, 5, "Fail")
                elif self.exp_result == "Fail":
                    Login_Status_List.append("Pass")
                    self.driver.save_screenshot("G:\\Sauce_demo_Automation_pract\\Screenshots\\Loginfail3.png")
                    XLutils.WriteData(self.xlPath, "Sheet1", r, 5, "Pass")

        print(Login_Status_List)
        if "Fail" not in Login_Status_List:
            assert True
        else:
            assert False
