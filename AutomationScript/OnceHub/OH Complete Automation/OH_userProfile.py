from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import datetime
from AutomationScript.OnceHub.OH_Profile.Date_and_Time_in_OH import datetime

class complete_automation():

    def oh_automate(self):
        personal_setting = OH_personal_setting()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()
        date1 = datetime(personal_setting.driver)
        date1.


# driver = webdriver.Chrome()
# driver.set_page_load_timeout(15)
# driver.maximize_window()
# driver.get("https://app3.onceplatform.com/")
# driver.implicitly_wait(35)
#
# #################################  Login to OH  #################################
#
# Ele=driver.find_element_by_name("email")
# driver.find_element_by_name("email").send_keys("death-mad-34@staticso2.com")
# Ele1=driver.find_element_by_name("password")
# driver.find_element_by_name("password").send_keys("testing@123")
# driver.find_element_by_id("signIn").click()
# time.sleep(10)
#
# #################################  Edit Profile settings  #################################
# driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[1]/a/span").click()
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/oh-page-header/div[1]/div[3]/div/button/span/oui-icon").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div/button/span").click()
# time.sleep(2)
# driver.find_element_by_name("lastName").clear()
# driver.find_element_by_name("lastName").send_keys("Admin")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/form/div[2]/div[1]/button").click()
# time.sleep(2)
#
# ##################################  Calendar connection settings in OH #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a/div/span").click()
# time.sleep(3)
#
# #################################  Exchange Calendar Connection  #################################
# driver.find_element_by_id("ExchangeCalendarConnectBtn").click()
# time.sleep(2)
# driver.find_element_by_id("email").send_keys("gilad@staticso.com")
# time.sleep(2)
# driver.find_element_by_id("password").send_keys("schEdu1e")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-1']/div[2]/div/form/div[3]/button/span").click()
# time.sleep(2)
# driver.find_element_by_id("ewsUrl").send_keys("https://mex09.emailsrvr.com/owa")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-1']/div[3]/div[2]/button").click()
# time.sleep(10)
#
# #################################  Changing reminder settings  #################################
# driver.find_element_by_id("oui-select-2").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-option-5']/span").click()
# time.sleep(3)
#
# #################################  2-way sync Toggle value  #################################
# Flag = driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-calendar-connection/div/div/oh-calendar-connected-state/div/div[2]/div/section[3]/div[2]/ul/li[1]/div[1]/oui-slide-toggle/label/span")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-calendar-connection/div/div/oh-calendar-connected-state/div/div[2]/div/section[3]/div[2]/ul/li[1]/div[1]/oui-slide-toggle/label/span").click()
# time.sleep(4)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-calendar-connection/div/div/oh-calendar-connected-state/div/div[2]/div/section[3]/div[2]/ul/li[2]/div[1]/oui-slide-toggle/label/span").click()
# time.sleep(3)
#
# #################################  Redirect to SO From "Continue setup" button #################################
# Flag = driver.find_element_by_id("ContinueSetupBtn")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_id("ContinueSetupBtn").click()
# time.sleep(10)
# driver.back()
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/div/sl-sidenav-category-container/div/span[2]").click()
# time.sleep(10)
#
#   #################################  Email Notification in OH##################################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a/div/span").click()
# time.sleep(5)
# driver.find_element_by_id("oui-input-2").clear()
# driver.find_element_by_id("oui-input-2").send_keys("Admin")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-email-notifications/div/div/form/div[3]/button[1]").click()
# time.sleep(2)
#
#  #################################  SMS notification #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[4]/a").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='keep-me']/label/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='discardButton']/span").click()
# time.sleep(2)
#
# #################################  Date and Time notification #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[5]/a/div/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-select-7']/div/div[1]/span").click()
# time.sleep(2)
# driver.find_element_by_id("oui-input-6").send_keys("India")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-option-367']/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-date-and-time/div/div/form/div[2]/button[1]").click()
# time.sleep(2)
#
# #################################  Password #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[6]/a/div/span").click()
# time.sleep(2)
# driver.find_element_by_id("current-password").send_keys("testing@123")
# time.sleep(2)
# driver.find_element_by_id("new-password").send_keys("testing@1234")
# time.sleep(2)
# driver.find_element_by_id("re-type-password").send_keys("testing@1234")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='discardButton']/span").click()
# time.sleep(2)
#
# #################################  Authentication page #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[7]/a/div/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-authentication/div/div/form/div[1]/div[1]/div/oui-slide-toggle/label/span").click()
# time.sleep(2)
# driver.find_element_by_id("current-password").send_keys("testing@123")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-1']/form/div[2]/div[1]/button/span").click()
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-authentication/div/div/form/div[2]/button[2]/span").click()
# time.sleep(3)
#
# #################################  SO module #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[8]/a/div/span").click()
# time.sleep(3)
# driver.find_element_by_id("pay-setup").click()
# time.sleep(2)
# driver.find_element_by_id("zap-setup").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='discardButton']/span").click()
# time.sleep(5)
#
# #################################  Billing Product  #################################
# Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/div/sl-sidenav-category-container/div/span[2]")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/div/sl-sidenav-category-container/div/span[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[1]/a[1]/div/span").click()
# time.sleep(2)
# # driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-products/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/a").click()
# # time.sleep(5)
# # driver.find_element_by_xpath("//*[@id='oui-dialog-0']/oh-intro-popup/div[3]/div/button").click()
# # time.sleep(3)
# # driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-products/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/a").click()
# # time.sleep(3)
# # driver.find_element_by_xpath("//*[@id='oui-dialog-1']/oh-intro-popup/div[3]/div/button").click()
# # time.sleep(5)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-products/div[1]/div[3]/div[1]/div[3]/div[2]/div[2]/a").click()
# time.sleep(5)
# driver.back()
# time.sleep(3)
#
# #################################  Billing Payment  #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a").click()
# time.sleep(3)
#
# #################################  Billing Notification  #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a").click()
# time.sleep(5)
#
# #################################  Billing Transaction  #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[4]/a").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-transactions/div[2]/div[1]/div/button/span/oui-icon").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div/button").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-1']/div[3]/div/button").click()
# time.sleep(4)
#
# #################################  Security SSO   #################################
# Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/div/sl-sidenav-category-container/div/span[2]")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/div/sl-sidenav-category-container/div/span[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[1]/a").click()
# time.sleep(3)
#
#
# #################################  Security Password    #################################
# Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='uppercaseCB']/label/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='specialcharacterCB']/label/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='exprRD']/label/div[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='hstryEnblRD']/label/div[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-security/div/oh-password-policies/div[1]/div[2]/form/div/div[2]/div[5]/button[2]/span").click()
# time.sleep(5)
#
#
# #################################  Security SSO   #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[4]/a").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='signOut']/label/div[2]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='timeOut']/label/div[2]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-security/div/oh-session-policies/div[1]/form/div/div/div[2]/button[1]").click()
# time.sleep(3)
#
# #################################  Privacy shield   #################################
# Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/div/sl-sidenav-category-container/div/span[2]")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/div/sl-sidenav-category-container/div/span[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[1]/a").click()
# time.sleep(3)
#
# #################################  Privacy GDPR information   #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a").click()
# time.sleep(3)
# driver.find_element_by_name("txtydpFullName").clear()
# time.sleep(2)
# driver.find_element_by_name("txtydpFullName").send_keys("Test 1")
# time.sleep(2)
# driver.find_element_by_name("txtydpEmailId").clear()
# time.sleep(2)
# driver.find_element_by_name("txtydpEmailId").send_keys("testinginviteoncetesting@gmail.com")
# time.sleep(2)
# driver.find_element_by_name("txtydpAddres").clear()
# time.sleep(2)
# driver.find_element_by_name("txtydpAddres").send_keys("testinginviteoncetesting@gmail.com")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-privacy/div/oh-gdpr-information/div[1]/form/div/div/div[4]/button[1]").click()
# time.sleep(5)
#
# #################################  Privacy GDPR compliance   #################################
# Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a").click()
# time.sleep(5)
#
# #################################  OH Compliance  #################################
# Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/li[1]/a/div/span[2]")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/li[1]/a/div/span[2]").click()
# time.sleep(4)
#
#
# #################################  OH Settings  #################################
# Flag = driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/li[2]/a/div/span[2]")
# driver.execute_script("arguments[0].scrollIntoView();", Flag)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/li[2]/a/div/span[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-account-settings/div[2]/div/div/div[2]/p/button").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='deleteAccount']/label/span").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='oui-dialog-1']/sl-oh-account-delete/div[3]/div[1]/button/span").click()
# time.sleep(3)
#
# #################################  Adding new user to Admin account  #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/li/a/div/span[2]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-users/div/div[2]/button").click()
# time.sleep(3)
# driver.find_element_by_id("firstName").send_keys("User")
# time.sleep(2)
# driver.find_element_by_id("lastName").send_keys("1")
# time.sleep(2)
# Email = Keys.CONTROL, 'V'
# driver.find_element_by_id("email").send_keys("shweta@staticso2.com")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
# time.sleep(10)
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/li/a/div/span[2]").click()
# time.sleep(5)
#
# #################################  Removing User from OH  #################################
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-users/oh-users-list/table/tbody/tr[2]/td[6]/button/span/oui-icon").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div/button[3]").click()
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
# time.sleep(8)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div/button").click()
# time.sleep(10)
# driver.close()