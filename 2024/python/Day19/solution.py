lines = open("input.txt").read().splitlines()
patterns = set(lines[0].split(", "))

def solution_part_01():
    maxLen = max(map(len, patterns))
    
    cache = {}

    def can_obtain(design):
        if design == "": return True
        if design in cache: return cache[design]
        
        for i in range(min(len(design), maxLen) + 1):
            if design[:i] in patterns and can_obtain(design[i:]):
                cache[design] = True
                return True
        cache[design] = False
        return False
    
    answer = sum(1 if can_obtain(design) else 0 for design in lines[2:])
    
    print("Anwser Part One", answer)


def solution_part_02():
    maxLen = max(map(len, patterns))
    
    cache = {}

    def num_possibilities(design):
        if design == "": return 1
        if design in cache: return cache[design]
        
        count = 0
    
        for i in range(min(len(design), maxLen) + 1):
            if design[:i] in patterns:
                count += num_possibilities(design[i:])
                cache[design] = count

        return count
    
    answer = sum(num_possibilities(design) for design in lines[2:])
    
    print("Anwser Part Two", answer)


solution_part_01()
solution_part_02()
