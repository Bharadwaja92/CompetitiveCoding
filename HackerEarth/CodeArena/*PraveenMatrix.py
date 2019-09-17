""""""
"""         DFS
Praveen went crazy yesterday and created an arbitrary matrix consisting of 0, 1 or 2. There was no rule observed in 
forming this matrix. But then he made up some rules himself.
If there are adjacent , they are said to be connected. Similarly, if there are adjacent , they are said to be connected.
Here adjacent means all the surrounding positions along with the diagonal positions.

Now given a matrix of 0, 1 or 2, do your computation according to the following rules:
If there is a path from any position in top row to any position in bottom row consisting only of 1, then print 1.
If there is a path from any position in first column to any position in last column consisting only of 2, then print 2.
If both Rule 1 & Rule 2 are true, print AMBIGUOUS.
If none of Rule 1, Rule 2 or Rule 3 satisfies, print 0.

Input format: First line of input contains a positive integer N, the size of matrix. Then N line follows, each 
containing N integers which are either 0, 1 or 2.

Output format: Print a single line containing the output according to the rule mentioned. Clearly, the output can only 
be 0, 1, 2 or AMBIGUOUS.

Example

4
0 0 0 0
2 0 1 0
0 2 1 2
0 1 2 0

Here the output is 2, as there is a connected path of 2 from first column to last column.

SAMPLE INPUT 
3
0 0 1
0 1 2
2 2 1
SAMPLE OUTPUT 
AMBIGUOUS
Explanation
In the sample input, there is a connected path of 1 from first row to last row, and there is a connected path of 2 from 
first column to last column as well. So, the result is AMBIGUOUS.
"""


def findpath(matrix, x, y, n, pathnum):
    # if matrix[x][y] == pathnum:
    #     print('--> Entering point x =', x, 'y =', y, 'n =', n)
    global count
    global visited
    global flag

    if x == n - 1 and pathnum == 1:  # Base case     and y == n - 1
        count += 1
        flag = True
    if y == n - 1 and pathnum == 2:  # Base case     and y == n - 1
        count += 1
        flag = True
    else:
        if x + 1 < n and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go east
            visited[x][y] += 1
            findpath(matrix, x + 1, y, n, pathnum)
            visited[x][y] -= 1
        if y + 1 < n and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go south
            visited[x][y] += 1
            findpath(matrix, x, y + 1, n, pathnum)
            visited[x][y] -= 1
        if x + 1 < n and y + 1 < n and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go south-east
            visited[x][y] += 1
            findpath(matrix, x + 1, y + 1, n, pathnum)
            visited[x][y] -= 1

        if x - 1 >= 0 and y + 1 < n and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go south-west
            visited[x][y] += 1
            findpath(matrix, x - 1, y + 1, n, pathnum)
            visited[x][y] -= 1
        if x - 1 >= 0 and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go west
            visited[x][y] += 1
            findpath(matrix, x - 1, y, n, pathnum)
            visited[x][y] -= 1
        if x + 1 < n and y - 1 >= 0 and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go north-east
            visited[x][y] += 1
            findpath(matrix, x + 1, y - 1, n, pathnum)
            visited[x][y] -= 1
        if y - 1 >= 0 and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go north
            visited[x][y] += 1
            findpath(matrix, x, y - 1, n, pathnum)
            visited[x][y] -= 1
        if x + 1 < n and y - 1 >= 0 and matrix[x][y] == pathnum and visited[x][y] < 1:  # Go north-east
            visited[x][y] += 1
            findpath(matrix, x + 1, y - 1, n, pathnum)
            visited[x][y] -= 1

    # return visited, count
    return flag


n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(" "))))

count = 0
flag = False
rule1, rule2 = False, False
r1, r2 = 0, 0

visited = [[0]*n for i in range(n)]
while not rule1 and r1 < 1:
    rule1 = findpath(matrix, 0, r1, n, pathnum=1)
    # print('Starting at', 0, r1, '-> value is', matrix[0][r1], 'rule1 is', rule1)
    r1 += 1

del visited
visited = [[0]*n for i in range(n)]
while not rule2 and r2 < n:
    print('Starting at', r2, 0, '-> value is', matrix[r2][0])
    rule2 = findpath(matrix, r2, 0, n, pathnum=2)
    print('rule2 is', rule2)
    r2 += 1

if rule1 and rule2:
    print('AMBIGUOUS')
elif rule1:
    print(1)
elif rule2:
    print(2)
else:
    print(0)





