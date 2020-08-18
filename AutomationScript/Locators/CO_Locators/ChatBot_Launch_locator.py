class website_Launch_Chatbot():
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_url_for_chatbot(self):
        self.driver.maximize_window()
        self.driver.get("file:///C:/Backup/desktop/Bot/Automation%20Bot/Test.HTML")
    def click_chatbot_icon(self):
        self.driver.switch_to_frame("co-widget-iframe")
        print("run")
        self.driver.find_element_by_xpath("//div[@data-testid='toggle-btn']").click()
        print("hello")
