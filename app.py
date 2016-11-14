from flask import Flask
import random
import os
app = Flask(__name__)
filePath = 'text/sherlockHolmes.txt'
listOfChars = [',', '"', ',', '.', '?', '!', ':', ';', '-', '/']
amountOfWords = 10


@app.route('/')
def main():
    return("Hello! Try /sentence or /word!")


@app.route('/sentence')
def sentence():
    histogram = makeHistogram(filePath)
    sentence = randomSentence(histogram, amountOfWords)
    return ("Your random sentence is: " + sentence)


@app.route('/word')
def word():
    histogram = makeHistogram(filePath)
    probList = getProbabilities(histogram)
    randomWord = randomWordWithProbability(probList)
    return("Your random word is: " + randomWord)


@app.route('/sentence/<wordCount>')
def sentenceWithAmountOfWords(wordCount):
    histogram = makeHistogram(filePath)
    sentence = randomSentence(histogram, int(wordCount))
    return ("Your random sentence is: " + sentence)


# Functions


def randomSentence(histogram, numberOfWords):
    sentence = ""
    for _ in range(numberOfWords):
        probList = getProbabilities(histogram)
        randWord = randomWordWithProbability(probList)
        sentence = sentence + " " + randWord
    return sentence


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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
