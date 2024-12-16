inputGrid, inputMoves = open("input.txt").read().split("\n\n")

def solution_part_01():
    moves = list(inputMoves.replace("\n", ""))
    grid = [list(line.strip()) for line in inputGrid.splitlines()]

    rows = len(grid)
    cols = len(grid[0])
    
    r = c = None

    for row in range(1, rows):
        for col in range(1, cols):
            if grid[row][col] == "@":
                r = row
                c = col
                break
        else:
            continue
        break

    for move in moves:
        dr = {"^": -1, "v": 1}.get(move, 0)
        dc = {"<": -1, ">": 1}.get(move, 0)
        targets = [(r, c)]
        
        cr = r
        cc = c
        go = True

        while True:
            cr += dr
            cc += dc
            char = grid[cr][cc]
            
            if char == "#":
                go = False
                break
            if char == "O":
                targets.append((cr, cc))
            if char == '.':
                break
        if not go: continue

        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = "O"
        
        r += dr
        c += dc

    anwserSum = sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "O")

    print("Anwser Part One", anwserSum)


def solution_part_02():
    expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    
    moves = list(inputMoves.replace("\n", ""))
    grid = [list("".join(expansion[char] for char in line)) for line in inputGrid.splitlines()]

    rows = len(grid)
    cols = len(grid[0])
    
    r = c = None

    for row in range(1, rows):
        for col in range(1, cols):
            if grid[row][col] == "@":
                r = row
                c = col
                break
        else:
            continue
        break

    for move in moves:
        dr = {"^": -1, "v": 1}.get(move, 0)
        dc = {"<": -1, ">": 1}.get(move, 0)
        targets = [(r, c)]
        go = True

        for cr, cc in targets:
            nr = cr + dr
            nc = cc + dc
            
            if (nr, nc) in targets: continue
            
            char = grid[nr][nc]
            
            if char == "#":
                go = False
                break
            
            if char == "[":
                targets.append((nr, nc))
                targets.append((nr, nc + 1))
            
            if char == "]":
                targets.append((nr, nc))
                targets.append((nr, nc - 1))

        if not go: continue
        
        copy = [list(row) for row in grid]

        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        
        for br, bc in targets[1:]:
            grid[br][bc] = "."
        
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = copy[br][bc]
        
        r += dr
        c += dc

    anwserSum = sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "[")

    print("Anwser Part Two", anwserSum)


solution_part_01()
solution_part_02()
