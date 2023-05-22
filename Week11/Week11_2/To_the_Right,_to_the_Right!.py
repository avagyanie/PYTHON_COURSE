"""
Create a class that imitates a select screen. For simplicity, the cursor can only move right!
In the display method, return a string representation of the list, but with square brackets around the 
currently selected element. Also, create the method to_the_right, which moves the cursor one element to the 
right.
The cursor should start at index 0.
Examples
menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"

menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"

Notes
The cursor should wrap back round to the start once it reaches the end.
"""



class Menu:
    def __init__(self, lst) -> None:
        self.lst = lst
        self.index = 0
    def display(self):
        new = [str(i) for i in self.lst]
        new[self.index] = f"[{new[self.index]}]"
        return "[" + ", ".join(new) + "]"
    def to_the_right(self):
        self.index = (self.index + 1) % len(self.lst)
    
        

menu = Menu([1, 2, 3])
print(menu.display())

menu.to_the_right()
print(menu.display())

menu.to_the_right()
print(menu.display())

menu.to_the_right()
print(menu.display())
