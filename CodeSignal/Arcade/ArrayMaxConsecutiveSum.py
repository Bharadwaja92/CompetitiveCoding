"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""

def arrayMaxConsecutiveSum(inputArray, k):
    sum0 = sum(inputArray[:k])
    sum1 = sum0
    for i in range(1, len(inputArray)-k+1):
        sum1 = sum1 - inputArray[i-1] + inputArray[i+k-1]
        if sum1 > sum0:
            sum0 = sum1
    return sum0

inputArray = [2, 3, 5, 1, 6]
k = 2

print(arrayMaxConsecutiveSum(inputArray, k))