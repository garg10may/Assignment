
import re

def cleanWords(text):
    words = re.findall('[a-zA-Z]+', text)
    words = map(lambda x: x.lower(), words)
    return words
