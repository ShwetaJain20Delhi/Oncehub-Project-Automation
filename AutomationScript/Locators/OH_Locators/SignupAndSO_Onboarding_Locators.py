from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class inbox_email():
    def __init__(self, driver):
        self.driver = driver
    def launch_inbox_email(self):
        self.driver.get("https://inbox.staticso2.com/")
    def copy_inbox_email(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='div-domain']"))).click()


class Signup():
    def __init__(self, driver):
        self.driver = driver
        self.name = "name"
        self.email = "email"
        self.password = "password"
        self.Repassword = "retypePassword"
    def Navigate_to_URL(self):
        self.driver.get("https://account2.onceplatform.com/signup")
        self.driver.implicitly_wait(35)
    def Enter_1stName(self, fname):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.name))).send_keys(fname)
    def Enter_email(self, email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.email))).send_keys(email)
    def Enter_password(self, password):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.password))).send_keys(password)
    def ReEnter_password(self, repassword):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.Repassword))).send_keys(repassword)
    def click_signup_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "signUp"))).click()


class Product_selection():
    def __init__(self, driver):
        self.driver = driver
    def select_so_product(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(ec.visibility_of_element_located((By.ID, "so-get-started"))).click()


class Timezone_selection():
    def __init__(self, driver):
        self.driver = driver
    def select_sunday(self):
        wait = WebDriverWait(self.driver, 80)
        wait.until(ec.presence_of_element_located((By.ID, "sunday"))).click()
    def select_saturday(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.ID, "saturday"))).click()
    def click_on_change_timezone(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "changetz"))).click()
    def click_on_dropdown(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "selectedCountry"))).click()
    def search_India(self, country):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@class='oui-input-element oui-select-search-input oui-input oui-primary cdk-text-field-autofill-monitored']"))).send_keys(country)
    def select_timezone(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'India')]"))).click()
    def click_save(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "saveTimeZone"))).click()
    def click_continue(self):
        flag = self.driver.find_element_by_id("continue")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "continue"))).click()

class Calendar_connection():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.ews_url = "ewsUrl"
    def click_calendar_expand_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// span[contains(text(), ' Using another calendar type?')]"))).click()
    def click_exchange_connect_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "ExchangeCalendarConnectBtn"))).click()
    def enter_username(self, email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, self.email))).send_keys(email)
    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, self.password))).send_keys(password)
    def expand_advanced_setting(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),' Advanced settings')]"))).click()
    def enter_ews_url(self, url):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, self.ews_url))).send_keys(url)
    def click_connect_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Connect']"))).click()
    def click_continue(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),' Continue ')]"))).click()


class video_conferencing():
    def __init__(self, driver):
        self.driver = driver
    def click_skip_for_video_conferencing(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@id='setUpLater']"))).click()


class test_booking():
    def __init__(self, driver):
        self.driver = driver
    def click_skip_for_test_booking(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// span[contains(text(), 'Skip')]"))).click()


class skip_tour():
    def __init__(self, driver):
        self.driver = driver
    def click_skip_for_test_booking(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Skip tour')]"))).click()


class chatonce():
    def __init__(self, driver):
        self.driver = driver
    def click_on_setup(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// span[@class ='product-link']"))).click()
    def select_ChatOnce(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'ChatOnce setup')]"))).click()
    def click_Get_started_button_on_popup(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// span[contains(text(), 'Get started')]"))).click()


class logout():
    def __init__(self, driver):
        self.driver = driver
    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='rAccountIcon']"))).click()
    def click_signout(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Sign out')]"))).click()


class select_CO_product():
    def __init__(self, driver):
        self.driver = driver
    def select_co_product(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "co-get-started"))).click()