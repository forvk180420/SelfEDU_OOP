"""
В названиях методов обычно используются глаголы, а в названиях свойств - существительные

self указывает (ссылается) на конкретный экземпляр класса.
Используется в методах экземпляра для работы с его атрибутами.
Без self нельзя изменять атрибуты конкретного объекта.
@classmethod использует cls, а @staticmethod не требует ни self, ни cls.

Почему нужен self?
Когда создаётся объект на основе класса, у каждого объекта должны быть свои уникальные атрибуты, но методы внутри
класса являются общими для всех экземпляров. self позволяет методам ссылаться на текущий объект и изменять или получать
 его атрибуты.
"""


class Point:
    "Класс для представления координат точек на плоскости"
    color = 'red'  # переменные внутри класса - это его атрибуты или свойства
    circle = 2

    def set_exmp(sefl):  # self - ссылка на экземпляр класса
        print('вызов метода set_exmp')
        print(str(sefl))

    def set_coords(sefl, x, y):  # self - ссылка на экземпляр класса
        sefl.x = x  # Создаем 2 локальных свойства
        sefl.y = y


pt = Point()
pt.set_exmp()  # вызов метода set_exmp \n<__main__.Point object at 0x000001DAE4A30EB0>
pt.set_coords(x=1, y=2)
print(pt.__dict__)  # {'x': 1, 'y': 2}

"Получаемые координаты x и y совершенно независимы в разных экземплярах класса"
pt2 = Point()
pt2.set_coords(x=10, y=20)
print(pt2.__dict__)  # {'x': 10, 'y': 20}
