
import re

def cleanWords(text):
    words = re.findall('[a-zA-Z]+', text)
    words = map(lambda x: x.lower(), words)
    return words


if __name__ == '__main__':
	print cleanWords("Hi, how are you? 777")
