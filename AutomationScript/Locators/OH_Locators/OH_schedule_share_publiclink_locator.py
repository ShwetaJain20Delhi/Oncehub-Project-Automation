from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip as pc

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
        self.driver.find_element_by_xpath("//span[contains(text(),'test151')]//parent::oui-option[@title='test151']").click()
    def copy_public_link(self):
        self.driver.find_element_by_id("bookingPageLink").click()
    def click_copy_close_button(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Copy & close')]").click()


class new_tab():
    def __init__(self, driver):
        self.driver = driver
    def open_new_window_and_paste_copied_url(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to_window(self.driver.window_handles[1])
        text = pc.paste()
        self.driver.get(text)
    def select_15minute_event_type(self):
        self.driver.find_element_by_xpath("//div[@title='Select  15-minute meeting']").click()
    def change_time_zone(self):
        self.driver.find_element_by_xpath("//a[@title='Edit your time zone']").click()
    def click_on_dropdown(self):
        self.driver.find_element_by_xpath("//input[@id='input_country']").click()
    def search_India(self, country):
        self.driver.find_element_by_xpath("//input[@id='input_country']").send_keys(country)
    def select_searched_country(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'India')]").click()
    def click_continue(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
    def select_time_slot(self):
        flag = self.driver.find_element_by_xpath("//button[contains(text(),'4:00 PM')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//button[contains(text(),'4:00 PM')]").click()
    def clickcontinue(self):
        self.driver.find_element_by_xpath("// button[ @ title = 'Proceed to next step']").click()


class Booking_form():
    def __init__(self, driver):
        self.driver = driver
        self.name = "customer_name"
        self.email = "customer_email"
    def enter_name(self, name):
        self.driver.find_element_by_name(self.name).send_keys(name)
    def enter_email(self, email):
        self.driver.find_element_by_name(self.email).send_keys(email)
    def click_done(self):
        flag = self.driver.find_element_by_xpath("// button[ @ title = 'Confirm your booking request']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("// button[ @ title = 'Confirm your booking request']").click()
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])
    # def copy_bookingID(self):
    #     self.driver.find_element_by_xpath("// small[contains(text(), 'Booking ID')]").send_keys(Keys.CONTROL + "c")
    #     self.driver.close()
    #     self.driver.switch_to_window(self.driver.window_handles[0])
    # def paste_booking_id_in_activity_page(self):
    #     paste = self.driver.find_element_by_name("freeSearchText")
    #     paste.send_keys(Keys.CONTROL + "v")
    #     paste.send_keys(Keys.ENTER)

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
    def clickcontinue(self):
        self.driver.find_element_by_xpath("// button[ @ title = 'Proceed to next step']").click()
    def close_meeting_tab_switch_to_application_tab(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])


class schedule_Publish():
    def __init__(self, driver):
        self.driver = driver
    def select_share_and_publish_option(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Publish on your website')]").click()



