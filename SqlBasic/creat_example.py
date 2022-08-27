import sqlite3

conn = sqlite3.connect('mock_db.slite3')
cursor = conn.cursor()
# create_statement = "CREATE TABLE test_table (name varchar(24), age integer);"
# cursor.execute(create_statement)

insert_statement = """INSERT INTO test_table
(name, age)
VALUES
("Jon", 24),
("Ben", 32);
"""

cursor.execute(insert_statement)

conn.commit()
cursor.close()
