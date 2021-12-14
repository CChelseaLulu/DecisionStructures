
def searchname():
    name = input("Enter your first name:").upper()
    
    for i in name:
        if name.startswith('A'):
            print(name)
        else:
            print("The name doesn't start with the letter A.")
            
searchname()
