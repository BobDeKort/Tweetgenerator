import re


def tokenize(text):
    cleanText = rejoinWords(text)
    noPuncText = remove_punctuation(cleanText)
    tokens = split_on_whitespace(noPuncText)
    return tokens


def split_on_whitespace(text):
    return re.split('\s+', text)


def remove_punctuation(text):
    noPuncText = re.sub('[,.()?''"-]', '', text)
    return noPuncText


def rejoinWords(text):
    newText = re.sub(r'([A-z]+)-\s+([A-z]+)', r'\1\2', text)
    return newText


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        source = open(sys.argv[1]).read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename given as argument')
