"""
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiplyNums("2, 3") ➞ 6
multiplyNums("1, 2, 3, 4") ➞ 24
multiplyNums("54, 75, 453, 0") ➞ 0
multiplyNums("10, -2") ➞ -20
Notes
Bonus: Try to complete this challenge in one line!
"""



# version_1
def multiplyNums(str_num: str):
    lst_num = str_num.split(",")
    mult = 1
    for i in lst_num:
        rep = int(i.strip())
        mult *= rep
    return mult

result = multiplyNums("10, -2")
print(result)
    


# version_2
def multiplyNums(str_num: str):
    return eval(str_num.replace(', ', '*'))

print(multiplyNums("1, 2, 3, 4"))
