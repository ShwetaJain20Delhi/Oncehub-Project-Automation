import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Security():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_security_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Security')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_Security(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Security')]"))).click()


class Security_lockout_policies():
    def __init__(self, driver):
        self.driver = driver
    def click_on_security_Lockout_policies(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Account lockout policies')]"))).click()
    def click_on_account_lockout_enabled(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// div[contains(text(), 'Account lockout is enabled')]"))).click()
    def click_on_account_lockout_disabled(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// div[contains(text(), 'Account lockout is disabled')]"))).click()
    def click_save_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// span[contains(text(), 'Save')]"))).click()
        time.sleep(3)


class Security_Password_Policies():
    def __init__(self, driver):
        self.driver = driver
    def click_on_security_password_policies(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Password policies')]"))).click()
    def select_passwordLength_dropdown(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'The minimum length for new passwords is')]//following-sibling::span[@class='ouiSelect']"))).click()
    def select_any_value_from_dropdown(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[@class ='oui-option-text' and starts-with(text(),'8')]"))).click()
    def select_capitalletters_from_complexity(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.ID, "uppercaseCB"))).click()
    def select_specialcharacters_from_complexity(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.ID, "specialcharacterCB"))).click()
    def select_2ndoption_from_password_expiration(self):
        flag = self.driver.find_element_by_xpath("//div[contains(text(),'Passwords automatically expire after')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Passwords automatically expire after')]"))).click()
    def select_2ndoption_from_password_history(self):
        flag = self.driver.find_element_by_xpath("//div[contains(text(),'Users cannot reuse their previous')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Users cannot reuse their previous')]"))).click()
    def click_discard_button(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Discard')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Discard')]"))).click()
        time.sleep(3)


class Security_Session_Policies():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_security_session_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Session policies')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_security_session_policies(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Session policies')]"))).click()
    def select_2ndoption_from_password_policies(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Users are signed out after')]"))).click()
    def select_1stoption_from_password_policies(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Session timeout is disabled')]"))).click()
    def select_save_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Save')]"))).click()


class Security_SSO_Policies():
    def __init__(self, driver):
        self.driver = driver
    def click_on_security_sso_policies(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'SSO')]"))).click()
