from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import password_policies
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class passwordpage():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def password_module(self):
        passpage = password_policies(self.driver)
        passpage.select_password_from_OH()
        time.sleep(3)
        passpage.enter_current_password("testing@1234")
        time.sleep(2)
        passpage.enter_new_password("testing@1234")
        time.sleep(2)
        passpage.Reenter_new_password("testing@1234")
        time.sleep(2)
        passpage.Discard_changes()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    password = passwordpage(driver)
    password.server_login()
    password.password_module()
    driver.close()

