"""
Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.
Examples
sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
// 2 & 3 are common in all 3 lists.
sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
// 2, 2 & 3 are common in all 3 lists.
sum_common([1], [1], [2]) ➞ 0
"""


def sum_common(lst1, lst2, lst3):
    summary = 0
    for i in lst1:
        if (i in lst2) and (i in lst3):
            summary += i
            lst2.remove(i)
            lst3.remove(i)
    return summary

print(sum_common([1, 2, 2, 3, 2], [5, 3, 2, 2, 1], [7, 3, 2, 2, 1]))
