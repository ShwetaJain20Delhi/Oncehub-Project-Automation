import time

from AutomationScript.Locators.OH_Locators.SignupAndSO_Onboarding_Locators import select_CO_product
from AutomationScript.Signup_and_SO_product_selection.Signup_and_SO_onboarding import Signup_SO_Onboarding
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class signup_CO_product_selection():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def select_co_product(self):
        co_product = select_CO_product(self.driver)
        co_product.select_co_product()
        time.sleep(10)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    Onboard_SO = Signup_SO_Onboarding(driver)
    Onboard_SO.Inbox_email()
    Onboard_SO.Signup_with_new_user()
    product = signup_CO_product_selection(driver)
    product.select_co_product()
    driver.close()