from qa.PageObjects.AccountPage import AccountPage
from qa.PageObjects.LoginPage import LoginPage
from qa.utilities.BaseClass import BaseClass


class TestAccountPage(BaseClass):

    def test_update_username_and_email(self):
        """Updating username and email"""
        self._successful_log_in()
        self.driver.get("http://127.0.0.1:5000/account")
        log = self.getLogger()
        account_page = AccountPage(self.driver)
        old_username = account_page.get_account_name()
        assert (account_page.get_account_name() ==
                account_page.get_username().get_attribute('value'))
        log.info("Updating user data")
        account_page.update_username_and_email("TestUser",
                                               "TestUser@gmail.com")
        new_username = account_page.get_account_name()
        log.info("User data has been updated")
        assert self.get_success_alert() == "Your account has been updated!"
        assert old_username != new_username
        assert (account_page.get_account_name() ==
                account_page.get_username().get_attribute('value'))

    def test_update_picture(self):
        """Updating user picture"""
        self._successful_log_in()
        self.driver.get("http://127.0.0.1:5000/account")
        log = self.getLogger()
        account_page = AccountPage(self.driver)
        old_picture = account_page.get_profile_picture()
        log.info("Updating user picture")
        account_page.upload_picture("avatar.jpg")
        log.info("User picture has been updated")
        assert self.get_success_alert() == "Your account has been updated!"
        new_picture = account_page.get_profile_picture()
        assert old_picture != new_picture

    def _successful_log_in(self):
        login_page = LoginPage(self.driver)
        self.driver.get("http://127.0.0.1:5000/login")
        login_page.log_in_to_flaskblog("TestUser@gmail.com",
                                       "passwordTest")