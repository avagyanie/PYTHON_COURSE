"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.
Assume that you are jumping from the point with coordinate 0 to the right. 
You are allowed only to make jumps of the same length represented by some integer.
Find the minimal length of the jump enough to avoid all the obstacles.

Example
For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] array.integer inputArray
    Non-empty array of positive integers.
    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 1000,
    1 ≤ inputArray[i] ≤ 1000.
    [output] integer
    The desired length.
"""



def solution(inputArray):
    jump_length = 1
    while True:
        for i in inputArray:
            if i % jump_length == 0:
                break
        else:
            return jump_length
        jump_length += 1

print(solution([5, 3, 6, 7, 9]))
