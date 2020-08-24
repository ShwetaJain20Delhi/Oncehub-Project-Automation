from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import ExchangeCalendar, o365_via_oAuth_Calendar
from AutomationScript.Locators.OH_Locators.Calendar_Locator import reminder_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import sync_2way_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import so_setup_calendarpage
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class O365_OAuth_calendar_connection_setting():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()

    def Calendarconnection_from_profilemenu(self):
        personal = Personalsetting(self.driver)
        personal.click_profile_icon()
    def calendarconnection_from_menu(self):
        exchangecalendar = ExchangeCalendar(self.driver)
        exchangecalendar.select_calendarconnection_from_menu()
    def Oh_O365_oAuth_calendar_connect(self):
        main_page = self.driver.current_window_handle
        oAuth_calendar = o365_via_oAuth_Calendar(self.driver)
        oAuth_calendar.click_on_connect_button_for_O365_oAuth()
        login_page = None
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
        self.driver.switch_to.window(login_page)
        oAuth_calendar.enter_email("shweta.jain@devsunil.onmicrosoft.com")
        oAuth_calendar.click_next_button()
        oAuth_calendar.enter_password("Oncehub@12345")
        oAuth_calendar.click_signin()
        oAuth_calendar.Accept_permission()
        self.driver.switch_to.window(main_page)

    def Oh_reminder_setting(self):
        reminder = reminder_setting(self.driver)
        reminder.click_reminder_dropdown()
        reminder.select_5minute_reminder()

    def so_setup(self):
        setup_so = so_setup_calendarpage(self.driver)
        setup_so.scroll_till_so_continueSetup_visible()
        setup_so.select_continue_setup_from_calendarpage()
        self.driver.back()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    calendar = O365_OAuth_calendar_connection_setting(driver)
    calendar.server_login()
    calendar.Calendarconnection_from_profilemenu()
    calendar.calendarconnection_from_menu()
    calendar.Oh_O365_oAuth_calendar_connect()
    calendar.Oh_reminder_setting()
    calendar.so_setup()
    driver.close()


# #################################  O365 via OAUth Calendar Connection  #################################
# main_page = driver.current_window_handle  # save the current window
# driver.find_element_by_xpath("//button[@aria-label='Connect to Office 365 Calendar via OAuth']").click()
# time.sleep(5)
# login_page = None
# for handle in driver.window_handles:
#     if handle != main_page:
#        login_page = handle
# driver.switch_to.window(login_page)    #switch to calendar connection window
# time.sleep(10)
# driver.find_element_by_name("loginfmt").send_keys("shweta.jain@oncehq.com")    #Calendar Email
# time.sleep(3)
# driver.find_element_by_id("idSIButton9").click()          #Click next after entered email
# time.sleep(3)
# driver.find_element_by_name("passwd").send_keys("Schedule@123")                  # Password for email connection
# time.sleep(3)
# driver.find_element_by_id("idSIButton9").click()    #Click on connect button on calendar connection popup
# time.sleep(3)
# driver.find_element_by_id("idBtn_Back").click()
# time.sleep(15)
# driver.switch_to.window(main_page)
# time.sleep(5)
