from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Oh_so_module
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class OH_scheduleonce():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def OH_SO_module(self):
        so_page = Oh_so_module(self.driver)
        so_page.select_so()
        time.sleep(3)
        so_page.select_payment_integration()
        time.sleep(2)
        so_page.select_zapier_integration()
        time.sleep(2)
        so_page.discard_changes()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    so_module = OH_scheduleonce(driver)
    so_module.server_login()
    so_module.OH_SO_module()
    driver.close()