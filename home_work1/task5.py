from math import sqrt
def distance_search_2D(a1, a2, b1 ,b2):
    distance = sqrt(((b1 - a1)**2) + ((b2 - a2)**2))
    return f'A ({a1},{a2}; B ({b1},{b2}) -> {round(distance, 2)}'
    
        


def main():
    a1, a2 = map(int, (input('Введите координату точки А: ')).split(','))
    b1, b2 = map(int, (input('Введите координату точки B: ')).split(','))
    print(distance_search_2D(a1, a2, b1, b2))

if __name__ == '__main__':
    main()