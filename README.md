# Автотесты Playwright + Pytest

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Test-green?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow?style=for-the-badge&logo=pytest&logoColor=white)

Этот проект содержит набор автоматизированных тестов для демонстрационного веб-сайта [SauceDemo](https://www.saucedemo.com/).
Тесты написаны на Python с использованием фреймворка **Playwright** для взаимодействия с браузером и **Pytest** для организации тестов.

## Функциональность

Все автотесты взаимодействуют с учебным сайтом **SauceDemo**.

### 1. Модуль tests/test_auth.py (Авторизация)
Этот блок проверяет, что пользователей пускает на сайт только с правильными данными, и не пускает с ошибками.

- **Успешный вход**: Вводит `standard_user` / `secret_sauce` -> Проверяет, что мы попали в магазин (`/inventory.html`).
- **Ошибки**:
    - Ввод несуществующего логина/пароля -> Ошибка "Username and password do not match...".
    - Пустые поля -> Ошибки "Username is required" или "Password is required".
    - Закрытие окна ошибки -> Проверяет, что красный крестик работает и сообщение пропадает.

### 2. Модуль tests/test_shop.py (Магазин)
Здесь проверяется основной путь покупателя (User Flow).

- **Работа с корзиной**:
    - Нажать "Add to cart" -> Проверка: у иконки корзины появилась цифра, товар внутри.
    - Нажать "Remove" -> Проверка: товар исчез.
- **Оформление заказа (E2E)**:
    - Добавить рюкзак -> Перейти в корзину -> Checkout -> Заполнить имя/индекс -> Finish.
    - **Результат**: Видим заголовок "Thank you for your order!".
- **Сортировка**:
    - Выбираем "Price (low to high)" -> Проверяем, что первый товар дешевле последнего.
    - Выбираем "Price (high to low)" -> Наоборот.
- **Выход (Logout)**: Открыть меню и нажать Logout -> Проверяем, что вернулись на экран логина.

## Установка и Запуск

### Предварительные требования
- Python 3.8+
- Установленный браузер (Chromium, Firefox или WebKit)

### Шаги установки

1.  **Клонируйте репозиторий** (или скачайте архив):
    ```bash
    git clone https://github.com/belwrex/autotests-project.git
    cd autotests-project
    ```

2.  **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Установите браузеры для Playwright**:
    ```bash
    playwright install chromium
    ```

### Запуск тестов

**Обычный запуск (с отображением браузера):**
```bash
pytest
```

**Запуск в фоновом режиме (headless):**
```bash
pytest --headless
```

**Замедленный режим (для демонстрации):**
```bash
pytest --slowmo 1000
```
(По-умолчанию - настроено в `pytest.ini`)

## Структура проекта

```text
.
├── tests/                  # Папка с тестами
│   ├── conftest.py         # Общие фикстуры (настройка браузера, авторизация)
│   ├── test_auth.py        # Тесты страницы авторизации
│   └── test_shop.py        # Тесты функционала магазина
├── pytest.ini              # Конфигурация запуска тестов
├── requirements.txt        # Список зависимостей
└── README.md               # Документация
```
