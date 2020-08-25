import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Chatonce():
    def __init__(self, driver):
        self.driver = driver
    def click_on_setupoption_from_setup(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "// span[contains(text(), 'Setup')]"))).click()
    def select_chatonce(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(text(), 'ChatOnce setup')]"))).click()

class chatbot():
    def __init__(self, driver):
        self.driver = driver
        self.scratch = "createBotFromScratch"
        self.name = "botNameTxt"
    def click_on_create_bot(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "// span[contains(text(), 'Create bot')]"))).click()
    def select_create_bot_from_scratch(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.scratch))).click()
    def enter_bot_name(self, name):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, self.name))).send_keys(name)
    def click_create(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "// span[contains(text(), ' Create ')]"))).click()


class text_message():
    def __init__(self, driver):
        self.driver = driver
    def select_messages_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//li[contains(text(),' Messages ')]"))).click()
    def select_text_message_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//strong[contains(text(),'Text message')]"))).click()
    def enter_internal_label(self, label):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "interactionName"))).send_keys(label)
    def enter_message_text(self, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "interactionText"))).send_keys(text)
    def click_save(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "// span[contains(text(), 'Save')]"))).click()
    def click_back_button_on_interaction(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@class='back_btn capitalize oui-icon-button oui-primary']"))).click()
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
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//li[contains(text(),'Questions')]"))).click()
    def select_single_select_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//strong[contains(text(),'Text question')]"))).click()
    def enter_internal_label(self, label):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "interactionName"))).send_keys(label)
    def enter_message_text(self, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "interactionText"))).send_keys(text)
    def click_save(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "// span[contains(text(), 'Save')]"))).click()
    def click_back_button_on_interaction(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@class='back_btn capitalize oui-icon-button oui-primary']"))).click()


class Actions_option():
    def __init__(self, driver):
        self.driver = driver
    def select_messages_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//li[contains(text(),' Actions ')]"))).click()
    def select_single_select_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//strong[contains(text(),'Schedule')]"))).click()
    def enter_internal_label(self, label):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "interactionName"))).send_keys(label)
    def click_on_dropdown_for_master_page(self):
        flag = self.driver.find_element_by_xpath("//oui-select[ @ formcontrolname = 'scheduleActionMasterPage']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//oui-select[ @ formcontrolname = 'scheduleActionMasterPage']"))).click()
    def select_master_page(self):
        try:
            # self.driver.find_element_by_xpath("//span[contains(text(),'Shweta_Test111')]").click()
            Master_page = self.driver.find_element_by_xpath("//span[contains(text(),'Shweta_Automation')]")
            if Master_page.is_displayed():
                print("page is found")
                Master_page.click()
        except NoSuchElementException:
            print("page is not found")
            wait = WebDriverWait(self.driver, 20)
            wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'shweta_a')]"))).click()
    def select_Event_type_drop_down(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//oui-select[@formcontrolname='scheduleActionEventRule']"))).click()
    def select_event_type(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'15-minute meeting')]"))).click()
    def click_save_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Save')]"))).click()
    def click_back_button_on_interaction(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@class='back_btn capitalize oui-icon-button oui-primary']"))).click()


class Preview_Chat():
    def __init__(self, driver):
        self.driver = driver
    def click_preview_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),' Preview ')]"))).click()
    def switch_to_bot(self):
        self.driver.switch_to_frame("co-widget-iframe")
    def enter_details(self, data):
        pinfo = self.driver.find_element_by_xpath("//div[@class='chat-footer']//following-sibling::div[1]//child::textarea")
        pinfo.send_keys(data)
        pinfo.send_keys(Keys.ENTER)
    def enter_email_address(self, email):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter email address']"))).send_keys(email)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter email address']"))).send_keys(Keys.ENTER)
    def Select_timeZone(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='time-zone-container']"))).click()
    def click_on_dropdown(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "custom-select-element"))).click()
    def search_India(self):
        flag = self.driver.find_element_by_xpath("//li[contains(text(),'India')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//li[contains(text(),'India')]"))).click()
    def click_continue(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "// button[contains(text(), 'Continue')]"))).click()
    def select_time_slot(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "// li[contains(text(), '10:15') and @class ='border-style border-primary text-secondary bg-primary-hover']"))).click()
    def click_confirm(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Confirm')]"))).click()
    def close_preview_bot(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[@class='chat-cross-icon']"))).click()
        self.driver.switch_to_default_content()


class toggle_on_publish_button():
    def __init__(self, driver):
        self.driver = driver
    def click_publish_ON_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[@class='on-off-btn']"))).click()


class return_to_Bot_lobby_page():
    def __init__(self, driver):
        self.driver = driver
    def click_back_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//parent::h3//parent::div//a[@href='/chatonce/bots']"))).click()

class Bot_3dot_functionality():
    def __init__(self, driver):
        self.driver = driver
    def click_on_bot_3dot_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Test')]//parent::div//parent::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//span[@class='bot-more-setting']"))).click()


class Bot_3dot_edit():
    def __init__(self, driver):
        self.driver = driver
    def select_edit_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Edit')]"))).click()

class Bot_3dot_duplicate():
    def __init__(self, driver):
        self.driver = driver
    def select_duplicate_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Duplicate')]"))).click()
    def enter_new_bot_name(self, name):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "botNameTxt"))).send_keys(name)
    def click_duplicate_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Duplicate')]"))).click()


class Bot_3dot_Rename():
    def __init__(self, driver):
        self.driver = driver
    def select_rename_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Rename')]"))).click()
    def Rename_bot(self, rename):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "nameTxt"))).clear()
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "nameTxt"))).send_keys(rename)
    def click_save_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Save')]"))).click()


class Bot_3dot_Delete():
    def __init__(self, driver):
        self.driver = driver
    def select_delete_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Delete')]"))).click()
    def click_deleteBot_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Delete bot')]"))).click()
    def click_close_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Close')]"))).click()