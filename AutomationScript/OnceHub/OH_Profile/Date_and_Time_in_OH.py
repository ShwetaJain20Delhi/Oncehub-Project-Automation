from selenium import webdriver
import time
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import datetime
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class DateAndtime():

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def datetime(self):
        date1 = datetime(self.driver)
        date1.select_datetime()
        time.sleep(2)
        date1.clickontimezone_tochange()
        time.sleep(3)
        date1.search_timezone("India")
        time.sleep(3)
        date1.select_searchedtimezone()
        time.sleep(3)
        date1.click_save()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    dateandtime = DateAndtime(driver)
    dateandtime.server_login()
    dateandtime.datetime()
    driver.close()