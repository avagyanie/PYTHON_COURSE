"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]

the output should be

solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]
"""


# version_1
def solution(picture):
    pic = [(len(picture[0]) + 2) * "*"]
    for i in range(len(picture)):
        pic += ["*" + picture[i] + "*"]
    
    return pic +[pic[0]]

print(solution(["abc", "ded"]))



# version_2
def solution(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]
