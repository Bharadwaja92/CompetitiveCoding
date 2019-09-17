""""""
"""
Aniruddha loves to code on HackerEarth. There are some type of problems which he likes the most. Problems are tagged 
with non empty strings containing only 'H' or 'E' or both. But he likes the problems tagged with strings containing 
no consecutive E's. Given an integer N, find maximum number of problems Aniruddha may like which are tagged with 
strings of length less than or equal to N.

Input: First line contains single integer, T, the number of test cases. Each of next T lines contains single integer N.

Output: For each test case output single integer, the answer to the problem i.e maximum number of problems Aniruddha 
may like which are tagged with strings of length less than or equal to N. Output answer modulo 109 + 7 (i.e. 1000000007).

Constraints:    1 ≤ T ≤ 10^6        1 ≤ N ≤ 10^6

SAMPLE INPUT 
2
2
3
SAMPLE OUTPUT 
5
10
"""

from itertools import permutations

n = 3
l = list(range(n))

print(l)

ps = list(permutations(l, n))
print(ps)

for x in range(len(ps)):
    ps[x] = ['H' if ps[x][i] % 2 == 0 else 'E' for i in range(n)]

print(ps)
