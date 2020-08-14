import time

from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Edit import bot_3dot_edit
from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.ChatOnce_Bot_locator import Bot_3dot_functionality, Bot_3dot_Rename
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class bot_3dot_rename():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def bot_rename(self):
        dot = Bot_3dot_functionality(self.driver)
        dot.click_on_bot_3dot_option()
        time.sleep(3)
        rename = Bot_3dot_Rename(self.driver)
        rename.select_rename_option()
        time.sleep(6)
        rename.Rename_bot("Test2")
        time.sleep(5)
        rename.click_save_button()
        time.sleep(10)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.navigate_to_url()
    chatbot_website.login_to_OH()
    chatbot_website.select_co_from_setup()
    bot_duplicate = bot_3dot_rename(driver)
    bot_duplicate.bot_rename()
    driver.close()