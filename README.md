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
This ia a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

This program uses the % and remained to determine if the number is odd or even. 
If the number is even it is divided by 2, if odd it is multiplied by 3 and 1 is added.
Using the while != 1, the program runs until it reaches one.

Originally when doing the program I was output format, each output was on a new line, and printing as a float as the numbers automatically convert to float when being divided. 

I fixed the output using the end = '' as part the string, 
to fix the float, I used floor division to ensure the item was an int to maitain the correct output format.

Ref for floor division solution: 
https://stackoverflow.com/questions/56799336/how-to-stop-python-from-converting-int-to-float

*****************
Weekly Task 05
weekday
******************
Write a program that outputs whether or not today is a weekday.

For this program I had to search up how to use datetime. 
The reference I used: 
https://www.delftstack.com/howto/python/python-datetime-day-of-week/

This is a program the reads in the day of the week as a string using datetime
datetime.today().strftime('%A')

My original solution I read the day in as a number, meaning I had a tuple of the days of the week to reference to check what day of the week it was based on the number. 
This was less efficient as it took more lines to complete the same output. 

The program checks if the day of the week is either saturday OR Sunday. 
if today2 == "Saturday" or today2 == "Sunday":

If it is it prints out the weekend statement. 
If it's not a weekend day, the program outputs the week day statemant. 


*****************
Weekly Task 06
sqrt
******************
This is a program that takes a positive floating-point number as input and outputs an approximation of its square root.
I reseached the newton method of estimating square roots at the below sources. 

References: https://www.youtube.com/watch?v=2158QbsunA8
 https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
 https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.

 The program takes in a number from the user using the readNum function, this is repurposed code from the lecture, that stops the user if they enter a non numerical value or if the number they entere is not a positive number

 When an acceptable number is added, the number to get the square root of is passed to the sqrt function, along with the margin for error number, Accuracy, originally I also had this as a read in value. but it is better to have a set value. 

 The numbers are passed to the sqrt function, and used in the newton method equation to work out the value of the square root. 
 
 Formula:
 root = 0.5 * (x + (toRoot / x))
 Where root is the new sqaure root estimate, x is the previous estimate, toRoot is the number to get the square root of.


 The progarm loops until the differnece between the number and the error reaches the accuaracy value, meaning the returned output is accuarate to this value. I am using accuracy  = 0.0000000000001, to ensure the returned value is quite accuarate. 

 *****************
Weekly Task 07
Es
******************
This program that reads in a text file and outputs the number of e's it contains.
I am assuming both Capital letters and lower case letters need to be counted.

To read the file in from a command line argument I used this page.
reference:
https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python

This allowed me to read in a file from the cmd line using, 

with open(sys.argv[1], 'r') as f:

I created a small documeant smallE.txt with 3 large and 3 small es to test. 

I then iteratred through the document testing if each letter is either 'e' or 'E', If so the count value is incremented by 1. 
The program goes through the full read in document, and adds up all intstances of e. 

When the program reaches the end of the document it prints out the count. 

To test an unknown text document, I created a document called howManyEs. This is a  document filled with generated text from https://www.lipsum.com/feed/html 


*****************
Weekly Task 08
Plottask 
******************
program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

To research further in to the functions and customisability of graphs and lines I used this webpage:
Ref:
https://matplotlib.org/stable/tutorials/introductory/pyplot.html#:~:text=matplotlib.,the%20plot%20with%20labels%2C%20etc.

I created a graph that has custom lines, colours, sampled more frequently to have a smother graphh, included a title, Legend, Labelled the axis, included a grid.

In the lecuture we used np.array, For this task I used np.arange instead as this allowed me to set the sampling frequecny  of the graph allowing for a smoother, less jagged graph.

I used the following equations to plot. 
ypoints = xpoints # f(x) = x
gpoints = xpoints**2 # f(x) = x^2
hpoints = xpoints**3 # f(x) = x^3

For this program I over commented the lines to explain the custisations chosen for each line>
I also added titles, legend, axis labels, and custom coloured each line, each line also has a different dotted line pattern. I also added a grid to just customise as many aspects of the graph as I could 