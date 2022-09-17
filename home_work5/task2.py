from random import randint, choice


names_bot = ['Лена_bot', 'Ваня_bot', 'Сергй_bot', 'Мария_bot']
CANDIES = 2021
MAX_CANDIE = 28


def game_pve(user1, user2):
    candis = CANDIES
    Flag = False

    if user1 in names_bot:
        candis = CANDIES
        while candis != 0:
            c_user2 = MAX_CANDIE + 1

            if candis < MAX_CANDIE:
                c_user1 = candis
            else:
                c_user1 = candis % MAX_CANDIE + 1

            print(f'{user1} взял {c_user1} конфет')
            candis -= c_user1
            Flag = True

            if candis == 0:
                break

            while c_user2 > MAX_CANDIE:
                print(f'Всего {candis} конфет')
                print(f"(Можно взять не больше {MAX_CANDIE} конфет)")
                c_user2 = int(input(f'{user2.title()} сколько конфет возьмете: '))
                if c_user2 > MAX_CANDIE:
                    print(f'(Вы взяли больше {c_user2}, а это больше {MAX_CANDIE} конфет!!!!)')
                    continue
                else:
                    candis -= c_user2

        return Flag
    else:
        while candis > 0:
            c_user1 = 29
            while c_user1 > MAX_CANDIE:
                print(f'У вас лежат {candis}')
                print(f"(Можно взять не больше {MAX_CANDIE} конфет)")
                c_user1 = int(input(f'{user1.title()} сколько конфет возьмете: '))
                if c_user1 > 28:
                    print(f'(Вы взяли больше {c_user1}, а это больше {MAX_CANDIE} конфет!!!!)')
                    continue
                else:
                    candis -= c_user1
            c_user2 = candis % 29
            if c_user2 == 0:
                c_user2 = randint(1, 28)
            print(f'{user2} взял {c_user2} конфет')
            candis -= c_user2


def game_pvp(user1, user2):
    Flag = False
    candis = CANDIES
    while candis > 0:
        c_user1 = 29
        c_user2 = 29
        while c_user1 > 28:
            print(f'У вас лежат {candis}')
            print("(Можно взять не больше 28 конфет)")
            c_user1 = int(input(f'{user1.title()} сколько конфет возьмете: '))
            if c_user1 > 28:
                print(f'(Вы взяли больше {c_user1}, а это больше 28 конфет!!!!)')
                continue
            else:
                candis -= c_user1
                Flag = True
        if candis == 0:
            break
        while c_user2 > 28:
            print(f'У вас лежат {candis}')
            print("(Можно взять не больше 28 конфет)")
            c_user2 = int(input(f'{user2.title()} сколько конфет возьмете: '))
            if c_user2 > 28:
                print(f'(Вы взяли больше {c_user2}, а это больше 28 конфет!!!!)')
                continue
            else:
                candis -= c_user2
    return Flag


def main():
    win = None
    print(f"""На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем {MAX_CANDIE} конфет. Все конфеты оппонента достаются сделавшему последний ход.
-----------------------------------------------------------------------------------------------------------""")
    print("1. PvP Режим\n2. PvE режим")
    mode = input("Выберите режим (1 | 2)\n>> ")
    if mode == '1':
        name_user1 = input("Введите имя первого игрока: ")
        name_user2 = input("Введите имя второго игрока: ")
        if randint(0, 1) == 0:
            print(f"Первый ходит - {name_user1.title()}")
            win = game_pvp(name_user1, name_user2)
        else:
            print(f"Первый ходит - {name_user2.title()}")
            win = game_pvp(name_user2, name_user1)

        if win:
            return f'Победил {name_user1}'
        return f'Победил {name_user2}'

    else:
        name_user = input("Введите свое имя: ")
        name_bot = choice(names_bot)

        if randint(0, 1) == 0:
            print(f"Первый ходит - {name_user.title()}")
            win = game_pve(name_user, name_bot)
        else:
            print(f"Первый ходит - {name_bot.title()}")
            win = game_pve(name_bot, name_user)
    if win:
        return f'Победил {name_user}'
    return f'Победил {name_bot}'


if __name__ == '__main__':
    print(main())
