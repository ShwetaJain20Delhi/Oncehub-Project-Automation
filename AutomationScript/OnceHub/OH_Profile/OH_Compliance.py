from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import compliance
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class compliancepage():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def compliance_module(self):
        comp = compliance(self.driver)
        comp.movescrollbar_tillcompliancevisible()
        comp.select_compliance()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    compli = compliancepage(driver)
    compli.server_login()
    compli.compliance_module()
    driver.close()
