import sqlite3 
import psycopg2
import pandas



conn = sqlite3.connect('rpg_db.sqlite3')

cur = conn.cursor()

# How many total Characters are there? 
cur.execute("SELECT COUNT(character_id) FROM charactercreator_character;")
print('There are total characters: ',cur.fetchall())


# How many of each specific subclass?
cur.execute("SELECT COUNT(character_id) FROM charactercreator_character WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_mage);")
print('Subclass mage :', cur.fetchall())

cur.execute("SELECT COUNT(character_id) FROM charactercreator_character WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_thief);")
print('Subclass thief :', cur.fetchall())

cur.execute("SELECT COUNT(character_id) FROM charactercreator_character WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_cleric);")
print('Subclass cleric :', cur.fetchall())

cur.execute("SELECT COUNT(character_id) FROM charactercreator_character WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_fighter);")
print('Subclass fighter :', cur.fetchall())


# How many total Items?
cur.execute("SELECT COUNT(item_id) FROM armory_item;")
print('There are total items:', cur.fetchall())

# How many of the Items are weapons? How many are not?
cur.execute("SELECT COUNT(item_id) FROM armory_item WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon);")
print('There are total weapons:', cur.fetchall())

cur.execute("SELECT COUNT(item_id) FROM armory_item WHERE item_id  NOT IN (SELECT item_ptr_id FROM armory_weapon);")
print('There are not weapons:', cur.fetchall())


# How many Items does each character have? (Return first 20 rows)
cur.execute("SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;")
print('In first 20 rows, each character has total items :', cur.fetchall())


# How many Weapons does each character have? (Return first 20 rows)
cur.execute("SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon) GROUP BY character_id LIMIT 20;")
print('In first 20 rows, each character has total weapons:', cur.fetchall())


# On average, how many Items does each Character have?
cur.execute("SELECT AVG(itemcount) FROM (SELECT character_id, COUNT(item_id) AS itemcount FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20);")
print('Each character has average items:', cur.fetchall())


# On average, how many Weapons does each character have?
cur.execute("SELECT AVG(weaponcount) FROM (SELECT character_id, COUNT(item_id) AS weaponcount FROM charactercreator_character_inventory WHERE item_id IN(SELECT item_ptr_id FROM armory_weapon) GROUP BY character_id LIMIT 20);")
print('Each character has average weapons:', cur.fetchall())

cur.close()














