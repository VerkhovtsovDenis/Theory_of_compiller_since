import random
import string
from Language import Language

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
    # print("Random string of length", length, "is:", rand_string)

def generate_language(count, lenght):
    res = []
    for _ in range(count):
        res.append(generate_random_string(lenght))

    return ' '.join(i for i in res)


# a = generate_language(10000, 100)
# b = generate_language(10000, 100)
a = generate_language(9999, 100)
b = generate_language(4, 2)

l1 = Language(a.strip().split())
print(9999**3)
l2 = Language(b.strip().split())
c = ' '.join(i for i in (l1*l2).value)

with open('test_10.txt', 'w') as file:
    file.write(a+'\n')
    file.write(b+'\n')
    file.write(c+'\n')





