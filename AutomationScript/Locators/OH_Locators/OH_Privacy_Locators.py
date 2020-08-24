from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Privacy():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_privacy_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Privacy')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_Privacy(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Privacy')]"))).click()


class Privacy_shield():
    def __init__(self, driver):
        self.driver = driver
    def click_on_privacy_shield(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Privacy shield')]"))).click()
    def Scroll_till_end(self):
        flag = self.driver.find_element_by_xpath("// a[contains(text(), 'Privacy Shield Framework website')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)


class Privacy_GDPR_Information():
    def __init__(self, driver):
        self.driver = driver
        self.name = "txtydpFullName"
        self.email = "txtydpEmailId"
        self.address = "txtydpAddres"
    def click_Privacy_GDPR(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'GDPR information')]"))).click()
    def enter_Fullname(self, name):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.name))).clear()
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.name))).send_keys(name)
    def enter_emailid(self, email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.email))).clear()
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.email))).send_keys(email)
    def enter_address(self, address):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.email))).clear()
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.address))).send_keys(address)
    def click_save(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Save')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Save')]"))).click()


class Privacy_GDPR_Compliance():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_privacy_compliance_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'GDPR compliance')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_privacy_compliance(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'GDPR compliance')]"))).click()
    def scroll_till_end(self):
        flag = self.driver.find_element_by_xpath("//a[contains(text(),'Using OnceHub in a GDPR compliant manner')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)





