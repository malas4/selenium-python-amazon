

from  pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.testdata import TestData

class SearchResultsPage(BasePage):

    search_result = (By.XPATH, "//div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]" )


    def __init__(self, driver):
        super().__init__(driver)


    def click_search_result(self):
        self.click(self.search_result)

    def is_results_link_exist(self):
        return self.is_visible(self.search_result)

    def title_contains_search_term(self):
        return self.get_title()