import time
from AutomationScript.Locators.OH_Locators.OH_schedule_share_publiclink_locator import share_without_personalised_link, \
    share_with_perosnalised_link, schedule_Publish, new_tab, Booking_form
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class share_public_link_without_personalised():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()

    def Schedule_without_personalised_link(self):
        without = share_without_personalised_link(self.driver)
        without.click_schedule_option_from_top_menu()
    ############# Copy Booking link #####################3
        without.from_so_click_share_booking_link()
        without.select_dropdown_option()
        without.select_booking_page()
        without.copy_public_link()
        without.click_copy_close_button()
    ############# Open new tab and paste the booking url #####################
        opentab = new_tab(self.driver)
        opentab.open_new_window_and_paste_copied_url()
        opentab.select_15minute_event_type()
        opentab.change_time_zone()
        opentab.click_on_dropdown()
        opentab.search_India("India")
        opentab.select_searched_country()
        opentab.click_continue()
        opentab.select_time_slot()
        opentab.clickcontinue()
    ########### Fill booking form ##################
        form = Booking_form(self.driver)
        form.enter_name("Test")
        form.enter_email("testinginviteoncetesting@gmail.com")
        form.click_done()
    #     form.copy_bookingID()
    #     time.sleep(7)
    # ############# search meeting entry in Activity page ####################
    #     form.paste_booking_id_in_activity_page()

    def Publish_your_website(self):
        without = share_without_personalised_link(self.driver)
        without.click_schedule_option_from_top_menu()
        publish = schedule_Publish(self.driver)
        publish.select_share_and_publish_option()
        self.driver.back()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    public_link = share_public_link_without_personalised(driver)
    public_link.server_login()
    public_link.Schedule_without_personalised_link()
    public_link.Publish_your_website()
    driver.close()