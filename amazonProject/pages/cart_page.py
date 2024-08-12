from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    GO_TO_CART = (By.LINK_TEXT, "Sepete Git")
    ADDED_TO_CART_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Sepete Eklendi')]")

    def go_to_cart(self):
        self.click_element(*self.GO_TO_CART)
        self.driver.implicitly_wait(5)
