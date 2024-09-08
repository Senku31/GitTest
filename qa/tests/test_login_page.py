import time

from qa.PageObjects.LoginPage import LoginPage
from qa.utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):
    def test_successful_log_in(self):
        """Verifying a successful login process"""
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        self.driver.get("http://localhost:5000/login")
        log.info("Filling in the log in form")
        login_page.log_in_to_flaskblog("TestUser@gmail.com",
                                       "passwordTest")
        buttons = self.get_logged_in_buttons()
        for button in buttons:
            assert button.is_displayed()
        log.info("The user has been logged in")

    def test_unsuccessful_log_in(self):
        """Verifying an unsuccessful login process"""
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        self.driver.get("http://localhost:5000/login")
        log.info("Filling in the log in form")
        login_page.log_in_to_flaskblog("TestUser@gmail.com",
                                       "passwordTest2")
        assert "Login unsuccessful" in login_page.get_login_failed_message()
        log.info("The user has not been logged in")

    def test_log_out(self):
        """Verifying a successful login process"""
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        self.driver.get("http://localhost:5000/login")
        log.info("Filling in the log in form")
        login_page.log_in_to_flaskblog("TestUser@gmail.com",
                                       "passwordTest")
        buttons = self.get_logged_in_buttons()
        for button in buttons:
            assert button.is_displayed()
        log.info("The user has been logged in")
        self.click_log_out()
        buttons = self.get_not_logged_in_buttons()
        for button in buttons:
            assert button.is_displayed()


