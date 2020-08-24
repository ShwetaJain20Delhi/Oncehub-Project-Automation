from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class get_chrome_driver():
    driver = None

    def launch_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # chrome_options.headless = True
        chrome_options.add_argument('enable-automation')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--disable-features=VizDisplayCompositor')
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver = webdriver.Chrome('C:\\Users\\ShwetaJain\\PycharmProjects\\SeleniumTest\\Driver\\chromedriver.exe', chrome_options=chrome_options)
        self.driver.set_page_load_timeout(15)
        return self.driver