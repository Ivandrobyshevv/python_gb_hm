def get_prime_numbers(num):
    """Простые числа до числа num"""
    prime_numbers = list()

    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers


def get_prime_multiplier(prime_numbers, num):
    """Простые множители"""
    result = list()

    for p_number in prime_numbers:
        if num % p_number == 0:
            result.append(p_number)
    return result


def main():
    """Главная функция"""
    while True:
        num = int(input("Введите натуральное число N:\n>> "))
        prime_numbers = get_prime_numbers(num)
        result = get_prime_multiplier(prime_numbers, num)
        print(result)
        stop = input("Повторить операцию (y|n)?\n>> ")
        if stop.lower() == 'n':
            print("--------")
            break
            

if __name__ == '__main__':
    main()
