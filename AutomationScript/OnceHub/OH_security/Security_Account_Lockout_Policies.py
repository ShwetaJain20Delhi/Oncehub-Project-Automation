from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Security_Locators import Security, Security_lockout_policies
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class security_Account_lockout_policies():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def security(self):
        secure = Security(self.driver)
        secure.scroll_till_security_visible()
        time.sleep(4)
        secure.click_on_Security()
        time.sleep(4)

    def security_account_lockout(self):
        lockout = Security_lockout_policies(self.driver)
        lockout.click_on_security_Lockout_policies()
        time.sleep(3)
        lockout.click_on_account_lockout_enabled()
        time.sleep(3)
        lockout.click_on_account_lockout_disabled()
        time.sleep(3)
        lockout.click_save_button()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    lockout_policies = security_Account_lockout_policies(driver)
    lockout_policies.server_login()
    lockout_policies.security()
    lockout_policies.security_account_lockout()
    driver.close()