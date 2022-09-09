def get_binary(num):
    """Преобразовывает десятичное число в двоичное"""
    binary = bin(num)
    return binary





def main():
    num = int(input("Введите число: "))
    binary = get_binary(num)
    return int(str(binary)[2:])
   


if __name__ == '__main__':
    print(main())
