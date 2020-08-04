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
    def



