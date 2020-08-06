class users():
    def __init__(self, driver):
        self.driver = driver
    def click_on_Users(self):
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Users')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//span[contains(text(),'Users')]").click()


class Add_user():
    def __init__(self, driver):
        self.driver = driver
        self.firstname = "firstName"
        self.lastname = "lastName"
        self.email = "email"
    def select_adduser_option(self):
        self.driver.find_element_by_xpath("//div[@class='addUserDiv']").click()
    def enter_first_name(self, fname):
        self.driver.find_element_by_id(self.firstname).send_keys(fname)
    def enter_last_name(self, lname):
        self.driver.find_element_by_id(self.lastname).send_keys(lname)
    def enter_email(self, email):
        self.driver.find_element_by_id(self.email).send_keys(email)
    def click_create_user_send_invitation_button(self):
        self.driver.find_element_by_xpath("//button[@title='Create new User and send invitation email']").click()
    def select_users(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Users')]").click()


class Remove_user():
    def __init__(self, driver):
        self.driver = driver
    def click_on_user_3dot(self):
        self.driver.find_element_by_xpath("//span[@title='Test User']//preceding::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following::button[@title='User profile menu']").click()
    def select_delete_user_profile(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Delete User profile')]").click()
    def click_on_delete_user_profile_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Delete User profile')]").click()
    def click_on_close_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Close')]").click()


class inbox_email():
    def __init__(self, driver):
        self.driver = driver
        self.email = "div-domain"
    def launch_inbox_email(self):
        self.driver.get("https://inbox.staticso2.com/")
    def copy_inbox_email(self):
        self.driver.find_element_by_id(self.email).click()


class Resend_link():
    def __init__(self, driver):
        self.driver = driver
    def click_on_user_3dot(self):
        self.driver.find_element_by_xpath("//span[@title='Test User']//preceding::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following-sibling::td[@role='gridcell']//following::button[@title='User profile menu']").click()
    def select_Resend_invitation_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Resend invitation')]").click()
    def click_close(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Close')]").click()








