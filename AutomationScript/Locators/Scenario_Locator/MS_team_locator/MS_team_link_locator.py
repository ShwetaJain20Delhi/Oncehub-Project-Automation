import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from AutomationScript.Calendar_connection.Exchange_Calendar import Exchange_calendar_connection_setting
from AutomationScript.Calendar_connection.O365_via_oAuth_Calendar import O365_OAuth_calendar_connection_setting


class Connection_check():
    def __init__(self, driver):
        self.driver = driver
    def disconnect_connected_calendar(self):
        try:
            if self.driver.find_element_by_xpath("//a[contains(text(),'Disconnect')]").is_displayed():
                wait = WebDriverWait(self.driver, 20)
                wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(text(),'Disconnect')]"))).click()
                wait = WebDriverWait(self.driver, 20)
                wait.until(ec.presence_of_element_located((By.XPATH, "//div[contains(text(),' I will connect')]"))).click()
                flag = self.driver.find_element_by_xpath("//span[contains(text(),'Disconnect')]")
                self.driver.execute_script("arguments[0].scrollIntoView();", flag)
                wait = WebDriverWait(self.driver, 20)
                wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Disconnect')]"))).click()
        except NoSuchElementException:
            print("Calendar is already disconnected")
    def check_MS_team_connected_state_visible_on_video_conferencing(self):
        if self.driver.find_element_by_xpath("//div[@class='microsoftTeam-icon']//following::div[3]//following-sibling::div[@class='next-step-content']").is_displayed:
            print("MS team calendar is connected")
        else:
            print("need to add different calendar")


class redirect_to_SO_setup_page():
    def __init__(self, driver):
        self.driver = driver
    def click_on_setup_menu(self):
        time.sleep(10)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[@class='product-link']"))).click()
    def select_SO_setup_option(self):
        time.sleep(4)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(text(),' ScheduleOnce setup')]"))).click()


class create_booking_page():
    def __init__(self, driver):
        self.driver = driver
    def click_plus_icon_to_create_booking_page(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Booking pages')]//parent::div//child::div//child::div[@class='addNewBox']"))).click()
    def enter_public_name(self, publicname):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "bpPublicName"))).send_keys(publicname)
    def click_internal_label(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "bpName"))).click()
    def click_save_and_edit_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//form[@name='BookingPageForm']//input[@value='Save & Edit']"))).click()
    def select_Conferecning_location_from_left_menu(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(text(),'Conferencing / Location')]"))).click()
    def check_or_select_virtual_location_option_from_meeting_channel(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//label[@for='virtualLocation']"))).click()
    def select_or_check_MS_team_video_conferecing_is_enabled_or_not(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//label[@for='virtualLocationMicrosoftTeam']"))).click()
    def click_3dot_menu_of_booking_page(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[@title='Booking page menu']"))).click()
    def select_public_link(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[@title='Open the public page in a new window']"))).click()


class Connection_checking():
    def __init__(self, driver):
        self.driver = driver
    def check_Whether_MS_calendar_is_connected_or_not_if_not_connect_MS_Calendar(self):
        try:
            if self.driver.find_element_by_xpath("//div[@class='ConnectedCal-icon office365_icon']//following::div[1]//section[1]//h4[contains(text(),' Connected to Office 365 Calendar ')]").is_displayed():
                print("MS calendar is already connected")
        except NoSuchElementException:
            check1 = Disconnect_any_connected_calendar(self.driver)
            check1.Disconnect_calendar()
            chck = Exchange_calendar_connection_setting(self.driver)
            chck.Oh_O365_oAuth_calendar_connect()
            print("Calendar disconnected and Connect MS calendar")


class Disconnect_any_connected_calendar():
    def __init__(self, driver):
        self.driver = driver
    def Disconnect_calendar(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(text(),'Disconnect')]"))).is_displayed()
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(text(),'Disconnect')]"))).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[contains(text(),' I will connect')]"))).click()
        flag = self.driver.find_element_by_xpath("//span[contains(text(),'Disconnect')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Disconnect')]"))).click()