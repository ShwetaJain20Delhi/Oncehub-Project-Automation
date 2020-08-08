from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import ExchangeCalendar, iCloudCalendar
from AutomationScript.Locators.OH_Locators.Calendar_Locator import reminder_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import so_setup_calendarpage
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class iCloud_calendar_connection_setting():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        time.sleep(5)

    def Calendarconnection_from_profilemenu(self):
        personal = Personalsetting(self.driver)
        personal.click_profile_icon()
        time.sleep(3)
        exchangecalendar = ExchangeCalendar(self.driver)
        exchangecalendar.select_calendarconnection_from_menu()
        time.sleep(7)

    def Oh_iCloud_calendar_connect(self):
        icloudcalendar = iCloudCalendar(self.driver)
        icloudcalendar.click_on_connect_button_for_iCloud()
        time.sleep(5)
        icloudcalendar.enter_email("sotestoptimus@icloud.com")
        time.sleep(3)
        icloudcalendar.enter_password("bjjc-hbdd-zgsg-dscb")
        time.sleep(3)
        icloudcalendar.click_on_connect_button()
        time.sleep(10)

    def Oh_reminder_setting(self):
        reminder = reminder_setting(self.driver)
        reminder.click_reminder_dropdown()
        time.sleep(3)
        reminder.select_5minute_reminder()
        time.sleep(5)

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
    calendar = iCloud_calendar_connection_setting(driver)
    calendar.server_login()
    calendar.Calendarconnection_from_profilemenu()
    calendar.Oh_iCloud_calendar_connect()
    calendar.Oh_reminder_setting()
    calendar.so_setup()
    driver.close()