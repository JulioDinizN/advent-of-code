blocks = open("input.txt").read().split("\n\n")

def solution_part_01():
    locks = []
    keys = []
    
    for block in blocks:
        grid = list(zip(*block.splitlines()))
        if grid[0][0] == "#":
            locks.append([row.count("#") - 1 for row in grid])
        else:
            keys.append([row.count("#") - 1 for row in grid])

    total = 0
    
    for lock in locks:
        for key in keys:
           if all(x + y <= 5 for x, y in zip(lock, key)):
               total += 1
    
    print("Anwser Part One", total)

solution_part_01()
