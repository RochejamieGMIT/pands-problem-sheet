#Program to At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#
#
#If less than 1 program does not progress
#using While not 1 to stop program when it reaches 1
#Using elif to decide between odd or even using % 2 = 0 to prove even
#
# Using floor division to stop int printing as a float when divided 
# https://stackoverflow.com/questions/56799336/how-to-stop-python-from-converting-int-to-float
#Author: Jamie Roche

num = int(input("Please only enter a positive integer: "))
while num < 0:
        num = int(input("Please only enter a positive integer: "))

print (num, end = " ") #print the number entered by the user for the output format
while num != 1: # run program until program reaches 1
    if ((num%2) == 0): # check if the number is even
        num = num //2  # divide by 2
        print (num,end = " ") #print out in line with output format 
    else:
        num = (num * 3) + 1 # if the number is odd, multiply by 3 and add 1
        print (num,end = " ") #print out in line wiht 
    