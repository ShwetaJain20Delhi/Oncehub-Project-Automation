from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Settings_OH
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class oh_settings():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def Oh_settings_module(self):
        setting = Settings_OH(self.driver)
        setting.Scroll_till_settingsoption_visible()
        setting.select_settings_oh()
        time.sleep(3)
        setting.click_deleteaccount_option()
        time.sleep(3)
        setting.select_checkbox_on_popup()
        time.sleep(3)
        setting.select_keepmyaccount_option()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    password = oh_settings(driver)
    password.server_login()
    password.Oh_settings_module()
    driver.close()