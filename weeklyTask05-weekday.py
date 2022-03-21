# Author: Jamie Roche
#Week 5 task
# Using this link to find how to import day of the week
#
# Reference:
# https://www.delftstack.com/howto/python/python-datetime-day-of-week/
# 

from datetime import datetime

######################################################################
# Redid the code to minimise lines 
# I liked original using the tuple for the week days, but it's less efficient 

today2 = datetime.today().strftime('%A') # Take the day of the week as a string
#print(today2) - Test if day is read in correctly 

if today2 == "Saturday" or today2 == "Sunday": #Test if the string matches the weekend days
    print ("Today is ", today2, "it is the weekend, yay!")
else :
    print ("Today is ", today2, "Yes, unfortunately It is a Weekday") # if it's not a weekend day, it's a weekday. 




