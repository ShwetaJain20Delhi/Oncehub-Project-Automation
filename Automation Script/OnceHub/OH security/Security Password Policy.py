from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://app3.onceplatform.com/")
driver.implicitly_wait(35)

#################################  Login to OH  #################################
Ele=driver.find_element_by_name("email")
driver.find_element_by_name("email").send_keys("death-mad-34@staticso2.com")
Ele1=driver.find_element_by_name("password")
driver.find_element_by_name("password").send_keys("testing@123")
driver.find_element_by_id("signIn").click()
time.sleep(10)

#################################  Edit Profile settings  #################################
driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[1]/a/span").click()
time.sleep(2)


#################################  Security Password    #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/div/sl-sidenav-category-container/div/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='uppercaseCB']/label/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='specialcharacterCB']/label/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='exprRD']/label/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='hstryEnblRD']/label/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-security/div/oh-password-policies/div[1]/div[2]/form/div/div[2]/div[5]/button[2]/span").click()
time.sleep(2)
driver.close()
