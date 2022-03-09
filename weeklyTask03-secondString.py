# Weekly task 03 - 
# Write a program that asks a user to input a string and outputs every second letter in reverse order.

# Author: Jamie Roche 
inputString = input('enter a string:')

lenghtOfString = len(inputString) - 1
count = 0 # using count to ensurereprint starts at last character 
even = 0 # printing every second charater using even/odd
out = ''

# using the remained of the number of letters left in the stirng divided by 2 to determine if the 
# number is even or odd, allows us to print every second letter. Adding only even numbers to the output
# string 

while lenghtOfString >= 0:
    if even == 0:
     out = out + (inputString[lenghtOfString])
     
    lenghtOfString = lenghtOfString - 1
    count += 1
    even = count % 2

 
print(out)

############################################################################
# Redo of code to minimise the amout of lines required ot complete the task
#
#
inputString2 = input('enter a string:') # Take input from user

textOut = inputString2[::-2] # reverse string and have every second character
print(textOut) # print reverse and every second




