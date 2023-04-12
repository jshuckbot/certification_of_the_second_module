from .animals.animal import Animal


class RegistryOfPets:
    """Класс реестра домашних животных"""

    _animals: list[Animal]

    def __init__(self):
        """Инициализирует реестр домашних животных"""
        self._animals = []

    def add_animal(self, value):
        """Добавляет животного в реестр"""

    def add_command_animal(self):
        """Добавляет команду животному"""

    def get_commands_animal(self):
        """Получает все команды животного"""
