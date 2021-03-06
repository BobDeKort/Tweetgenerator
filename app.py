from flask import Flask
from histogram import makeHistogram
from functions import getRandomSentence, getProbabilities, randomWordWithProbability
import os
app = Flask(__name__)
filePath = 'text/sherlockHolmes.txt'


@app.route('/')
def main():
    return('Hello! Try /sentence or /word!')


@app.route('/sentence')
def sentence():
    histogram = makeHistogram(filePath)
    sentence = getRandomSentence(histogram, 10)
    return ('Your random sentence is: ' + sentence + '.')


@app.route('/sentence/<wordCount>')
def sentenceWithAmountOfWords(wordCount):
    histogram = makeHistogram(filePath)
    sentence = getRandomSentence(histogram, int(wordCount))
    return ('Your random sentence is: ' + sentence + '.')


@app.route('/word')
def word():
    histogram = makeHistogram(filePath)
    probList = getProbabilities(histogram)
    randomWord = randomWordWithProbability(probList)
    return('Your random word is: ' + randomWord + '.')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
