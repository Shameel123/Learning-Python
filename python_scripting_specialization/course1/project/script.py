
"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 12:
        return 31

    date1 = datetime.date(year,month,1)
    date2 = datetime.date(year,month+1,1)
    # try:
    #     date2 = datetime.date(year,month+1,1)
    # except:
    #     date2 = datetime.date(year,1,1)
    #     diff = date1-date2
    #
    #     return diff.days - 303

    diff = date2-date1



    return diff.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year >= datetime.MINYEAR and year <= datetime.MAXYEAR:
        #print("year gone ok")
        pass
    else:
        return False

    if month > 0 and month < 13:
        #print("month gone ok")
        pass
    else:
        return False
    if day>0 and day<= days_in_month(year,month):
        #print("day gone ok")
        pass
    else:
        return False

    return True

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    try:
        date1 = datetime.date(year1,month1,day1)
        date2 = datetime.date(year2,month2,day2)
        days = date2-date1
        if days.days < 0:
            return 0
        print(days)
        return days.days
    except:
        return 0
    #---------checks if the date1 is before date2 or not-----#
    # if days.days < 0:
    #     return 0

    #     #-------check date is proper or not---------#
    # if is_valid_date(year1, month1, day1) == False:
    #     return 0
    #
    # if is_valid_date(year2, month2, day2) == False:
    #     return 0


    return days.days


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    try:
        date = datetime.date(year,month,day)
        #print(date.day)
        bday = date.today() - date
        if bday.days < 0:
            return 0
        return bday.days
    except:
        return 0

if __name__ == '__main__':
    #print(days_in_month(2019,12))
    # for i in range(1,13):
    #     print(i)
    #     print(is_valid_date(2001,i,30))
    print(is_valid_date(1,1,1))
    print(days_between(1973, 8, 14, 1973, 8, 13))
    print(age_in_days(2017,1,1))
