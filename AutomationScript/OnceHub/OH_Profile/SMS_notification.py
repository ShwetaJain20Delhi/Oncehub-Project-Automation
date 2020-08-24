from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import sms_notification
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class smsnotification():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def sms_notification_module(self):
        sms = sms_notification(self.driver)
        sms.select_smsnotification_oh()
        sms.user_notification_toggle()
        sms.discard_changes()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    notification = smsnotification(driver)
    notification.server_login()
    notification.sms_notification_module()
    driver.close()