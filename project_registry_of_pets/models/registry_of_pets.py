from .animals.animal import Animal
from .managerdb.managerdb import ManagerDataDB


class RegistryOfPets:
    """Класс реестра домашних животных"""
    _animals: list[Animal]

    def __init__(self):
        """Инициализирует реестр домашних животных"""
        self.managerdb = ManagerDataDB()
        self._animals = self.managerdb.get_full_data_animals_db()

    def add_animal(self, value):
        """Добавляет животного в реестр"""
        self._animals.append(value)

    def add_command_animal(self):
        """Добавляет команду животному"""

    def get_commands_animal(self):
        """Получает все команды животного"""

    def get_animals(self):
        """Получает спислок животных"""
        return self._animals

