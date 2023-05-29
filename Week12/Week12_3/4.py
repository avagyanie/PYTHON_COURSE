"""
Using filter function, filter the even numbers so that only odd numbers are passed to the new list.
"""


# version_1
def odd(num):
    return num % 2

lst = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(odd, lst))
print(result)



# version_2
result = list(filter(lambda n: n % 2, [1, 2, 3, 4, 5, 6, 7, 8]))
print(result)
