#-1 Make a list and print each value in it using a loop
def printList(list):
    for el in list:
        print(el)
#-2 Print all the numbers between 25 - 50
def printRange(a, b):
    for i in range(a, b):
        print(i)
#-3 Print each item and its index in a list
#TEST
def printItemAndIndex(list):
    for i in list.length():
        print(i + " : " list[i])
#-4 Using an infinite loop write a number guessing game with the
#   option to enter Q to quit the loop
def guessTheNumber():
    //randomNumber = Math.random()
    play = True
    while(play):
        guess = input("Guess a number(1-9): ")
        if guess == randomNumber:
            print("That's correct!")
        elif guess == "q":
            play = False
        else:
            print("Try again!")

#-5 Multiply all the numbers in listA into their same index in
#   listB and add each to their index in listC
def multiplyTwoListAndReturnResult(listA, listB):
    listC = []
    for i in listA.length():
        listC.append(listA[i] * listB[i])
    print(listC)

#FUNCTION CALLS
