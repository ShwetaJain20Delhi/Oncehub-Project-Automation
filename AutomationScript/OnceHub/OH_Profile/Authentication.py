from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import select_authentication
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class AuthenticationPage():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def authentication_module(self):
        auth = select_authentication(self.driver)
        auth.click_authentication()
        time.sleep(4)
        auth.enable_2factor_toggle()
        time.sleep(4)
        auth.enter_password("testing@123")
        time.sleep(4)
        auth.click_submit_button()
        time.sleep(5)
        auth.discard_changes()
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    authenticate = AuthenticationPage(driver)
    authenticate.server_login()
    authenticate.authentication_module()