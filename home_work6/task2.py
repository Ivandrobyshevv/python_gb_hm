from random import randint as ri

size = int(input('Введите размер списка: '))

numbers = [ri(0, 10) for i in range(size)]
unique = [i for i in numbers if numbers.count(i) < 2]
print(f'Начальный список: {numbers}')
print(f'Уникальные значения: {unique}')
