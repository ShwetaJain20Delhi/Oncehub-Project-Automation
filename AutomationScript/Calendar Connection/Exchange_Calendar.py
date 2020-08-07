from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import ExchangeCalendar
from AutomationScript.Locators.OH_Locators.Calendar_Locator import reminder_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import sync_2way_setting
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
        time.sleep(8)

    def Calendarconnection_from_profilemenu(self):
        personal = Personalsetting(self.driver)
        personal.click_profile_icon()
        time.sleep(3)
    def Oh_Exchange_calendar_connect(self):
        exchangecalendar = ExchangeCalendar(self.driver)
        exchangecalendar.select_calendarconnection_from_menu()
        time.sleep(5)
        exchangecalendar.click_exchange_connect_button()
        time.sleep(3)
        exchangecalendar.enter_username("gilad@staticso.com")
        time.sleep(3)
        exchangecalendar.enter_password("schEdu1e")
        time.sleep(3)
        exchangecalendar.expand_advanced_setting()
        time.sleep(3)
        exchangecalendar.enter_ews_url("https://mex09.emailsrvr.com/owa")
        time.sleep(3)
        exchangecalendar.click_connect_button()
        time.sleep(10)

    def Oh_reminder_setting(self):
        reminder = reminder_setting(self.driver)
        reminder.click_reminder_dropdown()
        time.sleep(3)
        reminder.select_5minute_reminder()
        time.sleep(5)

    def so_sync_setting(self):
        sync = sync_2way_setting(self.driver)
        sync.scroll_till_so_advanced_setting_visible()
        time.sleep(5)
        sync.change_togglevalue_for_delete_event()
        time.sleep(3)
        sync.change_togglevalue_for_change_event()
        time.sleep(3)

    def so_setup(self):
        setup_so = so_setup_calendarpage(self.driver)
        setup_so.scroll_till_so_continueSetup_visible()
        time.sleep(5)
        setup_so.select_continue_setup_from_calendarpage()
        time.sleep(10)
        self.driver.back()
        time.sleep(10)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    calendar = calendar_connection_setting(driver)
    calendar.server_login()
    calendar.Calendarconnection_from_profilemenu()
    calendar.Oh_Exchange_calendar_connect()
    calendar.Oh_reminder_setting()
    calendar.so_sync_setting()
    calendar.so_setup()
    driver.close()