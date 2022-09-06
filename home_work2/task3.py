numbers = list(range(1, int(input("Введите занчение n: "))+1))
numbers_d = {}
for i in numbers:
    numbers_d[i] = round((1 + (1/i))**i, 2)
print(numbers_d)
    