USE human_friends_db;

    
-- Команды домашних животных
INSERT INTO commands
(command)
VALUES
    ('сидеть'),
    ('лежать'),
    ('голос'),
    ('снять стресс'),
    ('поднять настроение');
    
-- Команды вьючных животных
INSERT INTO commands
(command)
VALUES
    ('нести'),
    ('бежать'),
    ('прыжок');
    
-- Категории животных
INSERT INTO category_animals
(category)
VALUES
    ('домашние'),
    ('вьючные');


-- еда животных
INSERT INTO foods
(food)
VALUES
    ('корм'),
    ('мясо'),
    ('мыши'),
    ('молоко'),
    ('трава'),
    ('сено'),
    ('орехи'),
    ('семечки'),
    ('укроп'),
    ('петрушка'),
    ('верблюжья колючка'),
    ('полынь');


-- Собаки
INSERT INTO dogs
(name, mind, smell, aggression, breed, birthday_at, category_animals_id)
VALUES
    ('лейла', 80, 'чуткий', FALSE, 'хаски', '2017-07-03', 1),
    ('джери', 90, 'чуткий', FALSE, 'немецкая овчарка', '2008-05-12', 1),
    ('мадонна', 50, 'средний', TRUE, 'той-терьер', '2020-11-12', 1),
    ('ричард', 70, 'чуткий', TRUE, 'Ротвейлер', '2022-01-01', 1);


-- Команды собак
INSERT INTO dogs_commands
(dog_id, command_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 2),
    (3, 3),
    (4, 1);

-- Еда собак
INSERT INTO dogs_foods
(dog_id, food_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 4),
    (2, 2),
    (3, 1),
    (4, 1),
    (4, 2);



-- Кошки
INSERT INTO cats
(name, vision, aggression, breed, birthday_at, category_animals_id)
VALUES
    ('соня', 100, TRUE, 'британская', '2016-10-22', 1),
    ('феня', 100, TRUE, 'сиамская', '2022-01-10', 1),
    ('ферзь', 100, TRUE, 'мейн-кун', '2020-04-27', 1);

-- Команды кошек
INSERT INTO cats_commands
(cat_id, command_id)
VALUES
    (1, 4),
    (2, 4),
    (2, 5),
    (3, 5);

-- Еда кошек
INSERT INTO cats_foods
(cat_id, food_id)
VALUES
    (1, 3),
    (2, 3),
    (2, 4),
    (3, 4),
    (3, 5);



-- Хомяки
INSERT INTO hamsters
(name, aggression, breed, birthday_at, category_animals_id)
VALUES
    ('тютя', FALSE, 'Сирийские', '2022-09-13', 1),
    ('виктор', TRUE, 'Кэмпбелл', '2021-03-20', 1);

-- Команды хомяков
INSERT INTO hamsters_commands
(hamster_id, command_id)
VALUES
    (1, 4),
    (1, 5),
    (2, 5);


-- Еда хомяков
INSERT INTO hamsters_foods
(hamster_id, food_id)
VALUES
    (1, 7),
    (1, 8),
    (1, 9),
    (2, 8),
    (2, 9);




-- Лошади
INSERT INTO horses
(name, strong, breed, personality, birthday_at, category_animals_id)
VALUES
    ('чемп', 90, 'мустанг', 'шальной', '2020-11-26', 2),
    ('нокс', 100, 'першерон', 'спокойный', '2022-06-29', 2),
    ('сява', 40, 'пони', 'добрый', '2019-03-03', 2);


-- Команды лошадей
INSERT INTO horses_commands
(horse_id, command_id)
VALUES
    (1, 6),
    (1, 7),
    (2, 8),
    (2, 6),
    (3, 7);


-- Еда лошадей
INSERT INTO horses_foods
(horse_id, food_id)
VALUES
    (1, 5),
    (1, 6),
    (2, 5),
    (3, 5),
    (3, 6);



-- Верблюды
INSERT INTO camels
(name, strong, breed, count_humps, birthday_at, category_animals_id)
VALUES
    ('афоня', 95, 'бактриан', 2, '2012-01-01', 2),
    ('граф', 85, 'дромадер', 1, '2016-03-07', 2),
    ('гуффи', 87, 'бактриан', 2, '2017-12-01', 2);


-- Команды верблюдов
INSERT INTO camels_commands
(camel_id, command_id)
VALUES
    (1, 6),
    (1, 8),
    (2, 7),
    (2, 6),
    (3, 6);


-- Еда верблюдов
INSERT INTO camels_foods
(camel_id, food_id)
VALUES
    (1, 11),
    (1, 12),
    (2, 11),
    (3, 11),
    (3, 12);



-- Ослы
INSERT INTO donkeys
(name, strong, breed, birthday_at, category_animals_id)
VALUES
    ('чича', 25, 'пиренейский', '2023-01-01', 2),
    ('гога', 40, 'каталонский', '2009-02-11', 2);


-- Команды ослов
INSERT INTO donkeys_commands
(donkey_id, command_id)
VALUES
    (1, 8),
    (1, 7),
    (2, 8);


-- Еда ослов
INSERT INTO donkeys_foods
(donkey_id, food_id)
VALUES
    (1, 5),
    (2, 6),
    (2, 5);
