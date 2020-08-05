from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Security_Locators import Security, Security_SSO_Policies
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class security_sso_policies():
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

    def security_SSO(self):
        session = Security_SSO_Policies(self.driver)
        session.click_on_security_sso_policies()
        time.sleep(5)
        driver.close()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    sso_policies = security_sso_policies(driver)
    sso_policies.server_login()
    sso_policies.security()
    sso_policies.security_SSO()