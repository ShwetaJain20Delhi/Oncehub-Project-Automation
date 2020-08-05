from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Privacy_Locators import Privacy_GDPR_Compliance, Privacy
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Privacy_compliance():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def Privacy(self):
        bill = Privacy(self.driver)
        bill.scroll_till_privacy_visible()
        time.sleep(4)
        bill.click_on_Privacy()
        time.sleep(4)

    def Privacy_Compliance(self):
        comp = Privacy_GDPR_Compliance(self.driver)
        comp.scroll_till_privacy_compliance_visible()
        time.sleep(4)
        comp.click_privacy_compliance()
        time.sleep(4)
        comp.scroll_till_end()
        time.sleep(3)
        driver.close()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    privacy_comp = Privacy_compliance(driver)
    privacy_comp.server_login()
    privacy_comp.Privacy()
    privacy_comp.Privacy_Compliance()
