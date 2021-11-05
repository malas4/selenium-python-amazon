import pytest

from tests.test_base import BaseTest
from pages.homepage import HomePage
from pages.SearchResultsPage import SearchResultsPage
from pages.addtocartpage import AddtocartPage
import allure

class Test_addtocart(BaseTest):

    @allure.description("Validates addtocartbutton is present")
    @allure.severity(severity_level="CRITICAL")
    def test_addtocartbutton_is_present(self):
        self.hp = HomePage(self.driver)
        self.hp.search()
        self.results = SearchResultsPage(self.driver)
        self.results.click_search_result()
        self.addtocart = AddtocartPage(self.driver)
        self.addtocart.add_to_cart_is_present()

    @pytest.mark.regression
    def test_user_should_be_able_to_add_to_cart(self):
        self.hp = HomePage(self.driver)
        self.hp.search()
        self.results = SearchResultsPage(self.driver)
        self.results.click_search_result()
        self.addtocart = AddtocartPage(self.driver)
        self.addtocart.click_add_to_cart()

