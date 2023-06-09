"""
Create a function that takes a string txt and censors any word from a given list lst. 
The text removed must be replaced by the given character char.
Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
Notes
N/A
"""



def censor_string(txt, lst, char):
    words = txt.split()
    for i in range(len(words)):
        for j in lst:
            if words[i].strip(".,!?").lower() in j.lower():
                words[i] = char * len(words[i])
    return " ".join(words)

print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
