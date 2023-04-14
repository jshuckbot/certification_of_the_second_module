class Creator:
    """Класс создателя животного"""
    _data = {}
    
    def __init__(self, animal):
        """Иницилизирует создателя"""
        self._data = self.__class__._data.copy()
        self._input()
        self._animal = animal
        self._animal = self._create()

    
    def _input(self):
        """Вводит данные о собаке"""
        for attr, text in self._data.items():
            if attr != 'category_animals_id':
                self._data[attr] = input(text)
    
    def _create(self):
        """Создает животного"""
        return self._animal(**self._data, foods=[], commands=[])
    
    def get_animal(self):
        """Получает объект животного"""
        return self._animal
        

class CreatorDog(Creator):
    """Класс создателя собаки"""
    _data = {
        'name': 'Введите имя: ',
        'mind': 'Введите уровень интелекта (1-100): ',
        'smell': 'Введите уровень нюха (низкий|средний|высокий): ',
        'aggression': 'Введите показатель агрессии (да|нет): ',
        'breed': 'Введите породу собаки: ',
        'birthday': 'Введите день рождения: ',
        'category_animals_id': '1',
    }


class CreatorCat(Creator):
    """Класс создателя кошки"""
    _data = {
        'name': 'Введите имя: ',
        'vision': 'Введите уровень зрения (1-100): ',
        'aggression': 'Введите показатель агрессии (да|нет): ',
        'breed': 'Введите породу кошки: ',
        'birthday': 'Введите день рождения: ',
        'category_animals_id': '1',
    }
    

class CreatorHamster(Creator):
    """Класс создателя хомяка"""
    _data = {
        'name': 'Введите имя: ',
        'aggression': 'Введите показатель агрессии (да|нет): ',
        'breed': 'Введите породу хомяка: ',
        'birthday': 'Введите день рождения: ',
        'category_animals_id': '1',
    }


class CreatorHorse(Creator):
    """Класс создателя лошади"""
    _data = {
        'name': 'Введите имя: ',
        'strong': 'Введите силу: ',
        'breed': 'Введите породу лошади: ',
        'personality': 'Введите характер лошади: ',
        'birthday': 'Введите день рождения: ',
        'category_animals_id': '2',
    }


class CreatorCamel(Creator):
    """Класс создателя верблюда"""
    _data = {
        'name': 'Введите имя: ',
        'strong': 'Введите силу: ',
        'breed': 'Введите породу верблюда: ',
        'count_humps': 'Введите количество горбов: ',
        'birthday': 'Введите день рождения: ',
        'category_animals_id': '2',
    }


class CreatorDonkey(Creator):
    """Класс создателя осла"""
    _data = {
        'name': 'Введите имя: ',
        'strong': 'Введите силу: ',
        'breed': 'Введите породу осла: ',
        'birthday': 'Введите день рождения: ',
        'category_animals_id': '2',
    }
