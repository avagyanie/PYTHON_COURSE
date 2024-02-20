"""EXTRA Knowledge
Create a function that takes two numbers as arguments num, length and 
returns a list of multiples of num until the list length reaches length.
Examples
7, 5 ➞ [7, 14, 21, 28, 35]
12, 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
17, 6 ➞ [17, 34, 51, 68, 85, 102]"""



first_number = 7
length = 5
lst = [first_number]

for i in range(length - 1):
    lst.extend([lst[i] + lst[0]])

print(lst)
