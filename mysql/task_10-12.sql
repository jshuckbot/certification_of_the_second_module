 USE human_friends_db;
 
/* Задание 10
 * Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. 
 * Объединить таблицы лошади, и ослы в одну таблицу. 
 */
 

SELECT * FROM camels;

DELETE FROM camels;

SELECT * FROM camels;


DROP TABLE IF EXISTS hourses_donkeys;
CREATE TABLE hourses_donkeys (
    id SERIAL PRIMARY KEY,
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория'
)
SELECT
    h.name,
    h.breed,
    h.birthday_at,
    h.category_animals_id 
FROM horses h 
UNION
SELECT 
    d.name,
    d.breed,
    d.birthday_at,
    d.category_animals_id 
FROM donkeys d;


ALTER TABLE hourses_donkeys
ADD FOREIGN KEY(category_animals_id)
REFERENCES category_animals(id)
ON UPDATE CASCADE ON DELETE SET NULL;

SELECT * FROM hourses_donkeys;


/* Задание 11
 * Создать новую таблицу “молодые животные” 
 * в которую попадут все животные старше 1 года, но младше 3 лет и в отдельном столбце
 *с точностью до месяца подсчитать возраст животных в новой таблице
 */

DROP TABLE IF EXISTS young_animals;
CREATE TABLE young_animals (
    id SERIAL PRIMARY KEY,
    category_animals_id BIGINT UNSIGNED COMMENT 'Категория',
    age DECIMAL(3,2)
)
SELECT  
    d.name,
    d.breed,
    d.birthday_at,
    d.category_animals_id,
    ROUND(datediff (CURDATE(), d.birthday_at)/365, 2) as age
FROM  dogs d
WHERE TIMESTAMPDIFF(YEAR, d.birthday_at, CURDATE()) BETWEEN 1 AND 3
UNION  
SELECT 
    c.name,
    c.breed,
    c.birthday_at,
    c.category_animals_id,
    ROUND(datediff (CURDATE(), c.birthday_at)/365, 2) as age
FROM  cats c 
WHERE TIMESTAMPDIFF(YEAR, c.birthday_at, CURDATE()) BETWEEN 1 AND 3
UNION 
SELECT
    h.name,
    h.breed,
    h.birthday_at,
    h.category_animals_id,
    ROUND(datediff (CURDATE(), h.birthday_at)/365, 2) as age
FROM hamsters h 
WHERE TIMESTAMPDIFF(YEAR, h.birthday_at, CURDATE()) BETWEEN 1 AND 3
UNION 
SELECT 
    hr.name,
    hr.breed,
    hr.birthday_at,
    hr.category_animals_id,
    ROUND(datediff (CURDATE(), hr.birthday_at)/365, 2) as age
FROM horses hr 
WHERE TIMESTAMPDIFF(YEAR, hr.birthday_at, CURDATE()) BETWEEN 1 AND 3
UNION 
SELECT 
    cm.name,
    cm.breed,
    cm.birthday_at,
    cm.category_animals_id,
    ROUND(datediff (CURDATE(), cm.birthday_at)/365, 2) as age
FROM camels cm 
WHERE TIMESTAMPDIFF(YEAR, cm.birthday_at, CURDATE()) BETWEEN 1 AND 3
UNION 
SELECT 
    dk.name,
    dk.breed,
    dk.birthday_at,
    dk.category_animals_id,
    ROUND(datediff (CURDATE(), dk.birthday_at)/365, 2) as age
FROM donkeys dk
WHERE TIMESTAMPDIFF(YEAR, dk.birthday_at, CURDATE()) BETWEEN 1 AND 3;
    
ALTER TABLE young_animals
ADD FOREIGN KEY(category_animals_id)
REFERENCES category_animals(id)
ON UPDATE CASCADE ON DELETE SET NULL;

SELECT * FROM young_animals;


/* Задание 12
 * Объединить все таблицы в одну, при этом сохраняя поля, 
 * указывающие на прошлую принадлежность к старым таблицам. 
 */

SELECT * FROM cats c 
LEFT JOIN dogs d 
USING(id)
LEFT JOIN hamsters h 
USING (id)
LEFT JOIN  horses hr  
USING (id)
LEFT JOIN  camels cm  
USING (id)
LEFT JOIN  donkeys dk
USING (id);
