# API-тесты [stub]

Папка зарезервирована для API-тестов. Сейчас пуста — и вот почему.

## Почему заглушка?

Демо-сайт [SauceDemo](https://www.saucedemo.com/) — это чисто фронтенд-приложение без публичного REST API. Все данные хранятся локально в браузере, бэкенд отсутствует. Тестировать нечего.

Если бы у сайта был API (например, `/api/products`, `/api/cart`), здесь лежали бы тесты на:
- Получение списка товаров
- Добавление/удаление из корзины
- Авторизацию через токены
- Валидацию ошибок (401, 404, 500)

## Как активировать

При работе с реальным проектом:

1. Добавить HTTP-клиент в `requirements.txt`:
```
requests
# или httpx для async
```

2. Создать `test_api.py`:
```python
import requests

BASE_URL = "https://api.example.com"

def test_get_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_unauthorized_access():
    response = requests.get(f"{BASE_URL}/admin")
    assert response.status_code == 401
```

3. Запустить: `pytest tests/api/`

## Ресурсы для практики

Если хочешь потренироваться на открытых API:

| API | Описание |
|-----|----------|
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Фейковый REST API для тестов |
| [Reqres](https://reqres.in/) | CRUD-операции, пагинация, задержки |
| [PetStore](https://petstore.swagger.io/) | Swagger-демо с OpenAPI-спекой |
| [httpbin](https://httpbin.org/) | Эхо-сервер для отладки запросов |
