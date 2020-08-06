from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Billing_Locators import Billing, Billing_Product
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class BillingPage():
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
        time.sleep(4)
        bill.click_on_Billing()
        time.sleep(4)

    def Billing_product(self):
        bill_notification = Billing_Product(self.driver)
        bill_notification.click_on_Billing_product()
        time.sleep(4)
        bill_notification.click_on_whatisscheduleonce()
        time.sleep(4)
        bill_notification.close_so_popup()
        time.sleep(4)
        bill_notification.click_on_whatisinviteonce()
        time.sleep(4)
        bill_notification.close_io_popup()
        time.sleep(4)
        bill_notification.view_sms_log()
        time.sleep(8)
        self.driver.back()
        time.sleep(3)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    billprod = BillingPage(driver)
    billprod.server_login()
    billprod.Billing()
    billprod.Billing_product()
    driver.close()