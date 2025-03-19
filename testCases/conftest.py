import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Chrome is opening")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print("Firefox is opening")
        driver = webdriver.Firefox()
    elif browser == 'Edge':
        print("Edge is opening")
        driver = webdriver.Edge()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver


@pytest.fixture(params=[
    ("standard_user","secret_sauce","Pass"),
    ("standard_user1","secret_sauce","Fail"),
    ("standard_user","secret_sauce1","Fail"),
    ("standard_user1","secret_sauce1","Fail")

])
def getDataForLogin(request):
    return request.param