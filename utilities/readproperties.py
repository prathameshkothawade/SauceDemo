import configparser

config = configparser.RawConfigParser()
config.read("G:\\Sauce_demo_Automation_pract\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def GetLoginUrl():
        LoginUrl = config.get('login info', 'loginUrl')
        return LoginUrl

    @staticmethod
    def GetUsername():
        Username = config.get('login info', 'username')
        return Username

    @staticmethod
    def GetPassword():
        Password = config.get('login info', 'password')
        return Password
