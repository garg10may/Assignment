

from wordFreq import wordFreq

def modifiedWordFreq(noiseFilePath, countDict):
    
    noiseWordsFreq = wordFreq(noiseFilePath)
    for word in noiseWordsFreq:
        del(countDict[word])

    return countDict
    


if __name__ == '__main__':

	countDict = wordFreq("abc.txt")
	print modifiedWordFreq("noise.txt", countDict)