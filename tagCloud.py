

def createHTML(sortedItems):    
    text = ''
    for i in sortedItems:        
        text += '<font size="' + str(i[1]) + '">' + str(i[0]) + '</font>' + " "
    return text          
    

def tagCloud(wordFreq):
    
    sortedItems = sorted( wordFreq.items())   
    return createHTML(sortedItems)
    

if __name__ == '__main__':

	from wordFreq import wordFreq
	from modifiedWordFreq import modifiedWordFreq
	countDict = wordFreq("abc.txt")
	md = modifiedWordFreq( "noise.txt", countDict)

	print tagCloud(md)
