import time

from AutomationScript.Locators.CO_Locators.ChatOnce_Bot_locator import Chatonce, chatbot, text_message, Questions_option, Actions_option
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Applicationlogin
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class Create_ChatOnce_bot():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def select_co_from_setup(self):
    ######### select Chatonce from setup menu ###############
        co1 = Chatonce(self.driver)
        co1.click_on_setupoption_from_setup()
        co1.select_chatonce()

    def create_bot(self):
    ############### create bot from scratch #####################
        co2 = chatbot(self.driver)
        co2.click_on_create_bot()
        co2.select_create_bot_from_scratch()
        co2.enter_bot_name("Test")
        co2.click_create()
    ############# select text message option ###################
        co3 = text_message(self.driver)
        co3.select_messages_option()
        co3.select_text_message_option()
        co3.enter_internal_label("Label 1")
        co3.enter_message_text("Hell0!!")
        co3.click_save()
        co3.click_back_button_on_interaction()
        co3.drag_Message_interaction_to_ReachingOut()
    ############# select Questions option ######################
        co4 = Questions_option(self.driver)
        co4.select_messages_option()
        co4.select_single_select_option()
        co4.enter_internal_label("Question 1")
        co4.enter_message_text("How's your day today??")
        co4.click_save()
        co4.click_back_button_on_interaction()
############# select text message option ###################
        co3 = text_message(self.driver)
        co3.select_messages_option()
        co3.select_text_message_option()
        co3.enter_internal_label("Label 2")
        co3.enter_message_text("Please schedule the meeting with us for further investigation")
        co3.click_save()
        co3.click_back_button_on_interaction()
############# select Actions option ###################
        co4 = Actions_option(self.driver)
        co4.select_messages_option()
        co4.select_single_select_option()
        co4.enter_internal_label("Action Performed")
        co4.click_on_dropdown_for_master_page()
        co4.select_master_page()
        co4.select_Event_type_drop_down()
        co4.select_event_type()
        co4.click_save_button()
        co4.click_back_button_on_interaction()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    chatbot_website = Create_ChatOnce_bot(driver)
    chatbot_website.select_co_from_setup()
    chatbot_website.create_bot()
    driver.close()