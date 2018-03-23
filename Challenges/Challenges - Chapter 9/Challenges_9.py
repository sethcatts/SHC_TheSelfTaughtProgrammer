import os
import csv
#-1 Print the contents of a file
def printFileContents(fileName):
    with open(fileName, "r") as file:
        print(file.read())

#-2 Get user input and write it to a file
def writeInput():
    contents = raw_input("Write to file: ")
    with open("writeInput.txt", "w+") as file:
        file.write(contents)
#-3 Take a multidimensional(3x3) list and write it to a csv file as inner list
#   per row
def createListFile():
    the_list = [[1,2,3],
                [4,5,6],
                [7,8,9]]
    with open("csvFile.csv", "w") as file:
        w = csv.writer(file, delimiter = ',')
        w.writerow(the_list[0])
        w.writerow(the_list[1])
        w.writerow(the_list[2])

#Function Calls
#printFileContents("printableFile.txt")
#writeInput()
#printFileContents("writeInput.txt")
createListFile()
