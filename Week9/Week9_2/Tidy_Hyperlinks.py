"""
Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier 
like this. Notice how the text "Go to the challenges!" appears when hovering over the link.
This was achieved by using this code:
[this](https://edabit.com/challenges "Go to the challenges!")
Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.
Examples

tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the challenges!")"

tidy_link("https://www.google.com", "Google", "Google Search") ➞ "[Google](https://www.google.com "Google Search")"

tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!") ➞ "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"

Notes

    Supply double quotes for the hover text.
    Keep in mind that some tests will not include an argument for hover_text.
"""



def tidy_link(url, name, hover_text = None):
    if hover_text:
        return f'[{name}]({url} "{hover_text}")'
    return f'[{name}]({url})'

print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
