
class Privacy():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_privacy_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Privacy')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_Privacy(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Privacy')]").click()


class Privacy_shield():
    def __init__(self, driver):
        self.driver = driver
    def click_on_privacy_shield(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Privacy shield')]").click()
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
        self.driver.find_element_by_xpath("//span[contains(text(),'GDPR information')]").click()
    def enter_Fullname(self, name):
        self.driver.find_element_by_name(self.name).clear()
        self.driver.find_element_by_name(self.name).send_keys(name)
    def enter_emailid(self, email):
        self.driver.find_element_by_name(self.email).clear()
        self.driver.find_element_by_name(self.email).send_keys(email)
    def enter_address(self, address):
        self.driver.find_element_by_name(self.email).clear()
        self.driver.find_element_by_name(self.address).send_keys(address)
    def click_save(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Save')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()


class Privacy_GDPR_Compliance():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_privacy_compliance_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'GDPR compliance')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_privacy_compliance(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'GDPR compliance')]").click()
    def scroll_till_end(self):
        flag = self.driver.find_element_by_xpath("//a[contains(text(),'Using OnceHub in a GDPR compliant manner')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)





