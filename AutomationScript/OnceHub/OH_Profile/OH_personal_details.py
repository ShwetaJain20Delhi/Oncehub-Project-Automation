from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Applicationlogin
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import Personalsetting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class OH_personal_setting():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.maximize_window()
        self.driver.get("https://app2.onceplatform.com/")
        self.driver.implicitly_wait(50)
        time.sleep(10)

    #################################  Login to OH  #################################
    def login_to_OH(self):
        login = Applicationlogin(self.driver)
        login.enter_username("location-numeral-38@staticso2.com")
        login.enter_password("testing@123")
        login.click_login()
        time.sleep(10)


#################################  Edit Profile settings  #################################

    def select_my_profile(self):
        personal = Personalsetting(self.driver)
        personal.click_profile_icon()
        personal.select_myprofile()

    def edit_personal_details(self):
        personal1 = Personalsetting(self.driver)
        personal1.click_3dot()
        personal1.select_editpersonaldetails_option()
        personal1.editpersonaldetails("Admin")
        personal1.click_save()
        time.sleep(5)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    personal_setting.select_my_profile()
    personal_setting.edit_personal_details()
    driver.close()




