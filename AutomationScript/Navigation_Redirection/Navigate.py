import time


class Navigate():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.maximize_window()
        self.driver.get("https://app3.onceplatform.com/")
        self.driver.implicitly_wait(50)
        time.sleep(4)