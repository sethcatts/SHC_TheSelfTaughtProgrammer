import random
#-1 Make a list and print each value in it using a loop
def printList(list):
    for el in list:
        print(el)
#-2 Print all the numbers between 25 - 50
def printRange(a, b):
    for i in range(a, b):
        print(i)
#-3 Print each item and its index in a list
def printItemAndIndex(list):
    for i in range(0, len(list)):
        print(i, ":", list[i])
#-4 Using an infinite loop write a number guessing game with the
#   option to enter Q to quit the loop
def guessTheNumber():
    randomNumber = random.randint(0, 10)
    print(randomNumber)
    play = True
    while(play):
        guess = input("Guess a number(1-9): ")
        print(guess)

        #This crashes on 'q' input because you cant convert to int
        if(int(guess) == randomNumber):
            print("That's correct!")
            play = False
        elif guess == "q":
            play = False
        else:
            print("Try again!")

#-5 Multiply all the numbers in listA into their same index in
#   listB and add each to their index in listC
def multiplyTwoListAndReturnResult(listA, listB):
    listC = []
    for i in range(0, len(listA)):
        listC.append(listA[i] * listB[i])
    print(listC)

#FUNCTION CALLS
listList = [1,2,3,4,5,6,7,8,9]
listList0 = [1,2,3,4,5,6,7,8,9]
#printList(listList)
#printRange(25,51)
#printItemAndIndex(listList)
#guessTheNumber()
#multiplyTwoListAndReturnResult(listList, listList0)
