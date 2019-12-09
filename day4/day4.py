def hasTwoAdjacent1(number):
    for i in range(len(number) - 1):
        # print(number[i] + " " + number[i+1])
        if number[i] == number[i + 1]:
            return True
    return False
    pass


def notDecreases(number):
    for i in range(len(number) - 1):
        # print(number[i] + " " + number[i+1])
        if int(number[i]) > int(number[i + 1]):
            return False
    return True
    pass


possiblePass = 272091

goodPassCounter = 0
while possiblePass <= 815432:
    if hasTwoAdjacent1(str(possiblePass)) and notDecreases(str(possiblePass)):
        goodPassCounter += 1
    possiblePass += 1

print(goodPassCounter)


def hasTotal2(number, toFind):
    found = 0
    for i in range(len(number)):
        if number[i] == toFind:
            found += 1
    return found == 2
    pass


def hasTwoAdjacent2(number):
    for i in range(len(number) - 1):
        if number[i] == number[i + 1] and hasTotal2(number, number[i]):
            return True
    return False
    pass


possiblePass = 272091

goodPassCounter = 0
while possiblePass <= 815432:
    if hasTwoAdjacent2(str(possiblePass)) and notDecreases(str(possiblePass)):
        goodPassCounter += 1
    possiblePass += 1

print(goodPassCounter)
