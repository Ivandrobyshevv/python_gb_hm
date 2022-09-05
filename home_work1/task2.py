
def write_num():
    x = int(input('Введите значение x: '))
    y = int(input('Введите значение y: '))
    z = int(input('Введите значение z: '))
    return [x, y, z]


def predicate(values):
    left_statement = not(values[0] or values[1] or values[2])
    right_statement = not values[0] and not values[1] and not values[2]
    result = left_statement == right_statement
    return result

    
if __name__ == '__main__':
    if predicate(write_num()) == True:
        print("Утверждение верно!")
    else: print("Утверждение неверно!")