from selenium.webdriver import ActionChains

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


class adjust_drop_down():
    def __init__(self, driver):
        self.driver = driver
    def drag_conversations_to_interactions_option(self):
        flag = self.driver.find_element_by_xpath("//oui-icon[@aria-label='Message-24']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        source_element = self.driver.find_element_by_xpath("//oui-icon[@aria-label='Message-24']")
        flag = self.driver.find_element_by_id("reachOutSection")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        target_element = self.driver.find_element_by_id("reachOutSection")
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element).pause(20).move_to_element(target_element).release(target_element).perform()
        # actions.drag_and_drop(source_element, target_element).perform()
        flag = self.driver.find_element_by_xpath("//oui-icon[@aria-label='Text-question-24']")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        source_element1 = self.driver.find_element_by_xpath("//oui-icon[@aria-label='Text-question-24']")
        target_element1 = self.driver.find_element_by_id("reachOutSection")
        actions = ActionChains(self.driver)
        # actions.drag_and_drop(source_element1, target_element1).perform()
        actions.click_and_hold(source_element1).pause(20).move_to_element(target_element1).release(target_element1).perform()





