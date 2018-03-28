import random

wordList = ["Cat", "Dog", "Pet", "Net", "Ten", "Cap", "Man"]

#This should return a multDem list
#filled out to the length of [word]
def newWord():
    return wordList(random.randInt(0, len(wordList)))
def returnWordLists(word):
    length = len(word)
    retLists = [[],[]]
    for idx in 2:
        for i in length:
            retLists[idx][i].append(0)

#Hangman main
def guessTheWord():
    word = newWord()
    wordLists = returnWordLists(word)
    image = [["          "],
             ["|-------  "],
             ["|      |  "],
             ["      ('')"],
             ["      \[]/"],
             ["       || "],
             ["          "]]
    incorrectGuesses = 0
    guessed = False;
    while not guessed:
        guess = input("Letter: ")
        if(word.contains("guess")):
            #Add to letters guessed
            print("filler.")
        else:
            incorrectGuesses = incorrectGuesses+1
#Start Game
guessTheWord()
