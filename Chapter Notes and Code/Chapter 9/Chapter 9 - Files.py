#FILE ACCESS AND WRITING
import os
import csv
#Path example: /users/bob/st.txt
os.path.join("users", "bob", "st.txt")

#The open method can be called with different parameters
#
# "r" -> read only
# "w" -> write only
# "w+" -> reading and writing

#The open function returns an object called a file object

#Example
st = open("st.txt", "w")
st.write("Hi from python")
st.close()

#Example of "with" file open/close
with open("st2.txt", "w") as f:
    f.write("Hello from python")

#Reading example
with open("st2.txt", "r") as f:
    print(f.read())

#Reading to a variable for later use
myList = list()
with open("st2.txt", "r") as f:
    myList.append(f.read())
print(myList)

#CSV Files
with open("st3.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter = ',')
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

#CSV read
with open("st3.csv", "r") as f:
    r = csv.reader(f, delimiter = ',')
    for row in r:
        print(",".join(row))
