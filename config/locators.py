from selenium.webdriver.common.by import By


class login_locators:
    EMAIL =(By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    Login_Button = (By.ID, "SubmitLogin")
    Sign_in = (By.XPATH, "//a[@class='login']")
    Create_account_Button = (By.ID, "SubmitCreate")
    Login_Invalid_cred = (By.XPATH, "//div[@class='alert alert-danger']")
    Sign_out = (By.XPATH, "//a[@class='logout']")
    email_create_account = (By.ID, "email_create")

class signup_locators:
    ########## Sign up locators############
    signup_firstname = (By.ID, "customer_firstname")
    signup_lastname = (By.ID, "customer_lastname")
    signup_password = (By.ID, "passwd")
    signup_dob_day = (By.ID, "days")
    signup_dob_month = (By.ID, "months")
    signup_dob_years = (By.ID, "years")
    signup_address = (By.ID, "address1")
    signup_city = (By.ID, "city")
    signup_state = (By.ID, "id_state")
    signup_state = (By.ID, "id_state")
    signup_mobile = (By.ID, "phone_mobile")
    signup_postcode = (By.ID, "postcode")
    signup_city = (By.ID, "city")
    signup_state = (By.ID, "id_state")
    signup_assign_address = (By.ID, "alias")
    signup_register = (By.ID, "submitAccount")