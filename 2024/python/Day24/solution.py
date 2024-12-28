inputs, connections = [
    value.splitlines() for value in open("input.txt").read().split("\n\n")
]


def solution_part_01():
    known = {}
    formulas = {}

    operators = {
        "OR": lambda x, y: x | y,
        "AND": lambda x, y: x & y,
        "XOR": lambda x, y: x ^ y,
    }

    def calc(wire):
        if wire in known:
            return known[wire]
        op, x, y = formulas[wire]
        known[wire] = operators[op](calc(x), calc(y))
        return known[wire]

    for line in inputs:
        x, y = line.split(": ")
        known[x] = int(y)

    for line in connections:
        x, op, y, z = line.replace("->", " ").split()
        formulas[z] = (op, x, y)

    i = 0
    z = []

    while True:
        key = "z" + str(i).rjust(2, "0")
        if key not in formulas:
            break
        z.append(calc(key))
        i += 1

    print("Anwser Part One", int("".join(map(str, z[::-1])), 2))


def solution_part_02():
    pass


solution_part_01()
solution_part_02()
