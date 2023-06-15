"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.
Example
For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:
    2 + 3 = 5;
    3 + 5 = 8;
    5 + 1 = 6;
    1 + 6 = 7.
    Thus, the answer is 8.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] array.integer inputArray
    Array of positive integers.
    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 105,
    1 ≤ inputArray[i] ≤ 1000.
    [input] integer k
    An integer (not greater than the length of inputArray).
    Guaranteed constraints:
    1 ≤ k ≤ inputArray.length.
    [output] integer
    The maximal possible sum.
"""


# version_1
# def solution(inputArray, k):
#     m = 0
#     s = set()
#     for i in range(len(inputArray) - (k - 1)):
#         s.add(sum(inputArray[m:k + m]))
#         m += 1
#     return max(s)

# print(solution([2, 3, 5, 1, 6], 2))



# version_2
# def solution(inputArray, k):
#     s = set()
#     while True:
#         s.add(sum(inputArray[0:k]))
#         inputArray.remove(inputArray[0])
#         if len(inputArray) < k:
#             break
#     return max(s)

# print(solution([2, 3, 5, 1, 6], 2))
