"""
Create a function that takes the month and year (as integers) and 
returns the number of days in that month.
Examples
days(2, 2018) ➞ 28
days(4, 654) ➞ 30
days(2, 200) ➞ 28
days(2, 1000) ➞ 28
Notes
Don't forget about leap years!
"""



thirty = [4, 6, 9, 11]
thirty_one = [1, 3, 5, 7, 8, 10, 12]

def days(month, year):
    if month in thirty:
        return 30
    elif month in thirty_one:
        return 31
    else:
        if year % 400 == 0:
            return 29
        elif year % 4 == 0 and year % 100 != 0:
            return 29
        else:
            return 28

print(days(2, 2018))
