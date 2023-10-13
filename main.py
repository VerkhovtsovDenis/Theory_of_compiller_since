def exception_factory(exception, message):
    return exception(message)


class Language:
    def __init__(self, file_path=None, value=None):
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.readlines()
                self.value = list(map(str, [c.rstrip() for c in data]))

            except ValueError:
                raise exception_factory(ValueError, 'Файл с данными заполнен неверно')
            return
        if value:
            self.value = value
            return

    def __mul__(self, other):

        if not isinstance(other, Language):
            raise exception_factory(TypeError, 'Неверное применение оператора конкатинации')

        result = []

        for _ in self.value:
            result.append(f'{_}')

        for __ in other.value:
            result.append(f'{__}')

        for _ in self.value:
            for __ in other.value:
                c = f'{_}{__}'
                if not (c in result):
                    result.append(c)

        return Language(value=result)

    def __str__(self):
        out_str = ''
        n = len(self.value)

        for i in range(n-1):
            out_str += f'{self.value[i]}, '
        out_str += self.value[n-1]

        return out_str

if __name__ == '__main__':
    path_1 = r'C:\Users\verkhovtcov.do\PycharmProjects\тяпик\дз_1\hw\L1'
    path_2 = r'C:\Users\verkhovtcov.do\PycharmProjects\тяпик\дз_1\hw\L2'

    L1 = Language(path_1)
    L2 = Language(path_2)

    L3 = L1*L2

    print(f'Koncat ({L1}) and ({L2}) is ({L3})')


