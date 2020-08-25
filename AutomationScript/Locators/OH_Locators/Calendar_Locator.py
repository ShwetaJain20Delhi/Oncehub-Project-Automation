import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ExchangeCalendar():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.ews_url = "ewsUrl"
    def select_calendarconnection_from_menu(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Calendar connection')]"))).click()
        time.sleep(3)
    def click_exchange_connect_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "ExchangeCalendarConnectBtn"))).click()
    def enter_username(self, email):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.email))).send_keys(email)
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.password))).send_keys(password)
    def expand_advanced_setting(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),' Advanced settings')]"))).click()
    def enter_ews_url(self, url):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.ews_url))).send_keys(url)
    def click_connect_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@title='Connect']"))).click()


class reminder_setting():
    def __init__(self, driver):
        self.driver = driver
    def click_reminder_dropdown(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//oui-select[@placeholder='Duration']//parent::div[@class='oui-form-field-infix']"))).click()
    def select_5minute_reminder(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[@class='oui-option-text' and starts-with(text(),' 5 minutes')]"))).click()


class sync_2way_setting():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_so_advanced_setting_visible(self):
        flag = self.driver.find_element_by_xpath("//p[contains(text(),'Deleting an event')]//following-sibling::div[@class='radioOuter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def change_togglevalue_for_delete_event(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//p[contains(text(),'Deleting an event')]//following-sibling::div[@class='radioOuter']"))).click()
    def change_togglevalue_for_change_event(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//p[contains(text(),'Changing the time')]//following-sibling::div[@class='radioOuter']"))).click()


class so_setup_calendarpage():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_so_continueSetup_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Continue setup')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def select_continue_setup_from_calendarpage(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "ContinueSetupBtn"))).click()


class iCloudCalendar():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
    def click_on_connect_button_for_iCloud(self):
        flag = self.driver.find_element_by_xpath("//button[@title='Connect to iCloud Calendar']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@title='Connect to iCloud Calendar']"))).click()
    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.email))).send_keys(email)
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.password))).send_keys(password)
    def click_on_connect_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),' Connect ')]//following::div[@class='oui-dialog-footer-action-right ng-star-inserted']"))).click()


class o365_via_ews_Calendar():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
    def click_on_connect_button_for_O365_EWS(self):
        # flag = self.driver.find_element_by_xpath("//button[@title='Connect to Office 365 Calendar via EWS']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@title='Connect to Office 365 Calendar via EWS']"))).click()
    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.email))).send_keys(email)
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.password))).send_keys(password)
    def click_on_connect_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),' Connect ')]//following::div[@class='oui-dialog-footer-action-right ng-star-inserted']"))).click()


class o365_via_oAuth_Calendar():
    def __init__(self, driver):
        self.driver = driver
    def click_on_connect_button_for_O365_oAuth(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@ title='Connect to Office 365 Calendar via OAuth']"))).click()
    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(email)
    def click_next_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@type='submit']"))).click()
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(password)
    def click_signin(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='submit']"))).click()
    def Accept_permission(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='submit']"))).click()


class Notification_connect():
    def __init__(self, driver):
        self.driver = driver
    def click_on_notication_icon(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[@class ='notification-icon-cont']"))).click()
    def click_connect_button_for_calendar_connection(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),' Connect your calendar ')]//following::a[contains(text(),'Connect')][1]"))).click()