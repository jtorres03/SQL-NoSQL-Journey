import sqlite3
import pandas as pd


# SQLite connection variable
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# load in the csv to pandas dataframe
df = pd.read_csv('buddymove_holidayiq.csv')

if __name__ == '__main__':
    # turn the df into a table called 'reviewl
    df.to_sql('review', conn, if_exists='replace')

    # Query the table to ensure that the data was truly added.
    curs.execute('''SELECT * FROM review;''')
    # print(curs.fetchall())

    # Nature and shopping >= 100
    NATURE_SHOPPING = """
    SELECT *
    FROM review
    WHERE Nature >= 100 AND Shopping >= 100;
    """
