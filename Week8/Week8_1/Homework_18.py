"""
You are given an array of integers. On each move you are allowed to increase exactly one of its 
element by one. Find the minimal number of moves required to obtain a strictly increasing sequence 
from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
"""


# version_1
# def solution(inputArray):
#     count = 0
#     i = 1
#     while i < len(inputArray):
#         if inputArray[i - 1] >= inputArray[i]:
#             inputArray[i] += 1
#             count += 1
#             i -= 1
#         i += 1
#     return count

# print(solution([1, 1, 1, 1, 1]))




# version_2
def solution(inputArray):
    moves = 0
    prev = inputArray[0]
    for i in range(1, len(inputArray)):
        if inputArray[i] <= prev:
            diff = prev - inputArray[i] + 1
            inputArray[i] += diff
            moves += diff
        prev = inputArray[i]
    return moves



# version_3
def solution(inputArray):
    a = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            f = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
            a += f
    return a
