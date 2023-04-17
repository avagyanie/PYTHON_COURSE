"""
Create a function that takes a string road and returns the car that's in first place. 
The road will be made of "=", and cars will be represented by letters in the alphabet.
Examples
firstPlace("====b===O===e===U=A==") ➞ "A"
firstPlace("e==B=Fe") ➞ "e"
firstPlace("proeNeoOJGnfl") ➞ "l"
Notes
Return "No car available" if there is no car on the road and "No road available" if there is no road.
"""



def firstPlace(road: str):
    cars = ""

    if not road:
        return "No road available"
    
    cars = [i for i in road if i.isalpha()]
    
    if cars:
        return cars[-1]
    else:
        return "No car available"

print(firstPlace("====b===O===e===U=A=="))
