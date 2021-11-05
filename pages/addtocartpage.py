from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class AddtocartPage(BasePage):

    add_to_cart = (By.ID, "add-to-cart-button")
    buy_now = (By.ID, "buy-now-button")
    warranty_pane_no_thanks = (By.CSS_SELECTOR, "#attachSiNoCoverage-announce")

    def __init__(self,driver):
        super().__init__(driver)

    def click_add_to_cart(self):
        self.click(self.add_to_cart)
        try:
            no_thanks_element = self.driver.find_element(*self.warranty_pane_no_thanks)
            self.driver.execute_script("arguments[0].click();", no_thanks_element)
        except NoSuchElementException:
            pass

    def click_buynow(self):
        self.click(self.buy_now)

    def add_to_cart_is_present(self):
        return self.is_visible(self.add_to_cart)

