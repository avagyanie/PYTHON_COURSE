"""
Write a map function that adds plus 5 to each item in the list.
"""


def plus_5(num):
    return num + 5

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map(plus_5, lst))
print(result)
