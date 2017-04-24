
def modifiedWordFreq(noiseFilePath, countDict):
    
    noiseWordsFreq = wordFreq(noiseFilePath)
    for word in noiseWordsFreq:
        del(countDict[word])

    return countDict
    