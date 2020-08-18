import time

from AutomationScript.Locators.CO_Locators.ChatBot_Launch_locator import website_Launch_Chatbot
from AutomationScript.Locators.CO_Locators.ChatOnce_Bot_locator import Preview_Chat
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Create_ChatOnce_bot():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url_for_chatbot(self):
        self.driver.maximize_window()
        self.driver.get("file:///C:/Backup/desktop/Bot/Automation%20Bot/Test.HTML")
        self.driver.implicitly_wait(30)
        time.sleep(20)

    def launch(self):
        bot = website_Launch_Chatbot(self.driver)
        bot.click_chatbot_icon()
        time.sleep(10)
        preview = Preview_Chat(self.driver)
        preview.enter_details("It is Good, thanks!!")
        time.sleep(5)
        preview.enter_email_address("Testinginviteoncetesting@gmail.com")
        time.sleep(17)
        preview.Select_timeZone()
        time.sleep(5)
        preview.click_on_dropdown()
        time.sleep(5)
        preview.search_India()
        time.sleep(5)
        preview.click_continue()
        time.sleep(18)
        preview.select_time_slot()
        time.sleep(5)
        preview.click_confirm()
        time.sleep(40)
        preview.close_preview_bot()
        time.sleep(7)



if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    launch_website = Create_ChatOnce_bot(driver)
    launch_website.navigate_to_url_for_chatbot()
    launch_website.launch()
    driver.close()