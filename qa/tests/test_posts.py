import time

from qa.PageObjects.LoginPage import LoginPage
from qa.PageObjects.PostPage import PostPage, UserPosts
from qa.utilities.BaseClass import BaseClass


class TestPosts(BaseClass):
    def test_post_is_displayed(self):
        """Checking number of articles on the homepage"""
        self.driver.get("http://127.0.0.1:5000/post/1")
        log = self.getLogger()
        post_page = PostPage(self.driver)
        """Checking if Post elements are displayed"""
        assert post_page.get_post_author().is_displayed()
        assert post_page.get_post_title().is_displayed()
        assert post_page.get_post_content().is_displayed()
        log.info("Post elements are displayed")

    def test_navigate_to_user_posts(self):
        """Checking number of articles on the homepage"""
        self.driver.get("http://127.0.0.1:5000/post/1")
        log = self.getLogger()
        post_page = PostPage(self.driver)
        author_name = post_page.get_author_name()
        user_profile = post_page.go_to_author_profile()
        assert f'Posts by {author_name}' in user_profile.get_header()

    def test_create_new_post(self):
        """Creting a new post"""
        log = self.getLogger()
        self._successful_log_in()
        log.info("The user has been logged in")
        self.driver.get('http://127.0.0.1:5000/post/new')
        post_page = PostPage(self.driver)
        post_page.create_new_post("Test Title", "Test Content")
        assert "Your post has been created!" in self.get_success_alert()

    def test_update_post(self):
        log = self.getLogger()
        self._successful_log_in()
        log.info("The user has been logged in")
        self.driver.get('http://127.0.0.1:5000/user/TestUser')
        user_profile = UserPosts(self.driver)
        post_page = user_profile.open_newest_post()
        post_page.update_post("Post Title Update", "Post Content Update")
        assert "Your post has been updated!" in self.get_success_alert()

    def test_delete_post(self):
        log = self.getLogger()
        self._successful_log_in()
        log.info("The user has been logged in")
        self.driver.get('http://127.0.0.1:5000/user/TestUser')
        user_profile = UserPosts(self.driver)
        post_page = user_profile.open_newest_post()
        post_page.delete_post()
        assert "Your post has been deleted!" in self.get_success_alert()

    def _successful_log_in(self):
        login_page = LoginPage(self.driver)
        self.driver.get("http://127.0.0.1:5000/login")
        login_page.log_in_to_flaskblog("TestUser@gmail.com",
                                       "passwordTest")




