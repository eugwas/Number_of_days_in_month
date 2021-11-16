# -*- coding: utf-8 -*-
"""
Get number of days in month from entered values.
"""

class Number_Of_Days_In_Month:
    
    def __init__(self, month, year):
        self.month = month
        self.year = year
        
    def is_leap_year(self, year):
        if year < 1 or year > 9999:
            return False
        elif year % 4 != 0:
            return False
        elif year % 100 == 0 and year % 400 != 0:
            return False
        return True
    
    def get_days_in_month(self, month, year):
        leap_year = self.is_leap_year(year)
        if month < 1 or month > 12 or year < 1 or year > 9999:
            print('Invalid number of the month.')
            return -1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        elif month == 2 and leap_year == True:
            return 29
        elif month == 2 and leap_year == False:
            return 28
        return 31
    

# %%
while True:
    try:
        month = int(input('Enter the number of month >>> '))
        year = int(input('Enter the number of year >>> '))
        break
    except:
        print('Wrong value. Enter the integer number')
        
number_of_days_in_month = Number_Of_Days_In_Month(month, year)
print(f'Number of days = {number_of_days_in_month.get_days_in_month(month, year)}')