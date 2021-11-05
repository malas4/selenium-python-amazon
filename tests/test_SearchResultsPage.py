import pytest

from tests.test_base import BaseTest
from pages.homepage import HomePage
from utilities.testdata import TestData
from pages.SearchResultsPage import SearchResultsPage

class Test_results(BaseTest):
    @pytest.mark.regression
    def test_result_displayed(self):
        self.hp = HomePage(self.driver)
        self.hp.search()

        self.results = SearchResultsPage(self.driver)
        self.results.is_results_link_exist()
        title = self.results.title_contains_search_term()
        print(title)
        self.results.click_search_result()




