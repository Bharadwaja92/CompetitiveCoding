""""""
"""
Trico is trying to impress a girl. But the girl is not showing any sign of interest to him. So his best friend suggested him to gift one Grovyle string to her. Grovlye string is a odd length string consisting of only lowercase alphabets arranged in such a way that a number X associated with it is smallest as possible.
X is calculated as : First take absolute distance of each character's position from the center of the string i.e., 
(string length/2) and then multiply the distance with its ASCII value. Similarly find all the values and add them.

Example : Given string : aaa
Here only one unique permutation is possible : aaa

distances are : for first a, d1 = 1, second a, d2 =0, third a, d3 = 1;
so X = 1 X 97 + 0 X 97 + 1 X 97 = 194;

So given a string of odd length consisting of only lowercase alphabets, find one permutation of the given string such 
that X is smallest as possible. And if there are many such strings then print the lexicographically smallest one.

Input: First line contains T, the number of test cases that follow. Next T lines, each contains one odd length string 
consisting of only lowercase alphabets.
Output: For each test case, print the desired result in separate lines.

SAMPLE INPUT 
2
aaa
abc
SAMPLE OUTPUT 
aaa
acb
"""
from itertools import permutations

t = int(input())

while t > 0:
    st = list(input())
    midVal = int(len(st)/2)
    ps = []
    for p in list(permutations(st, len(st))):
        if p[::-1] not in ps:
            ps.append(p)
    # print('ps is ', ps)
    sums = []
    for p in ps:
        mid = p[midVal]
        print('mid is', p[midVal], p, ord(mid))
        s1 = 0
        for i in range(midVal-1, -1, -1):
            print(p[i],' is at distance', i)
        # for i in range(len(p)-1, midVal, -1):
        #     print(p[i],' is at distance', i)

    t -= 1



