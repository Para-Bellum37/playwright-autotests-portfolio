import pytest
from playwright.sync_api import Page, expect

class TestAuthorizationFields:
    """Тесты авторизации"""
    
    def test_successful_authorization(self, page: Page):
        """Тестирование успешной авторизации"""
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="username"]').fill("standard_user")
        page.locator('[data-test="password"]').fill("secret_sauce")
        page.locator('[data-test="login-button"]').click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_unsuccessful_authorization_with_symbols(self, page: Page):
        """Тестирование неуспешной авторизации с неверными данными"""
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="username"]').fill("aaa")
        page.locator('[data-test="password"]').fill("aaa")
        page.locator('[data-test="login-button"]').click()
        expect(page.locator('[data-test="error"]')).to_be_visible()
        expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

    def test_unsuccessful_authorization_with_empty_fields(self, page: Page):
        """Тестирование неуспешной авторизации с пустыми полями"""
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="login-button"]').click()
        expect(page.locator('[data-test="error"]')).to_be_visible()
        expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")

    def test_unsuccessful_authorization_with_empty_password(self, page: Page):
        """Тестирование неуспешной авторизации с пустым полем пароля"""
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="username"]').fill("standard_user")
        page.locator('[data-test="login-button"]').click()
        expect(page.locator('[data-test="error"]')).to_be_visible()
        expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Password is required")

    def test_unsuccessful_authorization_with_empty_login(self, page: Page):
        """Тестирование неуспешной авторизации с пустым полем логина"""
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="password"]').fill("secret_sauce")
        page.locator('[data-test="login-button"]').click()
        expect(page.locator('[data-test="error"]')).to_be_visible()
        expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")
    
    def test_closing_the_error_window(self, page: Page):
        """Тестирование закрытия окна с ошибкой"""
        page.goto("https://www.saucedemo.com/")
        page.locator('[data-test="login-button"]').click()
        page.locator(".error-button").click()
        expect(page.locator('[data-test="error"]')).not_to_be_visible()
