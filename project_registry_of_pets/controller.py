from models.menu.menu import *
from models.registry_of_pets import RegistryOfPets
from models.finder_animal.finder import Finder


class Controller:
    """Класс контроллера"""
    def __init__(self):
        """Инициализирует контроллер"""
        self.menu = Menu()
        self.menu.show_menu()
        self.menu.input()
        self.manager_animals = RegistryOfPets()

    def run(self):
        """Запускает приложение"""
        while True:
            self._select_menu()

    def _select_menu(self):
        self.menu = self.menu.select_menu()
        
        if isinstance(self.menu, tuple):
            animal, self.menu = self.menu
            print(animal)
            self.manager_animals.add_animal(animal)
        elif self.menu == SHOW_COMMANDS:
            print(self._find_animal_from_id().get_commands())
        elif self.menu == SHOW_FOODS:
            print(self._find_animal_from_id().get_foods())
        elif self.menu == ADD_COMMAND:
            animal = self._find_animal_from_id()
            self.menu = MenuAddListCommand(animal)
        elif self.menu == ADD_FOOD:
            animal = self._find_animal_from_id()
            self.menu = MenuAddListFood(animal)
            
        self.menu.show_menu()
        self.menu.input()

    def _find_animal_from_id(self):
        animal = Finder(self.manager_animals.get_animals()).find_animal_id()
        if not animal:
            print('Такого животного в питомнике нет')
        
        self.menu = Menu()
        return animal
