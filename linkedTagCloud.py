
from wordFreq import wordFreq

def findLines(word, textFilePath):
    result = []
    for line in open(textFilePath):
        if word in line:
            result.append(line)
    return result


def createHTML2(sortedItems, textFilePath):    
    text = ''
    for i in sortedItems: 
        word = i[0]
        result = findLines(word, textFilePath)
        target = open(word, 'w')
        for line in result:
            target.write(line)
        target.close()
        linkHTMLStart = '<a href="' + word + ".txt" + '">'
        fontHTMLStart = '<font size="' + str(i[1]) + '">'
        text += linkHTMLStart + fontHTMLStart + word + '</font>' + '</a>' +" "
    return text


def linkedTagCloud(countDict, textFilePath) :
    
    sortedItems = sorted( countDict.items())   
    return createHTML2(sortedItems, textFilePath)
    

print linkedTagCloud(wordFreq("H://abc.txt"), "H://abc.txt")