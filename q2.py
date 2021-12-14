#Use a loop from 1 to 100 and print the numbers that satisfy the following conditions:

#Print the numbers that are divisible by 7 and 3
#Print the numbers that are divisible by 7 but not 3
#Print the ODD numbers divisible by 7 but not 3
#Print the numbers that are divisible by the sum of its digits (e.g. 36: 3+9=9 39/9 = 4)
#Print the numbers that are equal to the square of the sum of its digits 
print("Numbers that are divisible by 7 and 3")
for i in range (101):
    if i%7 == 0 and i%3 == 0:
        print(i)
    else:
        pass

print("Numbers that are divisible by 7 but not 3")    
for i in range(101):
    if i%7 == 0 and i%3 != 0:
        print(i)
    else:
        pass


print("Odd numbers that are divisible by 7 but not 3") 
for i in range(101):
    if i%2 != 0 and i%7 == 0 and i%3 !=0:
        print(i)
    else:
        pass

print("Numbers that are divisible by the sum of its digits ")
for i in range(101):
    sum_of_digits = sum(int(digit) for digit in str(i))
    if i%sum_of_digits == 0:
        print(i)


print("Numbers that are equal to the square of the sum of its digits")
for i in range(101):
    

    
    
         

