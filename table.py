import random
import itertools


class Table:
    VAR_NAMES = ["X", "Y", "Z", "W"]
    VAR_ID = {"X": 0, "Y": 1, "Z": 2, "W": 3}

    def __init__(self, arg_cnt=3, func_value=[]):
        """
        Инициализация объекта - таблицы истиности
        Можно передать значения функции в виде списка, где каждое число (0 или 1) означает 0 или 1 в таблици истинности
        для значений функции начиная с наибольшего (т.е. если 3 переменные, то для 111 110 101 ...)
        """
        self.arg_cnt = arg_cnt
        if func_value:
            self.__set_table(arg_cnt, func_value)
        else:
            self.__set_random_table(arg_cnt)

    @staticmethod
    def __generate_table(arg_cnt, func_value) -> list:
        """Генерация таблицы по значению функции и количеству неизвестных"""
        table = []
        i = 0
        for arg_values in itertools.product('10', repeat=arg_cnt):
            table += [(tuple(map(int, arg_values)), func_value[i])]
            i += 1
        return table

    def __set_table(self, arg_cnt, func_value):
        """Задаёт таблицу по значению функции и количеству неизвестных в таблице"""
        self.table = self.__generate_table(arg_cnt, func_value)

    def __set_random_table(self, arg_cnt):
        """Задаёт случайнею таблицу по количеству неизвестных в этой таблице"""
        func_value = [random.randint(0, 1) for _ in range(2 ** arg_cnt)]
        self.__set_table(arg_cnt, func_value)

    def show(self):
        """Отображение таблицы"""
        for i in range(self.arg_cnt):
            print(f'| {self.VAR_NAMES[i]} ', end='')
        print('| A |')

        for i in self.table:
            for j in i[0]:
                print(f'| {j} ', end='')
            print(f'| {i[1]} |')
