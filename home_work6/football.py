# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# print - Команда:Всего игр, Побед, Ничьих, Поражений, Всего очков.

import collections


def result_games(count):
    result_games = collections.defaultdict(list)

    for _ in range(count):
        team1, point1, team2, point2 = input().split(';')
        point1, point2 = int(point1), int(point2)

        if point1 == point2:
            result_games[team1].append(1)
            result_games[team2].append(1)
            continue

        if point1 > point2:
            result_games[team1].append(3)
            result_games[team2].append(0)
        else:
            result_games[team1].append(0)
            result_games[team2].append(3)

    return result_games


def print_result(results: dict):

    for team, point in results.items():
        games = len(point)
        wins = point.count(3)
        draws = point.count(1)
        loses = point.count(0)
        total = sum(point)
        print(f'{team}: {games} {wins} {draws} {loses} {total}')


def main():
    count = int(input('Количество завершенных игр: '))
    results = result_games(count)
    print_result(results)


if __name__ == '__main__':
    main()
