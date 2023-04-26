"""
Write a function that takes the base and height of a triangle and return its area.
Examples
tri_area(3, 2) ➞ 3
tri_area(7, 4) ➞ 14
tri_area(10, 10) ➞ 50
Notes
    The area of a triangle is: (base * height) / 2
    Don't forget to return the result.
    If you get stuck on a challenge, find help in the Resources tab.
    If you're really stuck, unlock solutions in the Solutions tab.
"""



def tri_area(base: int, height: int) -> int:
    area = base * height / 2
    return int(area)

print(tri_area(10, 10))
