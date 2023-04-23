"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair 
of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

    For a = [1, 2, 3] and b = [1, 2, 3], the output should be
    solution(a, b) = true.

    The arrays are equal, no need to swap any elements.

    For a = [1, 2, 3] and b = [2, 1, 3], the output should be
    solution(a, b) = true.

    We can obtain b from a by swapping 2 and 1 in b.

    For a = [1, 2, 2] and b = [2, 1, 1], the output should be
    solution(a, b) = false.

    Any swap of any two elements either in a or in b won't make a and b equal.
"""


# version_1
def solution(a, b):
    new_arr = []
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            new_arr.append([a[i], b[i]])
    if count == 0 or count == 2 and new_arr[0] == new_arr[1][::-1]:
        return True
    return False
    
print(solution([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], 
               [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))



# version_2
def solution(a, b):
    return sorted(a) == sorted(b) and sum([a != b for a, b in zip(a, b)]) <= 2


# version_3
def solution(a, b):

    r = []
    for i in range(len(a)):
        if a[i] != b[i]:
            r.append([a[i],b[i]])
            
    if len(r) == 0 or len(r) == 2 and r[0] == r[1][::-1]:
        return True
    return False
