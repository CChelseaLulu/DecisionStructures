def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print(s)
searchname()


def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print(s[:-1])
searchname()


#The first code is better because it is well-spaced, hence easy to read.
