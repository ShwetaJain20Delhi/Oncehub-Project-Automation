from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from AutomationScript.Locators.OH_Locators.OH_AddRemoveUsers_Locators import users, Add_user, inbox_email
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Add_Users():
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

    def add_user(self):
        user_add = Add_user(self.driver)
        user_add.select_adduser_option()
        time.sleep(3)
        user_add.enter_first_name("Test")
        time.sleep(2)
        user_add.enter_last_name("User")
        time.sleep(2)
        user_add.enter_email("shweta@staticso2.com")
        time.sleep(2)
        user_add.click_create_user_send_invitation_button()
        time.sleep(8)
        user_add.select_users()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    adding_user = Add_Users(driver)
    adding_user.server_login()
    adding_user.Users()
    adding_user.add_user()
    driver.close()


   ############################ Add user with Inbox email ##########################################
# class Add_Users():
#     driver = None
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def inbox_email_copy(self):
#         email = inbox_email(self.driver)
#         email.launch_inbox_email()
#         email.copy_inbox_email()
#
#     def server_login(self):
#         personal_setting = OH_personal_setting(driver)
#         personal_setting.navigate_to_url()
#         personal_setting.login_to_OH()
#         personal_setting.select_my_profile()
#         time.sleep(10)
#
#     def Users(self):
#         user_module = users(self.driver)
#         user_module.click_on_Users()
#         time.sleep(5)
#
#     def add_user(self):
#         user_add = Add_user(self.driver)
#         user_add.select_adduser_option()
#         time.sleep(3)
#         user_add.enter_first_name("Test")
#         time.sleep(2)
#         user_add.enter_last_name("User")
#         time.sleep(2)
#         user_add.enter_email(Keys.CONTROL+ "v")
#         time.sleep(2)
#         user_add.click_create_user_send_invitation_button()
#         time.sleep(7)
#         user_add.select_users()
#         time.sleep(5)
#         driver.close()
#
#
# if __name__ == "__main__":
#     driver = get_chrome_driver().launch_chrome()
#     adding_user = Add_Users(driver)
#     adding_user.inbox_email_copy()
#     adding_user.server_login()
#     adding_user.Users()
#     adding_user.add_user()
