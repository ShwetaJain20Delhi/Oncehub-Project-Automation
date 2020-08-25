import time

from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.Chatonce_Websites_locator import website, website_3dot_functionality, \
    website_3dot_edit, website_3dot_remove, no_website_popup
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Chatonce_Website():

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def No_website(self):
        no = no_website_popup(self.driver)
        no.click_on_close_button()
    def chatoncewebsite(self):
        web = website(self.driver)
        web.click_on_website()
        web.click_on_Add_website()
        web.enter_webiste_name("Test")
        web.enter_webiste_url("https://test.com/")
        web.click_on_Add_webiste_button()
        web.click_on_website()

    def dot3_functionality(self):
        dot = website_3dot_functionality(self.driver)
        dot.click_on_bot_3dot_option()
        ############# Edit Website ###################
        edit = website_3dot_edit(self.driver)
        edit.select_edit_name_url_option()
        edit.enter_webiste_name("Test")
        edit.enter_webiste_url("https://test.com/")
        edit.click_on_save_button()
        ############# Remove Website ###################
        dot = website_3dot_functionality(self.driver)
        dot.click_on_bot_3dot_option()
        remove = website_3dot_remove(self.driver)
        remove.select_remove_option()
        remove.click_checkbox_for_remove_website()
        remove.click_on_remove_website_button()
        remove.click_on_close_button()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.select_co_from_setup()
    site = Chatonce_Website(driver)
    site.No_website()
    site.chatoncewebsite()
    site.dot3_functionality()
    driver.close()