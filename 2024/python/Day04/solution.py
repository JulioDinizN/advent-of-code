grid = open("input.txt").read().splitlines()
rowSize = len(grid)
colSize = len(grid[0])


def solution_part_01():
    wordCount = 0

    for row in range(rowSize):
        for col in range(colSize):
            if grid[row][col] != "X":
                continue

            # U can use either variations that check all 8 directions
            # for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == dc == 0:
                        continue
                    if not (
                        0 <= row + 3 * dr < rowSize and 0 <= col + 3 * dc < colSize
                    ):
                        continue
                    if (
                        grid[row + dr][col + dc] == "M"
                        and grid[row + 2 * dr][col + 2 * dc] == "A"
                        and grid[row + 3 * dr][col + 3 * dc] == "S"
                    ):
                        wordCount += 1

    print("Anwser Part One", wordCount)


def solution_part_02():
    wordCount = 0

    for row in range(1, rowSize - 1):
        for col in range(1, colSize - 1):
            if grid[row][col] != "A":
                continue
            corners = [
                grid[row - 1][col - 1],
                grid[row - 1][col + 1],
                grid[row + 1][col + 1],
                grid[row + 1][col - 1],
            ]

            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                wordCount += 1

    print("Anwser Part Two", wordCount)


solution_part_01()
solution_part_02()
