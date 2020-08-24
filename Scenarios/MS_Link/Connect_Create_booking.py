import time

from AutomationScript.Calendar_connection.O365_via_oAuth_Calendar import O365_OAuth_calendar_connection_setting
from AutomationScript.Locators.OH_Locators.Calendar_Locator import ExchangeCalendar, o365_via_oAuth_Calendar
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Locators.SO_Locators.Video_conferencing_locator import profile_video_conferencing
from AutomationScript.Locators.Scenario_Locator.MS_team_locator.MS_team_link_locator import Connection_check, \
    redirect_to_SO_setup_page, create_booking_page
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class ms_team():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def calendar_disconnect(self):
        personal = Personalsetting(driver)
        personal.click_profile_icon()
        exchangecalendar = ExchangeCalendar(self.driver)
        exchangecalendar.select_calendarconnection_from_menu()
        connection = Connection_check(self.driver)
        connection.disconnect_connected_calendar()

    def MS_connected_state_on_video_conferencing(self):
        video = profile_video_conferencing(self.driver)
        video.select_video_conferencing()
        connection = Connection_check(self.driver)
        connection.check_MS_team_connected_state_visible_on_video_conferencing()

    def SO_setup(self):
        setup = redirect_to_SO_setup_page(self.driver)
        setup.click_on_setup_menu()
        setup.select_SO_setup_option()

    def Create_BP_and_create_meeting_with_MS_link(self):
        booking = create_booking_page(self.driver)
        booking.click_plus_icon_to_create_booking_page()
        booking.enter_public_name("Shweta_oncehub")
        booking.click_internal_label()
        booking.click_save_and_edit_button()
        booking.select_Conferecning_location_from_left_menu()
        booking.check_or_select_virtual_location_option_from_meeting_channel()
        booking.select_or_check_MS_team_video_conferecing_is_enabled_or_not()
        booking.click_3dot_menu_of_booking_page()
        booking.select_public_link()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    calendar = ms_team(driver)
    # calendar.calendar_disconnect()
    calendar1 = O365_OAuth_calendar_connection_setting(driver)
    # calendar1.Oh_O365_oAuth_calendar_connect()
    # calendar1.Calendarconnection_from_profilemenu()
    # calendar.MS_connected_state_on_video_conferencing()
    calendar.SO_setup()
    calendar.Create_BP_and_create_meeting_with_MS_link()
