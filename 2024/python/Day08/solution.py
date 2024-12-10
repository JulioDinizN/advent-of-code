grid = list(map(list, open("input.txt").read().splitlines()))


def solution_part_01():
    antennas = {}

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            element = grid[row][col]
            if element != ".":
                if element not in antennas:
                    antennas[element] = []
                antennas[element].append((row, col))

    antinodes = set()
    
    for array in antennas.values():
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                r1, c1 = array[i]
                r2, c2 = array[j]
                antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                antinodes.add((2 * r2 - r1, 2 * c2 - c1))
                
    validAntinodes = len([0 for r, c in antinodes if 0 <= r < len(grid) and 0 <= c < len(grid[0])])
    
    print("Anwser Part One", validAntinodes)


def solution_part_02():
    antennas = {}

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            element = grid[row][col]
            if element != ".":
                if element not in antennas:
                    antennas[element] = []
                antennas[element].append((row, col))

    antinodes = set()
    
    for array in antennas.values():
        for i in range(len(array)):
            for j in range(len(array)):
                if i == j: continue
                r1, c1 = array[i]
                r2, c2 = array[j]
                
                dr = r2 - r1
                dc = c2 - c1
                
                r = r1
                c = c1

                while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    antinodes.add((r, c))
                    r += dr
                    c += dc
                
    validAntinodes = len([0 for r, c in antinodes if 0 <= r < len(grid) and 0 <= c < len(grid[0])])
    
    print("Anwser Part Two", validAntinodes)


solution_part_01()
solution_part_02()
