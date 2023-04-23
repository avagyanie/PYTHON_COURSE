"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string s1

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ s1.length < 15.

    [input] string s2

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ s2.length < 15.

    [output] integer

"""



# version_1
def solution(s1, s2):
    count = 0
    for i in set(s1):
        count += min(s1.count(i), s2.count(i))
    return count


print(solution("aabcc", "adcaa"))



# version_2
def solution(s1, s2):
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))

print(solution("aabcc", "adcaa"))
