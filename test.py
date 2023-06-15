# """
# Create a function that takes a list of numbers and returns the sum of the two lowest positive 
# numbers.

# sum_two_smallest_nums([19, 5, 42, 2, 77]) ➞ 7

# sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]) ➞ 3453455

# sum_two_smallest_nums([2, 9, 6, -1]) ➞ 8

# sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]) ➞ 563

# sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]) ➞ 4519

# Notes
# Don't count negative numbers.
# Floats and empty lists will not be used in any of the test cases.
# """


# def sum_two_smallest_nums(lst):
#     positive = [i for i in lst if i > 0]
#     sorted_pos_num = sorted(positive)
#     result = sorted_pos_num[0] + sorted_pos_num[1]
#     return result

# print(sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))



# """
# Create a Person class which will have three properties:

# Name
# List of foods they like
# List of foods they hate

# In this class, create the method taste():

# It will take in a food name as a string.
# Return {person_name} eats the {food_name}.
# If the food is in the person's like list, add 'and loves it!' to the end.
# If it is in the person's hate list, add 'and hates it!' to the end.
# If it is in neither list, simply add an exclamation mark to the end.


# Examples
# p1 = Person("Sam", ["ice cream"], ["carrots"])
# p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

# p1.taste("cheese") ➞ "Sam eats the cheese!"

# p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"


# Notes
# A person can have an empty list for foods they hate and/or love.
# Check the Resources for some helpful tutorials on Python classes.
# """


# class Person:
#     def __init__(self, name, like, hate) -> None:
#         self.name = name
#         self.like = like
#         self.hate = hate
#     def taste(self, food_name):
#         if food_name in self.like:
#             return f"{self.name} eats the {food_name} and loves it!"
#         elif food_name in self.hate:
#             return f"{self.name} eats the {food_name} and hates it!"
#         else:
#             return f"{self.name} eats the {food_name}"
        
# p1 = Person("Sam", ["ice cream"], ["carrots"])
# print(p1.taste("ice cream"))

# print(p1.taste("cheese"))

# print(p1.taste("carrots"))


"""
Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z).

Examples
sort_by_letter(["932c", "832u32", "2344b"])
➞ ["2344b", "932c", "832u32"]

sort_by_letter(["99a", "78b", "c2345", "11d"])
➞ ["99a", "78b", "c2345", "11d"]

sort_by_letter(["572z", "5y5", "304q2"])
➞ ["304q2", "5y5", "572z"]

sort_by_letter([])
➞ []


Notes
Each string will only have one (lowercase) letter.
If given an empty list, return an empty list.
"""


def sort_by_letter(lst):
    if lst == []:
        return lst
    new_dct = {}
    for i in lst:
        for j in i:
            if j.isalpha():
                new_dct.setdefault(j, i)
                lst2 = list(new_dct.keys())
                lst2.sort()
                lst3 = []
                for g in lst2:
                    lst3.append(new_dct.get(g))
    return lst3

print(sort_by_letter(["99a", "78b", "c2345", "11d"]))
