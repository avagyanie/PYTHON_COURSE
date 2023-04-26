"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
Example
For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] array.integer inputArray
    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 10,
    -15 ≤ inputArray[i] ≤ 15.
    [output] integer
    The maximal absolute difference.
"""



def solution(inputArray):
    output = 0
    for index in range(len(inputArray) - 1):
        if inputArray[index + 1] - inputArray[index] > output:
            output = inputArray[index + 1] - inputArray[index]
            index += 1
        elif inputArray[index] - inputArray[index + 1] > output:
            output = inputArray[index] - inputArray[index + 1]
            index += 1

    return output

print(solution([2, 4, 1, 0]))
