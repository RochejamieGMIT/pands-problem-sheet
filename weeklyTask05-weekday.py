# Author: Jamie Roche
#Week 5 task
# Using this link to find how to import day of the week
#
# Reference:
# https://www.delftstack.com/howto/python/python-datetime-day-of-week/
# 

from datetime import datetime

Day = datetime.today().weekday() # read day as variable 
#Day = 0-6 to test

days = ("Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"
)

today = days[Day] # selecting day to print out as string based on number of the day of the week.

if Day >= 5:
    print ("Today is ", today, "it is the weekend, yay!")
else :
    print ("Today is ", today, "Yes, unfortunately It is a Weekday")


######################################################################
# Redid the code to minimise lines 
# I liked original using the tuple for the week days, but it's less efficient 

today2 = datetime.today().strftime('%A') # Take the day of the week as a string
#print(today2) - Test if day is rad in correctly 

if today2 == "Saturday" or today2 == "Sunday": #Test if the string matches the weekend days
    print ("Today is ", today2, "it is the weekend, yay!")
else :
    print ("Today is ", today2, "Yes, unfortunately It is a Weekday") # if it's not a weekend day, it's a weekday. 




