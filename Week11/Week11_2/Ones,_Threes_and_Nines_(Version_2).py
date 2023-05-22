"""
Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string 
in this format:
"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would at least take for the number of each to add up 
to the given integer when multiplied by one, three or nine (depends).
Examples
ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"
ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"
ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"
Notes
    Each of the ones, threes or nines could only be either 0, 1 or 2.
    You must use a class.
    After the comma, you must put a space.
    See version #1 of this series.
"""


class Ones_threes_nines:
    def __init__(self, num) -> None:
        self.num = num

        nines = self.num // 9
        self.num = self.num % 9
        threes = self.num // 3
        ones = self.num % 3
        print(f"nines: {nines}, threes: {threes}, ones: {ones}")

Ones_threes_nines(12)
