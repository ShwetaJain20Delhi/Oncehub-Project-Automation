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

#################################  O365 via OAUth Calendar Connection  #################################
main_page = driver.current_window_handle  # save the current window
driver.find_element_by_xpath("//*[@id='calendarListConatiner']/button").click()
time.sleep(5)
login_page = None
for handle in driver.window_handles:
    if handle != main_page:
       login_page = handle
driver.switch_to.window(login_page)    #switch to calendar connection window
time.sleep(10)
driver.find_element_by_name("loginfmt").send_keys("shweta.jain@oncehq.com")    #Calendar Email
time.sleep(3)
driver.find_element_by_id("idSIButton9").click()          #Click next after entered email
time.sleep(3)
driver.find_element_by_name("passwd").send_keys("Schedule@123")                  # Password for email connection
time.sleep(3)
driver.find_element_by_id("idSIButton9").click()    #Click on connect button on calendar connection popup
time.sleep(3)
driver.find_element_by_id("idBtn_Back").click()
time.sleep(15)
#driver.find_element_by_xpath("click()//*[@id='continue']/span").click()      #Permission allowed for calendar
#time.sleep(2)
driver.switch_to.window(main_page)
time.sleep(5)