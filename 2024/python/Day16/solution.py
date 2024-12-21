import heapq
from collections import defaultdict
from collections import deque

grid = [list(line.strip()) for line in open("input.txt")]

rows = len(grid)
cols = len(grid[0])


def solution_part_01():
    sr = sc = er = ec = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                sr = r
                sc = c
            if grid[r][c] == "E":
                er = r
                ec = c
                
    
    
    pq = [(0, sr, sc, 0, 1)]
    seen = {(sr, sc, 0, 1)}
    
    answser = None
    
    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        seen.add((r, c, dr, dc))

        if grid[r][c] == "E":
            answser = cost
            break
        
        for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
            if grid[nr][nc] == '#': continue
            if (nr, nc, ndr, ndc) in seen: continue
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))
            
    print("Anwser Part One", answser)


def solution_part_02():
    sr = sc = er = ec = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                sr = r
                sc = c
            if grid[r][c] == "E":
                er = r
                ec = c
                
    
    
    pq = [(0, sr, sc, 0, 1)]
    lowest_cost = defaultdict(lambda: float("inf"), {(sr, sc, 0, 1): 0})
    backtrack = {}
    best_cost = float("inf")
    end_states = set()
    
    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        
        if cost > lowest_cost[(r, c, dr, dc)]: continue
        
        lowest_cost[(r, c, dr, dc)] = cost

        if grid[r][c] == "E":
            if cost > best_cost: break
            best_cost = cost
            end_states.add((r, c, dr, dc))
            
        for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
            if grid[nr][nc] == '#': continue
            
            lowest = lowest_cost[(nr, nc, ndr, ndc)]
            
            if new_cost > lowest: continue
            
            if new_cost < lowest:
                backtrack[(nr, nc, ndr, ndc)] = set()
                lowest_cost[(nr, nc, ndr, ndc)] = new_cost
                
            backtrack[((nr, nc, ndr, ndc))].add((r, c, dr, dc))
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

    states = deque(end_states)
    seen = set(end_states)
    
    while states:
        key = states.popleft()
        for last in backtrack.get(key, []):
            if last in seen: continue
            seen.add(last)
            states.append(last)
    answser = len({(r, c) for r, c, _, _ in seen})

    print("Anwser Part Two", answser)


# solution_part_01()
solution_part_02()
