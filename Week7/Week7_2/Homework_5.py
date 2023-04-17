"""
Create a function that takes a string and censors words over four characters with *.
Examples
censor('The code is fourty') ➞ 'The code is ******'
censor('Two plus three is five') ➞ 'Two plus ***** is five'
censor('aaaa aaaaa 1234 12345') ➞ 'aaaa ***** 1234 *****'
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word.
"""



def censor(text: str):
    words = text.split()
    result = []
    for i in words:
        if len(i) <= 4:
            result.append(i)
        else:
            rep = i.replace(i, len(i) * "*")
            result.append(rep)
    return " ".join(result)

print(censor("aaaa aaaaa 1234 12345"))
