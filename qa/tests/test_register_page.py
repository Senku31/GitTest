from qa.PageObjects.LoginPage import LoginPage
from qa.PageObjects.RegisterPage import RegisterPage
from qa.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_register_user(self):
        log = self.getLogger()
        register_page = RegisterPage(self.driver)
        self.driver.get("http://localhost:5000/register")
        log.info("Filling in the register form with new user data")
        register_page.register_user("NewUser2",
                                    "NewUser2@gmail.com",
                                    "passwordTest",
                                    "passwordTest")
        login_page = register_page.submit_register_form()
        log.info("Checking if the success message has been displayed")
        assert (login_page.get_user_registered_message() ==
                "Your account has been  created! You are now able to log in.")
        log.info("The user has been registered")

    def test_username_is_taken_error_message(self):
        log = self.getLogger()
        register_page = RegisterPage(self.driver)
        self.driver.get("http://localhost:5000/register")
        log.info("Filling in the register form with existing user data")
        register_page.register_user("TestUser",
                                    "TestUser@gmail.com",
                                    "passwordTest",
                                    "passwordTest")
        register_page.submit_register_form()
        errors = register_page.get_error_messages()
        for error in errors:
            assert "That username is taken" in error

    def test_passwords_dont_match_error_message(self):
        log = self.getLogger()
        register_page = RegisterPage(self.driver)
        self.driver.get("http://localhost:5000/register")
        log.info("Filling in the register form with different confirm password")
        register_page.register_user("New",
                                    "New@gmail.com",
                                    "passwordTest",
                                    "passwordTest2")
        register_page.submit_register_form()
        errors = register_page.get_error_messages()
        for error in errors:
            assert "Field must be equal to password." in error

    def test_invalid_email_error_message(self):
        log = self.getLogger()
        register_page = RegisterPage(self.driver)
        self.driver.get("http://localhost:5000/register")
        log.info("Filling in the register form with invalid email format")
        register_page.register_user("New",
                                    "New",
                                    "passwordTest",
                                    "passwordTest")
        register_page.submit_register_form()
        errors = register_page.get_error_messages()
        for error in errors:
            assert "Invalid email address." in error


