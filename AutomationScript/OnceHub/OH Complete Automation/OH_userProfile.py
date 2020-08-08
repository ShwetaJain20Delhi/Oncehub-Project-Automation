from AutomationScript.OnceHub.Add_Remove_users.OH_Adding_User import Add_Users
from AutomationScript.OnceHub.Add_Remove_users.OH_Removing_User import Remove_Users
from AutomationScript.OnceHub.Add_Remove_users.OH_Resend_Invitation_link import Resend_invitation
from AutomationScript.OnceHub.OH_Billing.Billing_Notification import BillingNotify
from AutomationScript.OnceHub.OH_Billing.Billing_Product import BillingPage
from AutomationScript.OnceHub.OH_Billing.Billing_Transaction import BillingTrans
from AutomationScript.OnceHub.OH_Billing.Billing_Payment_method import BillingPay
from AutomationScript.OnceHub.OH_Privacy.Privacy_GDPR_compliance import Privacy_compliance
from AutomationScript.OnceHub.OH_Privacy.Privacy_GDPR_information import Privacy_info
from AutomationScript.OnceHub.OH_Privacy.Privacy_shield import PrivacyPage
from AutomationScript.OnceHub.OH_Profile.Authentication import AuthenticationPage
from AutomationScript.OnceHub.OH_Profile.OH_Calendar_Connection import calendar_connection_setting
from AutomationScript.OnceHub.OH_Profile.OH_Compliance import compliancepage
from AutomationScript.OnceHub.OH_Profile.OH_Settings import oh_settings
from AutomationScript.OnceHub.OH_Profile.OH_email_notification import emailnotification
from AutomationScript.OnceHub.OH_Profile.OH_left_menu_SO_module import OH_scheduleonce
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.OnceHub.OH_Profile.Date_and_Time_in_OH import datetime, DateAndtime
from AutomationScript.OnceHub.OH_Profile.Password_Change import passwordpage
from AutomationScript.OnceHub.OH_Profile.SMS_notification import smsnotification
from AutomationScript.OnceHub.OH_Schedule.OH_Schedule_Share_Public_link import share_public_link
from AutomationScript.OnceHub.OH_security.Security_Account_Lockout_Policies import security_Account_lockout_policies
from AutomationScript.OnceHub.OH_security.Security_Password_Policy import security_password_policies
from AutomationScript.OnceHub.OH_security.Security_SSO import security_sso_policies
from AutomationScript.OnceHub.OH_security.Security_Session_policies import security_session_policies
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class complete_automation():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def oh_automate(self):
        personal_setting = OH_personal_setting(driver)
    ########### Login to server #################
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    ########## edit personal setting ###########
        personal_setting.edit_personal_details()

    ########## Calendar Connection #############
        calendar = calendar_connection_setting(driver)
        calendar.Calendarconnection_from_profilemenu()
        calendar.Oh_Exchange_calendar_connect()
        calendar.Oh_reminder_setting()
        calendar.so_sync_setting()
        calendar.so_setup()

    ############### Email Notification #############
        email = emailnotification(driver)
        email.Emailnotification()

    ############### SMS Notification #############
        notification = smsnotification(driver)
        notification.sms_notification_module()

    ########## Date and time Module ############
        dateandtime = DateAndtime(driver)
        dateandtime.datetime()

    ########## Password ############
        password = passwordpage(driver)
        password.password_module()

    ########## Authentication ############
        authenticate = AuthenticationPage(driver)
        authenticate.authentication_module()

    ########## Scheduleonce ############
        so_module = OH_scheduleonce(driver)
        so_module.OH_SO_module()

    ########## Billing_Product ############
        billprod = BillingPage(driver)
        billprod.Billing()
        billprod.Billing_product()

    ########## Billing_payment_method ############
        billpay = BillingPay(driver)
        billpay.Billing_payment_method()

    ########## Billing_notification ############
        billnot = BillingNotify(driver)
        billnot.Billing_notification()

    ########## Billing_Transaction_page ############
        billProd = BillingTrans(driver)
        billProd.Billing_Transaction_page()

    # ########## security_sso_policies ############
    #     sso_policies = security_sso_policies(driver)
    #     sso_policies.security()
    #     sso_policies.security_SSO()

    ########## security_password_policies ############
        pass_policies = security_password_policies(driver)
        pass_policies.security()
        pass_policies.security_password()

    ########## security_Account_lockout_policies ############
        lockout_policies = security_Account_lockout_policies(driver)
        lockout_policies.security_account_lockout()

    ########## security_session_policies ############
        session_policies = security_session_policies(driver)
        session_policies.security_session()

    ########## Privacy_Shield ############
        privacy = PrivacyPage(driver)
        privacy.Privacy()
        privacy.Privacy_Shield()

    ########## Privacy_GDPR_information ############
        info = Privacy_info(driver)
        info.GDPR_Information()

    ########## Privacy_compliance ############
        privacy_comp = Privacy_compliance(driver)
        privacy_comp.Privacy_Compliance()

    ########## Compliance ############
        compli = compliancepage(driver)
        compli.compliance_module()

    ########## OHsettings ############
        password = oh_settings(driver)
        password.Oh_settings_module()

    ########## Add_Users ############
        adding_user = Add_Users(driver)
        adding_user.Users()
        adding_user.add_user()

    ########## Resend_invitation ############
        resend_invite = Resend_invitation(driver)
        resend_invite.Users()
        resend_invite.Resend_invitation_link()

    ########## Remove_Users ############
        removing_user = Remove_Users(driver)
        removing_user.Users()
        removing_user.Remove_user()

    ########## Share public link without personalised link ############
        public_link = share_public_link(driver)
        public_link.Schedule_without_personalised_link()

    ########## Share public link personalised link ############
        public_link.Schedule_with_personalised_link()

    ########## Publish webiste link ############
        public_link.Publish_your_website()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    automate = complete_automation(driver)
    automate.oh_automate()
    driver.close()