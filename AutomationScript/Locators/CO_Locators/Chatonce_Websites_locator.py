import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class website():
    def __init__(self, driver):
        self.driver = driver
    def click_on_website(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Websites')]"))).click()
    def click_on_Add_website(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add website')]"))).click()
    def enter_webiste_name(self, name):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "websiteNameTxt"))).send_keys(name)
    def enter_webiste_url(self, url):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "websiteUrlTxt"))).send_keys(url)
    def click_on_Add_webiste_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "savebutton"))).click()


class website_3dot_functionality():
    def __init__(self, driver):
        self.driver = driver
    def click_on_bot_3dot_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Test')]//parent::div//parent::td//following-sibling::td//following-sibling::td//following-sibling::td//following-sibling::td//span[@class='website-more-setting']"))).click()


class website_3dot_edit():
    def __init__(self, driver):
        self.driver = driver
    def select_edit_name_url_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Edit name & URL')]"))).click()
    def enter_webiste_name(self, name):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "websiteNameTxt"))).clear()
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "websiteNameTxt"))).send_keys(name)
    def enter_webiste_url(self, url):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "websiteUrlTxt"))).clear()
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.ID, "websiteUrlTxt"))).send_keys(url)
    def click_on_save_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Save')]"))).click()


class website_3dot_remove():
    def __init__(self, driver):
        self.driver = driver
    def select_remove_option(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@title='Remove']"))).click()
    def click_checkbox_for_remove_website(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),' I want to remove this website')]"))).click()
    def click_on_remove_website_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),' Remove website ')]"))).click()
    def click_on_close_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Close')]"))).click()


class no_website_popup():
    def __init__(self, driver):
        self.driver = driver
    def click_on_close_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Close')]"))).click()

