class share_without_personalised_link():
    def __init__(self, driver):
        self.driver = driver
    def click_schedule_option_from_top_menu(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' Schedule ')]").click()
    def from_so_click_share_booking_link(self):
        self.driver.find_element_by_xpath("//a[@class='share-a-booking-page-link']").click()
    def select_dropdown_option(self):
        self.driver.find_element_by_xpath("//div[@class='oui-select-trigger']").click()
    def select_booking_page(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' TestAdmin ')]//parent::oui-option[@title='TestAdmin']").click()
    def click_copy_close_button(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Copy & close')]").click()


class share_with_perosnalised_link():
    def __init__(self, driver):
        self.driver = driver
        self.name = "firstName"
        self.email = "customerEmail"
    def turn_on_personalised_toggle(self):
        self.driver.find_element_by_xpath("//span[@class='oui-slider round']").click()
    def enter_customer_name(self, name):
        self.driver.find_element_by_id(self.name).send_keys(name)
    def enter_customer_email(self, email):
        self.driver.find_element_by_id(self.email).send_keys(email)


class schedule_Publish():
    def __init__(self, driver):
        self.driver = driver
    def select_share_and_publish_option(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Publish on your website')]").click()
