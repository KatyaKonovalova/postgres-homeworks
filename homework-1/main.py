"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='LEGENDofTHEseeker1!1')

try:
    with conn:
        with conn.cursor() as cur:

            with open(os.path.join('north_data/customers_data.csv'), 'r', encoding='utf-8') as csvfile:
                pass_line = next(csvfile)
                data = csv.reader(csvfile)
                for row in data:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', row)

            with open(os.path.join('north_data/customers_data.csv'), 'r', encoding='utf-8') as csvfile:
                pass_line = next(csvfile)
                data = csv.reader(csvfile)
                for row in data:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', row)

            with open(os.path.join('north_data/customers_data.csv'), 'r', encoding='utf-8') as csvfile:
                pass_line = next(csvfile)
                data = csv.reader(csvfile)
                for row in data:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', row)
finally:
    conn.close()
