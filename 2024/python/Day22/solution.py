numbers = open("input.txt").readlines()

def solution_part_01():
    def step(num):
        num = (num ^ (num * 64)) % 16777216
        num = (num ^ (num // 32)) % 16777216
        num = (num ^ (num * 2048)) % 16777216
        return num
    
    total = 0
    
    for number in numbers:
        num = int(number)
        for _ in range(2000):
            num = step(num)
        total += num
    
    print("Anwser Part One", total)


def solution_part_02():
    def step(num):
        num = (num ^ (num * 64)) % 16777216
        num = (num ^ (num // 32)) % 16777216
        num = (num ^ (num * 2048)) % 16777216
        return num
    
    seq_to_total = {}
     
    for number in numbers:
        num = int(number)
        buyer = [num % 10]
        for _ in range(2000):
            num = step(num)
            buyer.append(num % 10)
        seen = set()
        for i in range(len(buyer) - 4):
            a, b, c, d, e = buyer[i:i + 5]
            seq = (b - a, c - b, d - c, e - d)
            if seq in seen: continue
            seen.add(seq)
            
            if seq not in seq_to_total: seq_to_total[seq] = 0
            seq_to_total[seq] += e
    

    print("Anwser Part Two", max(seq_to_total.values()))


solution_part_01()
solution_part_02()
