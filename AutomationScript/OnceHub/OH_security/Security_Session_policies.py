from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Security_Locators import Security, Security_Session_Policies
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class security_session_policies():
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
        secure.click_on_Security()
    def security_session(self):
        session = Security_Session_Policies(self.driver)
        session.scroll_till_security_session_visible()
        session.click_on_security_session_policies()
        session.select_2ndoption_from_password_policies()
        session.select_1stoption_from_password_policies()
        session.select_save_button()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    session_policies = security_session_policies(driver)
    session_policies.server_login()
    session_policies.security()
    session_policies.security_session()
    driver.close()