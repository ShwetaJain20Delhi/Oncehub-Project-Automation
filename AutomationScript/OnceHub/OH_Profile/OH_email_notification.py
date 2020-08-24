from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Emailnotification
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class emailnotification():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def Emailnotification(self):
        notification = Emailnotification(self.driver)
        notification.select_email_notification()
        notification.edit_sentfromname_field("Test Admin")
        notification.click_save()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    email = emailnotification(driver)
    email.server_login()
    email.Emailnotification()
    driver.close()

