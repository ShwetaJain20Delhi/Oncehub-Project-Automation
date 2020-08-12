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
        self.driver.find_element_by_xpath("//strong[contains(text(),'Single select')]").click()
    def enter_internal_label(self, label):
        self.driver.find_element_by_id("interactionName").send_keys(label)
    def enter_message_text(self, text):
        self.driver.find_element_by_id("interactionText").send_keys(text)
    def click_save(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Save')]").click()
    def click_back_button_on_interaction(self):
        self.driver.find_element_by_xpath("//button[@class='back_btn capitalize oui-icon-button oui-primary']").click()
