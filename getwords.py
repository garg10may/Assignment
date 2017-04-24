
import re

def getWords(text):
    tokens = re.findall('\w+', text)
    return tokens

if __name__ == '__main__':
	print getWords("Hi, how are you? 777")
