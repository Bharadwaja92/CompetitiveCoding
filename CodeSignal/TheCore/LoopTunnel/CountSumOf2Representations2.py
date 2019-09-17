""""""
"""
Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
countSumOfTwoRepresentations2(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.
"""

def countSumOfTwoRepresentations2(n, l, r):
    ns = list(range(l, r + 1))
    print(ns)
    count = 0
    for i in range(len(ns)):
        for j in range(i, len(ns)):
            # print(ns[i], ns[j])
            if ns[i] + ns[j] == n:
                count += 1
    return int(min(n / 2 - l, r - n / 2) + 1) if l <= n / 2 <= r else 0
    # return count


n, l, r = 6, 2, 4
print(countSumOfTwoRepresentations2(n, l, r))
n, l, r = 10, 9, 11
print(countSumOfTwoRepresentations2(n, l, r))
n, l, r = 6, 3, 3
print(countSumOfTwoRepresentations2(n, l, r))
n, l, r = 24, 8, 16
print(countSumOfTwoRepresentations2(n, l, r))
n, l, r = 93, 24, 58
print(countSumOfTwoRepresentations2(n, l, r))


