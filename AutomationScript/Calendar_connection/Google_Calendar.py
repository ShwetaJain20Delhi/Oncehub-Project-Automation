from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://app2.onceplatform.com/")
driver.implicitly_wait(35)

#################################  Login to OH  #################################
Ele=driver.find_element_by_name("email")
driver.find_element_by_name("email").send_keys("location-numeral-38@staticso2.com")
Ele1=driver.find_element_by_name("password")
driver.find_element_by_name("password").send_keys("testing@123")
driver.find_element_by_id("signIn").click()
time.sleep(10)

########################### Click on calendar connection page from profile menu  #################################
driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[2]/a/span").click()
time.sleep(5)

#################################  Google Calendar Connection  #################################
main_page = driver.current_window_handle  # save the current window
driver.find_element_by_id("GoogleCalendarConnectBtn").click()
time.sleep(5)
login_page = None
for handle in driver.window_handles:
    if handle != main_page:
       login_page = handle
driver.switch_to.window(login_page)    #switch to calendar connection window
time.sleep(10)
driver.find_element_by_name("identifier").send_keys("testinginviteoncetesting@gmail.com")    #Calendar Email
time.sleep(3)
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()          #Click next after entered email
time.sleep(3)
driver.find_element_by_name("passwd").send_keys("testing@123")                  # Password for email connection
time.sleep(3)
driver.find_element_by_id("idSIButton9").click()    #Click on connect button on calendar connection popup
time.sleep(3)
driver.find_element_by_id("idBtn_Back").click()
time.sleep(15)
driver.switch_to.window(main_page)
time.sleep(5)

#################################  Changing reminder settings  #################################
driver.find_element_by_xpath("//*[@id='oui-select-1']/div/div[1]/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-option-3']/span").click()
time.sleep(3)

#################################  Click on setup page  #################################
Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/div/sl-sidenav-category-container/div/span[2]")
driver.execute_script("arguments[0].scrollIntoView();", Flag)
driver.find_element_by_id("ContinueSetupBtn").click()
time.sleep(10)
driver.back()
driver.sleep(10)
driver.close()