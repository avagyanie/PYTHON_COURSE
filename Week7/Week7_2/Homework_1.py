"""
Create a function which returns the number of true values there are in an array.
Examples
countTrue([True, False, False, True, False]) ➞ 2
countTrue([False, False, False, False]) ➞ 0
countTrue([]) ➞ 0
Notes
Return 0 if given an empty array.
All array items are of the type bool (true or false).
"""

"""
returm: count of True in list
Args: my_list(list): list of bools
Returns: int: math expretion result
"""



def countTrue(my_list: list):
    return my_list.count(True)

result = countTrue([True, False, False, True, False])
print(result)
