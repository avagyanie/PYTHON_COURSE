"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between 
any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
Example
For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] integer n
    A positive even integer.
    Guaranteed constraints:
    4 ≤ n ≤ 20.
    [input] integer firstNumber
    Guaranteed constraints:
    0 ≤ firstNumber ≤ n - 1.
    [output] integer
"""


# version_1
def solution(n, firstNumber):
    if firstNumber < (n // 2):
        result = n // 2 + firstNumber
    elif firstNumber == (n // 2):
        result = 0
    else:
        result = firstNumber - (n // 2)
    return result

print(solution(10, 7))



# version_2
def solution(n, firstNumber):
    result = (firstNumber + n // 2) % n
    return result

print(solution(10, 7))
