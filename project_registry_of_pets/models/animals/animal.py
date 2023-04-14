class Counter:
    def __init__(self):
        self.num = 0


class Animal:
    """Класс животного"""
    _ID = 0
    _common_id = 0
    _counter = Counter()

    def __init__(self, num_id: int, name: str,  birthday: str, category_animals_id: int, foods: list, commands: list):
        """Инициализирует атрибуты животного"""
        Animal._counter.num += 1
        if num_id is None:
            self.__class__._ID += 1
        else:
            self.__class__._ID = num_id
        self._common_id = Animal._counter.num
        self._name = name
        self._birthday = birthday
        self.category_animals_id = category_animals_id
        self._foods = foods
        self._commands = commands

    def execute_command(self):
        """Выполняет команду"""

    def get_info(self):
        """Получает информацию о животном"""

    def __repr__(self):
        """Вывод животного"""
        return f'Общий id: {self._common_id}. Вид: {self.__class__.__name__}. Имя: {self._name}. Еда: {self._foods} Комманды: {self._commands}'

    def add_food_to_ration(self, item_id: int, item_food: str):
        """Добавляет еду в рацион"""
        for id_food, _ in self._foods:
            if id_food == item_id:
                return 'Такую еда есть в рационе!'
        self._foods.append((item_id, item_food))
        return 'Еда в рацион добавлена!'

    def memorize_the_command(self, item_id: int, item_command: str):
        """Обучает новой команде """
        for id_cmd, _ in self._commands:
            if id_cmd == item_id:
                return 'Такая команда изучена!'
        self._commands.append((item_id, item_command))
        return 'Команда животному добавлена!'

    def get_id(self):
        """Получает id из таблицы животного"""
        return self.__class__._ID

    def get_common_id(self):
        """Получает общий id из питомника животного"""
        return self._common_id

    def get_commands(self):
        """Получает команды животного"""
        return f'Вид:{self.__class__.__name__}. Имя: {self._name.title()}. список команд: {self._commands}'

    def get_foods(self):
        """Получает рацион питания животного"""
        return f'Вид:{self.__class__.__name__}. Имя: {self._name.title()}. Рацион питания: {self._foods}'


class Pet(Animal):
    """Класс домашнего животного"""

    def __init__(self, num_id=None, name='', aggression=False,
                 breed='', birthday='0000-01-01', category_animals_id=1, foods='', commands=''):
        """Инициализирует атрибуты домашнего животного"""
        super().__init__(num_id, name, birthday, category_animals_id, foods, commands)
        self._aggression = aggression
        self._breed = breed

    def improve_mood(self):
        """Поднимает настроение"""

    def reduce_stress(self):
        """Уменьшает стресс"""


class Dog(Pet):
    """Класс собаки"""
    _ID = 0

    def __init__(self, num_id=None, name='', mind=0, smell='', aggression=True,
                 breed='',  birthday='1970-02-01', category_animals_id=1, foods='', commands=''):
        """Инициализирует атрибуты собаки"""
        super().__init__(num_id, name, aggression, breed, birthday, category_animals_id, foods, commands)
        self._mind = mind
        self._smell = smell

    def execute_command(self):
        """Выполняет команду"""

    def howl(self):
        """Выть"""


class Cat(Pet):
    """Класс кошки"""

    def __init__(self, num_id=None, name='', vision=0, aggression=True,
                 breed='', birthday='0000-01-01', category_animals_id=1, foods='', commands=''):
        """Инициализирует атрибуты кошки"""
        super().__init__(num_id, name, aggression, breed, birthday, category_animals_id, foods, commands)
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

    def __init__(self, num_id=None, name='', strong=100, breed='',
                 birthday='0000-01-01', category_animals_id=2, foods='', commands=''):
        """Инициализирует атрибуты вьючного животного"""
        super().__init__(num_id, name, birthday, category_animals_id, foods, commands)
        self._strong = strong
        self._breed = breed

    def carry_the_weight(self):
        """Нести вес"""


class Horse(PackAnimal):
    """Класс лошади"""

    def __init__(self, num_id=None, name='', strong=80, breed='', personality='',
                 birthday='0000-01-01', category_animals_id=2, foods='', commands=''):
        super().__init__(num_id, name, strong, breed, birthday, category_animals_id, foods, commands)
        self._personality = personality

    def execute_command(self):
        """Выполняет команду"""


class Camel(PackAnimal):
    """Класс верблюда"""

    def __init__(self, num_id=None, name='', strong=0, breed='', count_humps=2,
                 birthday='0000-01-01', category_animals_id=2, foods='', commands=''):
        super().__init__(num_id, name, strong, breed, birthday, category_animals_id, foods, commands)
        self.count_humps = count_humps

    def execute_command(self):
        """Выполняет команду"""


class Donkey(PackAnimal):
    """Класс осла"""

    def execute_command(self):
        """Выполняет команду"""
