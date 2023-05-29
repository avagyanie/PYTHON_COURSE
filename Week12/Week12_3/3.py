"""
Using filter() function filter the list so that only negative numbers are left.
"""


# version_1
def negative(num):
    return num < 0

lst = [1, 0, -1, 20, -32, 100, -25, 5, -500]
result = list(filter(negative, lst))
print(result)


# version_2
result = list(filter(lambda n: n < 0, [1, 0, -1, 20, -32, 100, -25, 5, -500]))
print(result)
