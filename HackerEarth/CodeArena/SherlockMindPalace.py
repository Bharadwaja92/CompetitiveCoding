""""""
"""
Sherlock Holmes loves mind palaces! We all know that.

A mind palace, according to Mr. Holmes is something that lets him retrieve a given memory in the least time posible. 
For this, he structures his mind palace in a very special way. Let a NxM Matrix denote the mind palace of Mr. Holmes. 
For fast retrieval he keeps each row and each column sorted. Now given a memory X, you have to tell the position of the 
memory in Sherlock's mind palace.

Input
Input begins with a line containing space separated N and M.
The next N lines each contain M numbers, each referring to a memory Y.
The next line contains Q, the number of queries.
The next Q lines contain a single element X, the memory you have to search in Sherlock's mind palace.

Output
If Y is present in Mr. Holmes memory, output its position (0-based indexing).
Else output "-1 -1" (quotes for clarity only).

SAMPLE INPUT 
5 5
-10 -5 -3 4 9
-6 -2 0 5 10
-4 -1 1 6 12
2 3 7 8 13
100 120 130 140 150
3
0
-2
170
SAMPLE OUTPUT 
1 2
1 1
-1 -1
Explanation
The sample is self-explanatory.
"""
import math


def getCoord(palace, l, r, x):
    mid = -1
    while r != l and r > l:
        mid = math.ceil((l + r) // 2)
        if palace[mid] == x:
            return mid
        # print('l is', l, 'r is', r, 'Mid is', mid, 'Checking for', x)
        if palace[mid] < x:
            l = mid + 1
        else:
            r = mid
        if l == r:
            mid = l
    return mid


l1 = list(map(int, input().split(" ")))
n, m = l1[0], l1[1]
palace = []

for i in range(n):
    palace.append(list(map(int, input().split(" "))))

print('palace is\n')
print(palace)

t = int(input())

while t > 0:
    x = int(input())
    firstCol = [c[0] for c in palace]
    correctCol = firstCol[getCoord(firstCol, 0, len(firstCol), x)]
    print('correctCol is', correctCol)
    correctRow = getCoord(palace[correctCol], 0, len(palace[correctCol]), x)
    print(correctCol, correctRow)
    t -= 1

