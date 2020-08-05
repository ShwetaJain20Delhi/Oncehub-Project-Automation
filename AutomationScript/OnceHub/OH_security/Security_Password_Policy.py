from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Security_Locators import Security_Password_Policies, Security
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class security_password_policies():
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

    def security_password(self):
        password = Security_Password_Policies(self.driver)
        password.click_on_security_password_policies()
        time.sleep(3)
        password.select_passwordLength_dropdown()
        time.sleep(3)
        password.select_any_value_from_dropdown()
        time.sleep(3)
        password.select_capitalletters_from_complexity()
        time.sleep(3)
        password.select_specialcharacters_from_complexity()
        time.sleep(3)
        password.select_2ndoption_from_password_expiration()
        time.sleep(3)
        password.select_2ndoption_from_password_history()
        time.sleep(3)
        password.click_discard_button()
        time.sleep(5)
        driver.close()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    pass_policies = security_password_policies(driver)
    pass_policies.server_login()
    pass_policies.security()
    pass_policies.security_password()