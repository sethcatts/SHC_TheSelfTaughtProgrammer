#-1 Print every character in the string "Camus".
def printCharacters():
    print("Camus"[0])
    print("Camus"[1])
    print("Camus"[2])
    print("Camus"[3])
    print("Camus"[4])

#-2 Write a program that collects two strings from a user, inserts them into
#   the string "Yesterdy I wrote a [user_input_1]. I sent it to [user_input_2]!"
#   and prints the new string
def madLibs():
    str_One = input("Input String One: ")
    str_Two = input("Input String Two: ")
    new_str = "Yesterdy I wrote a {}. I sent it to {}!".format(str_One, str_Two)
    print(new_str)
#-3 Use a method to make the string "aldous Huxley was born in 1894."
#   grammatically correct by capitalizing the first letter in the sentence.
def capital():
    str_a = "aldous Huxley was born in 1894."
    str_a = str_a.capitalize()
    print(str_a)
#-4 Take the string "Where now? Who now? When now?" and call a method that
#   returns a list ["Where now?", "Who now?", "When now?"]
#   M:Split on '?'

#-5 Take the list ["The", "Fox", "Jumps", "Over", "The", "Fence", "."]
#   and turn it into a grammatically correct string. Spaces except after .
#   Method for this:?

#-6 Replace every s with a dollar sign in the string "A screaming comes across
#   the sky"

#-7 Write a method that returns the index of a specified character when
#   supplied with a string and character.

#-8 Write a string that contains quotes

#-9 Create the string "Three Three Three" using concatenation
#   and multiplication

#-10 Slice the string "It was a bright cold day in April, and the clocks were
#    striking thirteen" to only include the characters before the comma


#Functions Calls
#printCharacters()
#madLibs()
capital()
