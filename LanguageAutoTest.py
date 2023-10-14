import unittest
from Language import Language


class LanguageAutoTest(unittest.TestCase):

    def test_not_empty(self):
        """
        Тестовая ситуация, когда язык не пуст
        """
        for i in range(1, 4):
            # чтение файла с i-м тестом
            l1, l2, answer = self.readfile(i)

            # result - результат выполнения конкатенации программой
            result = (Language(value=l1) * Language(value=l2)).value
            # answer - ожидаемый результат конкатенации
            answer = Language(value=answer).value

            # проверка теста
            self.assertEqual(result, answer)


    def test_long_term(self):
        """
        Тестовая ситуация, длина терминала -> 100
        """
        for i in range(4, 9):
            # чтение файла с i-м тестом
            l1, l2, answer = self.readfile(i)

            # result - результат выполнения конкатенации программой
            result = (Language(value=l1)*Language(value=l2)).value
            # answer - ожидаемый результат конкатенации
            answer = Language(value=answer).value

            # проверка теста
            self.assertEqual(result, answer)

    def test_long_lang(self):
        """
        Тестовая ситуация, длина языка -> 1000
        """
        for i in range(9, 11):
            # чтение файла с i-м тестом
            l1, l2, answer = self.readfile(i)

            # result - результат выполнения конкатенации программой
            result = (Language(value=l1)*Language(value=l2)).value
            # answer - ожидаемый результат конкатенации
            answer = Language(value=answer).value

            # проверка теста
            self.assertEqual(result, answer)

    def test_one_is_empty(self):
        """
        Тестовая ситуация один язык пуст
        """
        for i in range(11, 12):
            # чтение файла с i-м тестом
            l1, l2, answer = self.readfile(i)

            # result - результат выполнения конкатенации программой
            result = (Language(value=l1)*Language(value=l2)).value
            # answer - ожидаемый результат конкатенации
            answer = Language(value=answer).value

            # проверка теста
            self.assertEqual(result, answer)

    def test_all_is_empty(self):
        """
        Тестовая ситуация оба языка пусты
        """
        for i in range(12, 13):
            # чтение файла с i-м тестом
            l1, l2, answer = self.readfile(i)

            # result - результат выполнения конкатенации программой
            result = (Language(value=l1)*Language(value=l2)).value
            # answer - ожидаемый результат конкатенации
            answer = Language(value=answer).value

            # проверка теста
            self.assertEqual(result, answer)

    @staticmethod
    def readfile(n):
        with open(f'tests\\test_{n}.txt') as file:
            l1 = file.readline().strip().split()
            l2 = file.readline().strip().split()
            answer = file.readline().strip().split()
        return l1, l2, answer
