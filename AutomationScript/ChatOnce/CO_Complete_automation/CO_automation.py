from AutomationScript.ChatOnce.ChatOnce_Display_Privacy_Install import Chatonce_Display_Privacy_Install
from AutomationScript.ChatOnce.ChatOnce_Website import Chatonce_Website
from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Delete import bot_3dot_delete
from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Duplicate import bot_3dot_duplicate
from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Edit import bot_3dot_edit
from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Preview_Publish import bot_Publish_Preview
from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Rename import bot_3dot_rename
from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver
import time


class signup_CO_product_selection():
    driver = None

    def __init__(self, driver):
        self.driver = driver


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.navigate_to_url()
    chatbot_website.login_to_OH()
    chatbot_website.select_co_from_setup()
    chatbot_website.create_bot()
    publish_preview = bot_Publish_Preview(driver)
    publish_preview.bot_publish()
    # publish_preview.bot_Preview()
    edit = bot_3dot_edit(driver)
    edit.back_to_lobby_page()
    edit.bot_edit()
    edit.back_to_lobby_page()
    bot_duplicate = bot_3dot_duplicate(driver)
    bot_duplicate.bot_duplicate()
    edit = bot_3dot_edit(driver)
    edit.back_to_lobby_page()
    bot_duplicate = bot_3dot_rename(driver)
    bot_duplicate.bot_rename()
    bot_duplicate = bot_3dot_delete(driver)
    bot_duplicate.bot_delete()
    dis_pri = Chatonce_Display_Privacy_Install(driver)
    dis_pri.Display()
    dis_pri.Privacy()
    dis_pri.installation()
    site = Chatonce_Website(driver)
    site.chatoncewebsite()
    site.dot3_functionality()
    driver.close()
