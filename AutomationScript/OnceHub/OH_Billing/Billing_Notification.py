from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Billing_Locators import Billing
from AutomationScript.Locators.OH_Locators.OH_Billing_Locators import Billing_notification
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class BillingNotify():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def Billing(self):
        bill = Billing(self.driver)
        bill.scroll_till_billing_visible()
        bill.click_on_Billing()

    def Billing_notification(self):
        bill_notification = Billing_notification(self.driver)
        bill_notification.click_on_Billing_Notification()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    billnot = BillingNotify(driver)
    billnot.server_login()
    billnot.Billing()
    billnot.Billing_notification()
    driver.close()