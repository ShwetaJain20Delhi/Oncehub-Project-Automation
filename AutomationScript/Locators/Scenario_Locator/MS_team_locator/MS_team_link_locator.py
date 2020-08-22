import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Connection_check():
    def __init__(self, driver):
        self.driver = driver
    def disconnect_connected_calendar(self):
        try:
            if self.driver.find_element_by_xpath("//a[contains(text(),'Disconnect')]").is_displayed():
                self.driver.find_element_by_xpath("//a[contains(text(),'Disconnect')]").click()
                time.sleep(4)
                self.driver.find_element_by_xpath("//div[contains(text(),' I will connect')]").click()
                time.sleep(3)
                flag = self.driver.find_element_by_xpath("//span[contains(text(),'Disconnect')]")
                self.driver.execute_script("arguments[0].scrollIntoView();", flag)
                self.driver.find_element_by_xpath("//span[contains(text(),'Disconnect')]").click()
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
        self.driver.find_element_by_xpath("//span[@class='product-link']").click()
    def select_SO_setup_option(self):
        self.driver.find_element_by_xpath("//a[contains(text(),' ScheduleOnce setup')]").click()


class create_booking_page():
    def __init__(self, driver):
        self.driver = driver
    def click_plus_icon_to_create_booking_page(self):
        self.driver.find_element_by_xpath("//h3[contains(text(),'Booking pages')]//parent::div//child::div//child::div[@class='addNewBox']").click()
    def enter_public_name(self, publicname):
        self.driver.find_element_by_id("bpPublicName").send_keys(publicname)
    def click_internal_label(self):
        self.driver.find_element_by_id("bpName").click()
    def click_save_and_edit_button(self):
        self.driver.find_element_by_xpath("//form[@name='BookingPageForm']//input[@value='Save & Edit']").click()
    def select_Conferecning_location_from_left_menu(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Conferencing / Location')]").click()
    def check_or_select_virtual_location_option_from_meeting_channel(self):
        self.driver.find_element_by_xpath("//label[@for='virtualLocation']").click()
    def select_or_check_MS_team_video_conferecing_is_enabled_or_not(self):
        self.driver.find_element_by_xpath("//label[@for='virtualLocationMicrosoftTeam']").click()
    def click_3dot_menu_of_booking_page(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_element_by_xpath("//a[@title='Booking page menu']").click()
    def select_public_link(self):
        self.driver.find_element_by_xpath("//a[@title='Open the public page in a new window']").click()

