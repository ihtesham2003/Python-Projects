Hey, hi today we're gonna make a nice looking printable text file of monthly calendars for the month and year you desire.

Don't scare from dates and calendars, yes, they are some tricky **topic** in programming because there are so many different rules for condioning the number of the days in a month, which years are leap years, and which day of the week a particular date falls on.

Thankfully, Python's **datetime module** handles these details for us. We will generate a multiline string for the monthly calendar page.

Are you still with me, if yes, let's make this shit!!

Things you need to make **This Calendar Builder** are:
* An [IDE] (https://code.visualstudio.com/) where you will write your code
* Python installed from [python official website] (https://www.python.org/downloads/)
* Then you're good to go!

First steps:
Make a file `Caledar_builder.py`
Now Code:

```
import datetime
# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('|| Calender-Builder ||')

```
* import datetime which is a python module. If you don't know about it [Check this] (https://docs.python.org/3/library/datetime.html).
* Setting up the constants Days name and months name.
* Print the Calender Builder.

**After this**
```
while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')
```
* First loop is to get the year from the user 
 * print the message 
* response variable contains input which will appear to the user to give Answer like the Year (2050)
* if condition to see the user put correct answer or not! by saying this I mean numeric value

The second loop:
* Second loop is to get the month from the user.
* And if statement to look up to the input of the user......

**After this**
```
def getCalendarFor(year, month):
    calText = '' 

    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    calText += '...Sun.....Mon....Tue..Wed...Thur....Fri....Sat..\n'

    weekSeparator = ('+----------' * 7) + '+\n'

    blankRow = ('|          ' * 7) + '|\n'
    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        calText += weekSeparator
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):  # (!) Try changing the 4 to a 5 or 10.
            calText += blankRow

        # Check if we're done with the month:
        if currentDate.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.

```
Are you still with me this one will be a bit big!

* def (declaration of Python function) getCalendarFor(year, month) will get the year and month.
* calText will contain the string of our calendar.
* 3 line will Put the month and year at the top of the calendar:
* 4 line Add the days of the week labels to the calendar:
 * Try to change the abbreviations to SUN, MON and so forth to the week days if you want.
*   `weekSeparator` The horizontal line string that separate weeks:
* `blankRow` The blank rows have ten spaces in between the | day separators:
* `  while currentDate.weekday() != 6:` Get the first date in the month. (The datetime module handles all the complicated calendar stuff for us here.)
    * `currentDate = datetime.date(year, month, 1)`
Roll back currentDate until it is Sunday. (weekday() returns 6 for Sunday, not 0.)
* `dayNumberRow` is the row with the day number labels:
*  `for i in range(3):` (!) Try changing the 4 to a 5 or 10.
* `calText = getCalendarFor(year, month)`
`print(calText)`  # Display the calendar.
### To save the printed code in a file
```
# Save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)
```

Check the code and then give me Reply!
For contacting me follow my handles.