"""
In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, 
as follows:
    0 = [ ] is the empty set
    1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
    2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
    n = n−1 ∪ [ n−1 ] = ...
Write a function that receives an integer n and produces the representing set.
Examples
rep_set(0) ➞ []
rep_set(1) ➞ [[]]
rep_set(2) ➞ [[], [[]]]
rep_set(3) ➞ [[], [[]], [[], [[ ]]]]
Notes
    Make sure to use list brackets [,].
    Technically we should use set brackets {,} instead, but Python doesn't approve.
    A neat feature of this representation is that n < m precisely if the set representing n is contained 
    in the set representing m.
"""


# version_1
def rep_set(n):
    result = []
    for i in range(n):
        result = result + [result]
    return result

print(rep_set(3))


# version_2
def rep_set(n):
    result = []
    for i in range(n):
        result.append(result[:])
    return result
print(rep_set(0))  
print(rep_set(1))  
print(rep_set(2)) 
print(rep_set(3))
