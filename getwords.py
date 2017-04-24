
import re

def getWords(text):
    tokens = re.findall('\w+', text)
    return tokens