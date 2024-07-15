from datetime import datetime

def backADay(date: datetime): 
    """
    Takes a datetime object as input and subtracts a day from it, returning a 
    new datetime objecty with the appropriate date. 
    """
    if date.month == 1 and date.day == 1:
        return datetime(date.year - 1, 12, 31, date.hour, date.minute, date.second)
    elif date.day == 1: 
        prevMonth = date.month - 1
        currentYear = date.year
        thirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
        thirtyDays = [4, 6, 9, 11]
        if prevMonth in thirtyOneDays: 
            return datetime(date.year, prevMonth, 31, date.hour, date.minute, date.second) 
        elif prevMonth in thirtyDays: 
            return datetime(date.year, prevMonth, 30, date.hour, date.minute, date.second) 
        else: # prev month is Feb 
            if ( currentYear % 4 == 0 and currentYear % 100 != 0 ) or ( currentYear % 400 == 0 ):
                return datetime(date.year, prevMonth, 29, date.hour, date.minute, date.second)
            else:
                return datetime(date.year, prevMonth, 28, date.hour, date.minute, date.second)

    else: 
        return datetime(date.year, date.month, date.day - 1, date.hour, date.minute, date.second)