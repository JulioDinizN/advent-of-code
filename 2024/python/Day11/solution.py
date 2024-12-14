from functools import cache

inputText = open("input.txt").read()

def solution_part_01():
    stones = inputText.split()
    
    for _ in range(25):
        newStones = []
        
        for stone in stones:
            if stone == '0':
                newStones.append("1")
                continue
            
            if len(stone) % 2 == 0:
                size = len(stone) // 2
                left = stone[:size].lstrip('0') or '0'
                right = stone[size:].lstrip('0') or '0'
                
                newStones.append(left)
                newStones.append(right)
                continue
            
            newStones.append(str(int(stone) * 2024))
            
        stones = newStones
                         
    print("Anwser Part One", len(stones))


def solution_part_02():
    stones = [int(x) for x in inputText.split()]
    
    @cache
    def count(stone, steps):
        if steps == 0:
            return 1
        if stone == 0:
            return count(1, steps - 1)
        
        string = str(stone)
        length = len(string)
        
        if length % 2 == 0:
            return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
        
        return count(stone * 2024, steps - 1)
    
    anwserSum = sum(count(stone, 75) for stone in stones)
    
    print("Anwser Part Two", anwserSum)


solution_part_01()
solution_part_02()
