CRUD User API
API by Python/Django/DRF

Описание
Тестовое задания для EmphaSoft
Реализация базового функционала CRUD с использованием токен аутентификации.

Задача
Сделайте CRUD для юзеров с токен аутентификацией.
Для примера можно взять https://emphasoft-test-assignment.herokuapp.com/swagger/
Опционально: тесты, линтер и статическая типизация

Используемые технологии
Python;
Django;
DRF;

токен: cd046f7286c95cd170f511a46b069776727ceb68

CREATE  http://127.0.0.1:8000/api/v1/data/

READ  http://127.0.0.1:8000/api/v1/data/

UPDATE DELETE http://127.0.0.1:8000/api/v1/data/<int:pk>/


user create http://127.0.0.1:8000/api/v1/auth/users/

login с выдачей токена http://127.0.0.1:8000/api/v1/auth_token/token/login