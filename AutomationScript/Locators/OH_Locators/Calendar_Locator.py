import time


class ExchangeCalendar():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.ews_url = "ewsUrl"
    def select_calendarconnection_from_menu(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Calendar connection')]").click()
    def click_exchange_connect_button(self):
        self.driver.find_element_by_id("ExchangeCalendarConnectBtn").click()
    def enter_username(self, email):
        self.driver.find_element_by_id(self.email).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).send_keys(password)
    def expand_advanced_setting(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' Advanced settings')]").click()
    def enter_ews_url(self, url):
        self.driver.find_element_by_id(self.ews_url).send_keys(url)
    def click_connect_button(self):
        self.driver.find_element_by_xpath("//button[@title='Connect']").click()


class reminder_setting():
    def __init__(self, driver):
        self.driver = driver
    def click_reminder_dropdown(self):
        self.driver.find_element_by_xpath("//oui-select[@placeholder='Duration']//parent::div[@class='oui-form-field-infix']").click()
    def select_5minute_reminder(self):
        self.driver.find_element_by_xpath("//span[@class='oui-option-text' and starts-with(text(),' 5 minutes')]").click()


class sync_2way_setting():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_so_advanced_setting_visible(self):
        flag = self.driver.find_element_by_xpath("//p[contains(text(),'Deleting an event')]//following-sibling::div[@class='radioOuter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def change_togglevalue_for_delete_event(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Deleting an event')]//following-sibling::div[@class='radioOuter']").click()
    def change_togglevalue_for_change_event(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Changing the time')]//following-sibling::div[@class='radioOuter']").click()


class so_setup_calendarpage():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_so_continueSetup_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Continue setup')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def select_continue_setup_from_calendarpage(self):
        self.driver.find_element_by_id("ContinueSetupBtn").click()


class iCloudCalendar():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
    def click_on_connect_button_for_iCloud(self):
        flag = self.driver.find_element_by_xpath("//button[@title='Connect to iCloud Calendar']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//button[@title='Connect to iCloud Calendar']").click()
    def enter_email(self, email):
        self.driver.find_element_by_id(self.email).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).send_keys(password)
    def click_on_connect_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' Connect ')]//following::div[@class='oui-dialog-footer-action-right ng-star-inserted']").click()


class o365_via_ews_Calendar():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
    def click_on_connect_button_for_O365_EWS(self):
        # flag = self.driver.find_element_by_xpath("//button[@title='Connect to Office 365 Calendar via EWS']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//button[@title='Connect to Office 365 Calendar via EWS']").click()
    def enter_email(self, email):
        self.driver.find_element_by_id(self.email).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).send_keys(password)
    def click_on_connect_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' Connect ')]//following::div[@class='oui-dialog-footer-action-right ng-star-inserted']").click()


class o365_via_oAuth_Calendar():
    def __init__(self, driver):
        self.driver = driver
    def click_on_connect_button_for_O365_oAuth(self):
        self.driver.find_element_by_xpath("//button[@ title='Connect to Office 365 Calendar via OAuth']").click()
    def enter_email(self, email):
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
    def click_next_button(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
    def enter_password(self, password):
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    def click_signin(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
    def Accept_permission(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()


class Notification_connect():
    def __init__(self, driver):
        self.driver = driver
    def click_on_notication_icon(self):
        self.driver.find_element_by_xpath("//span[@class ='notification-icon-cont']").click()
    def click_connect_button_for_calendar_connection(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Connect')]").click()