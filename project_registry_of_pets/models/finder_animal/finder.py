class Finder:
    """Класс поисковика"""
    def __init__(self, animals):
        """Инициализирует поисковика"""
        self._animals = animals
        self._id = self._input()

    def _input(self):
        """Вводит id для поиска животного"""
        try:
            num_id = int(input('Введите id животного: '))
        except ValueError:
            return -1
        
        if len(self._animals) < num_id <= 0:
            return -1
        
        return num_id
    
    def find_animal_id(self):
        """Ищет животного"""
        try:
            return next(filter(lambda x: x.get_common_id() == self._id, self._animals))
        except StopIteration:
            return 0

