DROP DATABASE IF EXISTS human_friends_db;
CREATE DATABASE human_friends_db;
USE human_friends_db;


-- Команды
DROP TABLE IF EXISTS commands;
CREATE TABLE commands(
    id SERIAL PRIMARY KEY,
    command VARCHAR(150) UNIQUE COMMENT 'Команда'
) COMMENT = 'Все команды';


DROP TABLE IF EXISTS foods;
CREATE TABLE foods(
    id SERIAL PRIMARY KEY,
    food VARCHAR(150) COMMENT 'Еда'
) COMMENT = 'Еда';


-- Категории животных
DROP TABLE IF EXISTS category_animals;
CREATE TABLE category_animals(
    id SERIAL PRIMARY KEY,
    category VARCHAR(200) UNIQUE COMMENT 'Категория'
) COMMENT = 'Категории животных';


-- Еда
DROP TABLE IF EXISTS foods;
CREATE TABLE foods(
    id SERIAL PRIMARY KEY,
    food VARCHAR(150) COMMENT 'Еда'
) COMMENT = 'Еда';


-- Собаки 
DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL COMMENT 'Имя собаки',
    mind TINYINT UNSIGNED COMMENT 'Интеллект',
    smell VARCHAR(150) COMMENT 'Обоняние',
    aggression BOOLEAN COMMENT 'Агрессия',
    breed VARCHAR(200) COMMENT 'Порода',
    birthday_at DATE COMMENT 'Дата рождения',
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория',
    FOREIGN KEY (category_animals_id) REFERENCES category_animals(id) ON UPDATE CASCADE ON DELETE SET NULL   
) COMMENT = 'Собаки';


