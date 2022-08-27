# from sqlite3 import connect
from os import getenv

import psycopg2
import queries
import sqlite3

dbname = getenv('dbname')
user = getenv('user')
password = getenv('password')
host = getenv('host')

print(dbname)

# Connects us to postgresql 
# def connect_to_pg():
#     connection = psycopg2.connect(
#         dbname=dbname,
#         user=user,
#         password=password,
#         host=host)
#     return connection
#
#
# # Create a connection object that represents the database. The sqlite3.connect()
# # fx returns a Connection object that we will use to interact with the SQLite
# # database held in the file "rpg_db.sqlite3"
# def connect_to_sqlite(db_name='rpg_db.sqlite3'):
#     return sqlite3.connect(db_name)
#
#
# def execute_query(connection, query):
#     cursor = connection.cursor()
#     cursor.execute(query)
#     return cursor.fetchall()
#
#
# def execute_ddl(connection, query):
#     cursor = connection.cursor()
#     cursor.execute(query)
#
#
# def insert_rpg_data(connection, rpg_data):
#     tuple_strs = ','.join([str(row) for row in rpg_data])
#     insert_statement = f"""
#         INSERT INTO charactercreator_character
#         (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
#         VALUES
#         {tuple_strs}
#         """
#     execute_ddl(connection, insert_statement)
#
#
# if __name__ == '__main__':
#     sqlite_conn = connect_to_sqlite()
#     rpg_data = execute_query(sqlite_conn, queries.select_all)
#     pg_conn = connect_to_pg()
#     execute_ddl(pg_conn, queries.create_character_table)
#     insert_rpg_data(pg_conn, rpg_data)
#     pg_conn.commit()

# cursor.execute(queries.create_character_table)
# cursor.close()
# connection.commit()
#
# print(cursor.execute(queries.get_characters))
