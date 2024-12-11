inputValue = open("input.txt").read()


def solution_part_01():
    disk = []
    fid = 0
    
    for i, char in enumerate(inputValue):
        x = int(char)
        if i % 2 == 0:
            disk += [fid] * x
            fid += 1
        else:
            disk += [-1] * x

    blanks = [i for i, x in enumerate(disk) if x == -1]
    
    for i in blanks:
        while disk[-1] == -1: disk.pop()
        if len(disk) <= i: break;
        disk[i] = disk.pop()
        
    checksum = sum(i * x for i, x in enumerate(disk))
    
    print("Anwser Part One", checksum)


def solution_part_02():
    files = {}
    blanks = []
    
    fId = 0
    pos = 0
    
    for i, char in enumerate(inputValue):
        x = int(char)
        if i % 2 == 0:
            if x == 0:
                raise ValueError("unexpected x=0 for file")
            files[fId] = (pos, x)
            fId += 1
        else:
            if x != 0:
                blanks.append((pos, x))
        pos += x

    while fId > 0:
        fId -= 1
        pos, size = files[fId]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[fId] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break
            
    checksum = 0
    
    for fId, (pos, size) in files.items():
        for x in range(pos, pos + size):
            checksum += fId * x
  
    print("Anwser Part Two", checksum)


solution_part_01()
solution_part_02()
