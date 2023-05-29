"""
Using map() and filter() functions add 2000 to the values below 8000.
"""


# version_1
def below(num):
    return num > 8000

def add(n):
    return n + 2000

lst = [1, 2, 8001, 3, 8050, 9000, 10000, 4, 15000]
result = list(map(add, list(filter(below, lst))))
print(result)



# version_2
result = list(map(lambda x: x + 2000, list(filter(lambda y: y > 8000, lst))))
print(result)
