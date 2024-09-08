import time

from qa.PageObjects.HomePage import HomePage
from qa.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_home_page_articles(self):
        """Checking number of articles on the homepage"""
        self.driver.get("http://localhost:5000/home")
        log = self.getLogger()
        home_page = HomePage(self.driver)
        log.info("Checking number of articles per page")
        assert home_page.get_articles_per_page() == 5

    def test_not_logged_user_buttons(self):
        """Checking buttons for a non-logged user"""
        self.driver.get("http://localhost:5000/home")
        log = self.getLogger()
        buttons = self.get_not_logged_in_buttons()
        log.info("Checking all buttons for a non-logged user")
        for button in buttons:
            assert button.is_displayed()

    def test_comparing_posts_on_page(self):
        """Moving to second posts page and comparing articles"""
        self.driver.get("http://localhost:5000/home")
        log = self.getLogger()
        home_page = HomePage(self.driver)
        page1_articles = home_page.get_article_titles()
        home_page.go_to_second_page()
        page2_articles = home_page.get_article_titles()
        log.info("Comparing page 1 and page 2 post titles")
        assert page1_articles != page2_articles



