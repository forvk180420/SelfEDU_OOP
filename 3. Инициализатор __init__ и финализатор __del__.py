"""
__init__(self) - инициализатор объекта класса
__del__(self0  - финализатор (деструктор) класса
"""


class Point:
    "Класс для представления координат точек на плоскости"
    color = 'red'  # переменные внутри класса - это его атрибуты или свойства
    circle = 2

    def __init__(self):
        print('вызов init')
        self.x = 0
        self.y = 0

    def set_exmp(sefl):  # self - ссылка на экземпляр класса
        print('вызов метода set_coords')
        print(str(sefl))

    def set_coords(sefl, x, y):  # self - ссылка на экземпляр класса
        sefl.x = x  # Создаем 2 локальных свойства
        sefl.y = y


"После создания объекта автоматически вызывается магический метод init"
pt = Point()  # вызов init

"При создании экземпляра класса можно инициализировать сразу со значениями a и b"


class Point2:
    def __init__(self, a, b):
        print('вызов init')
        self.x = a
        self.y = b

    def __del__(self):
        """Метод срабатывает после уничтожения (завершения) экземпляра класса.
        Происходит это в том случае, если "сборщик мусора" не находит внешнюю ссылку на объект
        """
        print('Удаление экземпляра: '+ str(self))


pt2 = Point2(1, 2)
