"""
Create a function based on the input and output. Look at the examples, there is a pattern.
Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"
secret("p.one") ➞ "<p class='one'></p>"
secret("p.four.five") ➞ "<p class='four five'></p>"
Notes
Input is a string.
"""



def secret(txt):
    new_txt = ""
    l = txt.split(".")
    first = l[0]
    last = " ".join(l[1:])
    return f"<{first} class='{last}'></{first}>"

print(secret("p.one.two.three"))
