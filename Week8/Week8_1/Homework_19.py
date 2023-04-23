"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""


# version_1
def solution(inputString):
    count = 0
    for i in inputString:
        if inputString.count(i) % 2 != 0:
            count += 1
            inputString = inputString.replace(i, "")

    return count <= 1
    # return inputString
    
print(solution("abccccca"))



# version_2
def solution(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1
