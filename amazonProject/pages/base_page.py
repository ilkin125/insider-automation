from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, text, *locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def accept_cookies(self):
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
            )
            accept_cookies_button.click()
            print("Çerez kabul etme butonuna tıklandı.")
        except (NoSuchElementException, TimeoutException):
            print("Çerez kabul etme butonu bulunamadı veya tıklanamaz durumda.")
