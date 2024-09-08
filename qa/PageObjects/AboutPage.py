from selenium.webdriver.common.by import By


class AboutPage:

    def __init__(self, driver):
        self.driver = driver

    header = (By.CSS_SELECTOR, "h1")

    def get_header(self):
        return self.driver.find_element(*self.header)