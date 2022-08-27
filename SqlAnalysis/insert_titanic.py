
import pandas as pd
import psycopg2
from credentials import elephantSqlCredentials


dbname = elephantSqlCredentials.get('dbname')
user = elephantSqlCredentials.get('user')
password = elephantSqlCredentials.get('password')
host = elephantSqlCredentials.get('host')

# make our postgres connection and cursor 
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

def execute_query_pg(curs, conn, query):
    resutls = curs.execute(query)
    conn.commit()
    return resutls

TITANIC_TABLE = """
CREATE TABLE IF NOT EXISTS titanic_table(
    passenger_id SERIAL PRIMARY KEY,
    survived INT NOT NULL,
    pclass INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    age FLOAT NOT NULL,
    Siblings_Spouses_Aboard INT NOT NULL,
    parents_children_aboard INT NOT NULL,
    fare FLOAT NOT NULL
);
"""

DROP_TITANIC_TABLE = """
DROP TABLE IF EXISTS titanic_table
"""

df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", '')

if __name__ == '__main__':
    #creates table and its' associated schema 
    # Drop Table
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)
    # Create Table
    execute_query_pg(pg_curs, pg_conn, TITANIC_TABLE)

    records = df.values.tolist() 

    for record in records:
        insert_statement = """
            INSERT INTO titanic_table (survived, pclass, name, sex, age, Siblings_Spouses_Aboard, parents_children_aboard, fare)
            VALUES {};
        """.format(tuple(record))
        execute_query_pg(pg_curs, pg_conn, insert_statement)