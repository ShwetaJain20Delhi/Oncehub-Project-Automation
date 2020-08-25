import time

from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.ChatOnce_Bot_locator import Bot_3dot_functionality, Bot_3dot_edit, return_to_Bot_lobby_page
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class bot_3dot_edit():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def bot_edit(self):
        dot = Bot_3dot_functionality(self.driver)
        dot.click_on_bot_3dot_option()
        edit = Bot_3dot_edit(self.driver)
        edit.select_edit_option()

    def back_to_lobby_page(self):
        lobby = return_to_Bot_lobby_page(self.driver)
        lobby.click_back_button()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.select_co_from_setup()
    edit = bot_3dot_edit(driver)
    edit.bot_edit()
    edit.back_to_lobby_page()
    driver.close()
