import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.testdata import TestData
import allure

@pytest.fixture(params=["chrome"],scope = 'class')
def init_driver(request):
    if request.param =="chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.maximize_window()
        request.cls.driver = web_driver
    yield
    web_driver.close()