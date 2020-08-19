import time

from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Locators.SO_Locators.Video_conferencing_locator import profile_video_conferencing, connect_zoom, \
    connect_gotomeeting, connect_webex, disconnect
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class video_conferencing():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def conferencing(self):
        personal = Personalsetting(driver)
        personal.click_profile_icon()
        time.sleep(5)
        video = profile_video_conferencing(self.driver)
        video.select_video_conferencing()
        time.sleep(8)
        # zoom1 = connect_zoom(self.driver)
        # zoom1.connect_zoom()
        # time.sleep(7)
        # g_meeting = connect_gotomeeting(self.driver)
        # g_meeting.connect_goto()
        # time.sleep(5)
        # web_meeting = connect_webex(self.driver)
        # web_meeting.connect_webex_meeting()
        # time.sleep(8)
        dis = disconnect(self.driver)
        dis.disconnect_zoom()
        time.sleep(5)
        dis.click_yes()
        time.sleep(5)
        dis.disconnect_goto_meeting()
        time.sleep(5)
        dis.click_yes()
        time.sleep(5)
        dis.disconnect_webex_meeting()
        time.sleep(5)
        dis.click_yes()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    conference = video_conferencing(driver)
    conference.conferencing()