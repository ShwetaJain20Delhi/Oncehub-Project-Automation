import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SO_setup_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_share_publish_page(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconShareandPublish']"))).click()
    def click_on_Mail_merge(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Mail merge')]"))).click()
    def click_on_Website_embed(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//li[@id='EmbedLi']//a[contains(text(),'Website embed')]"))).click()
    def click_on_Website_button(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//li[@id='ButtonLi']//a[contains(text(),'Website button')]"))).click()
    def click_on_Website_widget(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//li[@id='WidgetLi']//a[contains(text(),'Website widget')]"))).click()


class SO_integration_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_integration_page(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon integrationIcon']"))).click()
    def click_on_calendar(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Calendar')]"))).click()
        time.sleep(4)
        self.driver.back()
    def click_on_Video_conferencing(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Video conferencing')]"))).click()
        time.sleep(4)
        self.driver.back()
    def click_on_CRM(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'CRM')]"))).click()
        time.sleep(4)
        self.driver.back()
    def click_on_Zapier(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Zapier')]"))).click()
        time.sleep(4)
        self.driver.back()
    def click_on_Payment(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Payment')]"))).click()
        time.sleep(4)
        self.driver.back()
    def click_on_Webhook_and_API(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Webhook & API')]"))).click()
        time.sleep(4)
        self.driver.back()




class SO_Reports_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Reports_page(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconReports']"))).click()
    def click_on_Event_type_report(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Event type reports')]"))).click()
    def click_on_Booking_page_reports(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Booking page reports')]"))).click()
    def click_on_Master_page_reports(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Master page reports')]"))).click()
    def click_on_Customer_reports(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Customer reports')]"))).click()
    def click_on_User_reports(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'User reports')]"))).click()
    def click_on_Account_reports(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Account reports')]"))).click()
    def click_on_Revenue_reports(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Revenue reports')]"))).click()


class SO_booking_from_editor_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_booking_form_editor(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconBFE']"))).click()


class SO_Resource_pools_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Resource_pools(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconRP']"))).click()
    def click_on_add_resource_pool_button(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Resource pool')]"))).click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, "name"))).send_keys("Test1")
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@title='Click to save & edit']"))).click()
    def click_on_resources_tab(self):
        time.sleep(10)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Resources')]"))).click()
    def click_on_drop_down_for_adding_BP(self):
        time.sleep(10)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//app-multi-select-dropdown//div[@class='dropholder']"))).click()
    def select_any_BP(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),'test567')]"))).click()
    def click_add_button(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@title='Click Here To Add']"))).click()
    def click_save_button(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// input[ @ value = 'Save'"))).click()


class SO_Notification_template_editor_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Notification_template_editor(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconNTE']"))).click()


class SO_theme_designer_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Theme_designer(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconThemeE']"))).click()

class SO_Locatization_editor_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Localization_editor(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconLanguageE']"))).click()


class SO_email_from_your_domain_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_email_from_your_domain(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='settingIcon iconEFRD']"))).click()

