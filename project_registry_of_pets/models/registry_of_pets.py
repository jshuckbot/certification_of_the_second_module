from .animals.animal import Animal
from .managerdb.managerdb import ManagerDataDB


class RegistryOfPets:
    """Класс реестра домашних животных"""
    _animals: list[Animal]

    def __init__(self):
        """Инициализирует реестр домашних животных"""
        self._managerdb = ManagerDataDB()
        self._animals = self._managerdb.get_full_data_animals_db()

    def add_animal(self, value):
        """Добавляет животного в реестр"""
        self._animals.append(value)

    def get_animals(self):
        """Получает спислок животных"""
        return self._animals

    def show_animals(self):
        """Выводиь всех животных"""
        for animal in self._animals:
            print(animal)
