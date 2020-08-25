import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class website_Launch_Chatbot():
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_url_for_chatbot(self):
        self.driver.maximize_window()
        self.driver.get("file:///C:/Backup/desktop/Bot/Automation%20Bot/Test.HTML")
    def click_chatbot_icon(self):
        self.driver.switch_to_frame("co-widget-iframe")
        print("run")
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@data-testid='toggle-btn']"))).click()
        print("hello")
