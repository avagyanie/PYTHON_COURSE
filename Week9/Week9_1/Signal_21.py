"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating 
in a computer network that uses the Internet Protocol for communication. There are two versions of 
the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
Given a string, find out if it satisfies the IPv4 address naming rules.
Example
    For inputString = "172.16.254.1", the output should be
    solution(inputString) = true;
    For inputString = "172.316.254.1", the output should be
    solution(inputString) = false.
    316 is not in range [0, 255].
    For inputString = ".254.255.0", the output should be
    solution(inputString) = false.
    There is no first number.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] string inputString
    A string consisting of digits, full stops and lowercase English letters.
    Guaranteed constraints:
    1 ≤ inputString.length ≤ 30.
    [output] boolean
    true if inputString satisfies the IPv4 address naming rules, false otherwise.
"""


# version_1
def solution(inputString):
    lst = inputString.split(".")
    count = 0
    for i in lst:
        if len(i) > 1 and i.startswith("0"):
            return False
        if not i.isdigit():
            return False
        if 0 <= int(i) <= 255:
            count += 1
    if count == 4:
        return True
    return False

print(solution("172.316.254.1"))



# version_2
def solution(inputString):
    lst = inputString.split('.')
    return len(lst) == 4 and all(i.isdigit() and 0 <= int(i) <= 255 for i in lst)

print(solution("172.316.254.1"))
