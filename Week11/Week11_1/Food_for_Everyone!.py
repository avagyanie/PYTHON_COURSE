"""
Create a Person class which will have three properties:
    Name
    List of foods they like
    List of foods they hate
In this class, create the method taste():
    It will take in a food name as a string.
    Return {person_name} eats the {food_name}.
    If the food is in the person's like list, add 'and loves it!' to the end.
    If it is in the person's hate list, add 'and hates it!' to the end.
    If it is in neither list, simply add an exclamation mark to the end.
Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
p1.taste("cheese") ➞ "Sam eats the cheese!"
p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"
Notes
    A person can have an empty list for foods they hate and/or love.
    Check the Resources for some helpful tutorials on Python classes.
"""


class Person:
    def __init__(self, name, like, hate) -> None:
        self.name = name
        self.like = like
        self.hate = hate
    def taste(self, food):
        self.food = food
        if food in self.like:
            return F"{self.name} eats the {self.food} and loves it!"
        elif food in self.hate:
            return F"{self.name} eats the {self.food} and hates it!"
        return f"{self.name} eats the {self.food}!"
    
p1 = Person("Sam", ["ice cream"], ["carrots"])

print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))
