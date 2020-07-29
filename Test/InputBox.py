from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
#driver.set_page_load_timeout(5)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").is_enabled()
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[2]/td/label").is_enabled()
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[2]/td/label").click()
driver.find_element_by_id("RESULT_RadioButton-9").is_enabled()
Element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(Element)
drp.select_by_value("Radio-1")
time.sleep(5)
driver.quit()
