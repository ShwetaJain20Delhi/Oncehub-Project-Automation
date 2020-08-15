from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class chatonce():
    def __init__(self, driver):
        self.driver = driver
    def click_on_setupoption_from_setup(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Setup')]").click()
    def select_chatonce(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'ChatOnce setup')]").click()

class chatbot():
    def __init__(self, driver):
        self.driver = driver
        self.scratch = "createBotFromScratch"
        self.name = "botNameTxt"
    def click_on_create_bot(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Create bot')]").click()
    def select_create_bot_from_scratch(self):
        self.driver.find_element_by_id(self.scratch).click()
    def enter_bot_name(self, name):
        self.driver.find_element_by_id(self.name).send_keys(name)
    def click_create(self):
        self.driver.find_element_by_xpath("// span[contains(text(), ' Create ')]").click()


class text_message():
    def __init__(self, driver):
        self.driver = driver
    def select_messages_option(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Messages ')]").click()
    def select_text_message_option(self):
        self.driver.find_element_by_xpath("//strong[contains(text(),'Text message')]").click()
    def enter_internal_label(self, label):
        self.driver.find_element_by_id("interactionName").send_keys(label)
    def enter_message_text(self, text):
        self.driver.find_element_by_id("interactionText").send_keys(text)
    def click_save(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Save')]").click()
    def click_back_button_on_interaction(self):
        self.driver.find_element_by_xpath("//button[@class='back_btn capitalize oui-icon-button oui-primary']").click()
    def drag_Message_interaction_to_ReachingOut(self):
        flag = self.driver.find_element_by_xpath("//oui-icon[@aria-label='Message-24']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        source_element = self.driver.find_element_by_xpath("//oui-icon[@aria-label='Message-24']")
        target_element = self.driver.find_element_by_id("reachOutSection")
        actions = ActionChains(self.driver)
        flag = self.driver.find_element_by_id("reachOutSection")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        actions.click_and_hold(source_element).pause(7).move_to_element(target_element).release(target_element).perform()


class Questions_option():
    def __init__(self, driver):
        self.driver = driver
    def select_messages_option(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Questions')]").click()
    def select_single_select_option(self):
        self.driver.find_element_by_xpath("//strong[contains(text(),'Text question')]").click()
    def enter_internal_label(self, label):
        self.driver.find_element_by_id("interactionName").send_keys(label)
    def enter_message_text(self, text):
        self.driver.find_element_by_id("interactionText").send_keys(text)
    def click_save(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Save')]").click()
    def click_back_button_on_interaction(self):
        self.driver.find_element_by_xpath("//button[@class='back_btn capitalize oui-icon-button oui-primary']").click()


class Actions_option():
    def __init__(self, driver):
        self.driver = driver
    def select_messages_option(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Actions ')]").click()
    def select_single_select_option(self):
        self.driver.find_element_by_xpath("//strong[contains(text(),'Schedule')]").click()
    def enter_internal_label(self, label):
        self.driver.find_element_by_id("interactionName").send_keys(label)
    def click_on_dropdown_for_master_page(self):
        flag = self.driver.find_element_by_xpath("//oui-select[ @ formcontrolname = 'scheduleActionMasterPage']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//oui-select[ @ formcontrolname = 'scheduleActionMasterPage']").click()
    def select_master_page(self):
        self.driver.find_element_by_xpath("//span[contains(text(), 'Shweta_Test111')]").click()
    def select_Event_type_drop_down(self):
        self.driver.find_element_by_xpath("//oui-select[@formcontrolname='scheduleActionEventRule']").click()
    def select_event_type(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'15-minute meeting')]").click()
    def click_save_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
    def click_back_button_on_interaction(self):
        self.driver.find_element_by_xpath("//button[@class='back_btn capitalize oui-icon-button oui-primary']").click()


class Preview_Chat():
    def __init__(self, driver):
        self.driver = driver
    def click_preview_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),' Preview ')]").click()
    def enter_details(self, information):
        self.driver.switch_to_window().alert()
        pinfo = self.driver.find_element_by_xpath("//div[@class='chat-footer']//following-sibling::div[1]//child::textarea")
        pinfo.send_keys(information)
        pinfo.send_keys(Keys.ENTER)
    def enter_email_address(self, email):
        self.driver.find_element_by_xpath("//input[@placeholder='Enter email address']").send_keys(email)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter email address']").send_keys(Keys.ENTER)
    def Select_timeZone(self):
        self.driver.find_element_by_xpath("//div[@class='time-zone-container']").click()
    def click_on_dropdown(self):
        self.driver.find_element_by_xpath("//label[@class ='custom-select']").click()
    def search_India(self):
        flag = self.driver.find_element_by_xpath("//li[contains(text(),'India')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.find_element_by_xpath("//li[contains(text(),'India')]").click()
    def click_continue(self):
        self.driver.find_element_by_xpath("// button[contains(text(), 'Continue')]").click()
    def select_time_slot(self):
        self.driver.find_element_by_xpath("// li[contains(text(), '10:00') and @class ='border-style border-primary text-secondary bg-primary-hover']").click()
    def click_confirm(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Confirm')]").click()
    def close_preview_bot(self):
        self.driver.find_element_by_xpath("//span[@class='chat-cross-icon']").click()


class toggle_on_publish_button():
    def __init__(self, driver):
        self.driver = driver
    def click_publish_ON_button(self):
        self.driver.find_element_by_xpath("//span[@class='on-off-btn']").click()


class return_to_Bot_lobby_page():
    def __init__(self, driver):
        self.driver = driver
    def click_back_button(self):
        self.driver.find_element_by_xpath("//parent::h3//parent::div//a[@href='/chatonce/bots']").click()

class Bot_3dot_functionality():
    def __init__(self, driver):
        self.driver = driver
    def click_on_bot_3dot_option(self):
        self.driver.find_element_by_xpath("//h4[contains(text(),'Test')]//parent::div//parent::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//span[@class='bot-more-setting']").click()


class Bot_3dot_edit():
    def __init__(self, driver):
        self.driver = driver
    def select_edit_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Edit')]").click()

class Bot_3dot_duplicate():
    def __init__(self, driver):
        self.driver = driver
    def select_duplicate_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Duplicate')]").click()
    def enter_new_bot_name(self, name):
        self.driver.find_element_by_id("botNameTxt").send_keys(name)
    def click_duplicate_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Duplicate')]").click()


class Bot_3dot_Rename():
    def __init__(self, driver):
        self.driver = driver
    def select_rename_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Rename')]").click()
    def Rename_bot(self, rename):
        self.driver.find_element_by_id("nameTxt").clear()
        self.driver.find_element_by_id("nameTxt").send_keys(rename)
    def click_save_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()


class Bot_3dot_Delete():
    def __init__(self, driver):
        self.driver = driver
    def select_delete_option(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Delete')]").click()
    def click_deleteBot_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Delete bot')]").click()
    def click_close_button(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Close')]").click()








