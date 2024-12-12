from collections import deque

grid = [[int(char) for char in line.strip()] for line in open("input.txt")]
rows = len(grid)
cols = len(grid[0])


def solution_part_01():
    trailHeads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    # same stuff
    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 0:
    #             trailHeads.append((row, col))

    def bfs(grid, r, c):
        q = deque([(r, c)])
        seen = {(r, c)}
        summits = set()

        while len(q) > 0:
            cr, cc = q.popleft()
            
            for dr, dc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
                if dr < 0 or dc < 0 or dr >= rows or dc >= cols:
                    continue
                if grid[dr][dc] != (grid[cr][cc] + 1):
                    continue
                if (dr, dc) in seen:
                    continue
                seen.add((dr, dc))
                if grid[dr][dc] == 9:
                    summits.add((dr, dc))
                else:
                    q.append((dr, dc))

        return len(summits)
    
    validTrails = sum(bfs(grid, r,c) for r, c in trailHeads)

    print("Anwser Part One", validTrails)


def solution_part_02():
    trailHeads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    # same stuff
    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 0:
    #             trailHeads.append((row, col))

    def bfs(grid, r, c):
        q = deque([(r, c)])
        seen = {(r, c): 1}
        trails = 0

        while len(q) > 0:
            cr, cc = q.popleft()
            
            if grid[cr][cc] == 9:
                trails += seen[(cr, cc)]
            
            for dr, dc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
                if dr < 0 or dc < 0 or dr >= rows or dc >= cols:
                    continue
                if grid[dr][dc] != (grid[cr][cc] + 1):
                    continue
                if (dr, dc) in seen:
                    seen[(dr, dc)] += seen[(cr, cc)]
                    continue
                seen[(dr, dc)] = seen[(cr, cc)]
                q.append((dr, dc))

        return trails
    
    validTrails = sum(bfs(grid, r,c) for r, c in trailHeads)

    print("Anwser Part Two", validTrails)


solution_part_01()
solution_part_02()
