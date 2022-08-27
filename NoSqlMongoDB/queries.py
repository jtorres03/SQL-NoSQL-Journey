select_all = """
SELECT *
FROM charactercreator_character;
"""

TOTAL_CHARACTERS = """
select count(character_id)
from charactercreator_character;
""" 

TOTAL_NECROMANCERS = """
SELECT count(*)
FROM charactercreator_necromancer
"""

TOTAL_MAGE = """
SELECT count(*)
FROM charactercreator_mage
"""

TOTAL_THIEF = """
SELECT count(*)
FROM charactercreator_character as c
JOIN charactercreator_thief as t
"""

TOTAL_ARMORY_ITEMS = """
SELECT count(*)
FROM armory_item
"""

TOTAL_WEAPONS = """
SELECT count(*)
FROM armory_weapon
"""

TOTAL_NON_WEAPONS = """
SELECT count(DISTINCT item_id)
FROM charactercreator_character_inventory
LEFT JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.power IS NULL
"""

ITEMS_PER_CHARACTER = """
SELECT charactercreator_character_inventory.character_id, count(charactercreator_character_inventory.item_id)
FROM charactercreator_character_inventory
JOIN armory_item
ON charactercreator_character_inventory.item_id= armory_item.item_id
GROUP by charactercreator_character_inventory.character_id
LIMIT 20
"""

WEAPONS_PER_CHARACTER = """
SELECT character_id, count(character_id)
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP by character_id
LIMIT 20
"""

AVG_ITEMS_PER_CHARACTER = """
SELECT avg(total_items)
FROM (SELECT charactercreator_character_inventory.character_id, count(charactercreator_character_inventory.item_id) as total_items
FROM charactercreator_character_inventory
JOIN armory_item
ON charactercreator_character_inventory.item_id= armory_item.item_id
GROUP by charactercreator_character_inventory.character_id)
"""
AVG_WEAPONS_PER_CHARACTER = """
SELECT avg(total_weapons)
FROM (SELECT character_id, count(character_id) as total_weapons
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP by character_id)
"""

QUERY_LIST = [ITEMS_PER_CHARACTER,
              WEAPONS_PER_CHARACTER,
              ITEMS_PER_CHARACTER,
              TOTAL_ARMORY_ITEMS,
              TOTAL_CHARACTERS,
              TOTAL_NON_WEAPONS,
              TOTAL_WEAPONS,
              TOTAL_THIEF,
              TOTAL_MAGE,
              TOTAL_CHARACTERS,
              AVG_WEAPONS_PER_CHARACTER,
              AVG_ITEMS_PER_CHARACTER
              ]

GET_CHARACTER = """
SELECT * 
FROM charactercreator_character;
"""

create_character_table = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
);
"""
