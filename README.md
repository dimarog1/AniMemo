## Запуск

### Python

Для запуска приложения потребуется развернуть базу данных PostgreSQL и настроить её в [настройках](AniMemo/settings.py).

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

### Docker

Потребуется освободить порты `5432` и `8000`, первый можно поменять в [настройках](AniMemo/settings.py) и [docker-compose](docker-compose.yaml) 
файлах, второй - не советую.

```bash
docker-compose up --build
```

Если с первого раза не заработало, то просто ещё раз выполните эту команду (фикс в процессе...).
