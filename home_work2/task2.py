num = int(input("Введите число N: "))
product = 1
list_product = []
for i in range(1, num+1):
    product *= i
    list_product.append(product)
print(list_product)

