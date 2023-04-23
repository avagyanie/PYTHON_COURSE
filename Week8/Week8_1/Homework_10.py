"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.string inputArray

    A non-empty array.

    Guaranteed constraints:
    1 ≤ inputArray.length ≤ 10,
    1 ≤ inputArray[i].length ≤ 10.

    [output] array.string

    Array of the longest strings, stored in the same order as in the inputArray.

"""



# version_1
def solution(inputArray):
    inputArray.sort(key = len)
    result = []
    for i in inputArray:
        if len(i) == len(inputArray[-1]):
            result.append(i)
                
    return result

print(solution(["abc", "eeee", "abcd", "dcd"]))



# version_2
def solution(inputArray):
    m = max(len(s) for s in inputArray)
    result = [s for s in inputArray if len(s) == m]
    return result

print(solution(["abc", "eeee", "abcd", "dcd"]))



# version_3
def solution(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]

print(solution(["abc", "eeee", "abcd", "dcd"]))
