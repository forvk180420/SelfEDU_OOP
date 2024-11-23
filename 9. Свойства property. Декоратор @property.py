"""Сеттеры и геттеры класса необходимо использовать для работы с приватными свойствами.
Чтобы упростить работу с ними, существует надстройка property, которая оборачивает сеттер и геттер."""


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)


p = Person('Ivan', 20)
print(p.get_old())  # 20 (получение значения через геттер)
print(p.old)  # 20 (получение значения через property (old в этом случае)
p.old = 35  # присвоение значения через property
print(p.old)  # 35
# Причем приоритет выполнения в случае создания атрибута с таким же названием (old в этом случае) будет за property

"""Чтобы избежать функционального дублирования, когда работать с приватными свойствами можно через геттеры и сеттеры, а 
также через объект property (old в этом случае) можно использовать декоратор @property, что чаще используют"""


class Person2:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    # Декоратор @property всегда прописывается перед геттером. Затем все имена методов должны быть одинаковыми
    # (old в этом случае)
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):  # old - одинаковое имя метода как и в геттере
        self.__old = old

    @old.deleter
    # Вызывается для удаления определенного свойства (синтаксис аналогичен геттерам и сеттерам)
    def old(self):
        del self.__old
