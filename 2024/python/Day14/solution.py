import re

robots = [tuple(map(int, re.findall(r"-?\d+", robot))) for robot in open("input.txt").readlines()]

def solution_part_01():
    WIDTH = 101
    HEIGHT = 103
    MOVES = 100
    VM = (HEIGHT - 1) // 2
    HM = (WIDTH - 1) // 2
    
    tl = bl = tr = br = 0

    robotsAfterMoves = []
    
    for px, py, vx, vy in robots:
        robotsAfterMoves.append(((px + vx * MOVES) % WIDTH, (py + vy * MOVES) % HEIGHT))
        
    for px, py in robotsAfterMoves:
        if px == HM or py == VM: continue
        if px < HM:
            if py < VM:
                tl += 1
            else:
                bl += 1
        else:
            if py < VM:
                tr += 1
            else:
                br += 1
    
    anwserSum = tl * bl * tr * br
    
    print("Anwser Part One", anwserSum)


def solution_part_02():
    WIDTH = 101
    HEIGHT = 103

    VM = (HEIGHT - 1) // 2
    HM = (WIDTH - 1) // 2
    
    min_sf = float("inf")
    best_iteration = None
    
    for second in range(WIDTH * HEIGHT):
        robotsAfterMoves = []
        
        for px, py, vx, vy in robots:
            robotsAfterMoves.append(((px + vx * second) % WIDTH, (py + vy * second) % HEIGHT))
            
        tl = bl = tr = br = 0
            
        for px, py in robotsAfterMoves:
            if px == HM or py == VM: continue
            if px < HM:
                if py < VM:
                    tl += 1
                else:
                    bl += 1
            else:
                if py < VM:
                    tr += 1
                else:
                    br += 1
        
        sf = tl * bl * tr * br
        
        if sf < min_sf:
            min_sf = sf
            best_iteration = second
    
    print("Anwser Part Two", min_sf, best_iteration)


solution_part_01()
solution_part_02()
