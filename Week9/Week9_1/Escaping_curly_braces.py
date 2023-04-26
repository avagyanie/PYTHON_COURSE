"""
For each challenge of this series you do not need to submit a function. Instead, you need to submit 
a template string that can formatted in order to get a certain outcome.

Write a template string according to the following example. Notice that the template will be formatted twice:
Example

a = "John"
b = "Joe"
template = "yourtemplatestringhere"

template.format(1).format(a, b) ➞ "My best friend is Joe."

Tips

Curly braces can be escaped by doubling them. In a format string, {{ and }} are literal { and } respectively.

For example:

"{} these, not these {{}}".format("Substitute") ➞ "Substitute these, not these {}"

Notes

    Submit a string, not a function.
    Do not change the name of the variable template.
    You can find all the exercises in this series over here.
"""


a = "John"
b = "Joe"
template = "My best friend is {}"

print(template.format(b))
