"""Write a function that does the following operations: adding, subtracting, 
dividing, or multiplying values. It is simply referred to as variable 
operation variable. Of course, the variables have to be defined, but in this 
challenge the variables will be defined for you. All you have to do is look 
at the variables, do some string to integer conversions, use some if 
conditionals, and combine them based on the operation.
The numbers and operation will be given as strings, and you should return 
the value as a string as well.
Examples
operation('1', '2', 'add') ➞ '3'
operation('4', '5', 'subtract') ➞ '-1'
operation('6', '3', 'divide') ➞ '2'
Notes
The numbers and operation will be given as strings, and you should also 
return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide, go ahead and round down to an integer."""



operation = ('6', '2', 'multiply')

if operation[2] == "add":
    result = str(int(operation[0]) + int(operation[1]))

elif operation[2] == "subtract":
    result = str(int(operation[0]) - int(operation[1]))

elif operation[2] == "divide":
    if operation[1] == "0":
        result = "undefined"
    else:
        result = str(round(int(operation[0]) / int(operation[1])))

else:
    result = str(int(operation[0]) * int(operation[1]))

print(result)
