

def createHTML(sortedItems):    
    text = ''
    for i in sortedItems:        
        text += '<font size="' + str(i[1]) + '">' + str(i[0]) + '</font>' + " "
    return text          
    

def tagCloud(countDict):
    
    sortedItems = sorted( countDict.items())   
    return createHTML(sortedItems)
    