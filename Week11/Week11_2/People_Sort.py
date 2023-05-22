"""
Given a list of people objects, create a function that sorts the list by an attribute name. 
The attribute to sort by will be given as a string.
The Person class will only include these attributes in the following order:
    firstname
    lastname
    age
Examples
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey
people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters
people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40
Notes
    Sort the list in ASCENDING order.
    All objects will be valid.
"""



def people_sort(lst, attr):
    sorted_people = sorted(lst, key = lambda x: getattr(x, attr))
    return [getattr(x, attr) for x in sorted_people]

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

print(people_sort([p1, p2, p3], "firstname"))
print(people_sort([p1, p2, p3], "lastname"))
print(people_sort([p1, p2, p3], "age"))
