import os

from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    account = (By.CSS_SELECTOR, '.account-heading')
    username = (By.ID, 'username')
    email = (By.ID, 'email')
    submit = (By.ID, 'submit')
    upload = (By.ID, 'picture')
    picture = (By.CSS_SELECTOR, '.account-img')

    def get_account_name(self):
        return self.driver.find_element(*self.account).text

    def get_username(self):
        return self.driver.find_element(*self.username)

    def update_username_and_email(self, username, email):
        self.get_username().clear()
        self.get_username().send_keys(username)
        self.driver.find_element(*self.email).clear()
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.submit).click()

    def upload_picture(self, filename):
        upload = self.driver.find_element(*self.upload)
        upload.send_keys(os.getcwd() + f'/test_files/{filename}')
        self.driver.find_element(*self.submit).click()

    def get_profile_picture(self):
        return self.driver.find_element(*self.picture)

