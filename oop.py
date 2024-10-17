from abc import abstractmethod, ABC
# from itertools import count
from random import choice
from math import ceil


class Animals(ABC):
    def __init__(self, name: str, age: int, voice: str, weight: float):
        self.__name = name
        self.__voice = voice
        self.age = age
        self.weight = weight

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    name = property(get_name, set_name)

    @property
    def voice_command(self) -> str:
        # различать по голосам
        return self.__voice

    @voice_command.setter
    def voice_command(self, new_voice: str) -> None:
        self.__voice = new_voice

    @abstractmethod
    def daily_norm_eat(self) -> int:
        pass


class Cat(Animals):
    __count = 0

    def __init__(self, age: int, voice: str, weight: float, name: str = 'нет имени'):
        super().__init__(name, age, voice, weight)
        self.__name = name
        self.voice = voice
        self.age = age
        self.weight = weight

        Cat.__count += 1

    # метод помогает подобрать кличку(потом с помощью сеттера можно поменять)
    @staticmethod
    def choice_name() -> str:
        names = ["Мурка", "Барсик", "Рыжик", "Бусинка", "Матильда", "Леопольд", "Васька", "Симба", "Кузя", "Карамелька"]
        return choice(names)

    @staticmethod
    def count_cats() -> int:
        return Cat.__count

    # расчет суточной нормы корма исходя из веса
    def daily_norm_eat(self) -> int:
        if self.weight < 2:
            eat = 1.4 * (70 * self.weight ** 0.75)
        else:
            eat = 1.4 * (30 * self.weight + 70)
        return ceil(eat)


class Dog(Animals):
    __count = 0

    def __init__(self, age: int, voice: str, weight: int, name: str = 'нет имени'):
        super().__init__(name, age, voice, weight)

        Dog.__count += 1

    @staticmethod
    def choice_name() -> str:
        names = ['Шарик', 'Рекс', 'Барбос', 'Тузик', 'Бублик', 'Белка', 'Жучка', 'Снежок', 'Масяня', 'Зорька']
        return choice(names)

    @staticmethod
    def count_dogs() -> int:
        return Dog.__count

    # расчет суточной нормы корма исходя из веса
    def daily_norm_eat(self) -> int:

        if self.weight < 2:
            eat = 2 * (70 * self.weight ** 0.75)
        else:
            eat = 2 * (30 * self.weight + 70)
        return ceil(eat)


cat1 = Cat(22, 'Мяу', 3.5)
print(cat1.daily_norm_eat())
print(cat1.voice_command)
print(Cat.count_cats())
print(cat1.get_name())
cat1.set_name('Кошкаа')
print(cat1.get_name())
cat1.set_name(Cat.choice_name())
print(cat1.get_name())

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
