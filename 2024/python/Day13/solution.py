import re

clawMachines = [
    list(map(int, re.findall(r"\d+", block)))
    for block in open("input.txt").read().split("\n\n")
]


def solution_part_01():
    totalTokens = 0
    
    # Brute force
    for machine in clawMachines:
        ax, ay, bx, by, px, py = machine
        min_score = float("inf")
        
        for i in range(101):
            for j in range(101):
                if ax * i + bx * j == px and ay * i + by * j == py:
                    min_score = min(min_score, i * 3 + j)
        if min_score != float("inf"):
            totalTokens += min_score
    
    print("Anwser Part One", totalTokens)


def solution_part_02():
    totalTokens = 0
    
    for machine in clawMachines:
        ax, ay, bx, by, px, py = machine
        px += 10000000000000
        py += 10000000000000
        
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx

        if ca % 1 == cb % 1 == 0:
            totalTokens += int(ca * 3 + cb)
    
    print("Anwser Part Two", totalTokens)


solution_part_01()
solution_part_02()
