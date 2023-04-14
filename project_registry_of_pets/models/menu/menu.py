import sys
from ..managerdb.managerdb import ManagerDataDB
from ..animals.animal import *
from ..creator_animals.creator import *

SHOW_COMMANDS = 'show commands'
SHOW_ANIMALS = 'show animals'
SHOW_FOODS = 'show foods'
ADD_COMMAND = 'add command'
ADD_FOOD = 'add food'

class Menu:
    _menu = {
        '1': 'Завести новое животное',
        '2': 'Просмотреть список команд которые выполняет животное',
        '3': 'Просмотреть рацион питания животного',
        '4': 'Обучить командам животное',
        '5': 'Добавить новую еду в рацион животному',
        '6': 'Показать всех животных',
        '0': 'Выход',
    }
    
    _item = 0
    
    def show_menu(self):
        for k, v in self._menu.items():
            print(k, v)
            
    def select_menu(self):
        """Выбирает пункт меню"""
        match self._item:
            case 1: return MenuAddAnimal()
            case 2: return SHOW_COMMANDS
            case 3: return SHOW_FOODS
            case 4: return ADD_COMMAND
            case 5: return ADD_FOOD
            case 6: return SHOW_ANIMALS
            case 0: sys.exit()
            case _: return Menu()
            
    def input(self):
        try:
            self._item = int(input('Выберите пункт меню: '))
        except ValueError:
            self._item = -1



class MenuAddAnimal(Menu):
    _menu = {
        '1': 'Домашнее животное',
        '2': 'Вьючное животное',
        '0': 'Выход',
    }
    
    def select_menu(self):
        """Выбирает пункт меню"""
        match self._item:
            case 1: return MenuAddPetsAnimal()
            case 2: return MenuAddPackAnimal()
            case 0: sys.exit()
            case _: return Menu()
    

class MenuAddPetsAnimal(Menu):
    """Класс меню добавляет домашнего животного"""
    _menu = {
        '1': 'Собака',
        '2': 'Кошка',
        '3': 'Хомяк',
        '0': 'Выход'
    }
    
    def select_menu(self):
        """Выбирает пункт меню"""
        match self._item:
            case 1:
                animal = CreatorDog(Dog)
                print(id(animal))
                animal = animal.get_animal()
                return MenuAddAninimalAddListCommand(animal)
            case 2:
                animal = CreatorCat(Cat).get_animal()
                return MenuAddAninimalAddListCommand(animal)
            case 3:
                animal = CreatorHamster(Hamster).get_animal()
                return MenuAddAninimalAddListCommand(animal)
            case 0: sys.exit()
            case _: return Menu()


class MenuAddPackAnimal(Menu):
    _menu = {
        '1': 'Лошадь',
        '2': 'Верблюд',
        '3': 'Осел',
        '0': 'Выход',
    }
    
    def select_menu(self):
        """Выбирает пункт меню"""
        match self._item:
            case 1:
                animal = CreatorHorse(Horse).get_animal()
                return MenuAddAninimalAddListCommand(animal)
            case 2:
                animal = CreatorCamel(Camel).get_animal()
                return MenuAddAninimalAddListCommand(animal)
            case 3:
                animal = CreatorDonkey(Donkey).get_animal()
                return MenuAddAninimalAddListCommand(animal)
            case 0: sys.exit()
            case _: return Menu()


class MenuAddListCommand(Menu):
    """Класс меню добавить доступные комманды к существующему животному"""
    def __init__(self, animal):
        self._animal = animal
        self._menu = self.get_commands()
        
    def get_commands(self):
        return dict(ManagerDataDB().get_list_available_commands_db())
    
    def select_menu(self):
        if self._item > len(self._menu):
            return Menu()
        pair = filter(lambda x: x[0] == self._item, self._menu.items())
        self._animal.memorize_the_command(*next(pair))
        return Menu()
    
    def input(self):
        try:
            self._item = int(input('Выберете команду из пункта меню которой хотите обучить: '))
        except ValueError:
            self._item = len(self._menu) + 1


class MenuAddAninimalAddListCommand(MenuAddListCommand):
    """Класс меню добавить доступные комманды при добавлении животного"""
    def __init__(self, animal):
        super().__init__(animal)

    def get_commands(self):
        return dict(ManagerDataDB().get_list_available_commands_db())

    def select_menu(self):
        if self._item > len(self._menu):
            return Menu()
        pair = filter(lambda x: x[0] == self._item, self._menu.items())
        self._animal.memorize_the_command(*next(pair))
        return MenuAddListFood(self._animal)

    def input(self):
        try:
            self._item = int(input('Выберете команду из пункта меню которой хотите обучить: '))
        except ValueError:
            self._item = len(self._menu) + 1


class MenuAddListFood(Menu):
    """Класс меню добавить в рацион доступную еду"""
    def __init__(self, animal):
        self._animal = animal
        self._menu = self.get_foods()
        
    def get_foods(self):
        """Получает всю доступную еду"""
        return dict(ManagerDataDB().get_list_available_foods_db())
    
    def select_menu(self):
        if self._item > len(self._menu):
            return Menu()
        pair = filter(lambda x: x[0] == int(self._item), self._menu.items())
        self._animal.add_food_to_ration(*next(pair))
        return self._animal, Menu()

    def input(self):
        """Ввод данных"""
        try:
            self._item = int(input('Добавить в рацион еду из пункта меню: '))
        except ValueError:
            self._item = len(self._menu) + 1
