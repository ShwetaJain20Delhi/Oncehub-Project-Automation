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

########################### Click on calendar connection page from profile menu  #################################
driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[2]/a/span").click()
time.sleep(5)

#################################  Exchange Calendar Connection  #################################
driver.find_element_by_id("ExchangeCalendarConnectBtn").click()
time.sleep(2)
driver.find_element_by_id("email").send_keys("gilad@staticso.com")
time.sleep(2)
driver.find_element_by_id("password").send_keys("schEdu1e")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[2]/div/form/div[3]/button/span").click()
time.sleep(2)
driver.find_element_by_id("ewsUrl").send_keys("https://mex09.emailsrvr.com/owa")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
time.sleep(15)

#################################  Changing reminder settings  #################################
driver.find_element_by_xpath("//*[@id='oui-select-1']/div/div[1]/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-option-3']/span").click()
time.sleep(3)

#################################  2-way sync Toggle value  #################################
Flag = driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-calendar-connection/div/div/oh-calendar-connected-state/div/div[2]/div/section[3]/div[2]/ul/li[1]/div[1]/oui-slide-toggle/label/span")
driver.execute_script("arguments[0].scrollIntoView();", Flag)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-calendar-connection/div/div/oh-calendar-connected-state/div/div[2]/div/section[3]/div[2]/ul/li[1]/div[1]/oui-slide-toggle/label/span").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-calendar-connection/div/div/oh-calendar-connected-state/div/div[2]/div/section[3]/div[2]/ul/li[2]/div[1]/oui-slide-toggle/label/span").click()
time.sleep(3)
Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/div/sl-sidenav-category-container/div/span[2]")
driver.execute_script("arguments[0].scrollIntoView();", Flag)
driver.find_element_by_id("ContinueSetupBtn").click()
time.sleep(10)
driver.close()