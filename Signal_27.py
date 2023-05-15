"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a 
digit.
Check if the given string is a correct variable name.
Example
    For name = "var_1__Int", the output should be
    solution(name) = true;
    For name = "qq-q", the output should be
    solution(name) = false;
    For name = "2w2", the output should be
    solution(name) = false.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] string name
    Guaranteed constraints:
    1 ≤ name.length ≤ 10.
    [output] boolean
    true if name is a correct variable name, false otherwise.
"""


# version_1
def solution(name):
    if name[0].isdigit():
        return False
    for i in name:
        if i == "_":
            continue
        else:
            result = i.isalnum()
            if result == False:
                return result
    return result    
print(solution("var_1__Int"))



# version_2
def solution(name):
    return name.isidentifier()
print(solution("var_1__Int"))
