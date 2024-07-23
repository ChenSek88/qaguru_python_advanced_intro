# qaguru_python_advanced_intro
# Микросервис на стеке Python + FastAPI и API автотесты 

Установка:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt


Запуск сервера:
- uvicorn server:app --reload

Реализованы следующие запросы:
- GET запрос /api/users/{user_id} - получаем конкретного пользователя
- GET запрос /api/users - получаем список всех пользователей
- POST запрос /api/users - создаем нового пользователя
- PUT запрос /api/users/{user_id} - изменяем имя у конкретного пользователя
- DELETE запрос /api/users/{user_id} - удаляем конкретного пользователя, выставляя значение ключа **archive** в *true*

# Автотесты

Реализованы следующие автотесты:
- Получение пользователя по id
- Получение списка пользователей
- Изменение атрибута name у пользователя по id
- Удаление пользователя по id
- Создание нового пользователя

Запуск автотестов:

pytest api_tests/
