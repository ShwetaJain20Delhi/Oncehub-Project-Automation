from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()

#################################  Open Inbox URl and Copied the Email id  #################################
driver.get("https://inbox.staticso2.com/")
time.sleep(2)
driver.find_element_by_id("div-domain").click()
time.sleep(2)

#################################  Redirect to App3 server  #################################
driver.get("https://app2.onceplatform.com/")
driver.implicitly_wait(35)

#################################  Login to OH  #################################
Ele=driver.find_element_by_name("email")
driver.find_element_by_name("email").send_keys("location-numeral-38@staticso2.com")
Ele1=driver.find_element_by_name("password")
driver.find_element_by_name("password").send_keys("testing@123")
driver.find_element_by_id("signIn").click()
time.sleep(10)

#################################  Adding new user to Admin account  #################################
driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element_by_xpath("//span[contains(text(),'My profile')]").click()
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(),'Users')]").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='addUserDiv']").click()
time.sleep(3)
driver.find_element_by_id("firstName").send_keys("User")
time.sleep(2)
driver.find_element_by_id("lastName").send_keys("1")
time.sleep(2)
Email = Keys.CONTROL, 'V'
driver.find_element_by_id("email").send_keys(Keys.CONTROL, 'V')
time.sleep(2)
driver.find_element_by_xpath("//button[@title='Create new User and send invitation email']").click()
time.sleep(10)
driver.find_element_by_xpath("//span[contains(text(),'Users')]").click()
time.sleep(5)
driver.close()

