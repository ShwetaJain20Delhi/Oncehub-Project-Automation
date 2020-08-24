from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Privacy_Locators import Privacy, Privacy_shield
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class PrivacyPage():
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
        bill.click_on_Privacy()

    def Privacy_Shield(self):
        privacy = Privacy_shield(self.driver)
        privacy.click_on_privacy_shield()
        privacy.Scroll_till_end()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    privacy = PrivacyPage(driver)
    privacy.server_login()
    privacy.Privacy()
    privacy.Privacy_Shield()
    driver.close()