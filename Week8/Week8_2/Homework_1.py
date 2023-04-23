"""
Using .sort() method, create a lambda function that sorts the list in descending order. 
Refrain from using the reverse parameter.
(Hint: lambda will be passed to sort method's key parameter as argument)
Please check out Hint 0 below to be informed about a glitch regarding this exercise.
lst=[100, 10, 10000, 1, 9, 999, 99]
"""



def func(lst: list):
    return sorted(lst, key = lambda x: -x)

print(func(lst = [100, 10, 10000, 1, 9, 999, 99]))
