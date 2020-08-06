from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Privacy_Locators import Privacy, Privacy_GDPR_Information
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Privacy_info():
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

    def GDPR_Information(self):
        privacy_gdpr = Privacy_GDPR_Information(self.driver)
        privacy_gdpr.click_Privacy_GDPR()
        time.sleep(3)
        privacy_gdpr.enter_Fullname("Test 1")
        time.sleep(3)
        privacy_gdpr.enter_emailid("testinginviteoncetesting@gmail.com")
        time.sleep(3)
        privacy_gdpr.enter_address("Delhi")
        time.sleep(3)
        privacy_gdpr.click_save()
        time.sleep(4)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    info = Privacy_info(driver)
    info.server_login()
    info.Privacy()
    info.GDPR_Information()
    driver.close()
