#Find the square root using functions, newton method
#
#Author: Jamie Roche
#References: https://www.youtube.com/watch?v=2158QbsunA8
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
def sqrt(toRoot, rError) :
    #Pass in the number to root and the allowable error
    #Set the first check to be the number itself
    x = toRoot
 
    
    check = False # Set up while loop until correct margin of error is reached
    while (not check) :
        root = 0.5 * (x + (toRoot / x))
 
        # check to see if the differce is within the allowable margin
        if (abs(root - x) < rError) :
            check = True
 
        x = root
 
    return root # Return the square root of the number

#Reusing the code for the correct input type to allow different numbers to be squared
def readNum(message = "enter a number "):
    num = False
    while(num == False):
        try:
         num = int(input(message))
        except ValueError:
          print("just numbers no letters ",end ='')
    return num

    

numToRoot = readNum() # Read in number to find root of
accuracy  = 0.000000000000001 # Read in number to determine required accuaracy of estimate

sqroot = (sqrt(numToRoot, accuracy)) # Choosing to set the returned value to a variale before printing out incase other calculations could be required

print(sqroot)