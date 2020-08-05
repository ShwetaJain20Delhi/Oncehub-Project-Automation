class Security():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_security_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Security')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_Security(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Security')]").click()


class Security_lockout_policies():
    def __init__(self, driver):
        self.driver = driver
    def click_on_security_Lockout_policies(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Account lockout policies')]").click()
    def click_on_account_lockout_enabled(self):
        self.driver.find_element_by_xpath("// div[contains(text(), 'Account lockout is enabled')]").click()
    def click_on_account_lockout_disabled(self):
        self.driver.find_element_by_xpath("// div[contains(text(), 'Account lockout is disabled')]").click()
    def click_save_button(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Save')]").click()


class Security_Password_Policies():
    def __init__(self, driver):
        self.driver = driver
    def click_on_security_password_policies(self):
        self.driver.find_element_by_xpath("//span[contains(text(), 'Password policies')]").click()
    def select_passwordLength_dropdown(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'The minimum length for new passwords is')]//following-sibling::span[@class='ouiSelect']").click()
    def select_any_value_from_dropdown(self):
        self.driver.find_element_by_xpath("//span[@class ='oui-option-text' and starts-with(text(),'8')]").click()
    def select_capitalletters_from_complexity(self):
        self.driver.find_element_by_id("uppercaseCB").click()
    def select_specialcharacters_from_complexity(self):
        self.driver.find_element_by_id("specialcharacterCB").click()
    def select_2ndoption_from_password_expiration(self):
        flag = self.driver.find_element_by_xpath("//div[contains(text(),'Passwords automatically expire after')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//div[contains(text(),'Passwords automatically expire after')]").click()
    def select_2ndoption_from_password_history(self):
        flag = self.driver.find_element_by_xpath("//div[contains(text(),'Users cannot reuse their previous')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//div[contains(text(),'Users cannot reuse their previous')]").click()
    def click_discard_button(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Discard')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//span[contains(text(),'Discard')]").click()


class Security_Session_Policies():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_security_session_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Session policies')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_security_session_policies(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Session policies')]").click()
    def select_2ndoption_from_password_policies(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'Users are signed out after')]").click()
    def select_1stoption_from_password_policies(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'Session timeout is disabled')]").click()
    def select_save_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()


class Security_SSO_Policies():
    def __init__(self, driver):
        self.driver = driver
    def click_on_security_sso_policies(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'SSO')]").click()
