"""
Return product of integer lists.
"""


# version_1    If you mean map
def product(n1, n2):
    return n1 * n2

lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
result = list(map(product, lst1, lst2))
print(result)



# version_2    If you mean reduce
from functools import reduce

def product(n1, n2):
    return n1 * n2

lst = [1, 2, 3, 4, 5, 6, 7, 8]

print(reduce(product, lst))
