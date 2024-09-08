from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from qa.PageObjects.PostPage import PostPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    articles = (By.CSS_SELECTOR, "article")
    second_page = (By.CSS_SELECTOR, "a[href='/home?page=2']")

    def get_articles_per_page(self):
        articles_list = []
        articles = self.driver.find_elements(*self.articles)
        for article in articles:
            articles_list.append(article)
        return len(articles_list)

    def get_article_titles(self):
        articles_titles_list = []
        articles = self.driver.find_elements(*self.articles)
        for article in articles:
            article_titles = article.find_elements(By.CSS_SELECTOR, "h2")
            for article_title in article_titles:
                articles_titles_list.append(article_title.text)
        return articles_titles_list

    def go_to_second_page(self):
        action = ActionChains(self.driver)
        second_page = self.driver.find_element(*self.second_page)
        action.move_to_element(second_page).click().perform()




