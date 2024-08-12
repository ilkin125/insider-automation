from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    ACCEPT_COOKIES = (By.ID, "sp-cc-accept")
    SEARCH_TEXTBOX = (By.ID, "twotabsearchtextbox")
    RETURN_HOME = (By.XPATH, "//a[@id='nav-logo-sprites']")

    def return_home(self):
        self.click_element(*self.RETURN_HOME)

    def click_cookie(self):
        self.click_element(self.ACCEPT_COOKIES)

    def search_textbox(self, text):
        self.enter_text(text + Keys.RETURN, *self.SEARCH_TEXTBOX)

    def setup_method(self, method):
        self.accept_cookies()
