from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage():
    #all common elemnts and functionalities available to allpages
    def __init__(self,driver):
        self.driver = driver


    def click(self, by_locator):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(by_locator)).click()

    def mouse_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def assert_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self):
        #WebDriverWait(self.driver,10).until(EC.title_contains(title))
        return self.driver.title


    def is_visible(self, by_locator):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(web_element)

