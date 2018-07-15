#-1. Create a list of your favorite musicians/bands
favoriteMusic = ["Grimes", "Purity Ring", "CHVRCHES", "Anamanaguchi",
                 "Five Finger Death Punch", "Avenged Sevenfold", "CRAY",
                 "Joji", "Death Cab for Cutie", "Magic Sword", "Metric",
                 "Windrunner", "Porter Robinson", "Crywolf", "Eden Project"]
#print(favoriteMusic)

#-2. Create a list of tuples that are the geo-coordinates of somewhere
geo_tuple = ("41.7325° N, 49.9469° W", "60°54’59″N", "101°57’0″E",
             "32°46’44.57″N",  "96°48’31.17″W")

#-3. Create a dictionary with facts about yourself
my_facts = {"Favorite COLOR":"Pink",
            "Favorite MUSIC":"Grimes",
            "Favorite FOOD":"Toast",
            "Favorite GAME":"Skyrim",
            "Favorite SONG":"Grimes - Kill V. Maim",
            "Favorite MOVIE":"Drive"}

#-4. Create a function to print a selected fact about you from your dictionary
def getFact():
    print("Facts: Color, Music, Food, Game, Song, Movie")
    selection = input("Enter the fact you would like to know: ")
    try:
        print("My favorite " + selection + " is " +
              my_facts["Favorite " + selection.upper()])
    except KeyError:
        print("This fact is not in the dictionary")

#-5. Create a dictionary mapping your favorite musicians to a list of your
#    favorite songs by them
my_music = {"Grimes":["Pin", "Kill V. Maim", "World Princess part II"],
            "Joji":["Thom", "Will He", "Demons", "Window"],
            "Purity Ring":["heartsigh", "begin again", "dust hymn"],
            "Magic Sword":["The Beginning", "Kill Them All", "Retrogram"]}

#-6. Research python sets and other container types
#"The data type "set", which is a collection type, has been part of Python since
# version 2.4. A set contains an unordered collection of unique and immutable
# objects. The set data type is, as the name implies, a Python implementation of
# the sets as they are known from mathematics. This explains, why sets unlike
# lists or tuples can't have multiple occurrences of the same element."
# - [https://www.python-course.eu/sets_frozensets.php]
