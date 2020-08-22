import time

from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Applicationlogin


class Login():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def login_to_OH(self):
        login = Applicationlogin(self.driver)
        login.enter_username("basis-studied-57@staticso2.com")
        time.sleep(3)
        login.enter_password("testing@123")
        time.sleep(3)
        login.click_login()
        time.sleep(10)