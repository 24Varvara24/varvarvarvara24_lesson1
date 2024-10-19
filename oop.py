from abc import abstractmethod, ABC
from random import choice
from math import ceil


class Animals(ABC):
    def __init__(self, name: str, age: int, voice: str, weight: float, disease='заболеваний нет'):
        self.__name = name
        self.__voice = voice
        self.age = age
        self.weight = weight
        self._disease = disease

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    name = property(get_name, set_name)

    @property
    def voice_command(self) -> str:
        return self.__voice

    @voice_command.setter
    def voice_command(self, new_voice: str) -> None:
        self.__voice = new_voice

    @abstractmethod
    def daily_norm_eat(self) -> int:
        pass

    @abstractmethod
    def medical_examination(self) -> str:
        pass

    def get_disease(self) -> str:
        return self._disease

    def set_disease(self, new: str = 'заболеваний нет') -> None:
        self._disease = new

    property(get_disease, set_disease)


class Cat(Animals):
    __count = 0

    def __init__(self, age: int, voice: str, weight: float, name: str = 'нет имени', disease='заболеваний нет'):
        super().__init__(name, age, voice, weight, disease)

        Cat.__count += 1

    def medical_examination(self) -> str:
        diseases_list = [
            "Вирусный лейкоз кошек (FeLV)",
            "Иммунодефицит кошек (FIV)",
            "Хроническая болезнь почек",
            "Диабет",
            "Гастроэнтерит",
            "Панкреатит",
            "Инфекционный перитонит кошек (FIP)",
            "Астма",
            "Аллергии",
            "Кожные инфекции"
        ]
        if choice([0, 1]) == 0:
            self._disease = 'заболеваний нет'
        else:
            self._disease = choice(diseases_list)

        return f'был проведен медицинский осмотр,результат: {self._disease}'

    # метод помогает подобрать кличку(потом с помощью сеттера можно поменять)
    @staticmethod
    def choice_name() -> str:
        names = ["Мурка", "Барсик", "Рыжик", "Бусинка", "Матильда", "Леопольд", "Васька", "Симба", "Кузя", "Карамелька"]
        return choice(names)

    @staticmethod
    def count_cats() -> int:
        return Cat.__count

    def daily_norm_eat(self) -> str:
        if self.weight < 2:
            eat = 1.4 * (70 * self.weight ** 0.75)
        else:
            eat = 1.4 * (30 * self.weight + 70)
        return f"суточная норма корма для кошки составляет {ceil(eat)}гр на {self.weight}кг"


class Dog(Animals):
    __count = 0

    def __init__(self, age: int, voice: str, weight: float, name: str = 'нет имени', disease='заболеваний нет'):
        super().__init__(name, age, voice, weight, disease)

        Dog.__count += 1

    @staticmethod
    def choice_name() -> str:
        names = ['Шарик', 'Рекс', 'Барбос', 'Тузик', 'Бублик', 'Белка', 'Жучка', 'Снежок', 'Масяня', 'Зорька']
        return choice(names)

    @staticmethod
    def count_dogs() -> int:
        return Dog.__count

    def daily_norm_eat(self) -> str:

        if self.weight < 2:
            eat = 2 * (70 * self.weight ** 0.75)
        else:
            eat = 2 * (30 * self.weight + 70)
        return f"суточная норма корма для собаки составляет {ceil(eat)}гр на {self.weight}кг"

    def medical_examination(self) -> str:
        diseases_list = [
            "Паравирус",
            "Бешенство",
            "Лимфома",
            "Дисплазия тазобедренного сустава",
            "Сердечные заболевания",
            "Инфекционный гепатит",
            "Кожные инфекции",
            "Аллергии",
            "Эпилепсия",
            "Диабет"
        ]
        if choice([0, 1]) == 0:
            self._disease = 'заболеваний нет'
        else:
            self._disease = choice(diseases_list)

        return f'был проведен медицинский осмотр,результат: {self._disease}'


cat1 = Cat(22, 'Мяу', 3.5)
print(cat1.daily_norm_eat())
print(cat1.voice_command)
print(Cat.count_cats())
print(cat1.get_name())
cat1.set_name('Кошкаа')
print(cat1.get_name())
cat1.set_name(Cat.choice_name())
print(cat1.get_name())
print(cat1.get_disease())
cat1.set_disease('ушной клещ')
print(cat1.get_disease())
print(cat1.medical_examination())

print('-' * 15)

dog1 = Dog(22, 'Гав', 3.5)
dog2 = Dog(22, 'Гав', 3.5)
print(dog1.daily_norm_eat())
print(dog1.voice_command)
print(Dog.count_dogs())
print(dog1.get_name())
dog1.set_name('Собачкаа')
print(dog1.get_name())
dog1.set_name(Dog.choice_name())
print(dog1.get_name())
print(dog1.get_disease())
dog1.set_disease('лишай')
print(dog1.get_disease())
print(dog1.medical_examination())
