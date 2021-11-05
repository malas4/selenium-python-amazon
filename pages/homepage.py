from selenium.webdriver.common.by import By
from  pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.testdata import TestData

class HomePage(BasePage):
    search_field = (By.ID, "twotabsearchtextbox")
    search_button = (By.ID, "nav-search-submit-button")
    sign_in = (By.CLASS_NAME, 'nav-action-button')
    hello_sign_in = (By.CSS_SELECTOR, "div.nav-line-1-container span")
    auto_suggest_elements_list = (By.XPATH, "//div[@id ='suggestions']//div")
    auto_search_list_elements = (By.CSS_SELECTOR, '#suggestions >div')


    def __init__(self,driver):

        super().__init__(driver)
        self.driver.get(TestData.Base_url)

    def search(self):

        self.driver.find_element(*self.search_field).clear()
        self.send_keys(self.search_field, TestData.search_term)
        self.click(self.search_button)

    def get_homepage_title(self):
        return self.get_title()

    def get_auto_suggestions_list(self):
        self.driver.find_element(*self.search_field).clear()
        self.send_keys(self.search_field, TestData.auto_suggestion_search_term)
        list_elements = self.driver.find_elements(*self.auto_search_list_elements)
        for i in list_elements:
            if i.text == TestData.search_term:
                break
        return True


