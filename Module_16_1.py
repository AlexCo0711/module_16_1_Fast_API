# Домашнее задание по теме "Основы Fast Api и маршрутизация"

# импорт библиотеки FastAPI
from fastapi import FastAPI

# Создано приложение(объект) FastAPI
app = FastAPI()

# Создан декоратор маршрута к главной странице - "/"
@app.get("/")
async def get_p_main() -> dict:
    return {'message': 'Главная страница'}

# Создан декоратор маршрута к странице администратора
@app.get("/user/admin")
async def get_p_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

# Создан декоратор маршрута к страницам пользователей используя параметр в пути
@app.get("/user/{user_id}")
async def get_p_user_id(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

# Создан декоратор маршрута к страницам пользователей передавая данные в адресной строке
@app.get("/user")
async def get_p_data_user(username: str, age: int) -> dict:
    return {'message':
            f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
