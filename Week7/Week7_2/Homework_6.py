"""
Given a sentence, create a function that replaces every "a" as an article with "an absolute". 
It should return the same string without any change if it doesn't have any "a".
Examples
absolute("I am a champion!!!") ➞ "I am an absolute champion!!!"
absolute("Such an amazing bowler.") ➞ "Such an amazing bowler."
absolute("A man with no haters.") ➞ "An absolute man with no haters."
Notes
Watch for uppercase letters as shown in example #3.
"""



def absolute(text: str):
    words = text.split()
    result = []
    for i in words:
        if i.lower() != "a":
            result.append(i)
        else:
            rep = i.replace("a", "an absolute").replace("A", "An absolute")
            result.append(rep)
    return " ".join(result)

print(absolute("A man with no haters."))
