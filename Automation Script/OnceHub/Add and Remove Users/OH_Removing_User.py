from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()

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

#################################  Removing User from OH  #################################
driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[1]/a/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/li/a/div/span[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-users/oh-users-list/table/tbody/tr[2]/td[6]/button/span/oui-icon").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div/button[3]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div/button").click()
time.sleep(10)
driver.close()