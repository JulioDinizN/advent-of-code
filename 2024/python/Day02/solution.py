lines = open("input.txt").read().split("\n")


def isSafe(levels):
    diffs = list()

    # or diffs = [x - y for x, y in zip(levels, levels[1:])]
    for index in range(len(levels) - 1):
        currNum = int(levels[index])
        nextNum = int(levels[index + 1])
        diffs.append(currNum - nextNum)

    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)


def solution_part_01():
    safeReports = 0

    for line in lines:
        nums = line.split()
        levels = list(map(int, nums))

        if isSafe(levels):
            safeReports += 1

    print("Anwser Part One", safeReports)


def solution_part_02():
    safeReports = 0

    for line in lines:
        nums = line.split()
        levels = list(map(int, nums))

        if any(
            isSafe(levels[:index] + levels[index + 1 :]) for index in range(len(levels))
        ):
            safeReports += 1

    print("Anwser Part Two", safeReports)


solution_part_01()
solution_part_02()
