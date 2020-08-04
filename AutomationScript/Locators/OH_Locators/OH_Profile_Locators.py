class Applicationlogin():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "email"
        self.password_textbox_name = "password"
        self.login_button_id = "signIn"
    def enter_username(self, username):
         self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)
    def click_login(self):
        self.driver.find_element_by_id("signIn").click()


class Personalsetting():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_lastname = "lastName"
    def click_profile_icon(self):
        self.driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
    def select_myprofile(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'My profile')]").click()
    def click_3dot(self):
        self.driver.find_element_by_xpath("//button[@title='User menu']").click()
    def select_editpersonaldetails_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Edit personal details')]").click()
    def editpersonaldetails(self, lastname):
        self.driver.find_element_by_name(self.username_textbox_lastname).clear()
        self.driver.find_element_by_name(self.username_textbox_lastname).send_keys(lastname)
    def click_save(self):
        self.driver.find_element_by_xpath("//button[@title='Save']").click()


class select_authentication():
    def __init__(self, driver):
        self.driver = driver
        self.password_textbox = "current-password"
    def click_authentication(self):
        self.driver.find_element_by_xpath("//a[@href='https://app2.onceplatform.com/users/user-profile/USR-KE7N20HJ59/general/authentication']").click()
    def enable_2factor_toggle(self):
        self.driver.find_element_by_xpath("//span[@class='oui-slider round']").click()
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox).send_keys(password)
    def click_submit_button(self):
        self.driver.find_element_by_xpath("//button[@class='oui-button oui-primary']").click()
    def disable_2factor_toggle(self):
        self.driver.find_element_by_xpath("//span[@class='oui-slider round']").click()


class datetime():
    def __init__(self, driver):
        self.driver = driver
        self.searchbox_id = "oui-input-0"
    def select_datetime(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Date and time')]").click()
    def clickontimezone_tochange(self):
        self.driver.find_element_by_xpath("//label[contains(text(),'Default time zone')]//following-sibling::div[@class='form-control ng-star-inserted'][1]").click()
    def search_timezone(self, timezone):
        self.driver.find_element_by_id(self.searchbox_id).send_keys(timezone)
    def select_searchedtimezone(self):
        self.driver.find_element_by_xpath("//span[@class='oui-option-text' and contains(text(),'India')]").click()
    def click_save(self):
        self.driver.find_element_by_xpath("//button[@title='Save changes']").click()


class exchange_calendar():
    def __init__(self,driver):
        self.driver = driver
        self.email_enter_by_user = 'email'
        self.password_enter_by_user = 'password'
    def scroll_till_(self):
        obj = self.driver.find_element_by_xpath("//*[@id='GoogleCalendarConnectBtn']")
        self.driver.execute_script("arguments[0].scrollIntoView();", obj)



