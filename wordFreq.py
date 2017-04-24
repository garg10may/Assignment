from cleanWords import cleanWords
def wordFreq(textFilePath):        f = open(textFilePath)    countDict = {}        for line in f:        words = cleanWords(line)        for word in words:            countDict[word] = countDict.get(word, 0) + 1        return countDict
