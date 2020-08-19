import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class profile_video_conferencing():
    def __init__(self, driver):
        self.driver = driver
    def select_video_conferencing(self):
        self.driver.find_element_by_xpath("// span[contains(text(), 'Video conferencing')]").click()


class connect_zoom():
    def __init__(self, driver):
        self.driver = driver
    def connect_zoom(self):
        zoom = self.driver.find_element_by_xpath("//div[@id='connectZoom']//input[@type='button']")
        if zoom.is_displayed():
            zoom.click()
            self.driver.switch_to_window(self.driver.window_handles[1])
            time.sleep(10)
            self.driver.find_element_by_xpath("//span[contains(text(),'Sign in with Google')]").click()
            time.sleep(5)
            self.driver.find_element_by_id("identifierId").send_keys("testinginviteoncetesting@gmail.com")
            time.sleep(5)
            self.driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
            time.sleep(5)
        else:
            print("Zoom is already connected..")


class connect_gotomeeting():
    def __init__(self, driver):
        self.driver = driver
    def connect_goto(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.implicitly_wait(10)
        gotomeeting = self.driver.find_element_by_xpath("//div[@id='connectGotoLink']//input[@type='button']")
        if gotomeeting.is_displayed():
            ActionChains(self.driver).move_to_element(gotomeeting).click(gotomeeting).perform()
            self.driver.switch_to_window(self.driver.window_handles[1])
            time.sleep(10)
            self.driver.find_element_by_id("emailAddress").send_keys("333oncehub@gmail.com")
            time.sleep(3)
            self.driver.find_element_by_id("next-button").click()
            time.sleep(5)
            self.driver.find_element_by_id("password").send_keys("test@1234")
            time.sleep(5)
            self.driver.find_element_by_id("submit").click()
            time.sleep(15)
            self.driver.switch_to_window(self.driver.window_handles[0])
            self.driver.find_element_by_xpath("//span[contains(text(),'Connected to GoToMeeting')]//following-sibling::div[@title='Close']").click()
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            print("GoToMeeting is already connected..")


class connect_webex():
    def __init__(self, driver):
        self.driver = driver
    def connect_webex_meeting(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.implicitly_wait(10)
        webex_m = self.driver.find_element_by_xpath("//div[@class='webExOAuth']//input[@type='button']")
        if webex_m.is_displayed():
            ActionChains(self.driver).move_to_element(webex_m).click(webex_m).perform()
            time.sleep(10)
            self.driver.switch_to_window(self.driver.window_handles[1])
            time.sleep(30)
            self.driver.find_element_by_xpath("//input[@aria-label='Your email address']").send_keys("ushankar@oncehub.com")
            time.sleep(3)
            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Next')]").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("// span[contains(text(), 'oncehub.webex.com')]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("// span[contains(text(), 'Continue')]").click()
            time.sleep(5)
            self.driver.find_element_by_name("IDToken2").send_keys("Once1once1@")
            time.sleep(5)
            self.driver.find_element_by_name("Login.Submit").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("// button[ @ type = 'submit' and contains(text(), 'Accept')]").click()
            time.sleep(15)
            self.driver.switch_to_window(self.driver.window_handles[0])
            self.driver.find_element_by_xpath("//span[contains(text(),'Connected to Webex')]//following-sibling::div[@title='Close']").click()
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            print("Webex is already connected..")


class disconnect():
    def __init__(self, driver):
        self.driver = driver
    def disconnect_zoom(self):
        self.driver.find_element_by_xpath("//span[@id='zoomUserName']//following::a[contains(text(),'Disconnect')][1]").click()
    def disconnect_goto_meeting(self):
        flag = self.driver.find_element_by_xpath("//span[@id='userName']//following::a[contains(text(),'Disconnect')][1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        time.sleep(5)
        self.driver.find_element_by_xpath("//span[@id='userName']//following::a[contains(text(),'Disconnect')][1]").click()
    def disconnect_webex_meeting(self):
        flag = self.driver.find_element_by_xpath("//div[@id='WebExLoadData']//following::a[contains(text(),'Disconnect')][1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@id='WebExLoadData']//following::a[contains(text(),'Disconnect')][1]").click()
    def click_yes(self):
        self.driver.find_element_by_id("yesbtn").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
