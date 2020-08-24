from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.Locators.OH_Locators.OH_Billing_Locators import Billing, Billing_Transaction
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class BillingTrans():
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

    def Billing_Transaction_page(self):
        bill_trans = Billing_Transaction(self.driver)
        bill_trans.click_on_Billing_transaction()
        bill_trans.click_on_3dot_of_transaction()
        bill_trans.select_Buyer_details_on_invoice_option()
        bill_trans.click_on_save_button()
        bill_trans.close_popup()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    billProd = BillingTrans(driver)
    billProd.server_login()
    billProd.Billing()
    billProd.Billing_Transaction_page()
    driver.close()