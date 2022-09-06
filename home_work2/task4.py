num = int(input("Введити число n: "))
numbers = [int(i) for i in range(-num, num+1)]
product = 1

with open('home_work2/values.txt', 'r') as file:
    array = file.read().splitlines()

for index in array:
    product *= numbers[int(index)]

print(product)