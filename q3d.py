#Define a new function named searchage().
#Again, copy the code that opens and prints the file.
#This time, modify the code such that it prints only the lines where the age is equal to 5.

def searchage():
    infile = open("names.txt", "r")
    for line in infile:
        phrase = "5"
        if phrase in line:
            print(line)
        
searchage()


