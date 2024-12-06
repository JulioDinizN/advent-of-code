import re
inputValue = open("input.txt").read()

validChars = ["m", "u", "l", "(", ",", ")"]
validNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def isRightChar(char, status):
    if 1 in status:
        return (char == "u", [2])

    if 2 in status:
        return (char == "l", [3])

    if 3 in status:
        return (char == "(", [4])

    if 4 in status:
        if char in validNums:
            return (True, [4, 5])

    if 5 in status:
        return (char == ",", [6])

    if 6 in status:
        if char in validNums:
            return (True, [6, 7])

    if 7 in status:
        return (char == ")", [0])
    
    return (False, [0])
    print((charDo, statusDo), 'insideDOOO')
    
    if 1 in statusDo:
        return (charDo == "o", [2])
    
    if 2 in statusDo:
        return (charDo == "(", [3])
    
    if 3 in statusDo:
        return (charDo == ")", [0])
    
    return (False, statusDo)

def solution_part_01():
    anserSum = 0
    index = 0

    while index < len(inputValue):
        currValidSequence = ""

        if inputValue[index] == "m":
            index += 1
            currCheckStatus = [1]
            currValidSequence += "m"

            while True:
                isValidChar, nextSequence = isRightChar(
                    inputValue[index], currCheckStatus
                )

                currCheckStatus = nextSequence

                if not isValidChar:
                    currValidSequence = ""
                    break

                currValidSequence += inputValue[index]

                if 0 in currCheckStatus:
                    filteredString = ''.join(char for char in currValidSequence if char.isnumeric() or char == ',')
                    num1, num2 = list(map(int, filteredString.split(',')))
                    anserSum += num1 * num2
                    break

                index += 1
        index += 1

    print("Anwser Part One", anserSum)

def solution_part_02():
    anserSum = 0
    isEnabled = True
    
    
    for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", inputValue):
        if match == 'do()':
            isEnabled = True
        elif match == "don't()":
            isEnabled = False
        elif isEnabled:
            x, y = map(int, match[4:-1].split(","))
            anserSum += x * y

    print("Anwser Part Two", anserSum)



solution_part_01()
solution_part_02()