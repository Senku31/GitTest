from selenium.webdriver.common.by import By

# from qa.PageObjects.UserPosts import UserPosts
from qa.utilities.BaseClass import BaseClass


class PostPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    post_title = (By.CSS_SELECTOR, ".article-title")
    post_author = (By.CSS_SELECTOR, "a[href*='/user']")
    update_btn = (By.CSS_SELECTOR, "a[href*='/update']")
    delete_btn = (By.XPATH, "//*[text()='Delete']")
    post_content = (By.CSS_SELECTOR, ".article-content")
    confirm_delete = (By.CSS_SELECTOR, "input[value='Delete']")
    post_title_field = (By.ID, "title")
    post_content_field = (By.ID, "content")
    submit_post = (By.ID, "submit")

    def get_post_title(self):
        return self.driver.find_element(*self.post_title)

    def get_post_content(self):
        return self.driver.find_element(*self.post_content)

    def get_post_author(self):
        return self.driver.find_element(*self.post_author)

    def go_to_author_profile(self):
        self.get_post_author().click()
        user_profile = UserPosts(self.driver)
        return user_profile

    def get_author_name(self):
        return self.get_post_author().text

    def delete_post(self):
        self.driver.find_element(*self.delete_btn).click()
        self.driver.find_element(*self.confirm_delete).click()

    def create_new_post(self, title, content):
        self.driver.find_element(*self.post_title_field).send_keys(title)
        self.driver.find_element(*self.post_content_field).send_keys(content)
        self.driver.find_element(*self.submit_post).click()

    def update_post(self, title, content):
        self.driver.find_element(*self.update_btn).click()
        self.driver.find_element(*self.post_title_field).clear()
        self.driver.find_element(*self.post_title_field).send_keys(title)
        self.driver.find_element(*self.post_content_field).clear()
        self.driver.find_element(*self.post_content_field).send_keys(content)
        self.driver.find_element(*self.submit_post).click()


class UserPosts(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    header = (By.CSS_SELECTOR, "h1")
    post_title = (By.CSS_SELECTOR, ".article-title")

    def get_header(self):
        return self.driver.find_element(*self.header).text

    def open_newest_post(self):
        self.driver.find_element(*self.post_title).click()
        post_page = PostPage(self.driver)
        return post_page


