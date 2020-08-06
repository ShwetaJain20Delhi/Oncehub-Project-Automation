class Applicationlogin():
    def __init__(self, driver):
        self.driver = driver
        self.username = "email"
        self.password = "password"
        self.login_button_id = "signIn"
    def enter_username(self, username):
        self.driver.find_element_by_name(self.username).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element_by_name(self.password).send_keys(password)
    def click_login(self):
        self.driver.find_element_by_id("signIn").click()


class Personalsetting():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_lastname = "lastName"
    def click_profile_icon(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
    def select_myprofile(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'My profile')]").click()
    def click_3dot(self):
        self.driver.find_element_by_xpath("//button[@title='User menu']").click()
    def select_editpersonaldetails_option(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//span[contains(text(),'Edit personal details')]").click()
    def editpersonaldetails(self, lastname):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name(self.username_textbox_lastname).clear()
        self.driver.find_element_by_name(self.username_textbox_lastname).send_keys(lastname)
    def click_save(self):
        self.driver.implicitly_wait(20)
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
    def discard_changes(self):
        self.driver.find_element_by_xpath("//span[@class='oui-button-wrapper' and contains(text(),'Discard')]").click()


class datetime():
    def __init__(self, driver):
        self.driver = driver
    def select_datetime(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Date and time')]").click()
    def clickontimezone_tochange(self):
        self.driver.find_element_by_xpath("//label[contains(text(),'Default time zone')]//following-sibling::div[@class='form-control ng-star-inserted'][1]").click()
    def search_timezone(self, timezone):
        self.driver.find_element_by_xpath("//input[@class='oui-select-search-input oui-input-element oui-input oui-primary cdk-text-field-autofill-monitored']").send_keys(timezone)
    def select_searchedtimezone(self):
        self.driver.find_element_by_xpath("//span[@class='oui-option-text' and contains(text(),'India')]").click()
    def click_save(self):
        self.driver.find_element_by_xpath("//button[@title='Save changes']").click()


class compliance():
    def __init__(self, driver):
        self.driver = driver
    def movescrollbar_tillcompliancevisible(self):
        flag = self.driver.find_element_by_xpath("//span[@class='sl-sidenav-link-text' and contains(text(),'Compliance')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def select_compliance(self):
        self.driver.find_element_by_xpath("//span[@class='sl-sidenav-link-text' and contains(text(),'Compliance')]").click()


class Emailnotification():
    def __init__(self, driver):
        self.driver = driver
        self.edit_name = "oui-input-0"
    def select_email_notification(self):
        self.driver.find_element_by_xpath("//span[@class='sl-sidenav-link-text' and contains(text(),'Email notifications')]").click()
    def edit_sentfromname_field(self, name):
        flag = self.driver.find_element_by_id("oui-input-0")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_id(self.edit_name).clear()
        self.driver.find_element_by_id(self.edit_name).send_keys(name)
    def click_save(self):
        self.driver.find_element_by_xpath("//button[@title='Save changes']").click()


class Oh_so_module():
    def __init__(self, driver):
        self.driver = driver
        self.tick_payment = "pay-setup"
        self.tick_zapier = "zap-setup"
    def select_so(self):
        self.driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[8]/a/div/span").click()
    def select_payment_integration(self):
        self.driver.find_element_by_id(self.tick_payment).click()
    def select_zapier_integration(self):
        self.driver.find_element_by_id(self.tick_zapier).click()
    def discard_changes(self):
        self.driver.find_element_by_xpath("//*[@id='discardButton']/span").click()


class password_policies():
    def __init__(self, driver):
        self.driver = driver
        self.current_password = "current-password"
        self.new_password = "new-password"
        self.reenter_password = "re-type-password"
    def select_password_from_OH(self):
        self.driver.find_element_by_xpath("//span[@class='sl-sidenav-link-text' and contains(text(),'Password')]").click()
    def enter_current_password(self, password):
        self.driver.find_element_by_id(self.current_password).send_keys(password)
    def enter_new_password(self, password1):
        self.driver.find_element_by_id(self.new_password).send_keys(password1)
    def Reenter_new_password(self, password2):
        self.driver.find_element_by_id(self.reenter_password).send_keys(password2)
    def Discard_changes(self):
        self.driver.find_element_by_xpath("//*[@id='discardButton']/span").click()


class sms_notification():
    def __init__(self, driver):
        self.driver = driver
    def select_smsnotification_oh(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'SMS notifications')]").click()
    def user_notification_toggle(self):
        self.driver.find_element_by_xpath("//input[@type='checkbox'and@id='keep-me']//parent::label[@class='oui-slide-toogle-wrapper']").click()
    def discard_changes(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Discard')]").click()


class Settings_OH():
    def __init__(self, driver):
        self.driver = driver
    def Scroll_till_settingsoption_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(), 'Settings')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def select_settings_oh(self):
        self.driver.find_element_by_xpath("//span[contains(text(), 'Settings')]").click()
    def click_deleteaccount_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Delete account')]").click()
    def select_checkbox_on_popup(self):
        self.driver.find_element_by_id("deleteAccount").click()
    def select_keepmyaccount_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Keep my account')]").click()









