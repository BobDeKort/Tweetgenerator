# -*- coding: utf-8 -*-

import re
import sys


# /^\d+$/gm -> selects pagenumbers
# /Chapter \d+/g -> selects chapter heading in guide 1 and 5
# ^\d CHAPTER \d\.$ -> selects chapter heading in other guides
# corpus uses regular dash when a word is cut of at the end of line and a
# EN dash when it is used as part of the sentence
# remove punctuation except for end of scentence punctuation (! ,? ,. )
# -[ 0-9\na-zA-Z]*CHAPTER \d.\n -> disjointed words over chapter


def rejoinSplitWords(dataFile):  # Check!!!!!
    matches = re.sub('([A-z]+)-\s+([A-z]+)', '\1\2', dataFile)
    for match in matches:
        print match
        # TODO: remove dash and space


def removeChapterHeading(dataFile):  # Works
    matches = re.sub(
        'Chapter \d+|^\d CHAPTER \d\.?$|-[ 0-9\na-zA-Z]*CHAPTER \d.\n', '',  dataFile)
    for match in matches:
        print match
        # TODO: remove matches


def removePageNumbers(dataFile):  # Works
    matches = re.sub('^\d+$', '', dataFile, re.MULTILINE)
    for match in matches:
        print match
        # TODO: remove matches

# def removeOtherPunctuations(dataFile):
#     matches = re.findall('', dataFile)
#     for match in matches:
#         print match

if __name__ == '__main__':

    userArgumentCount = len(sys.argv)
    if userArgumentCount == 1:
        print 'Error: No textFile provided'
    else:
        newFile = open("cleaned.txt", "w")
        data = open(sys.argv[1], 'r').read()
        data = re.sub(r'--+Page \d--+', '', data)

        # rejoin over chapter split words
        # data = re.sub(r'-[ 0-9\na-zA-Z]*CHAPTER \d.\n', '', data)
        # remove page numbers
        data = re.sub(r'\n\d+\s', '\n', data, re.MULTILINE)
        # remove chapter headers
        data = re.sub(
            r'Chapter \d+|^\d CHAPTER \d\.?$|-[ 0-9\na-zA-Z]*CHAPTER \d.\n', '',  data)
        # rejoin split words
        data = re.sub(r'([A-z]+)-\s+([A-z]+)', r'\1\2', data)
        newFile.write(data)
        newFile.close()
