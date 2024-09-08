from selenium.webdriver.common.by import By

from qa.PageObjects.LoginPage import LoginPage
from qa.utilities.BaseClass import BaseClass


class RegisterPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    email = (By.ID, "email")
    password = (By.ID, "password")
    confirm_password = (By.ID, "confirm_password")
    remember_me = (By.ID, "remember")
    sign_up = (By.ID, "submit")
    errors = (By.CSS_SELECTOR, ".invalid-feedback")

    def register_user(self, username, email, password, c_password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(c_password)

    def submit_register_form(self):
        self.driver.find_element(*self.sign_up).click()
        loginPage = LoginPage(self.driver)
        return loginPage

    def get_error_messages(self):
        errors_list = []
        errors = self.driver.find_elements(*self.errors)
        for error in errors:
            errors_list.append(error.text)
        return errors_list

