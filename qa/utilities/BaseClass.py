import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("run_server", "setup")
class BaseClass:

    homeBtn = (By.CSS_SELECTOR, "a[href='/home']")
    aboutBtn = (By.CSS_SELECTOR, "a[href='/about']")
    registerBtn = (By.CSS_SELECTOR, "a[href='/register']")
    loginBtn = (By.CSS_SELECTOR, "a[href='/login']")
    new_postBtn = (By.CSS_SELECTOR, "a[href='/post/new']")
    accountBtn = (By.CSS_SELECTOR, "a[href='/account']")
    logoutBtn = (By.CSS_SELECTOR, "a[href='/logout']")
    success_alert = (By.CSS_SELECTOR, ".alert-success")


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("./../utilities/logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def get_not_logged_in_buttons(self):
        buttons_list = []
        buttons_list.append(self.driver.find_element(*self.homeBtn))
        buttons_list.append(self.driver.find_element(*self.aboutBtn))
        buttons_list.append(self.driver.find_element(*self.loginBtn))
        buttons_list.append(self.driver.find_element(*self.registerBtn))
        return buttons_list

    def get_logged_in_buttons(self):
        buttons_list = []
        buttons_list.append(self.driver.find_element(*self.homeBtn))
        buttons_list.append(self.driver.find_element(*self.aboutBtn))
        buttons_list.append(self.driver.find_element(*self.new_postBtn))
        buttons_list.append(self.driver.find_element(*self.accountBtn))
        buttons_list.append(self.driver.find_element(*self.logoutBtn))
        return buttons_list

    def get_success_alert(self):
        return self.driver.find_element(*self.success_alert).text

    def click_log_out(self):
        self.driver.find_element(*self.logoutBtn).click()






