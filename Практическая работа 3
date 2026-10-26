# Практическая работа № 3

**Выполнила: Волкова Виктория**

— Установка окружения и первый запуск

Учебный каркас Django-проекта: PostgreSQL используется как основная база данных, Memurai — как Redis-совместимый сервер кэша.

## Стек
- Python 3.11 или 3.12
- Django 5.1.4
- PostgreSQL
- Memurai (Redis-compatible) для Windows
- VS Code

## 1. Подготовка
Установите Python, PostgreSQL, VS Code и Memurai. Создайте базу данных `ams_db` в PostgreSQL. Для пользователя `postgres` используйте свой локальный пароль.

## 2. Запуск в Windows PowerShell
Откройте папку проекта в VS Code и выполните команды в терминале:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Откройте `.env` и укажите свой пароль PostgreSQL. Не загружайте `.env` в GitHub: он уже включён в `.gitignore`.

## 3. Создание базы данных
В PostgreSQL создайте базу `ams_db`, например в `psql`:

```sql
CREATE DATABASE ams_db;
```

Если база уже существует, повторно создавать её не нужно.

## 4. Миграции и администратор
В активированном виртуальном окружении выполните:

```powershell
python manage.py check
python manage.py makemigrations accounts catalog
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Откройте `http://127.0.0.1:8000/admin/` и войдите под созданным суперпользователем.

## 5. Проверка Redis/Memurai
Убедитесь, что служба Memurai запущена и слушает порт `6379`. Проверить можно командой `memurai-cli ping` (если команда доступна); ожидаемый ответ — `PONG`. Если Redis не запущен, страница админки может работать, но использование кэша приведёт к ошибке подключения.

## 6. Загрузка в GitHub
1. Создайте пустой репозиторий GitHub.
2. В терминале из папки проекта выполните:

```powershell
git init
git add .
git commit -m "Практическая работа 3: Django environment"
git branch -M main
git remote add origin https://github.com/ВАШ_ЛОГИН/ИМЯ_РЕПОЗИТОРИЯ.git
git push -u origin main
```

Замените URL на адрес своего репозитория. Если GitHub запросит авторизацию, следуйте подсказкам Git Credential Manager.

## Структура
```text
config/                 настройки Django и URL
apps/accounts/          пользователь и его админка
apps/catalog/           справочники и их админка
manage.py               команды Django
requirements.txt        зависимости Python
.env.example            шаблон локальных настроек
.gitignore              исключение секретов и временных файлов
```

## Важно
Это исходный проект для выполнения практической работы, а не подтверждение того, что он уже запускался на вашем компьютере. Для фактической проверки нужно установить зависимости, указать параметры PostgreSQL, запустить миграции и проверить админку. В GitHub загружайте исходники, но не `.env`, `.venv` и пароли.
