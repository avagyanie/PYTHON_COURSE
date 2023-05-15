"""
Check if all digits of the given integer are even.
Example
    For n = 248622, the output should be
    solution(n) = true;
    For n = 642386, the output should be
    solution(n) = false.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] integer n
    Guaranteed constraints:
    1 ≤ n ≤ 109.
    [output] boolean
    true if all digits of n are even, false otherwise.
"""


# version_1
def solution(n):
    for i in str(n):
        if int(i) % 2:
            return False
    return True

print(solution(642386))


# version_2
def solution(n):
    return sum([int(i)%2 for i in str(n)])==0

print(solution(642386))
