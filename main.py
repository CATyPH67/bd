import psycopg2
from psycopg2 import Error
import datetime
from random import randint
from dateutil.relativedelta import relativedelta

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    for i in range(125):
        # Выполнение SQL-запроса для вставки даты и времени в таблицу
        insert_query = """ INSERT INTO note_type (note_id, name, score, date)
                                      VALUES (%s, %s, %s, %s)"""
        time_date = datetime.datetime.now()
        item_tuple = (2, "Мстители " + str(i + 1), randint(1, 10), time_date + relativedelta(years=i))
        cursor.execute(insert_query, item_tuple)
        connection.commit()
        # print("элемент успешно добавлен")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")