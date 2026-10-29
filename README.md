# Автосалон — Практическая работа № 5

Учебный проект на Django REST Framework: авторизация сотрудников, каталог автомобилей,
клиенты, заказы, отчёты и отдельный Streamlit-дашборд.

## Быстрый запуск

1. Установите Python 3.10+.
2. Создайте виртуальное окружение и активируйте его.
3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создайте таблицы и администратора:

   ```bash
   python manage.py makemigrations accounts catalog clients orders
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Запустите API:

   ```bash
   python manage.py runserver
   ```

6. Откройте `http://127.0.0.1:8000/admin/` для панели администратора,
   `http://127.0.0.1:8000/api/` для API и `http://127.0.0.1:8000/api-auth/login/`
   для браузерной авторизации DRF.

## API

- `POST /api/auth/register/` — регистрация сотрудника
- `POST /api/auth/login/` — получение JWT-токенов
- `GET /api/auth/me/` — текущий пользователь (нужен Bearer access token)
- `/api/cars/`, `/api/brands/` — каталог
- `/api/clients/` — клиенты
- `/api/orders/` — заказы
- `/api/reports/kpi/`, `/revenue/`, `/top-models/`, `/manager-load/`, `/stock/` — отчёты

Вход в API через JWT: передавайте заголовок `Authorization: Bearer <access>`.

## Streamlit-дашборд

При работающем Django-сервере в другом терминале:

```bash
streamlit run dashboard/app.py
```

По умолчанию API расположен на `http://127.0.0.1:8000/api/reports/`.
Можно изменить адрес переменной окружения `API_BASE_URL`.

## Примечания

- Это учебный шаблон. Перед развёртыванием в production задайте безопасный `DJANGO_SECRET_KEY`,
  настройте `DEBUG=False`, разрешённые хосты, HTTPS, CORS/CSRF и резервное копирование.
- Заказы защищают смену статуса автомобиля: завершённый заказ помечает авто проданным,
  отменённый возвращает его в наличие.
