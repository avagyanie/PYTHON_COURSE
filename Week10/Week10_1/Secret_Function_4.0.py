"""
Create a function based on the input and output. Look at the examples, there is a pattern.
Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"
secret("p.one") ➞ "<p class='one'></p>"
secret("p.four.five") ➞ "<p class='four five'></p>"
Notes
Input is a string.
"""



def secret(text):
    lst = text.split(".")
    new_str = " ".join(lst[1:])
    return F"<{lst[0]} class='{new_str}'></{lst[0]}'"

print(secret("p.four.five"))
