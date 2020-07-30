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
driver.get("https://app3.onceplatform.com/")
driver.implicitly_wait(35)

#################################  Login to OH  #################################
Ele=driver.find_element_by_name("email")
driver.find_element_by_name("email").send_keys("death-mad-34@staticso2.com")
Ele1=driver.find_element_by_name("password")
driver.find_element_by_name("password").send_keys("testing@123")
driver.find_element_by_id("signIn").click()
time.sleep(10)

#################################  Adding new user to Admin account  #################################
driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[1]/a/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/li/a/div/span[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-users/div/div[2]/button").click()
time.sleep(3)
driver.find_element_by_id("firstName").send_keys("User")
time.sleep(2)
driver.find_element_by_id("lastName").send_keys("1")
time.sleep(2)
Email = Keys.CONTROL, 'V'
driver.find_element_by_id("email").send_keys(Keys.CONTROL, 'V')
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/li/a/div/span[2]").click()
time.sleep(5)
driver.close()

