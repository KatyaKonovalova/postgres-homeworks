"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')

try:
    with conn:
        with conn.cursor() as cur:

            with open(os.path.join('north_data/customers_data.csv'), 'r', encoding='utf-8') as csvfile:
                pass_line = next(csvfile)
                data = csv.reader(csvfile)
                for row in data:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (row[0],
                                                                              row[1],
                                                                              row[2]))

            with open(os.path.join('north_data/employees_data.csv'), 'r', encoding='utf-8') as csvfile:
                pass_line = next(csvfile)
                data = csv.reader(csvfile)
                for row in data:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (row[0],
                                                                                          row[1],
                                                                                          row[2],
                                                                                          row[3],
                                                                                          row[4],
                                                                                          row[5]))

            with open(os.path.join('north_data/orders_data.csv'), 'r', encoding='utf-8') as csvfile:
                pass_line = next(csvfile)
                data = csv.reader(csvfile)
                for row in data:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (row[0],
                                                                                   row[1],
                                                                                   row[2],
                                                                                   row[3],
                                                                                   row[4]))
finally:
    conn.close()
