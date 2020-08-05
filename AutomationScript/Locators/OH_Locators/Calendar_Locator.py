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
        self.driver.find_element_by_xpath("//span[contains(text(),' 15 minutes ') and @id='selected-values']").click()
    def select_5minute_reminder(self):
        self.driver.find_element_by_xpath("//span[@class='oui-option-text' and starts-with(text(),' 5 minutes')]").click()


class sync_2way_setting():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_so_advanced_setting_visible(self):
        flag = self.driver.find_element_by_xpath("//p[contains(text(),'Deleting an event in Exchange/Outlook Calendar cancels the booking in ScheduleOnce')]//following-sibling::div[@class='radioOuter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def change_togglevalue_for_delete_event(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Deleting an event in Exchange/Outlook Calendar cancels the booking in ScheduleOnce')]//following-sibling::div[@class='radioOuter']").click()
    def change_togglevalue_for_change_event(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Changing the time in Exchange/Outlook Calendar updates the booking in ScheduleOnce')]//following-sibling::div[@class='radioOuter']").click()


class so_setup_calendarpage():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_so_continueSetup_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Continue setup')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def select_continue_setup_from_calendarpage(self):
        self.driver.find_element_by_id("ContinueSetupBtn").click()





