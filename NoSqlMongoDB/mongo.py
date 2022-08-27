from pprint import pprint
import sys
sys.path.append("your_path")
import pymongo
import queries
from SqlAnalysis import pipeline


# Open Connection to Mongo
def create_mdb_conn():
    client = pymongo.MongoClient(
        "hide"
    )
    db = client.test
    return db


def tuples_to_dicts(rpg_data):
    result = []
    for row in rpg_data:
        query = f"""
        SELECT name, value, weight
        FROM charactercreator_character_inventory as ci
        JOIN armory_item as ai
            ON ci.item_id = ai.item_id
        WHERE ci.character_id = {row[0]}
        """
        sqlite_conn = pipeline.connect_to_sqlite()
        item_data = pipeline.execute_query(sqlite_conn, query)
        items = []
        for item_row in item_data:
            item_dict = {
                'name': item_row[0],
                'value': item_row[1],
                'weight': item_row[2],
            }
            items.append(item_dict)
        d = {
            'character_id': row[0], 
            'name': row[1],
            'level': row[2],
            'exp': row[3],
            'hp': row[4],
            'strength': row[5],
            'intelligence': row[6],
            'dexterity': row[7],
            'wisdom': row[8],
            'items': items,
        }
        result.append(d)
    return result


# # insert a person into the database
# db.person.insert_one({'name': 'bob'})

# # access a specific person and the details associated with that person. 
# doc = db.person.find_one({'name': 'bob'})
# print(doc)

if __name__ == '__main__':
    # connect to sqlite
    sqlite_conn = pipeline.connect_to_sqlite()
    # query sqlite
    rpg_data = pipeline.execute_query(sqlite_conn, queries.select_all )
    # transform rpg data
    rpg_dicts = tuples_to_dicts(rpg_data)
    # connect to mongo 
    db = create_mdb_conn()
    # Delete existing table
    # pipeline.execute_query(sqlite_conn, DROP_CHARACTER_TABLE)
    # insert rpg data into mongo
    db.character.insert_many(rpg_dicts)
    # db.character.delete_many({})
