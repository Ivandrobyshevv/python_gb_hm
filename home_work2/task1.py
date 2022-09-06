num = input("Введите вещественное число: ")
numbers = [int(i) for i in num if i not in ',.']
print(f'{num} -> {sum(numbers)}')