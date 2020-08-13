import time

from selenium.webdriver.common.by import By

from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class login():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.maximize_window()
        self.driver.get("https://go3.onceplatform.com/screen345")
        self.driver.implicitly_wait(40)
        time.sleep(4)

    def BookingPage_Overview(self):
        self.driver.implicitly_wait(20)
        time.sleep(10)
        # time.sleep(10)self.driver.find_element(By.XPATH, value="//a[@class='semiBold ng-binding']").click()
        self.driver.find_element(By.XPATH, value="//button[@aria-label='Show next month']").click()
        time.sleep(3)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    Chatbot_website = login(driver)
    Chatbot_website.navigate_to_url()
    Chatbot_website.BookingPage_Overview()




