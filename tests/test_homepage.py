import pytest

from tests.test_base import BaseTest
from pages.homepage import HomePage
from utilities.testdata import TestData
import allure

class Test_Login(BaseTest):
    @pytest.mark.regression
    def test_homepage_title(self):
        self.hp = HomePage(self.driver)
        title = self.hp.get_title()
        try:
            assert title == TestData.homepage_title
        finally:
            if(AssertionError):
                allure.attach(self.driver.get_screenshot_as_png(), name='home page title', attachment_type=allure.attachment_type.PNG)
        self.hp.search()

    @pytest.mark.regression
    def test_auto_suggestions_has_search_term(self):
        self.hp = HomePage(self.driver)
        assert self.hp.get_auto_suggestions_list()