import time

from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.ChatOnce_Display_Privacy_Install_locator import display, Privacy, \
    Installation
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Chatonce_Display_Privacy_Install():

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Display(self):
        dis = display(self.driver)
        dis.click_on_display()
        dis.choose_a_shape()
        dis.choose_a_theme()
        dis.click_on_save_button()

    def Privacy(self):
        pri = Privacy(self.driver)
        pri.click_on_privacy()
        pri.select_Website_analytics()
        pri.select_2nd_radio_button()
        pri.copied_script_when_consent_is_granted()
        pri.copied_script_when_consent_is_revoked()
        pri.click_discard_button()
        pri.turn_toggle_off_for_website_analytics()
        pri.click_discard()

    def installation(self):
        install = Installation(self.driver)
        install.click_on_Installation()
        install.select_Intall_it_yourself_option()
        install.click_copy_code()
        install.click_verify_installation()
        install.click_close()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.select_co_from_setup()
    dis_pri = Chatonce_Display_Privacy_Install(driver)
    dis_pri.Display()
    dis_pri.Privacy()
    dis_pri.installation()