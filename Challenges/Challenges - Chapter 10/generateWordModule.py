import random

wordList = ["Cat", "Dog", "Pet", "Cow", "Not", "Pow"]

def returnWord():
    return wordList[random.randint(0, len(wordList)-1)]
