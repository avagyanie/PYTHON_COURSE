"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky 
if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    solution(n) = true;
    For n = 239017, the output should be
    solution(n) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    A ticket number represented as a positive integer with an even number of digits.

    Guaranteed constraints:
    10 ≤ n < 106.

    [output] boolean

    true if n is a lucky ticket number, false otherwise.

"""



def solution(n):
    num = str(n)
    first = num[:len(num) // 2]
    last = num[len(num) // 2:]
    first_count = 0
    last_count = 0
    for i in first:
        first_count += int(i)
    for j in last:
        last_count += int(j)
        
    return first_count == last_count
        
print(solution(239017))



# version_2
def solution(n):
    s = [int(x) for x in str(n)]
    l = int(len(s)/2)    
    return sum(s[:l]) == sum(s[l:])

print(solution(239017))