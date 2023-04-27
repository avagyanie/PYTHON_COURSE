"""
Python got drunk and the built-in functions str() and int() are acting odd:
str(4) ➞ 4
str("4") ➞ 4
int("4") ➞ "4"
int(4) ➞ "4"
You need to create two functions to substitute str() and int(). A function called int_to_str() that converts 
integers into strings and a function called str_to_int() that converts strings into integers.
Examples:
int_to_str(4) ➞ "4"
str_to_int("4") ➞ 4
int_to_str(29348) ➞ "29348"
Notes
    This is meant to illustrate the dangers of using already-existing function names.
    Extra points if you can de-drunk Python.
"""



def int_to_str(num):
    return str(num)

def str_to_int(string):
    return int(string)

import builtins

def str(obj):
    if type(obj) == int:
        return int_to_str(obj)
    else:
        return obj

def int(obj):
    if type(obj) == str:
        return str_to_int(obj)
    else:
        return obj

# reload the builtins module to replace the original str and int functions
builtins.str = str
builtins.int = int


print(func(4))
