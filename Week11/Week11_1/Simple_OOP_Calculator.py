"""
Create methods for the Calculator class that can do the following:
    Add two numbers.
    Subtract two numbers.
    Multiply two numbers.
    Divide two numbers.
Examples
calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2
Notes
    The methods should return the result of the calculation.
    Don't worry about needing to handle division by zero errors.
    See the Resources tab for some helpful tutorials on Python classes.
"""

# version_1
class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a // b
        return "Can't do this operation"

calculator = Calculator()

print(calculator.add(10, 5))

print(calculator.subtract(10, 5))

print(calculator.multiply(10, 5))

print(calculator.divide(10, 5))



# version_2
class Calculator:
    def __init__(self, a, b) -> None:
        self.add = a + b
        self.subtract = a - b
        self.multiply = a * b
        if b != 0:
            self.divide = a // b
        else:
            self.divide = "Can't do this operation"

calculator = Calculator(10, 2)

print(calculator.add)

print(calculator.subtract)

print(calculator.multiply)

print(calculator.divide)
