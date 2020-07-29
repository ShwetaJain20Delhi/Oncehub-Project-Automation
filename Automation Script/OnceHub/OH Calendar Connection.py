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
time.sleep(5)

##################################  Calendar connection settings in OH #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a/div/span").click()
time.sleep(3)
# driver.find_element_by_id("ExchangeCalendarConnectBtn").click()
# time.sleep(3)
# main_page = driver.current_window_handle      #save the current window
# time.sleep(5)
# login_page = None
# for handle in driver.window_handles:
#     if handle != main_page:
#        login_page = handle
# driver.switch_to.window(login_page)    #switch to calendar connection window
# time.sleep(10)
# driver.find_element_by_id("email").send_keys("shweta.jain@oncehq.com")    #Calendar Email
# driver.find_element_by_id("password").send_keys("Schedule@123")                  # Password for email connection
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-4']/div[3]/div[2]/button/span").click()    #Click on connect button on calendar connection popup
# time.sleep(2)
# driver.switch_to.window(main_page)
# time.sleep(10)

time.sleep(5)
driver.close()