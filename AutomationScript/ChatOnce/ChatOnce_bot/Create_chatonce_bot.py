import time

from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Applicationlogin
from AutomationScript.Locators.CO_Locators.ChatOnce_Bot_locator import chatonce, chatbot, text_message, \
    Questions_option, \
    Actions_option, Preview_Chat
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Create_ChatOnce_bot():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.maximize_window()
        self.driver.get("https://app3.onceplatform.com/")
        self.driver.implicitly_wait(50)
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

    def select_co_from_setup(self):
    ######### select Chatonce from setup menu ###############
        co1 = chatonce(self.driver)
        co1.click_on_setupoption_from_setup()
        time.sleep(3)
        co1.select_chatonce()
        time.sleep(8)

    def create_bot(self):
    ############### create bot from scratch #####################
        co2 = chatbot(self.driver)
        co2.click_on_create_bot()
        time.sleep(5)
        co2.select_create_bot_from_scratch()
        time.sleep(3)
        co2.enter_bot_name("Test")
        time.sleep(5)
        co2.click_create()
        time.sleep(5)
    # ############# select text message option ###################
    #     co3 = text_message(self.driver)
    #     co3.select_messages_option()
    #     time.sleep(3)
    #     co3.select_text_message_option()
    #     time.sleep(5)
    #     co3.enter_internal_label("Label 1")
    #     time.sleep(3)
    #     co3.enter_message_text("Hell0!!")
    #     time.sleep(3)
    #     co3.click_save()
    #     time.sleep(3)
    #     co3.click_back_button_on_interaction()
    #     time.sleep(5)
    #     co3.drag_Message_interaction_to_ReachingOut()
    #     time.sleep(5)
#     ############# select Questions option ######################
#         co4 = Questions_option(self.driver)
#         co4.select_messages_option()
#         time.sleep(3)
#         co4.select_single_select_option()
#         time.sleep(3)
#         co4.enter_internal_label("Question 1")
#         time.sleep(3)
#         co4.enter_message_text("How's your day today??")
#         time.sleep(5)
#         co4.click_save()
#         time.sleep(7)
#         co4.click_back_button_on_interaction()
#         time.sleep(5)
# ############# select text message option ###################
#         co3 = text_message(self.driver)
#         co3.select_messages_option()
#         time.sleep(3)
#         co3.select_text_message_option()
#         time.sleep(5)
#         co3.enter_internal_label("Label 2")
#         time.sleep(3)
#         co3.enter_message_text("Please schedule the meeting with us for further investigation")
#         time.sleep(3)
#         co3.click_save()
#         time.sleep(3)
#         co3.click_back_button_on_interaction()
#         time.sleep(5)
############# select Actions option ###################
        co4 = Actions_option(self.driver)
        co4.select_messages_option()
        time.sleep(3)
        co4.select_single_select_option()
        time.sleep(3)
        co4.enter_internal_label("Action Performed")
        time.sleep(3)
        co4.click_on_dropdown_for_master_page()
        time.sleep(3)
        co4.select_master_page()
        time.sleep(3)
        co4.select_Event_type_drop_down()
        time.sleep(3)
        co4.select_event_type()
        time.sleep(3)
        co4.click_save_button()
        time.sleep(10)
        co4.click_back_button_on_interaction()
        time.sleep(3)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.navigate_to_url()
    chatbot_website.login_to_OH()
    chatbot_website.select_co_from_setup()
    chatbot_website.create_bot()
    driver.close()