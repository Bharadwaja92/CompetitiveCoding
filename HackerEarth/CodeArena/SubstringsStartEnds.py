""""""
"""
Given a string S of length N consisting of only lower-case English alphabets, you will be asked to process Q queries 
over it . In each query you will be given two lower case characters X and Y. Your task is to find out the number of 
such substrings of the the string S which have the characters X and Y on either of its end points, both X...Y and Y...X 
are considered to be valid. 
Note : Substrings length should be greater than 1. 

Input:  The first line of the input will contain N , the length of the string.  Next line will contain as string of 
length N. Next line will will contain Q , the number of queries. Then Q subsequent lines will contain two lowercase 
characters X and Y separated by a space.

Output:
For each query , output the answer in a separate line.

Constraints:
SAMPLE INPUT 
5
aacbb
2
a c
a b
SAMPLE OUTPUT 
2
4
Explanation
For the first query, the possible substrings are  and  . Hence the answer is 2. 
For the second query, the possible substrings are  ,  ,  , and  , hence making a total of 4 substrings.
"""

n = int(input())
s = input()
q = int(input())

while q > 0:
    l1 = input().split(' ')
    fc, lc = l1[0], l1[1]
    count, i = 0, 0

    fcpos = [i for i in range(n) if s[i] == fc]
    lcpos = [i for i in range(n) if s[i] == lc]

    # print(fcpos)
    # print(lcpos)

    for f in fcpos:
        x1 = [i for i in lcpos if i > f]
        # print('x1 is', x1)
        count += len(x1)

    # print('-'*50)

    for f in fcpos:
        x1 = [i for i in lcpos if i < f]
        # print('x1 is', x1)
        count += len(x1)

    print(count)

    q -= 1


"""
10
sdqonsvqzf
5
d d
s q
v p
i w
r n

sdq, sdqonsvq, sdq, sdqonsvq

"""




