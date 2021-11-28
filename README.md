# M.A.N.G.A
### Установка и запуск приложения
- Скачайте репозиторий
- В директории `hahaton` создайте виртуальное окружение
```
python3 -m venv venv
```

- Активируйте виртуальное окружение
```
source venv/bin/activate
```

- Установите необходимые зависимости
```
pip install -r requirements.txt
```

- Задайте переменную окружения FLASK_APP
```
export FLASK_APP=main.py
```

- Запустите приложение
```
flask run
```

### Доступные api-handlers

| HTTP      | Resource URL | Notes | CONTENT
| ----------- | ----------- | ---- | -----
| POST  | `/api/v1/login/`      | авторизация пользователя | {"username": username, "password": password}
| GET   | `/api/v1/users/<string:username>/`       | информация о пользователе **username**
| GET   | `/api/v1/posts/<string:username>/`       | публикации пользователя **username**
| PUT   | `/api/v1/posts/<string:username>/`       | изменить пост **pid** | {"content": content, "post_id": pid, "user_id": "user_id"}
| DELETE| `/api/v1/posts/<string:username>/`       | удалить пост **pid** 
| GET   | `/api/v1/followed/posts/<string:username>/`       | публикации пользователей на которых подписан **username**
| GET   | `/api/v1/recomendations/<string:username>/`       | показать пользователю **username** рекомендованных для подписки пользователей
| POST   | `/api/v1/recomendations/<string:username>/`       | подписать на пользователя **username** | {"user_id": uid} - uid авторизованного пользователя
| GET   | `/api/v1/comments/<int:id>/`       | показать комментарии к посту **id**
| POST   | `/api/v1/comments/<int:id>/`       | добавить комментарий к посту **id** | {"content": content, "post_id": pid, "user_id": "user_id"}
| PUT   | `/api/v1/comments/<int:id>/`       | обновить комментарий **cid=id** | {"content": content}
| DELETE   | `/api/v1/comments/<int:id>/`       | удалить комментарий с **cid=id** |
| GET   | `/api/v1/tickers/<string:username>/`       | показать информацию по финансовым инструментам пользователя **username**
| PUT   | `/api/v1/post/<int:pid>/`       | обновить пост **pid** | {"content": content}
| DELETE   | `/api/v1/post/<int:pid>/`       | удалить пост **pid** | {"content": content}
| POST   | `/api/v1/post/create/`       | создание нового поста | {"content": content, "user_id": user_id, "media": media}
