from .sqllite import SQLite
from .requests import *
from ..animals.animal import *


class ManagerDataDB:
    _animals: list[Animal]

    def __init__(self):
        """Инициализирует менеджер БД"""
        self._animals = []

    def get_full_data_animals_db(self):
        """Получает данные о животных с бд"""
        with SQLite('nursery.db') as cur:
            self._animals += self._get_specific_kind_animals_db(
                cur, Dog,
                REQUESTS_SELECT['all_dogs'],
                REQUESTS_SELECT['food_dogs'],
                REQUESTS_SELECT['command_dogs'],
            )
            self._animals += self._get_specific_kind_animals_db(
                cur, Cat,
                REQUESTS_SELECT['all_cats'],
                REQUESTS_SELECT['food_cats'],
                REQUESTS_SELECT['command_cats'],
            )
            self._animals += self._get_specific_kind_animals_db(
                cur, Hamster,
                REQUESTS_SELECT['all_hamsters'],
                REQUESTS_SELECT['food_hamsters'],
                REQUESTS_SELECT['command_hamsters'],
            )
            self._animals += self._get_specific_kind_animals_db(
                cur, Horse,
                REQUESTS_SELECT['all_horses'],
                REQUESTS_SELECT['food_horses'],
                REQUESTS_SELECT['command_horses'],
            )
            self._animals += self._get_specific_kind_animals_db(
                cur, Camel,
                REQUESTS_SELECT['all_camels'],
                REQUESTS_SELECT['food_camels'],
                REQUESTS_SELECT['command_camels'],
            )
            self._animals += self._get_specific_kind_animals_db(
                cur, Donkey,
                REQUESTS_SELECT['all_donkeys'],
                REQUESTS_SELECT['food_donkeys'],
                REQUESTS_SELECT['command_donkeys'],
            )

        return self._animals

    def _get_specific_kind_animals_db(self, cur, obj: type[Animal], req_all_animals: str, req_food: str, req_cmd: str):
        """Получает из базы животных конктретного вида"""
        foods = cur.execute(req_food).fetchall()
        commands = cur.execute(req_cmd).fetchall()
        query = cur.execute(req_all_animals)

        animals = []
        for animal in query.fetchall():
            eats = [food for ID, *food in foods if animal[0] == ID]
            cmds = [cmd for ID, *cmd in commands if animal[0] == ID]
            animals.append(obj(*animal, foods=eats, commands=cmds))

        return animals

    def get_list_available_commands_db(self):
        """Получает список доступных команд"""
        with SQLite('nursery.db') as cur:
            return cur.execute(REQUESTS_SELECT['menu_commands']).fetchall()

    def get_list_available_foods_db(self):
        """Получает список доступной еды"""
        with SQLite('nursery.db') as cur:
            return cur.execute(REQUESTS_SELECT['menu_foods']).fetchall()

        