import pyperclip as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class share_without_personalised_link():
    def __init__(self, driver):
        self.driver = driver
    def click_schedule_option_from_top_menu(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),' Schedule ')]"))).click()
    def from_so_click_share_booking_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='share-a-booking-page-link']"))).click()
    def select_dropdown_option(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='oui-select-trigger']"))).click()
    def select_booking_page(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'test151')]//parent::oui-option[@title='test151']"))).click()
    def copy_public_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, "bookingPageLink"))).click()
    def click_copy_close_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// span[contains(text(), 'Copy & close')]"))).click()


class new_tab():
    def __init__(self, driver):
        self.driver = driver
    def open_new_window_and_paste_copied_url(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to_window(self.driver.window_handles[1])
        text = pc.paste()
        self.driver.get(text)
    def select_15minute_event_type(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Select  15-minute meeting']"))).click()
    def change_time_zone(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Edit your time zone']"))).click()
    def click_on_dropdown(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='input_country']"))).click()
    def search_India(self, country):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='input_country']"))).send_keys(country)
    def select_searched_country(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(),'India')]"))).click()
    def click_continue(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    def select_time_slot(self):
        flag = self.driver.find_element_by_xpath("//button[contains(text(),'4:00 PM')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'4:00 PM')]"))).click()
    def clickcontinue(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// button[ @ title = 'Proceed to next step']"))).click()


class Booking_form():
    def __init__(self, driver):
        self.driver = driver
        self.name = "customer_name"
        self.email = "customer_email"
    def enter_name(self, name):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.name))).send_keys(name)
    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.NAME, self.email))).send_keys(email)
    def click_done(self):
        flag = self.driver.find_element_by_xpath("// button[ @ title = 'Confirm your booking request']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// button[ @ title = 'Confirm your booking request']"))).click()
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
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='oui-slider round']"))).click()
    def enter_customer_name(self, name):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, self.name))).send_keys(name)
    def enter_customer_email(self, email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.ID, self.email))).send_keys(email)
    def clickcontinue(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "// button[ @ title = 'Proceed to next step']"))).click()
    def close_meeting_tab_switch_to_application_tab(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])


class schedule_Publish():
    def __init__(self, driver):
        self.driver = driver
    def select_share_and_publish_option(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Publish on your website')]"))).click()



