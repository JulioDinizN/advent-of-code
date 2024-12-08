inputValue = open("input.txt").read().splitlines()


def solution_part_01():
    answerSum = 0
    splitIndex = inputValue.index("")
    orderingRules = inputValue[:splitIndex]
    updates = inputValue[splitIndex + 1 :]

    for update in updates:
        pages = update.split(",")
        pagesDictionary = {char: index for index, char in enumerate(pages)}

        validRules = [
            rule.split("|")
            for rule in orderingRules
            if all(inside in update for inside in rule.split("|"))
        ]

        isValid = True
        for before, after in validRules:
            if pagesDictionary[before] > pagesDictionary[after]:
                # print((before, after) , pages)
                isValid = False

        if isValid:
            answerSum += int(pages[len(pages) // 2])

    print("Anwser Part One", answerSum)


def solution_part_02():
    answerSum = 0;
    splitIndex = inputValue.index("")
    orderingRules = []
    
    for line in inputValue[:splitIndex]:
        a, b = line.split("|")
        orderingRules.append((int(a), int(b)))
        
    updates = [list(map(int, update.split(","))) for update in inputValue[(splitIndex + 1):]]
    
    def follows_rules(update):
        pagesDictionary = {char: index for index, char in enumerate(update)}
        
        for a, b in orderingRules:
            if a in pagesDictionary and b in pagesDictionary and not pagesDictionary[a] < pagesDictionary[b]:
                return False, 0
        return True, update[len(update) // 2]
    
    def sort_correctly(update):
        while True:
            is_sorted = True
            for i in range(len(update) - 1):
                # Out of order?
                if (update[i+1], update[i]) in orderingRules:
                    is_sorted = False
                    update[i], update[i+1] = update[i+1], update[i]
            
            if is_sorted:
                return update
    
    for outerUpdate in updates:
        if follows_rules(outerUpdate)[0]:
            continue
        
        correctedUpdate = sort_correctly(outerUpdate)
        answerSum += correctedUpdate[len(correctedUpdate) // 2]

    print("Anwser Part Two", answerSum)


solution_part_01()
solution_part_02()
