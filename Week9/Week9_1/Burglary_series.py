"""
Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. 
Is it gone?!
Given a dictionary of the stolen items and a string in lowercase representing the name of the pet 
(e.g. "rambo"), return:
    "Rambo is gone..." if the name is on the list.
    "Rambo is here!" if the name is not on the list.
Note that the first letter of the name in the return statement is capitalized.
Examples
 items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
} ➞ "Timmy is gone..."
# Timmy is in the dictionary.

 items = {
  "tv": 30,
  "stereo": 50,
} ➞ "Timmy is here!"
# Timmy is not in the  dictionary.

items = { } ➞ "Timmy is here!"
# Timmy is not in the dictionary.

Notes
N/A
"""


# version_1
def pet(input_dict: dict) -> str:
    name = "Rambo"
    if name.lower() in input_dict:
        return f"{name} is gone..."
    return f"{name} is here!"

my_dict = {
  "tv": 30,
  "rambo": 20,
  "stereo": 50,
}
print(pet(my_dict))



# version_2
def pet(input_dict: dict, pet_name: str) -> str:
    if pet_name.lower() in input_dict:
        return f"{pet_name.capitalize()} in gone..."
    return f"{pet_name.capitalize()} is here!"

print(pet({
  "tv": 30,
  "rambo": 20,
  "stereo": 50,
}, "rambo"))
