"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
# import datetime
from datetime import datetime

# print(sys.argv)
recieved=sys.argv
# - If the user doesn't specify any input, your program should
#    print the calendar for the current month. The 'datetime'
#    module may be helpful for this.
if(len(recieved)==1): 
    month = datetime.today().month
    year = datetime.today().year
    cal=calendar.TextCalendar()
    print(cal.formatmonth(year,month))
    print("Welcome to the calendar app. \nif you wish to see other months and years, please call our program in this format:\n14_cal.py [month] [year]")
    # other ways to make calenders
    # for x in cal.itermonthdates(year, month)):
      #print(x)
    # monthCalender = calendar.monthcalendar(year, month)
    # print(monthCalender)

# - If the user specifies one argument, assume they passed in a
#    month and render the calendar for that month of the current year.
if(len(recieved)==2): 
    month = int(recieved[1])
    year = datetime.today().year
    cal=calendar.TextCalendar()
    print(cal.formatmonth(year,month))

#  - If the user specifies two arguments, assume they passed in
#    both the month and the year. Render the calendar for that
#    month and year.
if(len(recieved)==3): 
    month = int(recieved[1])
    year = int(recieved[2])
    cal=calendar.TextCalendar()
    print(cal.formatmonth(year,month))

#  - Otherwise, print a usage statement to the terminal indicating
#    the format that your program expects arguments to be given.
#    Then exit the program.
#I added on to the base case for this