from AutomationScript.Locators.OH_Locators.SignupAndSO_Onboarding_Locators import inbox_email, Product_selection, \
    Timezone_selection, Calendar_connection, video_conferencing, test_booking, Signup, skip_tour, logout, chatonce
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver
import time
from selenium.webdriver.common.keys import Keys


class Signup_SO_Onboarding():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Inbox_email(self):
        inbox = inbox_email(self.driver)
        self.driver.maximize_window()
        inbox.launch_inbox_email()
        time.sleep(3)
        inbox.copy_inbox_email()
        time.sleep(3)

    def Signup_with_new_user(self):
        onboard = Signup(self.driver)
        onboard.Navigate_to_URL()
        time.sleep(3)
        onboard.Enter_1stName("Test User")
        time.sleep(2)
        onboard.Enter_email(Keys.CONTROL + "v")
        time.sleep(2)
        onboard.Enter_password("testing@123")
        time.sleep(2)
        onboard.ReEnter_password("testing@123")
        time.sleep(2)
        onboard.click_signup_button()
        time.sleep(8)

    def select_product(self):
        product = Product_selection(self.driver)
        product.select_so_product()
        time.sleep(10)

    def select_timezone(self):
        timezone = Timezone_selection(self.driver)
        timezone.select_sunday()
        time.sleep(2)
        timezone.select_saturday()
        time.sleep(2)
        timezone.click_on_change_timezone()
        time.sleep(3)
        timezone.click_on_dropdown()
        time.sleep(4)
        timezone.search_India("India")
        time.sleep(3)
        timezone.select_timezone()
        time.sleep(3)
        timezone.click_save()
        time.sleep(5)
        timezone.click_continue()
        time.sleep(4)

    def connect_Exchange_calendar(self):
        connect = Calendar_connection(self.driver)
        connect.click_calendar_expand_button()
        time.sleep(3)
        connect.click_exchange_connect_button()
        time.sleep(3)
        connect.enter_username("gilad@staticso.com")
        time.sleep(2)
        connect.enter_password("schEdu1e")
        time.sleep(2)
        connect.expand_advanced_setting()
        time.sleep(2)
        connect.enter_ews_url("https://mex09.emailsrvr.com/owa")
        time.sleep(2)
        connect.click_connect_button()
        time.sleep(10)
        connect.click_continue()
        time.sleep(3)

    def Conferencing_option(self):
        video = video_conferencing(self.driver)
        video.click_skip_for_video_conferencing()
        time.sleep(5)

    def Booking_test(self):
        test = test_booking(self.driver)
        test.click_skip_for_test_booking()
        time.sleep(7)

    def SO_tour_skip(self):
        tour = skip_tour(self.driver)
        tour.click_skip_for_test_booking()
        time.sleep(5)

    def ChatOnce_started(self):
        co_start = chatonce(self.driver)
        co_start.click_on_setup()
        time.sleep(3)
        co_start.select_ChatOnce()
        time.sleep(10)
        co_start.click_Get_started_button_on_popup()
        time.sleep(10)

    def Application_logout(self):
        log_out = logout(self.driver)
        log_out.click_profile_icon()
        time.sleep(3)
        log_out.click_signout()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    Onboard_SO = Signup_SO_Onboarding(driver)
    Onboard_SO.Inbox_email()
    Onboard_SO.Signup_with_new_user()
    Onboard_SO.select_product()
    Onboard_SO.select_timezone()
    Onboard_SO.connect_Exchange_calendar()
    Onboard_SO.Conferencing_option()
    Onboard_SO.Booking_test()
    Onboard_SO.SO_tour_skip()
    Onboard_SO.ChatOnce_started()
    Onboard_SO.Application_logout()
    driver.close()
