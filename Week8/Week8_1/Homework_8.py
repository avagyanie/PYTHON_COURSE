"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly 
increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. 
Sequence containing only one element is also considered to be strictly increasing.

Example

    For sequence = [1, 3, 2, 1], the output should be
    solution(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    solution(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. 
    Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer sequence

    Guaranteed constraints:
    2 ≤ sequence.length ≤ 105,
    -105 ≤ sequence[i] ≤ 105.

"""


# version_1
def solution(sequence):
    n = len(sequence)
    decreasing_count = 0
    decreasing_index = -1
    for i in range(1, n):
        if sequence[i] <= sequence[i-1]:
            decreasing_count += 1
            decreasing_index = i-1
    if decreasing_count > 1:
        return False
    if decreasing_count == 0:
        return True
    if decreasing_index == 0 or decreasing_index == n-2:
        return True
    if sequence[decreasing_index-1] < sequence[decreasing_index+1] or sequence[decreasing_index] < sequence[decreasing_index+2]:
        return True
    return False

print(solution([40, 50, 60, 10, 20, 30]))



# version_2
def solution(sequence):
    error = 0
    second_error = 0
    
    for index, i in enumerate(sequence[:-1]):
        
        if sequence[index + 1] <= i:
            error += 1
            
            if index < len(sequence) - 2 and sequence[index + 2] <= i:
                second_error += 1
       
        if error <= 1 and second_error <= 1:
            
            return True
        
        return False
    
print(solution([40, 50, 60, 10, 20, 30]))
