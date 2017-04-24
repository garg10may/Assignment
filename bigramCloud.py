
from cleanWords import cleanWords
from itertools import combinations

def wordPairGenerator(wordsList):
    return combinations(wordsList, 2)
    
       
def biGramWordFreq(textFilePath):
    
    f = open(textFilePath)
    countDict = {}
    biGramCountDict = {}

    allWords = []
    for line in f:
        words = cleanWords(line)
        allWords.extend(words)        
        for word in words:
            countDict[word] = countDict.get(word, 0) + 1
            
    uniqueWords = set(allWords)
    wordPairs = list(wordPairGenerator(uniqueWords))
    
    for pair in wordPairs:
        biGramCountDict[pair] = countDict[pair[0]] + countDict[pair[1]]
    
    modBiGramCountDict = {}
    for item in biGramCountDict:
        modBiGramCountDict[item[0] + item[1]] = biGramCountDict[item]
    return modBiGramCountDict

def modBiGramWordFreq(noiseFilePath, biGramCountDict):
        
    noiseWordsFreq = biGramWordFreq(noiseFilePath)
    for word in noiseWordsFreq:
        del(biGramCountDict[word])

    return biGramCountDict

from tagCloud import tagCloud, createHTML
from linkedTagCloud import linkedTagCloud, findLines, createHTML2











    
    