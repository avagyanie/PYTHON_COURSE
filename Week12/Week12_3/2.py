"""
Write a map function that adds "Hello, " in front of each item in the list.
"""

# version_1
def add_in_front(txt):
    return "Hello, " + txt

lst = ["Ani", "Suren", "Narine", "Naira", "Varsenik"]
result = list(map(add_in_front, lst))
print(result)



# version_2
def add_in_front(txt):
    return f"Hello, {txt}!"

lst = ["Ani", "Suren", "Narine", "Naira", "Varsenik"]
result = list(map(add_in_front, lst))
print(result)



# version_3
lst = ["Ani", "Suren", "Narine", "Naira", "Varsenik"]
result = list(map(lambda x: "Hello, " + x, lst))
print(result)
