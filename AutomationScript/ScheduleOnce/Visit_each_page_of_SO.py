from AutomationScript.Locators.SO_Locators.Visit_each_page_of_SO_Locator import SO_setup_page, SO_integration_page, \
    SO_Reports_page, SO_booking_from_editor_page, SO_Resource_pools_page, SO_Notification_template_editor_page, \
    SO_theme_designer_page, SO_Locatization_editor_page, SO_email_from_your_domain_page
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver
from Scenarios.MS_Link.Connect_Create_booking import ms_team


class Visit_SO_setup_page():
    #################################  launch Chrome server  #################################

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def so_visit_page(self):
        ############ Share and Publish page ################
        # page = SO_setup_page(self.driver)
        # page.click_on_share_publish_page()
        # page.click_on_Mail_merge()
        # page.click_on_Website_embed()
        # page.click_on_Website_button()
        # page.click_on_Website_widget()

        ############ Integration page ################
        # page1 = SO_integration_page(self.driver)
        # page1.click_on_integration_page()
        # page1.click_on_calendar()
        # page1.click_on_Video_conferencing()
        # page1.click_on_CRM()
        # page1.click_on_Zapier()
        # page1.click_on_Payment()
        # page1.click_on_Webhook_and_API()

        ############ Reports_page ################
        # page2 = SO_Reports_page(self.driver)
        # page2.click_on_Reports_page()
        # page2.click_on_Event_type_report()
        # page2.click_on_Booking_page_reports()
        # page2.click_on_Master_page_reports()
        # page2.click_on_Customer_reports()
        # page2.click_on_User_reports()
        # page2.click_on_Account_reports()
        # page2.click_on_Revenue_reports()

        ############ Booking_from_editor_page ################
        # page3 = SO_booking_from_editor_page(self.driver)
        # page3.click_on_booking_form_editor()

        ############ Resource_pools_page ################
        page4 = SO_Resource_pools_page(self.driver)
        page4.click_on_Resource_pools()
        page4.click_on_add_resource_pool_button()
        page4.click_on_resources_tab()
        page4.click_on_drop_down_for_adding_BP()
        page4.select_any_BP()
        page4.click_add_button()
        page4.click_save_button()

        ############ Notification_template_editor_page ################
        # page5 = SO_Notification_template_editor_page(self.driver)
        # page5.click_on_Notification_template_editor()

        ############ theme_designer_page ################
        # page6 = SO_theme_designer_page(self.driver)
        # page6.click_on_Theme_designer()

        ############ Locatization_editor_page ################
        # page7 = SO_Locatization_editor_page(self.driver)
        # page7.click_on_Localization_editor()

        ############ email_from_your_domain_page ################
        # page8 = SO_email_from_your_domain_page(self.driver)
        # page8.click_on_email_from_your_domain()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    personal_setting = OH_personal_setting(driver)
    personal_setting.navigate_to_url()
    personal_setting.login_to_OH()
    calendar = ms_team(driver)
    calendar.SO_setup()
    pge = Visit_SO_setup_page(driver)
    pge.so_visit_page()
    driver.close()