"""
Create a function that validates whether a number n is within the bounds of lower and upper. 
Return false if n is not an integer.
Examples
intWithinBounds(3, 1, 9) ➞ true
intWithinBounds(6, 1, 6) ➞ false
intWithinBounds(4.5, 3, 8) ➞ false
Notes
The term "within bounds" means a number is considered equal or greater than a lower bound and lesser 
(but not equal) to an upper bound, (see example #2).
Bounds will be always given as integers.
"""



# version_1
# def intWithinBounds(n, first_num, last_num):
#     match type(n) != int:
#         case True:
#             return False
#         case _:
#             match n >= first_num and n < last_num:
#                 case True:
#                     return True
#                 case _:
#                     return False

# print(intWithinBounds(4.5, 3, 8))


# version_2
def intWithinBounds(n, lower, upper):
    if not isinstance(n, int):
        return False
    if lower <= n < upper:
        return True
    return False

result = intWithinBounds(4.5, 3, 8)
print(result)
