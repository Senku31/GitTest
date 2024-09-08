from qa.PageObjects.AboutPage import AboutPage
from qa.utilities.BaseClass import BaseClass


class TestAboutPage(BaseClass):

    def test_selenium_about(self):
        self.driver.get("http://127.0.0.1:5000/about")
        log = self.getLogger()
        about_page = AboutPage(self.driver)
        self.driver.get(self.driver.current_url)
        log.info("Checking if About Page header is displayed")
        assert about_page.get_header().text == 'About Page'
