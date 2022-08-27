import sqlite3
from queries import QUERY_LIST

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


def execute_query(curs, query):
    curs.execute(query)
    return curs.fetchall()


def execute_queries(curs, queries):
    answers = {}
    for index, query in enumerate(queries):
        answers[index] = execute_query(curs, query)
    return answers


# when the if statement below is not present then when we call on this module
# from another module it will run and we don't want it to run when we import
# it to another module. This is more of a test. Only runs when weexecute/run
# this module.
if __name__ == '__main__':
    answers = execute_queries(curs, QUERY_LIST)
    for key, value in enumerate(answers.values()):
        print(f"{key}: {value}")