DROP TABLE IF EXISTS dogs_commands;
CREATE TABLE dogs_commands(
    id SERIAL PRIMARY KEY,
    dog_id BIGINT UNSIGNED NOT NULL,
    command_id BIGINT UNSIGNED,
    FOREIGN KEY (dog_id) REFERENCES dogs(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON UPDATE CASCADE ON DELETE SET NULL  
) COMMENT = 'Команды собак';


DROP TABLE IF EXISTS dogs_foods;
CREATE TABLE dogs_foods(
    id SERIAL PRIMARY KEY,
    dog_id BIGINT UNSIGNED NOT NULL,
    food_id BIGINT UNSIGNED,
    FOREIGN KEY (dog_id) REFERENCES dogs(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES foods(id) ON UPDATE CASCADE ON DELETE SET NULL  
) COMMENT = 'Еда собак';


-- Кошки
DROP TABLE IF EXISTS cats;
CREATE TABLE cats(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL COMMENT 'Имя кошки',
    vision TINYINT UNSIGNED COMMENT 'Зрение',
    aggression BOOLEAN COMMENT 'Агрессия',
    breed VARCHAR(200) COMMENT 'Порода',
    birthday_at DATE COMMENT 'Дата рождения',
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория',
    FOREIGN KEY (category_animals_id) REFERENCES category_animals(id) ON UPDATE CASCADE ON DELETE SET NULL
) COMMENT = 'Кошки';


DROP TABLE IF EXISTS cats_commands;
CREATE TABLE cats_commands(
    id SERIAL PRIMARY KEY,
    cat_id BIGINT UNSIGNED NOT NULL,
    command_id BIGINT UNSIGNED,
    FOREIGN KEY (cat_id) REFERENCES cats(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Команды кошек';


DROP TABLE IF EXISTS cats_foods;
CREATE TABLE cats_foods(
    id SERIAL PRIMARY KEY,
    cat_id BIGINT UNSIGNED NOT NULL,
    food_id BIGINT UNSIGNED,
    FOREIGN KEY (cat_id) REFERENCES cats(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES foods(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Еда кошек';


-- Хомяки
DROP TABLE IF EXISTS hamsters;
CREATE TABLE hamsters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL COMMENT 'Имя хомяка',
    aggression BOOLEAN COMMENT 'Агрессия',
    breed VARCHAR(200) COMMENT 'Порода',
    birthday_at DATE COMMENT 'Дата рождения',
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория',
    FOREIGN KEY (category_animals_id) REFERENCES category_animals(id) ON UPDATE CASCADE ON DELETE SET NULL
) COMMENT = 'Хомяки';


DROP TABLE IF EXISTS hamsters_commands;
CREATE TABLE hamsters_commands(
    id SERIAL PRIMARY KEY,
    hamster_id BIGINT UNSIGNED NOT NULL,
    command_id BIGINT UNSIGNED,
    FOREIGN KEY (hamster_id) REFERENCES hamsters(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Команды хомяков';


DROP TABLE IF EXISTS hamsters_foods;
CREATE TABLE hamsters_foods(
    id SERIAL PRIMARY KEY,
    hamster_id BIGINT UNSIGNED NOT NULL,
    food_id BIGINT UNSIGNED,
    FOREIGN KEY (hamster_id) REFERENCES hamsters(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES foods(id) ON UPDATE CASCADE ON DELETE SET NULL   
) COMMENT = 'Еда хомяков';


-- Лошади
DROP TABLE IF EXISTS horses;
CREATE TABLE horses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL COMMENT 'Имя лошади',
    strong BOOLEAN COMMENT 'Сила',
    breed VARCHAR(200) COMMENT 'Порода',
    personality VARCHAR(200) COMMENT 'Характер',
    birthday_at DATE COMMENT 'Дата рождения',
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория',
    FOREIGN KEY (category_animals_id) REFERENCES category_animals(id) ON UPDATE CASCADE ON DELETE SET NULL
) COMMENT = 'Лошади';


DROP TABLE IF EXISTS horses_commands;
CREATE TABLE horses_commands(
    id SERIAL PRIMARY KEY,
    horse_id BIGINT UNSIGNED NOT NULL,
    command_id BIGINT UNSIGNED,
    FOREIGN KEY (horse_id) REFERENCES horses(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Команды лошадей';


DROP TABLE IF EXISTS horses_foods;
CREATE TABLE horses_foods(
    id SERIAL PRIMARY KEY,
    horse_id BIGINT UNSIGNED NOT NULL,
    food_id BIGINT UNSIGNED,
    FOREIGN KEY (horse_id) REFERENCES horses(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES foods(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Еда лошадей';


-- Верблюды
DROP TABLE IF EXISTS camels;
CREATE TABLE camels(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL COMMENT 'Имя верблюда',
    strong BOOLEAN COMMENT 'Сила',
    breed VARCHAR(200) COMMENT 'Порода',
    count_humps TINYINT UNSIGNED COMMENT 'Количество горбов',
    birthday_at DATE COMMENT 'Дата рождения',
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория',
    FOREIGN KEY (category_animals_id) REFERENCES category_animals(id) ON UPDATE CASCADE ON DELETE SET NULL
) COMMENT = 'Верблюды';


DROP TABLE IF EXISTS camels_commands;
CREATE TABLE camels_commands(
    id SERIAL PRIMARY KEY,
    camel_id BIGINT UNSIGNED NOT NULL,
    command_id BIGINT UNSIGNED,
    FOREIGN KEY (camel_id) REFERENCES camels(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Команды верблюдов';


DROP TABLE IF EXISTS camels_foods;
CREATE TABLE camels_foods(
    id SERIAL PRIMARY KEY,
    camel_id BIGINT UNSIGNED NOT NULL,
    food_id BIGINT UNSIGNED,
    FOREIGN KEY (camel_id) REFERENCES camels(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES foods(id) ON UPDATE CASCADE ON DELETE SET NULL   
) COMMENT = 'Еда верблюдов';


-- Ослы
DROP TABLE IF EXISTS donkeys;
CREATE TABLE donkeys(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL COMMENT 'Имя осла',
    strong BOOLEAN COMMENT 'Сила',
    breed VARCHAR(200) COMMENT 'Порода',
    birthday_at DATE COMMENT 'Дата рождения',
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория',
    FOREIGN KEY (category_animals_id) REFERENCES category_animals(id) ON UPDATE CASCADE ON DELETE SET NULL   
) COMMENT = 'Ослы';


DROP TABLE IF EXISTS donkeys_commands;
CREATE TABLE donkeys_commands(
    id SERIAL PRIMARY KEY,
    donkey_id BIGINT UNSIGNED NOT NULL,
    command_id BIGINT UNSIGNED,
    FOREIGN KEY (donkey_id) REFERENCES donkeys(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Команды ослов';


DROP TABLE IF EXISTS donkeys_foods;
CREATE TABLE donkeys_foods(
    id SERIAL PRIMARY KEY,
    donkey_id BIGINT UNSIGNED NOT NULL,
    food_id BIGINT UNSIGNED,
    FOREIGN KEY (donkey_id) REFERENCES donkeys(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES foods(id) ON UPDATE CASCADE ON DELETE SET NULL 
) COMMENT = 'Еда ослов';
