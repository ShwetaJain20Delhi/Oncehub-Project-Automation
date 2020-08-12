import time

from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Applicationlogin
from AutomationScript.Locators.CO_Locators.ChatOnce_locator import chatonce, chatbot, text_message, Questions_option
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class ChatOnce_bot():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.maximize_window()
        self.driver.get("https://app3.onceplatform.com/")
        self.driver.implicitly_wait(40)
        time.sleep(4)

    #################################  Login to OH  #################################
    def login_to_OH(self):
        login = Applicationlogin(self.driver)
        login.enter_username("basis-studied-57@staticso2.com")
        time.sleep(3)
        login.enter_password("testing@123")
        time.sleep(3)
        login.click_login()
        time.sleep(10)

    def CO_bot(self):
    ######### select Chatonce from setup menu ###############
        co1 = chatonce(self.driver)
        co1.click_on_setupoption_from_setup()
        time.sleep(3)
        co1.select_chatonce()
        time.sleep(5)
    ############### create bot from scratch #####################
        co2 = chatbot(self.driver)
        co2.click_on_create_bot()
        time.sleep(5)
        co2.select_create_bot_from_scratch()
        time.sleep(3)
        co2.enter_bot_name("Test")
        time.sleep(5)
        co2.click_create()
    ############# select text message option ###################
        co3 = text_message(self.driver)
        co3.select_messages_option()
        time.sleep(3)
        co3.select_text_message_option()
        time.sleep(5)
        co3.enter_internal_label("Label 1")
        time.sleep(3)
        co3.enter_message_text("Hell0!!")
        time.sleep(3)
        co3.click_save()
        time.sleep(3)
        co3.click_back_button_on_interaction()
        time.sleep(5)
    ############# select Questions option ######################
        co4 = Questions_option(self.driver)
        co4.select_messages_option()
        time.sleep(3)
        co4.select_single_select_option()
        time.sleep(3)
        co4.enter_internal_label("Question 1")
        time.sleep(3)
        co4.enter_message_text("Do you want to schedule any meeting??")
        time.sleep(3)
        co4.click_save()
        time.sleep(3)
        co4.click_back_button_on_interaction()
        time.sleep(3)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    Chatbot_website = ChatOnce_bot(driver)
    Chatbot_website.navigate_to_url()
    Chatbot_website.login_to_OH()
    Chatbot_website.CO_bot()