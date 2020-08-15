class display():
    def __init__(self, driver):
        self.driver = driver
    def click_on_display(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Display')]").click()
    def choose_a_shape(self):
        flag = self.driver.find_element_by_xpath("//label[@title='Square']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//label[@title='Square']").click()
    def choose_a_theme(self):
        self.driver.find_element_by_xpath("//label[@title='Icon 3']").click()
    def click_on_save_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()


class Privacy():
    def __init__(self, driver):
        self.driver = driver
    def click_on_privacy(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Privacy')]").click()
    def select_Website_analytics(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Website analytics')]").click()
    def select_2nd_radio_button(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'Only collect')]").click()
    def copied_script_when_consent_is_granted(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'consent is granted')]//parent::div//following::div[1]//following::span[1]//button//span").click()
    def copied_script_when_consent_is_revoked (self):
        flag = self.driver.find_element_by_xpath("//p[contains(text(),'consent is granted')]//parent::div//following::div[3]//following::span[1]//button//span")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//p[contains(text(),'consent is granted')]//parent::div//following::div[3]//following::span[1]//button//span").click()
    def click_discard_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Discard')]").click()
    def turn_toggle_off_for_website_analytics(self):
        self.driver.find_element_by_xpath("//span[@class='on-off-btn toggle-spacing']").click()
    def click_discard(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Discard')]").click()


class Installation():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Installation(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Installation')]").click()
    def select_Intall_it_yourself_option(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'We’ve created a video tutorial for you')]//following-sibling::div//div//button").click()
    def click_copy_code(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Copy code')]").click()
    def click_verify_installation(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Verify installation')]").click()
    def click_close(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Close')]").click()
