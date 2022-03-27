# pands-problem-sheet

Initally all committs for my PANDS work was being committed at :
https://github.com/RochejamieGMIT/Programming2022_SSH

About week 4/5 I realised this was incorrect and created a new repo(this repo) Just for the problem sheet.

*****************
Weekly Task 02
BMI
******************

This program is a simple program that reads in a height and weight from a user 
and calculates the user BMI using the formula found at:
https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used.

*****************
Weekly Task 03
Second string
******************

This program tasks an input string from a user and outputs every second letter in reverse order.

Originally I had the program solved in a convoluted way, the program would keep track of the number of letters left in the string and use the % 2 function to divide by 2 and get the remainder. If the letter was even it would be added to the output string. if it was even it would print out the letter, if it was odd it would not. The program then moved backwards through the string creating a new string with every second letter. 

After learning more pythomn a much simpler solution was discovered. 
using the built in string function, inputString2[::-2]
You can just print out every second charater in the string reveresed. 
A much simpler and effective solution. 

*****************
Weekly Task 04
Collatz
******************