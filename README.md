# qaguru_python_advanced_intro
# Микросервис Python + FastAPI
Установка зависимостей:
- pip install fastapi uvicorn

Запуск сервера:
- uvicorn server:app --reload

Реализованы следующие запросы:
- GET запрос /api/users/{user_id} - получаем конкретного пользователя
- GET запрос /api/users - получаем список всех пользователей
- POST запрос /api/users - создаем нового пользователя
- PUT запрос /api/users/{user_id} - изменяем имя у конкретного пользователя
- DELETE запрос /api/users/{user_id} - удаляем конкретного пользователя, выставляя значение ключа **archive** в *true*


# Примеры запросов


# Запуск автотестов
