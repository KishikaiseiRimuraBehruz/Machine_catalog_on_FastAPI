from fastapi import FastAPI
from __init__ import Base, engine
from fastapi import Request
from carservice import *
from  database.models import *
from __init__ import *

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Поиск в базе по айди
@app.get("/car/car_id")
async def get_exact_car_info(request:Request):
    # Получить JSON со всеми данными которые пришли из front
    data = await request.json()

    # Получить ключь post_id из data
    car_id = data.get('car_id')


    if car_id:
        # Получаем данные из базы
        exact_post_comment = get_exact_car_db(car_id)


        return {'status': 1, 'message': exact_post_comment}

    return {'status': 0, 'message': 'Неверный ввод данных'}

# Функциия добовить в базу
@app.get("/add-car/")
async def public_car_db (car_name, car_model, car_year):


    if car_name and car_model and car_year:
        add_user_post = public_car_db(car_name, car_model, car_year)

        return {'status': 1, 'message': add_user_post}

    return {'status': 0, 'message': 'Неверный ввод данных'}


# Удалить определенную пост
@app.delete("/car/car_id")
async def delete_car(request: Request):
    # Получить JSON со всеми данными которые пришли из front
    data = await request.json()

    # Получить ключь post_id из data
    car_id_delete = data.get('car_id')


    if car_id_delete:
        car_delete = delete_car_in_db(car_id_delete)

        return {'status': 1, 'message': car_delete}

    return {'status': 0, 'message': 'Неверный ввод данных'}

