import time

from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.ChatOnce_Display_Privacy_Install_locator import display, Privacy, \
    Installation
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Chatonce_Display_Privacy_Install():

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def Display(self):
        dis = display(self.driver)
        dis.click_on_display()
        time.sleep(5)
        dis.choose_a_shape()
        time.sleep(5)
        dis.choose_a_theme()
        time.sleep(5)
        dis.click_on_save_button()
        time.sleep(5)

    def Privacy(self):
        pri = Privacy(self.driver)
        pri.click_on_privacy()
        time.sleep(7)
        pri.select_Website_analytics()
        time.sleep(5)
        pri.select_2nd_radio_button()
        time.sleep(3)
        pri.copied_script_when_consent_is_granted()
        time.sleep(5)
        pri.copied_script_when_consent_is_revoked()
        time.sleep(5)
        pri.click_discard_button()
        time.sleep(5)
        pri.turn_toggle_off_for_website_analytics()
        time.sleep(5)
        pri.click_discard()
        time.sleep(5)

    def installation(self):
        install = Installation(self.driver)
        install.click_on_Installation()
        time.sleep(5)
        install.select_Intall_it_yourself_option()
        time.sleep(5)
        install.click_copy_code()
        time.sleep(5)
        install.click_verify_installation()
        time.sleep(5)
        install.click_close()
        time.sleep(7)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.navigate_to_url()
    chatbot_website.login_to_OH()
    chatbot_website.select_co_from_setup()
    dis_pri = Chatonce_Display_Privacy_Install(driver)
    dis_pri.Display()
    dis_pri.Privacy()
    dis_pri.installation()