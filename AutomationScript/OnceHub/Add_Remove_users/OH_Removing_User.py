from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from AutomationScript.Locators.OH_Locators.OH_AddRemoveUsers_Locators import users, Remove_user
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Remove_Users():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def Users(self):
        user_module = users(self.driver)
        user_module.click_on_Users()
        time.sleep(5)

    def Remove_user(self):
        remove = Remove_user(self.driver)
        remove.click_on_user_3dot()
        time.sleep(3)
        remove.select_delete_user_profile()
        time.sleep(3)
        remove.click_on_delete_user_profile_button()
        time.sleep(10)
        remove.click_on_close_button()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    removing_user = Remove_Users(driver)
    removing_user.server_login()
    removing_user.Users()
    removing_user.Remove_user()
    driver.close()

