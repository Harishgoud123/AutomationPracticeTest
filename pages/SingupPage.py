from config.config import signup_testdata
from config.locators import login_locators, signup_locators
from pages.BasePage import BasePage


class SignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def create_account(self):
        self.do_click(login_locators.Sign_in)
        self.do_send_keys(login_locators.email_create_account, self.get_random_email_for_create())
        self.do_click(login_locators.Create_account_Button)
        # just entering dummy data here
        self.wait_for_element(signup_locators.signup_firstname)
        self.do_send_keys(signup_locators.signup_firstname, self.get_random_names())
        self.do_send_keys(signup_locators.signup_lastname, self.get_random_names())
        self.select_drop_down(signup_locators.signup_dob_day, self.get_random_day())
        self.select_drop_down(signup_locators.signup_dob_month, self.get_random_month())
        self.select_drop_down(signup_locators.signup_dob_years, self.get_random_year())
        self.do_send_keys(signup_locators.signup_address, signup_testdata.address)
        self.do_send_keys(signup_locators.signup_password, signup_testdata.password)
        self.do_send_keys(signup_locators.signup_mobile, signup_testdata.mobile_number)
        self.select_drop_down(signup_locators.signup_state, self.get_random_day())
        self.do_send_keys(signup_locators.signup_assign_address, 'my address')
        self.do_send_keys(signup_locators.signup_postcode, '60601')
        self.do_send_keys(signup_locators.signup_city, 'illinois')
        self.do_click(signup_locators.signup_register)

    def is_registration_Successful(self):
        return self.is_enabled(login_locators.Sign_out)




