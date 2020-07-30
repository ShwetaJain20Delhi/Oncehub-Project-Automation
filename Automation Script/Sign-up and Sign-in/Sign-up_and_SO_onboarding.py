from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()

# Open Inbox URl and Copied the Email id

driver.get("https://inbox.staticso2.com/")
time.sleep(2)
driver.find_element_by_id("div-domain").click()
time.sleep(2)

                # Open App3 server and sign-up with new user
driver.get("https://account3.onceplatform.com/signup")
driver.find_element_by_name("name").send_keys("Test")
time.sleep(1)
Ele=driver.find_element_by_name("email")
Ele.is_displayed()
Ele.is_enabled()
driver.find_element_by_name("email").send_keys(Keys.CONTROL, 'v')
time.sleep(1)
Ele1=driver.find_element_by_name("password")
Ele1.is_displayed()
Ele1.is_enabled()
driver.find_element_by_name("password").send_keys("testing@123")
time.sleep(1)
driver.find_element_by_name("retypePassword").send_keys("testing@123")
time.sleep(2)
driver.find_element_by_id("signUp").click()
time.sleep(5)

                       # Select SO from Products page
driver.find_element_by_id("so-get-started").click()   #SO Product Select
time.sleep(5)

                        # TimeZone detection

driver.find_element_by_xpath("//*[@id='sunday']/label/span/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='saturday']/label/span/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='changetz']/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='selectedCountry']/div/div[1]/span").click()
time.sleep(2)
driver.find_element_by_id("oui-input-0").send_keys("India")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-option-159']/span").click()
time.sleep(2)
driver.find_element_by_id("saveTimeZone").click()
time.sleep(2)
driver.find_element_by_id("continue").click()
time.sleep(3)

                         # Calendar Connection

driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-onboarding/div/oh-onboarding-calendar-connection/oh-calendar-connection/div/div/div/button/span").click()
time.sleep(3)
driver.find_element_by_id("ExchangeCalendarConnectBtn").click()
time.sleep(2)
driver.find_element_by_id("email").send_keys("gilad@staticso.com")
time.sleep(2)
driver.find_element_by_id("password").send_keys("schEdu1e")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-1']/div[2]/div/form/div[3]/button/span").click()
time.sleep(2)
driver.find_element_by_id("ewsUrl").send_keys("https://mex09.emailsrvr.com/owa")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-1']/div[3]/div[2]/button").click()
time.sleep(15)
driver.find_element_by_id("continue").click()
time.sleep(3)

# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-onboarding/div/oh-onboarding-calendar-connection/oh-calendar-connection/div/div/div/button/span").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='ExchangeCalendarConnectBtn']").click()     #Calendar Connection
# main_page= driver.current_window_handle      #save the current window
# time.sleep(5)
# login_page = None
# for handle in driver.window_handles:
#     if handle != main_page:
#        login_page = handle
# driver.switch_to.window(login_page)    #switch to calendar connection window
# time.sleep(10)
# driver.find_element_by_id("email").send_keys("gilad@staticso.com")    #Calendar Email
# #driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()          #Click next after entered email
# #time.sleep(2)
# driver.find_element_by_name("password").send_keys("schEdu1e")                  # Password for email connection
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()    #Click on connect button on calendar connection popup
# time.sleep(2)
# #driver.find_element_by_xpath("click()//*[@id='continue']/span").click()      #Permission allowed for calendar
# #time.sleep(2)
# driver.switch_to.window(main_page)
# time.sleep(10)

                             # Video conferencing Click continue
driver.find_element_by_xpath("//*[@id='setUpLater']").click()
time.sleep(2)
                              # Skip for meeting
driver.find_element_by_xpath("//*[@id='skip']/span").click()
time.sleep(10)
                               # skip for tour
driver.find_element_by_xpath("//*[@id='OrientationTour2']/div[4]/a[1]").click()
time.sleep(8)
driver.close()

