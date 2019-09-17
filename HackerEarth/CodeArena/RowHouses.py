"""
In the college where Utkarsh studies, all the students live in N Row Houses. The colony containing the Row Houses is a
straight line = x axis. Ith Row House is located at x = i and Ai students live in it.

Every week the students of some Row House at x=K organize a party and invite all the students living in Row Houses from
 x=L to x=R.
"""

"""
SEGMENT TREES   \_(@-@)_/
"""

t = int(input())
l1 = list(map(int, input().split(" ")))

n, q = l1[0], l1[1]

ns = list(map(int, input().split(" ")))

while q > 0:
    ip = list(map(int, input().split(" ")))
    if ip[0] == 1:
        k, l, r = ip[1], ip[2], ip[3]

    else:
        k, s = ip[1], ip[2]
