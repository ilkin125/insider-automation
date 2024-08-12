from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PAGE_2 = (By.XPATH, f"//a[@aria-label='{2} sayfasına git']")
    SELECT_PRODUCT = (By.XPATH, "(//div[@data-component-type='s-search-result'])[21]")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    PRODUCT_TITLE = (By.ID, "productTitle")

    def go_to_page_2(self):
        self.click_element(*self.PAGE_2)
        self.driver.implicitly_wait(5)

    def is_on_page_2(self):
        return "page=2" in self.driver.current_url

    def select_product(self):
        self.click_element(*self.SELECT_PRODUCT)
        self.driver.implicitly_wait(5)

    def is_product_page(self):
        return "/dp/" in self.driver.current_url

    def add_to_cart(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def get_product_title(self):
        try:
            return self.driver.find_element(*self.PRODUCT_TITLE).text
        except NoSuchElementException:
            return None
