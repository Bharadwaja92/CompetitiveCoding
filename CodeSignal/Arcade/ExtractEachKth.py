"""
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

"""

def extractEachKth(inputArray, k):
    lt = list(reversed(list(range(k-1, len(inputArray), k))))
    print(lt)
    for v in lt:
        inputArray.pop(v)
    return inputArray

inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(extractEachKth(inputArray, k))