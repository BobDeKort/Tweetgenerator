from flask import Flask
import random
app = Flask(__name__)
filePath = 'text/sampleText.txt'
listOfChars = [',', '"', ',', '.', '?', '!', ':', ';', '-', '/']


@app.route('/')
def hello_world():
    histogram = makeHistogram(filePath)
    probabilityList = getProbabilities(histogram)
    randWord = randomWordWithProbability(probabilityList)
    return('random word: ' + randWord)


def makeHistogram(filePath):  # returns dictionary
    wordList = getWordListFromFile(filePath)
    histogram = {}
    for word in wordList:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram


def getWordListFromFile(filePath):
    source = open(filePath, 'r')
    wordList = source.read().strip().translate(None, ''.join(listOfChars)).split()
    return wordList


def getProbabilities(histogram):
    amountOfWords = getTotalAmountOfWords(histogram)
    listWithProbability = []
    for key in histogram:
        valueOfKey = histogram[key]
        probability = float(valueOfKey) / amountOfWords
        listWithProbability.append([key, probability])
    return listWithProbability


def randomWordWithProbability(listWithProbability):
    randomFlt = random.uniform(0, 1)

    probValue = 0
    for word in listWithProbability:
        probValue += word[1]
        if probValue >= randomFlt:
            return word[0]


def getTotalAmountOfWords(histogram):
    total = 0
    for key in histogram:
        count = histogram[key]
        total += count
    return total
