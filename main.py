import unittest
from LanguageHandTest import LanguageHandTest
from LanguageAutoTest import LanguageAutoTest
from Language import Language

LanguageHandTest()
LanguageAutoTest()

TESTING = True


def main():
    l1, l2, _ = LanguageHandTest.readfile()

    # result - результат выполнения конкатенации программой
    result = (Language(value=l1) * Language(value=l2)).value

    print(result)


if __name__ == '__main__':
    if TESTING:
        unittest.main()
    else:
        main()

