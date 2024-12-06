import heapq
from collections import defaultdict

input01 = open("input01.txt").read().split("\n")

# big O(nLogn)
def solution_part_01():
    sortedListOne = []
    sortedListTwo = []

    for line in input01:
        [fistListNumber, secondListNumber] = line.split()
        heapq.heappush(sortedListOne, int(fistListNumber))
        heapq.heappush(sortedListTwo, int(secondListNumber))

    differenceSum = 0
    while sortedListOne or sortedListTwo:
        differenceSum += abs(
            heapq.heappop(sortedListOne) - heapq.heappop(sortedListTwo)
        )

    print("Answer Part One", differenceSum)

# big O(n)
def solution_part_02():
    frequencyMapListTwo = defaultdict(int)

    for line in input01:
        [_, secondListNumber] = line.split()
        frequencyMapListTwo[secondListNumber] += 1

    ans = 0
    for line in input01:
        [firstListNumber, _] = line.split()
        ans += int(firstListNumber) * frequencyMapListTwo[firstListNumber]

    print("Answer Part Two", ans)


solution_part_01()
solution_part_02()
