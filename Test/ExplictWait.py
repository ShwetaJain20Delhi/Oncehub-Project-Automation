from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
#driver.set_page_load_timeout(5)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.implicitly_wait(10)
driver.find_element_by_id("hotel-destination-hp-hotel").send_keys("Taj Mahal")
time.sleep(2)
driver.find_element_by_id("hotel-checkin-hp-hotel").clear()
driver.find_element_by_id("hotel-checkin-hp-hotel").send_keys("07/26/2020")
driver.find_element_by_id("hotel-checkout-hp-hotel").clear()
driver.find_element_by_id("hotel-checkout-hp-hotel").send_keys("07/28/2020")
driver.find_element_by_xpath("//*[@id='gcw-hotel-form-hp-hotel']/div[13]/label/button").click()
wait = WebDriverWait(driver, 10)
Element = wait.until(EC.element_to_be_clickable(By.ID, "popularFilter-0-FREE_BREAKFAST"))
Element.click()
time.sleep(3)
driver.quit()