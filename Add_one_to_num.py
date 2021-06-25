"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
"""

def plusOne(arr):
    str_result=''
    result = []
    for i in range(len(arr)):
        str_result += str(arr[i])
    int_result = str(int(str_result)+1)
    for i in range(len(int_result)):
        result.append(int(int_result[i]))
    return result
print(plusOne([1, 2, 3]))