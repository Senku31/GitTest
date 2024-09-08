from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "email")
    password = (By.ID, "password")
    remember_me = (By.ID, "remember")
    login = (By.ID, "submit")
    forgot_password = (By.CSS_SELECTOR, "a[href='/reset_password']")
    sign_up = (By.CSS_SELECTOR, "a[href='/register']")
    user_created_msg = (By.CSS_SELECTOR, ".alert-success")
    wrong_credentials_msg = (By.CSS_SELECTOR, ".alert-danger")

    def log_in_to_flaskblog(self, email, password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.remember_me).click()
        self.driver.find_element(*self.login).click()

    def get_user_registered_message(self):
        return self.driver.find_element(*self.user_created_msg).text

    def get_login_failed_message(self):
        return self.driver.find_element(*self.wrong_credentials_msg).text





