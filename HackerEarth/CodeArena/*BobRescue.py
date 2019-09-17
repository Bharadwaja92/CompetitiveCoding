""""""
"""
Today is a very hot day for rescuer Bob. And right now he's just noticed new sinking drunk man in the sea! Let's assume 
that resort is Euclidean plane and the shoreline is y=0 line. The sea is everything above y=0. And 
respectively everything below y=0 is a beach. The Bob's speed on the land equals to v1, and his speed while swimming equals to v2.
Now Bob is at point (x1, y1) and the sinking man is at point (x2, y2). 
What is the minimum time Bob need to get to the poor fellow and rescue his life?

In one test file you have to handle T test cases.

Input

The first line contains one integer T denoting the number of test cases. The following T lines describe test cases.
The first and the only line of each test case contains 6 space-separated integers: x1, y1, x2, y2, v1, v2

Output

Output the minimum required time with exactly 5 digits after decimal point.

SAMPLE INPUT 
1
3 -20 3 25 40 5
SAMPLE OUTPUT 
5.50000

1
369815192 -999974109 -999997167 368786142 24813 11473
>  98261.67680

1
1 -1 3 1 1 1
"""


def getTimeUtil(x1, x2, y1, y2, v):
    return ((((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))) ** 0.5) / v


def getTime(xcross, ycross, v1, v2):
    return getTimeUtil(x1, xcross, y1, 0, v1) + getTimeUtil(xcross, x2, 0, y2, v2)


t = int(input())

while t > 0:
    l1 = list(map(int, input().split(" ")))
    x1, y1, x2, y2, v1, v2 = l1[0], l1[1], l1[2], l1[3], l1[4], l1[5]
    # UniModal function
    if x1 > x2:
        x1, x2 = x2, x1
    res, a, b = 10**9, x1, x2

    while a <= b:
        if a == b:
            res = min([res, getTime(a, 0, v1, v2)])
            break
        # Doing a Ternary Search
        m1 = a + (b - a) / 3
        m2 = b - (b - a) / 3
        time1 = getTime(m1, 0, v1, v2)
        time2 = getTime(m2, 0, v1, v2)

        if time1 > time2:
            res = min([res, time2])
            a = m1 + 1
        elif time1 < time2:
            res = min([res, time1])
            b = m2 - 1
        else:
            res = min([res, time1])
            a = m1 + 1
            b = m2 - 1

    print('res is', res)
    print('{0:.5f}'.format(res))
    print(m1, m2)

    t -= 1



"""
    v1 = 1
    v2 = 1
    a = v2-v1
    b = (v2-v1)*2*(x1-x2)
    c = (v2-v1)*((x1+x2)**2 + (2*x1*x2) + (v2*y2*y2 - v1*y1*y1))
    d = 2*x1*x2*x2*(v2-v1) + (2*x1*y2*y2*v2) + (2*x2*y1*y1*v1)
    e = 1*((v2-v1)*(x1*x1*x2*x2) + (v2*x1*x1*y2*y2) + (v1*x2*x2*y1*y1))

    coeffs = [a, b, c, d, e]
    print(np.roots(coeffs))
"""
