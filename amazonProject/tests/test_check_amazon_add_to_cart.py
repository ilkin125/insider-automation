import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from tests.base_test import BaseTest


class TestCheckAmazonAddToCart(BaseTest):

    def test_check_amazon_add_to_cart(self):
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)
        self.driver.get(self.base_url)

        home_page.search_textbox("Samsung")
        home_page.accept_cookies()
        product_page.go_to_page_2()

        self.assertTrue(product_page.is_on_page_2(), "Sayfa 2'de değilsiniz.")
        print("2. sayfadasınız.")

        product_page.select_product()

        new_url = self.driver.current_url
        self.assertIn("/dp/", new_url, "Ürün sayfasında değilsiniz.")
        try:
            product_title = self.driver.find_element(By.ID, "productTitle")
            self.assertIsNotNone(product_title, "Ürün sayfasında değilsiniz.")
            print("Ürün sayfasındasınız.")

        except NoSuchElementException:
            self.fail("Ürün sayfasına ulaşılamadı veya ürün başlığı bulunamadı.")

        product_page.add_to_cart()
        added_to_cart_message = self.driver.find_element(By.LINK_TEXT, "Sepete Git")
        self.assertIsNotNone(added_to_cart_message, "Ürün sepete eklenemedi.")
        print("Ürün sepete başarıyla eklendi.")
        cart_page.go_to_cart()
        home_page.return_home()
        home_url = 'https://www.amazon.com.tr/ref=nav_logo'
        self.assertEqual(self.driver.current_url, home_url, "Anasayfaya dönülemedi.")
        print("Anasayfaya başarıyla döndünüz.")


if __name__ == "__main__":
    unittest.main()
