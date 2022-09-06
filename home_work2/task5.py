
def mixing(numbers):
    from random import randint

    for i in range(len(numbers)):
        rand = randint(0, len(numbers)-1)
        numbers[i] = numbers[rand]
    
    return numbers

def main():
    numbers = [i for i in range(1, int(input("Введите размер списка: ")) + 1)]
    print(f'Старый список - {numbers}')
    new_numbers = mixing(numbers)
    print(f'Новый список - {new_numbers}')

if __name__ == '__main__':
    main()