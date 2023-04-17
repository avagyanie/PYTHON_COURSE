"""
Create a function that takes three values:
h hours
m minutes
s seconds
Return the value that's the longest duration.
Examples
longestTime(1, 59, 3598) ➞ 1
longestTime(2, 300, 15000) ➞ 300
longestTime(15, 955, 59400) ➞ 59400
"""



def longestTime(h, m, s):
   if (h > m / 60) and (h > s / 3600):
      return h
   elif (m > s / 60) and (m > 60 * h):
      return m
   elif (s > 60 * m) and (s > 3600 * h):
      return s
   else:
      return "There are two equal values"

print(longestTime(1, 59, 3598))
