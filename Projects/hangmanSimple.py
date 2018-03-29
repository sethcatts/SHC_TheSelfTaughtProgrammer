#--TO_DO--
#-Combine return word list and new word to one function?
#-Cut down variables in general
#-Complete main if statement logic
#-REFACTOR, REFACTOR, REFACTOR
import random
wordList = ["Cat", "Dog", "Pet", "Net", "Ten", "Cap", "Man"]

#Return a word from wordList
def newWord():
    return wordList[random.randint(0, 6)]

#This should return a multDem list
#filled out to the length of [word]
def returnWordLists(word):
    length = len(word)
    retLists = [[],[]]
    for idx in range(0,2):
        for i in range(0, len(word)):
            retLists[idx].append("_")
    return retLists
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
    guess   = "string"
    #Debug outside loop
    print("Word: " + word)
    print("Lists: " + str(wordLists))
    #---

    while not guessed:
        guess = raw_input("Letter: ")
        if(guess in word):
            print("filler.")
        else:
            incorrectGuesses = incorrectGuesses+1
#Start Game
guessTheWord()
