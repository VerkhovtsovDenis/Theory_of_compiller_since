def exception_factory(exception, message):
    return exception(message)


class Language:
    def __init__(self, value=None):
        self.value = value

    def __mul__(self, other):
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

        for i in range(n - 1):
            out_str += f'{self.value[i]}, '
        out_str += self.value[n - 1]

        return out_str
