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
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/oh-page-header/div[1]/div[3]/div/button/span/oui-icon").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div/button/span").click()
time.sleep(2)
driver.find_element_by_name("lastName").clear()
driver.find_element_by_name("lastName").send_keys("Admin")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/form/div[2]/div[1]/button").click()
time.sleep(2)

##################################  Calendar connection settings in OH #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a/div/span").click()
time.sleep(3)

  #################################  Email Notification in OH##################################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a/div/span").click()
time.sleep(5)
driver.find_element_by_id("oui-input-2").clear()
driver.find_element_by_id("oui-input-2").send_keys("Admin")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-email-notifications/div/div/form/div[3]/button[1]").click()
time.sleep(2)

 #################################  SMS notification #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[4]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='keep-me']/label/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='discardButton']/span").click()
time.sleep(2)

#################################  Date and Time notification #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[5]/a/div/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-select-7']/div/div[1]/span").click()
time.sleep(2)
driver.find_element_by_id("oui-input-6").send_keys("India")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-option-367']/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-date-and-time/div/div/form/div[2]/button[1]").click()
time.sleep(2)

#################################  Password #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[6]/a/div/span").click()
time.sleep(2)
driver.find_element_by_id("current-password").send_keys("testing@123")
time.sleep(2)
driver.find_element_by_id("new-password").send_keys("testing@1234")
time.sleep(2)
driver.find_element_by_id("re-type-password").send_keys("testing@1234")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='discardButton']/span").click()
time.sleep(2)

#################################  Authentication page #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[7]/a/div/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-authentication/div/div/form/div[1]/div[1]/div/oui-slide-toggle/label/span").click()
time.sleep(2)
driver.find_element_by_id("current-password").send_keys("testing@123")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-1']/form/div[2]/div[1]/button/span").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-authentication/div/div/form/div[2]/button[2]/span").click()
time.sleep(3)

#################################  SO module #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[8]/a/div/span").click()
time.sleep(3)
driver.find_element_by_id("pay-setup").click()
time.sleep(2)
driver.find_element_by_id("zap-setup").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='discardButton']/span").click()
time.sleep(5)

#################################  Billing Product  #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/div/sl-sidenav-category-container/div/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[1]/a[1]/div/span").click()
time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-products/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/a").click()
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='oui-dialog-0']/oh-intro-popup/div[3]/div/button").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-products/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/a").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='oui-dialog-1']/oh-intro-popup/div[3]/div/button").click()
# time.sleep(5)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-products/div[1]/div[3]/div[1]/div[3]/div[2]/div[2]/a").click()
time.sleep(5)
driver.back()
time.sleep(3)

#################################  Billing Payment  #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a").click()
time.sleep(3)

#################################  Billing Notification  #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a").click()
time.sleep(5)

#################################  Billing Transaction  #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[4]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-billing/oh-transactions/div[2]/div[1]/div/button/span/oui-icon").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/div[3]/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-1']/div[3]/div/button").click()
time.sleep(4)

#################################  Security SSO   #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/div/sl-sidenav-category-container/div/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[1]/a").click()
time.sleep(3)


#################################  Security Password    #################################
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
time.sleep(5)

#################################  Security SSO   #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='accountEnabled']/label/div[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='accountDisable']/label/div[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-security/div/oh-account-lockout-policies/div[1]/div[2]/form/div/div/div[3]/button[1]").click()
time.sleep(3)

#################################  Security SSO   #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[2]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[4]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='signOut']/label/div[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='timeOut']/label/div[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-security/div/oh-session-policies/div[1]/form/div/div/div[2]/button[1]").click()
time.sleep(3)

#################################  Privacy shield   #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/div/sl-sidenav-category-container/div/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[1]/a").click()
time.sleep(3)

#################################  Privacy GDPR information   #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element_by_name("txtydpFullName").clear()
time.sleep(2)
driver.find_element_by_name("txtydpFullName").send_keys("Test 1")
time.sleep(2)
driver.find_element_by_name("txtydpEmailId").clear()
time.sleep(2)
driver.find_element_by_name("txtydpEmailId").send_keys("testinginviteoncetesting@gmail.com")
time.sleep(2)
driver.find_element_by_name("txtydpAddres").clear()
time.sleep(2)
driver.find_element_by_name("txtydpAddres").send_keys("testinginviteoncetesting@gmail.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-privacy/div/oh-gdpr-information/div[1]/form/div/div/div[4]/button[1]").click()
time.sleep(5)

#################################  Privacy GDPR compliance   #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[3]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[3]/a").click()
time.sleep(5)

#################################  OH Compliance  #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/li[1]/a/div/span[2]").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/sl-sidenav-category[1]/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[2]/a").click()
time.sleep(3)


#################################  OH Settings  #################################
driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[3]/ul/li[2]/a/div/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-account-settings/div[2]/div/div/div[2]/p/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='deleteAccount']/label/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/sl-oh-account-delete/div[3]/div[1]/button/span").click()
time.sleep(3)
driver.close()