from collections import deque

grid = [list(line.strip()) for line in open("input.txt")]
rows = len(grid)
cols = len(grid[0])


def solution_part_01():
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                break
        else:
            continue
        break

    dists = [[-1] * cols for _ in range(rows)]
    dists[r][c] = 0

    q = deque([(r, c)])

    while q:
        cr, cc = q.popleft()

        for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if grid[nr][nc] == "#":
                continue
            if dists[nr][nc] != -1:
                continue
            dists[nr][nc] = dists[cr][cc] + 1
            q.append((nr, nc))

    count = 0

    for r in range(rows):
        for c in range(cols):
            if dists[r][c] == -1:
                continue
            for nr, nc in [(r + 2, c), (r + 1, c + 1), (r, c + 2), (r - 1, c + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if dists[nr][nc] == -1:
                    continue
                if abs(dists[r][c] - dists[nr][nc]) >= 102:
                    count += 1

    print("Anwser Part One", count)


def solution_part_02():
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                break
        else:
            continue
        break

    dists = [[-1] * cols for _ in range(rows)]
    dists[r][c] = 0

    q = deque([(r, c)])

    while q:
        cr, cc = q.popleft()

        for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if grid[nr][nc] == "#":
                continue
            if dists[nr][nc] != -1:
                continue
            dists[nr][nc] = dists[cr][cc] + 1
            q.append((nr, nc))

    count = 0

    for r in range(rows):
        for c in range(cols):
            if dists[r][c] == -1:
                continue

            for radius in range(2, 21):
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in {
                        (r + dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c + dc),
                        (r - dr, c - dc),
                    }:
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                            continue
                        if dists[nr][nc] == -1:
                            continue
                        if dists[r][c] - dists[nr][nc] >= 100 + radius:
                            count += 1

    print("Anwser Part Two", count)


solution_part_01()
solution_part_02()
