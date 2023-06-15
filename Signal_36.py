"""
Given a string, find the number of different characters in it.
Example
For s = "cabca", the output should be
solution(s) = 3.
There are 3 different characters a, b and c.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] string s
    A string of lowercase English letters.
    Guaranteed constraints:
    3 ≤ s.length ≤ 1000.
    [output] integer
"""


# version_1
def solution(s):
    dif = set()
    for i in s:
        dif.add(i)
    return len(dif)

print(solution("cabca"))


# version_1
def solution(s):
    return len(set(s))

print(solution("cabca"))
