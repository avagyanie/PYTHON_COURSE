"""
"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower 
one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, 
loves them back.
Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every 
alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.
Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"
loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
loves_me(1) ➞ "LOVES ME"
Notes
    Remember to return a string.
    The first phrase is always "Loves me".
"""



def loves_me(n):
    flower = "Loves me"
    
    if n == 1:
        flower = flower.upper()
    
    i = 1
    while i < n:
        if i != n - 1:
            if i % 2 == 0:
                flower += ", Loves me"
            else:
                flower += ", Loves me not"
        else:
            if i % 2 == 0:
                flower += ", LOVES ME"
            else:
                flower += ", LOVES ME NOT"
        i +=1
    
    return flower

print(loves_me(4))
