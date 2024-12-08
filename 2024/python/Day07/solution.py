inputValue = open("input.txt").read().splitlines()


def parseLine(line):
    target, numbers = line.split(":")
    # or [int(x) for x in numbers.split()]
    return (int(target), list(map(int, numbers.split())))


def solution_part_01():
    def possible_values(numbers):
        if len(numbers) == 1:
            return {numbers[0]}
        subset = possible_values(numbers[:-1])
        return {x + numbers[-1] for x in subset} | {x * numbers[-1] for x in subset}

    anserTotal = 0

    for line in inputValue:
        target, numbers = parseLine(line)
        if target in possible_values(numbers):
            anserTotal += target

    print("Anwser Part One", anserTotal)


def solution_part_02():
    def possible_values(numbers):
        if len(numbers) == 1:
            return {numbers[0]}
        subset = possible_values(numbers[:-1])
        return (
            {x + numbers[-1] for x in subset}
            | {x * numbers[-1] for x in subset}
            | {int(str(x) + str(numbers[-1])) for x in subset}
        )

    anserTotal = 0

    for line in inputValue:
        target, numbers = parseLine(line)
        if target in possible_values(numbers):
            anserTotal += target

    print("Anwser Part Two", anserTotal)


solution_part_01()
solution_part_02()
