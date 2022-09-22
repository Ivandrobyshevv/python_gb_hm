from parser import rpn

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '*': lambda x, y: x * y,
    '/': lambda x, y: y / x,
    '**': lambda x, y: y ** x
}


def main():
    # Инициализировать пустой стек и получить выражение RPN пользователя, разбитое на токены
    stack, tokens = [], rpn(input("Введите выражение: "))
    for token in tokens:
        if token in OPERATORS:
            # Работа с двумя верхними числами в стеке
            res = OPERATORS[token](stack.pop(), stack.pop())
            stack.append(res)
        else:
            # Мы столкнулись с числом: поместите его на вершину стека
            stack.append(float(token))
    return stack[0]


if __name__ == '__main__':
    print(main())
