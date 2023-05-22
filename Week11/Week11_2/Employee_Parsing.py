"""
In the class Employee, implement the instance attributes as firstname, lastname and salary.
Create the method from_string() which parses a string containing these attributes and assigns them to the 
correct properties. Properties will be separated by a dash.
Examples
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

emp1.firstname ➞ "Mary"
emp1.salary ➞ 60000
emp2.firstname ➞ "John"
emp2.salary ➞ 55000

Notes
    The salary is an integer.
    Check the Resources for some helpful tutorials on how to do this.
"""


class Employee:
    def __init__(self, firstname, lastname,  salary) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    @staticmethod
    def from_string(text):
        text = text
        lst = text.split("-")
        firstname = lst[0]
        lastname = lst[1]
        salary = int(lst[2])
        return Employee(firstname, lastname, salary)

emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.firstname)
print(emp1.salary)
print(emp2.firstname)
print(emp2.salary)
