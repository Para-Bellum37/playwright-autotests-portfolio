import pytest
from playwright.sync_api import Page, expect

class TestShopActions:
    """Тесты магазина и корзины (требуют авторизации)"""

    def test_logout(self, authorized_page: Page):
        """Тестирование выхода из аккаунта"""
        page = authorized_page
        page.locator("#react-burger-menu-btn").click()
        page.locator("#logout_sidebar_link").click()
        expect(page).to_have_url("https://www.saucedemo.com/")

    def test_adding_product_to_cart(self, authorized_page: Page):
        """Тестирование добавления товара в корзину"""
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator(".shopping_cart_link").click()
        expect(page.locator("text=Sauce Labs Backpack")).to_be_visible()

    def test_deleting_product_from_cart(self, authorized_page: Page):
        """Тестирование удаления товара из корзины"""
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator(".shopping_cart_link").click()
        page.locator('[data-test="remove-sauce-labs-backpack"]').click()
        expect(page.locator("text=Sauce Labs Backpack")).not_to_be_visible()

    def test_successful_order_placement(self, authorized_page: Page):
        """Тестирование успешного оформления заказа"""
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator(".shopping_cart_link").click()
        page.locator('[data-test="checkout"]').click()
        page.locator('[data-test="firstName"]').fill("John")
        page.locator('[data-test="lastName"]').fill("Doe")
        page.locator('[data-test="postalCode"]').fill("12345")
        page.locator('[data-test="continue"]').click()
        page.locator('[data-test="finish"]').click()
        expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

    def test_check_cart_quantity_indicator(self, authorized_page: Page):
        """Тестирование индикатора количества товаров в корзине"""
        page = authorized_page
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
        expect(page.locator(".shopping_cart_badge")).to_have_text("2")

    def test_sorting_products_by_price_low_to_high(self, authorized_page: Page):
        """Тестирование сортировки: Low to High"""
        page = authorized_page
        page.locator('[data-test="product-sort-container"]').select_option("lohi")
        prices = page.locator(".inventory_item_price").all_inner_texts()
        # Простая проверка первого и последнего, более надежная проверка требует парсинга цен
        assert "$7.99" in prices[0]
        assert "$49.99" in prices[-1]

    def test_sorting_products_by_price_high_to_low(self, authorized_page: Page):
        """Тестирование сортировки: High to Low"""
        page = authorized_page
        page.locator('[data-test="product-sort-container"]').select_option("hilo")
        prices = page.locator(".inventory_item_price").all_inner_texts()
        assert "$49.99" in prices[0]
        assert "$7.99" in prices[-1]
