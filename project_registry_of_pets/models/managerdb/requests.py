REQUESTS_SELECT = {}

# Выборка все животных из БД
REQUESTS_SELECT['all_dogs'] = """SELECT * FROM dogs;"""
REQUESTS_SELECT['all_cats'] = """SELECT * FROM cats;"""
REQUESTS_SELECT['all_hamsters'] = """SELECT * FROM hamsters;"""
REQUESTS_SELECT['all_horses'] = """SELECT * FROM horses;"""
REQUESTS_SELECT['all_camels'] = """SELECT * FROM camels;"""
REQUESTS_SELECT['all_donkeys'] = """SELECT * FROM donkeys;"""


# Выборка еды которую едят животные
REQUESTS_SELECT['food_dogs'] = """
SELECT 
    d.id,
    f.id,
    f.food 
FROM dogs_foods df
JOIN dogs d 
ON  df.dog_id = d.id
JOIN 
foods f 
ON df.food_id = f.id;
"""

REQUESTS_SELECT['food_cats'] = """
SELECT 
    c.id,
    f.id,
    f.food 
FROM cats_foods cf 
JOIN cats c 
ON cf.cat_id = c.id 
JOIN 
foods f 
ON cf.food_id = f.id;
"""

REQUESTS_SELECT['food_hamsters'] = """
SELECT 
    h.id,
    f.id,
    f.food 
FROM hamsters_foods hf 
JOIN hamsters h 
ON hf.hamster_id = h.id 
JOIN 
foods f 
ON hf.food_id = f.id;
"""

REQUESTS_SELECT['food_horses'] = """
SELECT 
    h.id,
    f.id,
    f.food 
FROM horses_foods hf 
JOIN horses h 
ON hf.horse_id = h.id 
JOIN foods f 
ON hf.food_id = f.id;
"""

REQUESTS_SELECT['food_camels'] = """
SELECT 
    c.id,
    f.id,
    f.food 
FROM camels_foods cf
JOIN camels c 
ON cf.camel_id = c.id 
JOIN foods f 
ON cf.food_id = f.id;
"""

REQUESTS_SELECT['food_donkeys'] = """
SELECT 
    d.id,
    f.id,
    f.food 
FROM donkeys_foods df 
JOIN donkeys d 
ON df.donkey_id = d.id 
JOIN foods f 
ON df.food_id =f.id;
"""

# выборка комманд каждого животного
REQUESTS_SELECT['command_dogs'] = """
SELECT 
    d.id,
    c.id,
    c.command 
FROM dogs_commands dc 
JOIN dogs d 
ON dc.dog_id = d.id
JOIN commands c 
ON dc.command_id = c.id;
"""
REQUESTS_SELECT['command_cats'] = """
SELECT 
    c.id,
    cmd.id,
    cmd.command
FROM cats_commands cc 
JOIN cats c
ON cc.cat_id = c.id 
JOIN commands cmd 
ON cc.command_id = cmd.id;
"""
REQUESTS_SELECT['command_hamsters'] = """
SELECT 
    h.id,
    c.id,
    c.command 
FROM hamsters_commands hc 
JOIN hamsters h 
ON hc.hamster_id = h.id 
JOIN commands c 
ON hc.command_id = c.id;
"""
REQUESTS_SELECT['command_horses'] = """
SELECT 
    h.id,
    c.id,
    c.command 
FROM horses_commands hc 
JOIN horses h 
ON hc.horse_id = h.id
JOIN commands c 
ON hc.command_id = c.id;
"""
REQUESTS_SELECT['command_camels'] = """
SELECT 
    c.id,
    cmd.id,
    cmd.command 
FROM camels_commands cc 
JOIN camels c
ON cc.camel_id = c.id
JOIN commands cmd
ON cc.command_id = cmd.id;
"""
REQUESTS_SELECT['command_donkeys'] = """
SELECT 
    d.id,
    c.id,
    c.command 
FROM donkeys_commands dc 
JOIN donkeys d 
ON dc.donkey_id = d.id 
JOIN commands c 
ON dc.command_id = c.id;
"""

# Выборка для меню
REQUESTS_SELECT['menu_foods'] = """SELECT id, food FROM foods;"""
REQUESTS_SELECT['menu_commands'] = """SELECT id, command FROM commands;"""
