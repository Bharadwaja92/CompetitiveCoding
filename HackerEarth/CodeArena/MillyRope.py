""""""
"""
Milly and her friends are playing a game in which there is a straight rope that is fitted from both the sides between two walls. Now say leftmost endpoint is at 0-th coordinate and rightmost is at M-th coordinate. According to this game, every player Pi will attach balloons at each index in their particular segment [Li, Ri]. But the problem is that one part of any segment can belong to multiple players. Milly wants to know the number of indexes in her assigned segment that are disjoint to any other's segment.
Note : Starting (0) and ending (M) indexes of the rope can be used if comes in any of the segment.

Input:  First line will contain T (No. of test cases). For every test case, first line will contain four space 
separated integers : N (No. of friends), M(ending coordinate of the rope), A (starting coordinate of Milly's segment) 
and B(ending coordinate of Milly's segment).

Next each N lines will contain two space separated integers denoting Li and Ri of ith friend.
Output
For every test case, print the required answer in a new line.
SAMPLE INPUT 
1
2 10 0 5
3 7
9 10
SAMPLE OUTPUT 
3
Explanation
She can use 0, 1, 2 coordinates to attach her own balloons disjointly.
"""


t = int(input())

while t > 0:
    l1 = list(map(int, input().split(" ")))
    n, m, a, b = l1[0], l1[1], l1[2], l1[3]
    av = set(range(a, b+1))
    # print('av is', av)
    friends = []
    for i in range(n):
        f = list(map(int, input().split(" ")))
        fe = set(range(f[0], f[1]+1))
        # print('fe is', fe)
        av = av.difference(fe)
        # print('upd is', av)
    print(len(av))
    t -= 1


