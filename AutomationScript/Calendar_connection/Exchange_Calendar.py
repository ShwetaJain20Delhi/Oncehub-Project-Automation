from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import ExchangeCalendar, Connection_checking_for_exchange
from AutomationScript.Locators.OH_Locators.Calendar_Locator import reminder_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import sync_2way_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import so_setup_calendarpage
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Exchange_calendar_connection_setting():
    driver = None

    def __init__(self, driver):
        self.driver = driver

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
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    personal = Personalsetting(driver)
    personal.click_profile_icon()
    exchangecalendar = ExchangeCalendar(driver)
    exchangecalendar.select_calendarconnection_from_menu()
    calendar = Connection_checking_for_exchange(driver)
    calendar.check_Whether_Exchange_calendar_is_connected_or_not_if_not_connect_Exchange_Calendar()
    # calendar1 = Exchange_calendar_connection_setting(driver)
    # calendar1.Oh_reminder_setting()
    # calendar1.so_sync_setting()
    # calendar1.so_setup()
    # driver.close()