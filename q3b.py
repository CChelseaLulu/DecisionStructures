def searchname():
    infile = open("names.txt", "r")
    for s in infile:
         if s.startswith('A'):
              print(s)
searchname()


def searchname():
    infile = open("names.txt", "r")
    for s in infile:
         if s.startswith('A'):
             print(s[:-1])
searchname()
