def rpn(s):
    lex = parse(s)
    s2 = []
    r = []
    operators = ["+", "-", "*", "/", "(", ")"]
    for a in lex:
        if a == "(":
            s2 = [a] + s2
        elif a in operators:
            if s2 == []:
                s2 = [a]
            elif a == ")":
                while True:
                    q = s2[0]
                    s2 = s2[1:]
                    if q == "(":
                        break
                    r += [q]
            elif get_priority(s2[0]) < get_priority(a):
                s2 = [a] + s2
            else:
                while True:
                    if s2 == []:
                        break
                    q = s2[0]
                    r += [q]
                    s2 = s2[1:]
                    if get_priority(q) == get_priority(a):
                        break
                s2 = [a] + s2
        else:
            r += [a]
    while s2 != []:
        q = s2[0]
        r += [q]
        s2 = s2[1:]
    return r


def get_priority(o):
    if o == "+" or o == "-":
        return 1
    elif o == "*" or o == "/":
        return 2
    elif o == "(":
        return 0


def parse(string):
    operators = ["+", "-", "*", "/", "(", ")"]
    lex = []
    tmp = ""
    for elem in string:
        if elem != " ":
            if elem in operators:
                if tmp != "":
                    lex += [tmp]
                lex += [elem]
                tmp = ""
            else:
                tmp += elem
    if tmp != "":
        lex += [tmp]
    return lex
