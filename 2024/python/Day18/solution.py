from collections import deque

coords = [list(map(int, line.split(","))) for line in open("input.txt")]


def solution_part_01():
    s = 70
    n = 1024

    grid = [[0] * (s + 1) for _ in range(s + 1)]

    for c, r in coords[:n]:
        grid[r][c] = 1

    q = deque([(0, 0, 0)])
    seen = {(0, 0)}

    anwser = None

    while q:
        r, c, d = q.popleft()

        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr > s or nc > s:
                continue
            if grid[nr][nc] == 1:
                continue
            if (nr, nc) in seen:
                continue
            if nr == nc == s:
                anwser = d + 1
                break
            seen.add((nr, nc))
            q.append((nr, nc, d + 1))
        else:
            continue
        break

    print("Anwser Part One", anwser)


def connected(n):
    s = 70

    grid = [[0] * (s + 1) for _ in range(s + 1)]

    for c, r in coords[:n]:
        grid[r][c] = 1

    q = deque([(0, 0)])
    seen = {(0, 0)}

    while q:
        r, c = q.popleft()

        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr > s or nc > s:
                continue
            if grid[nr][nc] == 1:
                continue
            if (nr, nc) in seen:
                continue
            if nr == nc == s:
                return True
            seen.add((nr, nc))
            q.append((nr, nc))


def solution_part_02():
    lo = 0
    hi = len(coords) - 1
    
    while lo < hi: 
        mid = (lo + hi) // 2
        if connected(mid + 1):
            lo = mid + 1
        else:
            hi = mid


    print("Anwser Part Two", coords[lo])


solution_part_01()
solution_part_02()
