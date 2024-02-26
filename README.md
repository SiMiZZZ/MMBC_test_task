
### MMVS Python Test

# Приложение на Django rest framework

- Выполнены все заявленные требования по API
- Приложение обернуто в docker контейнеры (app, celery, redis)
- Прикручена автодокументация API (Swagger)
- Обрезка видео происходит асинхронно через celery, тем самым не забивая поток сервера

# Запуск приложения

```Bash
docker compose up -d --build
```
