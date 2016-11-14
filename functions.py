import random


def getRandomSentence(histogram, numberOfWords):
    sentence = ''
    for _ in range(numberOfWords):
        probList = getProbabilities(histogram)
        randWord = randomWordWithProbability(probList)
        sentence = sentence + " " + randWord
    return sentence


def getProbabilities(histogram):
    amountOfWords = getTotalAmountOfWords(histogram)
    listWithProbability = []
    for key in histogram:
        valueOfKey = histogram[key]
        probability = float(valueOfKey) / amountOfWords
        listWithProbability.append([key, probability])
    return listWithProbability


def getTotalAmountOfWords(histogram):
    total = 0
    for key in histogram:
        count = histogram[key]
        total += count
    return total


def randomWordWithProbability(listWithProbability):
    randomFlt = random.uniform(0, 1)

    probValue = 0
    for word in listWithProbability:
        probValue += word[1]
        if probValue >= randomFlt:
            return word[0]
