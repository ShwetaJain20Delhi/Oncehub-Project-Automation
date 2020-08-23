from selenium import webdriver


class get_chrome_driver():
    driver = None

    def launch_chrome(self):
        # options = webdriver.ChromeOptions()
        # options.headless = True
        # options.add_argument('--incognito')
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(15)
        return self.driver