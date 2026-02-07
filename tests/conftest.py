import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def authorized_page(page: Page):
    """Авторизованная страница для тестов, требующих входа."""
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    
    # Ожидаем успешного перехода
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    return page
