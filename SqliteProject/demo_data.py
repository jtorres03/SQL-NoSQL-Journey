import sqlite3


create_table = """
CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR(1),
    x INTEGER,
    y INTEGER
)
"""

insert_demo_data = """
INSERT INTO demo
(s, x, y)
VALUES
("g", 3, 9),
("v", 5, 7),
("f", 8, 7)
"""

row_count_query = """
SELECT count(*)
FROM demo
"""

xy_at_least_5_query = """
SELECT count(*)
FROM demo
WHERE x >= 5
AND y >= 5
"""

unique_y_query = """
SELECT count(DISTINCT y)
FROM demo
"""


def connect_to_db(db_name='demo_data.sqlite3'):
    """Connect to a database"""
    return sqlite3.connect(db_name)


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def execute_ddl(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)


row_count = execute_query(connect_to_db(), row_count_query)
xy_at_least_5 = execute_query(connect_to_db(), xy_at_least_5_query)
unique_y = execute_query(connect_to_db(), unique_y_query)


if __name__ == '__main__':
    conn = connect_to_db()
    execute_ddl(conn, create_table)
    execute_ddl(conn, insert_demo_data)
    conn.commit()
