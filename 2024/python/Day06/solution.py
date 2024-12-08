grid = list(map(list, open("input.txt").read().splitlines()))

positionsVisited = set()

def isOutOfBounds(position):
    r, c = position
    
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        return False
    else:
        return True

def safeToGo(position):
    r, c = position
    
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#':
        return True
    else:
        return False

def simulateWalk(position, char):
    r, c = position
    
    if char == '^':
        iteration = 1
        while True:
            newPosition = (r - iteration, c)
            
            if safeToGo(newPosition):
                positionsVisited.add(newPosition)
                iteration += 1
            else:
                if isOutOfBounds(newPosition):
                    return;
                else:
                    return simulateWalk((r - iteration + 1, c), ">")
    if char == '>':
        iteration = 1
        while True:
            newPosition = (r, c + iteration)
            
            if safeToGo(newPosition):
                positionsVisited.add(newPosition)
                iteration += 1
            else:
                if isOutOfBounds(newPosition):
                    return;
                else:
                    return simulateWalk((r, c + iteration - 1), "v")
                
    if char == 'v':
        iteration = 1
        while True:
            newPosition = (r + iteration, c)
            
            if safeToGo(newPosition):
                positionsVisited.add(newPosition)
                iteration += 1
            else:
                if isOutOfBounds(newPosition):
                    return;
                else:
                    return simulateWalk((r + iteration - 1, c), "<")
                
    if char == '<':
        iteration = 1
        while True:
            newPosition = (r, c - iteration)
            
            if safeToGo(newPosition):
                positionsVisited.add(newPosition)
                iteration += 1
            else:
                if isOutOfBounds(newPosition):
                    return;
                else:
                    return simulateWalk((r, c - iteration + 1), "^")
            
def solution_part_01():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                positionsVisited.add((r, c))
                simulateWalk((r, c), grid[r][c])
    print("Anwser Part One", len(positionsVisited))
            
def loops(grid, r, c):
    dr = -1
    dc = 0
    
    seen = set()
    
    while True:
        seen.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= len(grid) or c + dc < 0 or c + dc >= len(grid[0]): return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in seen:
            return True

def solution_part_02():
    def initialPosition():
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '^':
                    return (r, c)
    
    initialPosition = initialPosition()
    anserCount = 0
    (initialR, initialC) = initialPosition
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".": continue
            grid[r][c] = "#"
            if loops(grid, initialR, initialC):
                anserCount += 1
            grid[r][c] = "."
                
    print("Anwser Part Two", anserCount)
    
solution_part_01()
solution_part_02()
