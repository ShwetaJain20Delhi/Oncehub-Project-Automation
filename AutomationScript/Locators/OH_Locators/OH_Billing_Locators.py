from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Billing():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_billing_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Billing')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_Billing(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Billing')]"))).click()


class Billing_notification():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Billing_Notification(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Notifications')]"))).click()


class Billing_PaymentMethods():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Billing_payment_method(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Payment methods')]"))).click()


class Billing_Product():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Billing_product(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Products')]"))).click()
    def click_on_whatisscheduleonce(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'What is ScheduleOnce?')]"))).click()
    def close_so_popup(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Close')]"))).click()
    def click_on_whatisinviteonce(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'What is InviteOnce?')]"))).click()
    def close_io_popup(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Close')]"))).click()
    def view_sms_log(self):
        flag = self.driver.find_element_by_xpath("//a[contains(text(),'View SMS log')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'View SMS log')]"))).click()


class Billing_Transaction():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Billing_transaction(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Transactions')]"))).click()
    def click_on_3dot_of_transaction(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Transactions menu']"))).click()
    def select_Buyer_details_on_invoice_option(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Buyer details on invoice')]"))).click()
    def click_on_save_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Save')]"))).click()
    def close_popup(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Close')]"))).click()