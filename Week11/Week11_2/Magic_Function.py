"""
Create a class with a few functions like these examples.
    magic.replace("string", 'char', char') is a function that replaces all of the specified characters 
    with different specified characters.
    magic.str_length("string") is a function that returns the length of the string.
    magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning 
    and end.
    magic.list_slice(list, tuple) is a function that returns the items in the list that are between the 
    specified indexes. If the length of the new list is 0, return -1.
Examples
magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"
magic.str_length("hello world") ➞ 11
magic.trim("      python is awesome      ") ➞ "python is awesome"
magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]
"""


class Magic:
    @staticmethod
    def replace(string, old_char, new_char):
        return string.replace(old_char, new_char)

    @staticmethod
    def str_length(string):
        return len(string)

    @staticmethod
    def trim(string):
        return string.strip()

    @staticmethod
    def list_slice(lst, tpl):
        result = lst[tpl[0]:tpl[1] + 1]
        if len(result) > 0:
            return result
        return -1
    
magic = Magic()

print(magic.replace("AzErty-QwErty", "E", "e"))
print(magic.str_length("hello world"))
print(magic.trim("      python is awesome      "))
print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)))
