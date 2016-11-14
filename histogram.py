listOfChars = [',', '"', ',', '.', '?', '!', ':', ';', '-', '/']


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
