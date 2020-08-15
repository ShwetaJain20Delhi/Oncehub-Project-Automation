import time

from AutomationScript.ChatOnce.ChatOnce_bot.Create_chatonce_bot import Create_ChatOnce_bot
from AutomationScript.Locators.CO_Locators.Chatonce_Websites_locator import website, website_3dot_functionality, \
    website_3dot_edit, website_3dot_remove, no_website_popup
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Chatonce_Website():

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def No_website(self):
        no = no_website_popup(self.driver)
        no.click_on_close_button()
        time.sleep(7)
    def chatoncewebsite(self):
        web = website(self.driver)
        web.click_on_Add_website()
        time.sleep(3)
        web.enter_webiste_name("Test")
        time.sleep(3)
        web.enter_webiste_url("https://test.com/")
        time.sleep(3)
        web.click_on_Add_webiste_button()
        time.sleep(7)
        web.click_on_website()
        time.sleep(7)

    def dot3_functionality(self):
        dot = website_3dot_functionality(self.driver)
        dot.click_on_bot_3dot_option()
        time.sleep(3)
        ############# Edit Website ###################
        edit = website_3dot_edit(self.driver)
        edit.select_edit_name_url_option()
        time.sleep(5)
        edit.enter_webiste_name("Test")
        time.sleep(3)
        edit.enter_webiste_url("https://test.com/")
        time.sleep(3)
        edit.click_on_save_button()
        time.sleep(7)
        ############# Remove Website ###################
        dot = website_3dot_functionality(self.driver)
        dot.click_on_bot_3dot_option()
        time.sleep(3)
        remove = website_3dot_remove(self.driver)
        remove.select_remove_option()
        time.sleep(5)
        remove.click_checkbox_for_remove_website()
        time.sleep(3)
        remove.click_on_remove_website_button()
        time.sleep(5)
        remove.click_on_close_button()
        time.sleep(7)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.navigate_to_url()
    chatbot_website.login_to_OH()
    chatbot_website.select_co_from_setup()
    site = Chatonce_Website(driver)
    site.No_website()
    site.chatoncewebsite()
    site.dot3_functionality()
    driver.close()