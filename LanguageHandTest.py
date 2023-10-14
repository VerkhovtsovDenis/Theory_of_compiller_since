import unittest
from Language import Language


class LanguageHandTest(unittest.TestCase):
    def test_1(self):
        global PATH_TEST_FILE
        l1, l2, answer = self.readfile()

        # result - результат выполнения конкатенации программой
        result = (Language(value=l1) * Language(value=l2)).value
        # answer - ожидаемый результат конкатенации
        answer = Language(value=answer).value

        # проверка теста
        self.assertEqual(result, answer)

    @staticmethod
    def readfile():
        with open('tests\\test.txt') as file:
            l1 = file.readline().strip().split()
            l2 = file.readline().strip().split()
            answer = file.readline().strip().split()
        return l1, l2, answer
