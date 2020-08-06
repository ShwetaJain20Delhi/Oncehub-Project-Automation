from AutomationScript.Locators.OH_Locators.OH_AddRemoveUsers_Locators import users, Remove_user, Resend_link
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver
import time


class Resend_invitation():
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

    def Resend_invitation_link(self):
        resend = Resend_link(self.driver)
        resend.click_on_user_3dot()
        time.sleep(5)
        resend.select_Resend_invitation_option()
        time.sleep(5)
        resend.click_close()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    resend_invite = Resend_invitation(driver)
    resend_invite.server_login()
    resend_invite.Users()
    resend_invite.Resend_invitation_link()
    driver.close()


