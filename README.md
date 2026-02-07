# Playwright Autotests

E2E-тесты для [SauceDemo](https://www.saucedemo.com/) — учебного интернет-магазина.

![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-green?logo=playwright&logoColor=white)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=github-actions&logoColor=white)

## Что это?

Набор автотестов, покрывающих основные сценарии интернет-магазина:
- Авторизация (позитивные и негативные кейсы)
- Работа с корзиной
- Оформление заказа (E2E)
- Сортировка товаров
- Выход из системы

Тесты написаны на **Playwright** (современный инструмент для браузерной автоматизации) и организованы через **Pytest**.

## Быстрый старт

```bash
# Клонировать
git clone https://github.com/Para-Bellum37/playwright-autotests-portfolio.git
cd playwright-autotests-portfolio

# Установить зависимости
pip install -r requirements.txt
playwright install chromium

# Запустить тесты
pytest
```

## Покрытие тестами

### test_auth.py — Авторизация

| Тест | Что проверяет |
|------|---------------|
| Успешный вход | Валидные креды → переход в каталог |
| Неверные данные | Ошибка "Username and password do not match" |
| Пустой логин | Ошибка "Username is required" |
| Пустой пароль | Ошибка "Password is required" |
| Закрытие ошибки | Кнопка × скрывает сообщение |

### test_shop.py — Магазин

| Тест | Что проверяет |
|------|---------------|
| Добавление в корзину | Товар появляется, badge обновляется |
| Удаление из корзины | Товар исчезает |
| Полный checkout | Корзина → данные → подтверждение → "Thank you" |
| Счётчик корзины | Добавить 2 товара → badge = "2" |
| Сортировка Low→High | Первый товар дешевле последнего |
| Сортировка High→Low | Первый товар дороже последнего |
| Logout | Меню → Logout → возврат на логин |

## Варианты запуска

```bash
# С браузером (для отладки)
pytest

# Без UI (для CI)
pytest --headless

# Замедленный режим (для демо)
pytest --slowmo 1000

# С генерацией Allure-отчёта
pytest --alluredir=allure-results
allure serve allure-results
```

## CI/CD

Тесты запускаются автоматически при каждом пуше в `main`.

**Что делает пайплайн:**
1. Чекаут кода
2. Установка Python 3.11
3. Установка зависимостей + Playwright + Chromium
4. Запуск тестов в headless-режиме
5. Сохранение Allure-артефактов

Конфиг: [`.github/workflows/tests.yml`](.github/workflows/tests.yml)

## Структура проекта

```
.
├── .github/workflows/tests.yml   # CI-конфиг
├── tests/
│   ├── conftest.py               # Фикстуры (авторизация)
│   ├── test_auth.py              # Тесты логина
│   ├── test_shop.py              # Тесты магазина
│   └── api/README.md             # [stub] — см. ниже
├── docker/README.md              # [stub] — см. ниже
├── pytest.ini                    # Настройки pytest
├── requirements.txt              # Зависимости
└── README.md
```

## Расширяемость

Проект подготовлен для роста. Две папки оставлены как заглушки с инструкциями:

| Папка | Статус | Почему stub |
|-------|--------|-------------|
| `tests/api/` | Заглушка | SauceDemo не имеет публичного API |
| `docker/` | Заглушка | Для демо-проекта избыточен — CI работает без него |

Каждая папка содержит README с объяснением, когда и как её активировать.

## Технологии

- **Python 3.10+** — основной язык
- **Playwright** — браузерная автоматизация
- **Pytest** — тестовый фреймворк
- **Allure** — генерация отчётов
- **GitHub Actions** — CI/CD
