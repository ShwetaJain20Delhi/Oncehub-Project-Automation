class website():
    def __init__(self, driver):
        self.driver = driver
    def click_on_website(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Websites')]").click()
    def click_on_Add_website(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Add website')]").click()
    def enter_webiste_name(self, name):
        self.driver.find_element_by_id("websiteNameTxt").send_keys(name)
    def enter_webiste_url(self, url):
        self.driver.find_element_by_id("websiteUrlTxt").send_keys(url)
    def click_on_Add_webiste_button(self):
        self.driver.find_element_by_id("savebutton").click()


class website_3dot_functionality():
    def __init__(self, driver):
        self.driver = driver
    def click_on_bot_3dot_option(self):
        self.driver.find_element_by_xpath("//h4[contains(text(),'Test')]//parent::div//parent::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//span[@class='website-more-setting']").click()


class website_3dot_edit():
    def __init__(self, driver):
        self.driver = driver
    def select_edit_name_url_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Edit name & URL')]").click()
    def enter_webiste_name(self, name):
        self.driver.find_element_by_id("websiteNameTxt").clear()
        self.driver.find_element_by_id("websiteNameTxt").send_keys(name)
    def enter_webiste_url(self, url):
        self.driver.find_element_by_id("websiteUrlTxt").clear()
        self.driver.find_element_by_id("websiteUrlTxt").send_keys(url)
    def click_on_save_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()


class website_3dot_remove():
    def __init__(self, driver):
        self.driver = driver
    def select_remove_option(self):
        self.driver.find_element_by_xpath("//button[@title='Remove']").click()
    def click_checkbox_for_remove_website(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' I want to remove this website')]").click()
    def click_on_remove_website_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' Remove website ')]").click()
    def click_on_close_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Close')]").click()


class no_website_popup():
    def __init__(self, driver):
        self.driver = driver
    def click_on_close_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Close')]").click()

