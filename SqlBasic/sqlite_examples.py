import sqlite3

#connect to database
connection = sqlite3.connect('rpg_db.sqlite3')
#make a cursor
cursor = connection.cursor()
#write our query 
query = "SELECT * FROM charactercreator_character;"
#run query
cursor.execute(query)
#return results of query 
results = cursor.fetchall()

print(results[:5])
