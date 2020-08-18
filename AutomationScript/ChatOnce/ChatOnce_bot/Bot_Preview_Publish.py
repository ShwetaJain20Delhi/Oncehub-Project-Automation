import time

from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Edit import bot_3dot_edit
from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.ChatOnce_Bot_locator import Preview_Chat, toggle_on_publish_button
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class bot_Publish_Preview():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def bot_Preview(self):
    ############# Preview option ###################
        preview = Preview_Chat(self.driver)
        preview.click_preview_button()
        time.sleep(10)
        preview.switch_to_bot()
        time.sleep(4)
        preview.enter_details("It is Good, thanks!!")
        time.sleep(5)
        preview.enter_email_address("Testinginviteoncetesting@gmail.com")
        time.sleep(10)
        preview.Select_timeZone()
        time.sleep(5)
        preview.click_on_dropdown()
        time.sleep(5)
        preview.search_India()
        time.sleep(5)
        preview.click_continue()
        time.sleep(10)
        preview.select_time_slot()
        time.sleep(5)
        preview.click_confirm()
        time.sleep(40)
        preview.close_preview_bot()
        time.sleep(7)

    def bot_publish(self):
        ############# Publish Bot ###################
        publish = toggle_on_publish_button(self.driver)
        publish.click_publish_ON_button()
        time.sleep(7)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.navigate_to_url()
    chatbot_website.login_to_OH()
    chatbot_website.select_co_from_setup()
    edit = bot_3dot_edit(driver)
    edit.bot_edit()
    publish_preview = bot_Publish_Preview(driver)
    publish_preview.bot_publish()
    publish_preview.bot_Preview()
    edit.back_to_lobby_page()
    driver.close()