
class inbox_email():
    def __init__(self, driver):
        self.driver = driver
    def launch_inbox_email(self):
        self.driver.get("https://inbox.staticso2.com/")
    def copy_inbox_email(self):
        self.driver.find_element_by_xpath("//div[@id='div-domain']").click()


class Signup():
    def __init__(self, driver):
        self.driver = driver
        self.name = "name"
        self.email = "email"
        self.password = "password"
        self.Repassword = "retypePassword"
    def Navigate_to_URL(self):
        self.driver.get("https://account3.onceplatform.com/signup")
        self.driver.implicitly_wait(35)
    def Enter_1stName(self, fname):
        self.driver.find_element_by_name(self.name).send_keys(fname)
    def Enter_email(self, email):
        self.driver.find_element_by_name(self.email).send_keys(email)
    def Enter_password(self, password):
        self.driver.find_element_by_name(self.password).send_keys(password)
    def ReEnter_password(self, repassword):
        self.driver.find_element_by_name(self.Repassword).send_keys(repassword)
    def click_signup_button(self):
        self.driver.find_element_by_id("signUp").click()


class Product_selection():
    def __init__(self, driver):
        self.driver = driver
    def select_so_product(self):
        self.driver.find_element_by_id("so-get-started").click()


class Timezone_selection():
    def __init__(self, driver):
        self.driver = driver
    def select_sunday(self):
        self.driver.find_element_by_id("sunday").click()
    def select_saturday(self):
        self.driver.find_element_by_id("saturday").click()
    def click_on_change_timezone(self):
        self.driver.find_element_by_id("changetz").click()
    def click_on_dropdown(self):
        self.driver.find_element_by_id("selectedCountry").click()
    def search_India(self, country):
        self.driver.find_element_by_xpath("//input[@class='oui-select-search-input oui-input-element oui-input oui-primary cdk-text-field-autofill-monitored']").send_keys(country)
    def select_timezone(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'India')]").click()
    def click_save(self):
        self.driver.find_element_by_id("saveTimeZone").click()
    def click_continue(self):
        flag = self.driver.find_element_by_id("continue")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_id("continue").click()

class Calendar_connection():
    def __init__(self, driver):
        self.driver = driver
        self.email = "email"
        self.password = "password"
        self.ews_url = "ewsUrl"
    def click_calendar_expand_button(self):
        self.driver.find_element_by_xpath("// span[contains(text(), ' Using another calendar type?')]").click()
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
    def click_continue(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' Continue ')]").click()


class video_conferencing():
    def __init__(self, driver):
        self.driver = driver
    def click_skip_for_video_conferencing(self):
        self.driver.find_element_by_xpath("//a[@id='setUpLater']").click()


class test_booking():
    def __init__(self, driver):
        self.driver = driver
    def click_skip_for_test_booking(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Skip')]").click()


class skip_tour():
    def __init__(self, driver):
        self.driver = driver
    def click_skip_for_test_booking(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Skip tour')]").click()


class chatonce():
    def __init__(self, driver):
        self.driver = driver
    def click_on_setup(self):
        self.driver.find_element_by_xpath("// span[@class ='product-link']").click()
    def select_ChatOnce(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'ChatOnce setup')]").click()
    def click_Get_started_button_on_popup(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Get started')]").click()


class logout():
    def __init__(self, driver):
        self.driver = driver
    def click_profile_icon(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
    def click_signout(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Sign out')]").click()


class select_CO_product():
    def __init__(self, driver):
        self.driver = driver
    def select_co_product(self):
        self.driver.find_element_by_id("co-get-started").click()