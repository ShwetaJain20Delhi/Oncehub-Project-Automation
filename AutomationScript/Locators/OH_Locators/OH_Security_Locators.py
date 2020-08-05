class Security():
    def __init__(self, driver):
        self.driver = driver
    def scroll_till_privacy_visible(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Security')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
    def click_on_Privacy(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Security')]").click()


class Security_logout_policies():
    def __init__(self, driver):
        self.driver = driver
    def click_on_security_Logout_policies(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Account lockout policies')]").click()
    