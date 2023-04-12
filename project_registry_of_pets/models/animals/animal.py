class Animal:
    """Класс животного"""

    def __init__(self, name: str, foods: list, birthday: str):
        """Инициализирует атрибуты животного"""
        self._name = name
        self._foods = foods
        self._birthday = birthday

    def execute_command(self):
        """Выполняет команду"""

    def get_info(self):
        """Получает информацию о животном"""


class Pet(Animal):
    """Класс домашнего животного"""

    def __init__(self, name: str, foods: list, birthday: str, aggression: bool, breed: str):
        """Инициализирует атрибуты домашнего животного"""
        super().__init__(name, foods, birthday)
        self._aggression = aggression
        self._breed = breed

    def improve_mood(self):
        """Поднимает настроение"""

    def reduce_stress(self):
        """Уменьшает стресс"""


class Dog(Pet):
    """Класс собаки"""

    def __init__(self, name: str, foods: list, birthday: str, aggression: bool, breed: str, mind: int, smell: str):
        """Инициализирует атрибуты собаки"""
        super().__init__(name, foods, birthday, aggression, breed)
        self._mind = mind
        self._smell = smell

    def execute_command(self):
        """Выполняет команду"""

    def howl(self):
        """Выть"""


class Cat(Pet):
    """Класс кошки"""

    def __init__(self, name: str, foods: list, birthday: str, aggression: bool, breed: str, vision: str):
        """Инициализирует атрибуты кошки"""
        super().__init__(name, foods, birthday, aggression, breed)
        self._vision = vision

    def execute_command(self):
        """Выполняет команду"""

    def sleep(self):
        """Спать"""

    def tear_up_wallpaper(self):
        """Рвать обои"""


class Hamster(Pet):
    """Класс хомяка"""

    def execute_command(self):
        """Выполняет команду"""

    def run_on_the_wheel(self):
        """Бежать в колесе"""

    def inflate_cheeks(self):
        """Дуть щеки"""


class PackAnimal(Animal):
    """Класс вьючного животного"""

    def __init__(self, name: str, foods: list, birthday: str, strong: int, breed: str):
        """Инициализирует атрибуты вьючного животного"""
        super().__init__(name, foods, birthday)
        self._strong = strong
        self._breed = breed

    def carry_the_weight(self):
        """Нести вес"""


class Horse(PackAnimal):
    """Класс лошади"""

    def __init__(self, name: str, foods: list, birthday: str, strong: int, breed: str, personality: str):
        super().__init__(name, foods, birthday, strong, breed)
        self._personality = personality

    def execute_command(self):
        """Выполняет команду"""


class Camel(PackAnimal):
    """Класс верблюда"""

    def __init__(self, name: str, foods: list, birthday: str, strong: int, breed: str, count_humps: int):
        super().__init__(name, foods, birthday, strong, breed)
        self.count_humps = count_humps

    def execute_command(self):
        """Выполняет команду"""


class Donkey(PackAnimal):
    """Класс осла"""

    def execute_command(self):
        """Выполняет команду"""
