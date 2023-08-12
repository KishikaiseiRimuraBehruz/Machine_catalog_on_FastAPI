from database.models import Car

from datetime import datetime

from __init__ import get_db


# Функция добовление машини в базу
def registter_car(car_id, name, model,):
    db = next(get_db())

    new_car = Car(id=car_id, name=name, model=model, reg_date=datetime.now())

    db.add(new_car)
    db.commit()

    return "Успешно добовлен спасибо за труд"


# Функция получение информаниции (нахощдение) машини (car_id)
def get_exact_car_db(car_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_car = db.query(Car).filter_by(id=car_id).first()

    # проверка
    if exact_car:
        return exact_car

    return 'Ошибка в данных'


# Функция удаление машины
def delete_car_in_db(car_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_car_delete = db.query(Car).filter_by(id=car_id).first()

    # проверка
    if exact_car_delete:
        db.delete(exact_car_delete)
        db.commit()

        return 'Успешно удален'

    return 'Ошибка в данных'