import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.base_url = 'https://www.amazon.com.tr/'

    def tearDown(self):
        self.driver.quit()
