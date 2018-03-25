def guessTheWord():
    image = [["          "],
             ["|-------  "],
             ["|      |  "],
             ["      ('')"],
             ["      \[]/"],
             ["       || "],
             ["          "]]
    incorrectGuesses = 0
    guessed = False;
    while !guessed:
        guess = input("Letter: ")
        if(word.contains("guess")):
            #Add to letters guessed
        else:
            incorrectGuesses++
