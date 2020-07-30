from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://app3.onceplatform.com/")
driver.implicitly_wait(35)


Ele=driver.find_element_by_name("email")
# Ele.is_displayed()
# Ele.is_enabled()
driver.find_element_by_name("email").send_keys("testinginviteoncetesting+36@gmail.com")
Ele1=driver.find_element_by_name("password")
# Ele1.is_displayed()
# Ele1.is_enabled()
driver.find_element_by_name("password").send_keys("testing@123")
driver.find_element_by_id("signIn").click()
time.sleep(10)

driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[1]/ul/li[2]/sl-product-dropdown/div/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[1]/ul/li[2]/sl-product-dropdown/div/div/div/div[1]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='setupPage']/div/div[3]/div[1]/div/div[1]/div[1]/div/div[1]/a").click()
time.sleep(5)
driver.find_element_by_name("name").send_keys("30-Minutes")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='addCustomSOField']/div[2]/input[1]").click()

time.sleep(10)
driver.close()