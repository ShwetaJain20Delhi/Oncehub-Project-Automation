from AutomationScript.Locators.OH_Locators.Calendar_Locator import ExchangeCalendar
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Locators.Scenario_Locator.MS_team_locator.MS_team_link_locator import Connection_checking
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Calendar():
    #################################  launch Chrome server  #################################
   ## Test Automation1111
    
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def calendar_disconnect(self):
        personal = Personalsetting(driver)
        personal.click_profile_icon()
        exchangecalendar = ExchangeCalendar(self.driver)
        exchangecalendar.select_calendarconnection_from_menu()
        check = Connection_checking(self.driver)
        check.check_Whether_MS_calendar_is_connected_or_not_if_not_connect_MS_Calendar()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    check = Calendar(driver)
    check.calendar_disconnect()