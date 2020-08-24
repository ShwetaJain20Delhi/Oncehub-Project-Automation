from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import ExchangeCalendar, o365_via_ews_Calendar, \
    sync_2way_setting, Notification_connect
from AutomationScript.Locators.OH_Locators.Calendar_Locator import reminder_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import so_setup_calendarpage
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class calendar_connection_setting():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()

    def Connect_calendar_with_notification_center(self):
        connect = Notification_connect(self.driver)
        # connect.click_on_notication_icon()
        connect.click_connect_button_for_calendar_connection()

    def Oh_O365_via_ews_calendar_connect(self):
        calendar_O365 = o365_via_ews_Calendar(self.driver)
        calendar_O365.click_on_connect_button_for_O365_EWS()
        calendar_O365.enter_email("shalini@oncehq.com")
        calendar_O365.enter_password("msvrdzxhkdhvbrhj")
        calendar_O365.click_on_connect_button()

    def Oh_reminder_setting(self):
        reminder = reminder_setting(self.driver)
        reminder.click_reminder_dropdown()
        reminder.select_5minute_reminder()

    def so_sync_setting(self):
        sync = sync_2way_setting(self.driver)
        sync.scroll_till_so_advanced_setting_visible()
        sync.change_togglevalue_for_delete_event()
        sync.change_togglevalue_for_change_event()

    def so_setup(self):
        setup_so = so_setup_calendarpage(self.driver)
        setup_so.scroll_till_so_continueSetup_visible()
        setup_so.select_continue_setup_from_calendarpage()
        self.driver.back()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    calendar = calendar_connection_setting(driver)
    calendar.server_login()
    calendar.Connect_calendar_with_notification_center()
    calendar.Oh_O365_via_ews_calendar_connect()
    calendar.Oh_reminder_setting()
    calendar.so_sync_setting()
    calendar.so_setup()
    driver.close()





#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
#
#
# driver = webdriver.Chrome()
# driver.set_page_load_timeout(15)
# driver.maximize_window()
# driver.get("https://app3.onceplatform.com/")
# driver.implicitly_wait(35)
#
# #################################  Login to OH  #################################
# Ele=driver.find_element_by_name("email")
# driver.find_element_by_name("email").send_keys("death-mad-34@staticso2.com")
# Ele1=driver.find_element_by_name("password")
# driver.find_element_by_name("password").send_keys("testing@123")
# driver.find_element_by_id("signIn").click()
# time.sleep(10)
#
# ########################### Click on calendar connection page from profile menu  #################################
# driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[2]/a/span").click()
# time.sleep(5)
#
# #################################  O365 via EWS Calendar Connection  #################################
# Flag = driver.find_element_by_xpath("//*[@id='GoogleCalendarConnectBtn']")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("//*[@id='GoogleCalendarConnectBtn']").click()
# time.sleep(3)
# driver.find_element_by_id("email").send_keys("shalini@oncehq.com")
# time.sleep(2)
# driver.find_element_by_id("password").send_keys("msvrdzxhkdhvbrhj")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
# time.sleep(20)