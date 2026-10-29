# Help Desk — Практическая работа № 5

Учебный проект системы централизованной регистрации и обработки обращений пользователей.

## Возможности
- REST API на Django REST Framework.
- Пользователи и роли: заявитель, оператор, исполнитель, администратор.
- Создание и просмотр заявок, назначение исполнителя, изменение статуса и приоритета.
- Категории обращений и комментарии.
- Сводная статистика и отчёты.
- Streamlit-дашборд для демонстрации данных.
- SQLite для быстрого локального запуска.

## Стек
Python 3.11+, Django 5.2, Django REST Framework, Streamlit, Requests.

## Быстрый запуск (Windows)
```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations accounts tickets reports
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Откройте:
- API: http://127.0.0.1:8000/api/
- Админ-панель: http://127.0.0.1:8000/admin/

В отдельном терминале для дашборда:
```powershell
.venv\Scripts\activate
streamlit run dashboard/app.py
```
Дашборд: http://localhost:8501

## Быстрый запуск (Linux/macOS)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations accounts tickets reports
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```
Во втором терминале:
```bash
source .venv/bin/activate
streamlit run dashboard/app.py
```

## Демонстрационные учётные записи
Команда `seed_demo` создаёт демонстрационные данные и пользователей `demo_operator`, `demo_agent`, `demo_requester`, `demo_admin` с паролем `HelpDesk123!`, если их ещё нет. Для входа в Django Admin используйте `demo_admin`; для дашборда — `demo_operator`. Используйте эти данные только локально для демонстрации. Перед реальным развёртыванием измените пароли и настройте `SECRET_KEY`, `DEBUG` и `ALLOWED_HOSTS`.

## Основные API-маршруты
| Метод | Маршрут | Назначение |
|---|---|---|
| GET/POST | `/api/tickets/` | Список заявок / создание |
| GET/PATCH/DELETE | `/api/tickets/{id}/` | Просмотр / изменение / удаление заявки |
| GET/POST | `/api/categories/` | Категории |
| GET/POST | `/api/comments/` | Комментарии |
| GET | `/api/users/` | Пользователи |
| GET | `/api/reports/summary/` | Сводная статистика |
| GET | `/api/reports/by-status/` | Заявки по статусам |
| GET | `/api/reports/by-priority/` | Заявки по приоритетам |
| GET | `/api/health/` | Проверка доступности API |

Для учебной демонстрации API использует стандартную сессию Django и базовую аутентификацию DRF. В интерфейсе `/admin/` можно управлять пользователями, категориями, заявками и комментариями.

## Структура проекта
```text
helpdesk-pr5/
├── config/                 # настройки и маршруты Django
├── apps/
│   ├── accounts/           # пользователи и роли
│   ├── tickets/            # заявки, категории, комментарии
│   └── reports/            # API отчётов
├── dashboard/              # Streamlit-дашборд
├── requirements.txt
├── manage.py
└── README.md
```

## Для GitHub
1. Создайте пустой репозиторий на GitHub.
2. Распакуйте архив.
3. Загрузите содержимое папки `helpdesk-pr5` в репозиторий.
4. Не добавляйте в репозиторий локальную базу `db.sqlite3`, виртуальное окружение или секреты.

## Примечание
Проект является учебным прототипом. Для промышленной эксплуатации следует добавить полноценную политику доступа, аудит действий, защищённое хранение секретов, HTTPS, резервное копирование и тесты.
