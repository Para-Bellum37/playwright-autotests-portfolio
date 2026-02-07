# Docker [stub]

Папка зарезервирована для Docker-конфигурации. Сейчас пуста — и вот почему.

## Почему заглушка?

Для этого проекта Docker избыточен:

1. **CI уже работает** — GitHub Actions предоставляет чистое Ubuntu-окружение с Python и браузерами. Контейнеризация не даёт преимуществ.

2. **Локальный запуск прост** — `pip install` + `playwright install` занимает 30 секунд. Docker добавил бы только сложность.

3. **Нет приложения для поднятия** — мы тестируем внешний сайт (SauceDemo), не свой сервис. Нечего контейнеризировать.

## Когда Docker нужен

Docker становится полезен, когда:

| Сценарий | Зачем |
|----------|-------|
| Тестирование своего приложения | Поднять backend + frontend + DB в docker-compose |
| Self-hosted CI runners | Изолировать окружение от хоста |
| Матричное тестирование | Python 3.9 / 3.10 / 3.11 параллельно |
| Воспроизводимость | "У меня работает" → работает везде |

## Как активировать

1. Создать `Dockerfile`:
```dockerfile
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["pytest", "--headless", "--alluredir=allure-results"]
```

2. Собрать и запустить:
```bash
docker build -t playwright-tests .
docker run -v $(pwd)/allure-results:/app/allure-results playwright-tests
```

3. (Опционально) `docker-compose.yml` для сложных сетапов:
```yaml
version: '3.8'
services:
  tests:
    build: .
    volumes:
      - ./allure-results:/app/allure-results
    environment:
      - BASE_URL=http://app:3000
  app:
    image: my-app:latest
    ports:
      - "3000:3000"
```
