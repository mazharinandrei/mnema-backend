# 📔Mnema Backend

Бэкенд веб-приложения дневника

## Особенности проекта

- Регистрация и аутентификация пользователей с использованием JWT.
- Создание, просмотр и поиск записей.
- REST API для взаимодействия с фронтендом.

## Технологии и зависимости

Проект реализовывается на Python с использованием Django и Django REST Framework. Основные зависимости приведены в `requirements.txt`
## Установка и локальный запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/mazharinandrei/mnema-backend.git
cd mnema-backend
```

2. Создать виртуальное окружение и активировать его:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Создать файл `.env` в корне проекта с необходимыми параметрами:
```
SECRET_KEY = 'ваш-секретный-ключ'
ALLOWED_HOSTS = ["*"]
```

5. Применить миграции:
```bash
python manage.py migrate
```

6. Запустить сервер
```bash
python manage.py runserver
```

Сервер будет доступен по адресу `http://127.0.0.1:8000/`.

## Планы на будущее

- Миграция базы данных на PostgreSQL
- Шифрование записей
- Усовершенствование поиска
- Возможность прикрепления фото к записям
