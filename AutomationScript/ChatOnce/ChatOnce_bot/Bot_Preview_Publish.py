import time

from AutomationScript.ChatOnce.ChatOnce_bot.Bot_Edit import bot_3dot_edit
from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.ChatOnce_Bot_locator import Preview_Chat, toggle_on_publish_button
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
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
        preview.switch_to_bot()
        preview.enter_details("It is Good, thanks!!")
        preview.enter_email_address("Testinginviteoncetesting@gmail.com")
        preview.Select_timeZone()
        preview.click_on_dropdown()
        preview.search_India()
        preview.click_continue()
        preview.select_time_slot()
        preview.click_confirm()
        preview.close_preview_bot()

    def bot_publish(self):
        ############# Publish Bot ###################
        publish = toggle_on_publish_button(self.driver)
        publish.click_publish_ON_button()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.select_co_from_setup()
    edit = bot_3dot_edit(driver)
    edit.bot_edit()
    publish_preview = bot_Publish_Preview(driver)
    publish_preview.bot_publish()
    publish_preview.bot_Preview()
    edit.back_to_lobby_page()
    driver.close()