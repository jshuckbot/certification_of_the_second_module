from models.menu.menu import *
from models.registry_of_pets import RegistryOfPets
from models.finder_animal.finder import Finder


class Controller:
    """Класс контроллера"""
    def __init__(self):
        """Инициализирует контроллер"""
        self._menu = Menu()
        self._menu.show_menu()
        self._menu.input()
        self._manager_animals = RegistryOfPets()

    def run(self):
        """Запускает приложение"""
        while True:
            self._select_menu()

    def _select_menu(self):
        self._menu = self._menu.select_menu()
        
        if isinstance(self._menu, tuple):
            animal, self._menu = self._menu
            self._manager_animals.add_animal(animal)
        elif self._menu == SHOW_COMMANDS:
            print(self._find_animal_from_id().get_commands())
        elif self._menu == SHOW_FOODS:
            print(self._find_animal_from_id().get_foods())
        elif self._menu == ADD_COMMAND:
            animal = self._find_animal_from_id()
            self._menu = MenuAddListCommand(animal)
        elif self._menu == ADD_FOOD:
            animal = self._find_animal_from_id()
            self._menu = MenuAddListFood(animal)
        elif self._menu == SHOW_ANIMALS:
            self._manager_animals.show_animals()
            self._menu = Menu()

        self._menu.show_menu()
        self._menu.input()

    def _find_animal_from_id(self):
        animal = Finder(self._manager_animals.get_animals()).find_animal_id()
        if not animal:
            print('Такого животного в питомнике нет')
        
        self._menu = Menu()
        return animal
