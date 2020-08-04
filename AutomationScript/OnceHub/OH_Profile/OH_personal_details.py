from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
        self.driver.implicitly_wait(35)

    #################################  Login to OH  #################################
    def login_to_OH(self):
        login = Applicationlogin(self.driver)
        login.enter_username("location-numeral-38@staticso2.com")
        login.enter_password("testing@123")
        login.click_login()
        # driver.find_element_by_name("email")
        # driver.find_element_by_name("email").send_keys("death-mad-34@staticso2.com")
        # driver.find_element_by_name("password")
        # driver.find_element_by_name("password").send_keys("testing@123")
        # driver.find_element_by_id("signIn").click()
        time.sleep(10)

#################################  Edit Profile settings  #################################

    def select_my_profile(self):
        personal = Personalsetting(self.driver)
        personal.click_profile_icon()
        time.sleep(3)
        personal.select_myprofile()
        time.sleep(5)

    def edit_personal_details(self):
        personal1 = Personalsetting(self.driver)
        personal1.click_3dot()
        time.sleep(5)
        personal1.select_editpersonaldetails_option()
        time.sleep(3)
        personal1.editpersonaldetails("Admin")
        time.sleep(3)
        personal1.click_save()
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    personal_setting.select_my_profile()
    personal_setting.edit_personal_details()

        # driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
        # time.sleep(3)
        # driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[1]/a/span").click()
        # time.sleep(5)
        # driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/oh-page-header/div[1]/div[3]/div/button/span/oui-icon").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//span[contains(text(),'Edit personal details')]").click()
        # time.sleep(2)
        # driver.find_element_by_name("lastName").clear()
        # driver.find_element_by_name("lastName").send_keys("Admin")
        # time.sleep(2)
        # driver.find_element_by_xpath("//*[@id='oui-dialog-0']/form/div[2]/div[1]/button").click()
        # time.sleep(5)
        # driver.close()



