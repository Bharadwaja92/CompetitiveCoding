""""""
"""
http://techiekhannotes.blogspot.com/2015/08/tom-jerry.html
http://techiekhannotes.blogspot.com/2015/08/capture-castle.html
https://www.geeksforgeeks.org/count-number-ways-reach-destination-maze/
https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/


Tom and Jerry are wonderful characters. They are always running and make us laugh. Right now, they are in a grid of 
houses and Jerry is running away from Tom. The grid of houses is represented as 0 and 1, 
where 0 means that Jerry can enter the house, and 1 means Jerry can't. Jerry can only move horizontally or vertically. 
Also, Jerry doesn't enter the same house more than once.

Jerry started running from the house at (1, 1) which is the top-left house in the grid and have to reach (N, N) which 
is the  bottom-right house in the grid. You have find the number of ways in which Jerry can reach the destination house 
where he can be safe.

Input Format: First line is an integer N (N <= 100), which is the size of the grid. N lines follow, each containing 
N space separated numbers which are either '0' or '1'.

Output format: Print a single line showing the number of ways in which Jerry can reach from (1, 1) to (N, N).

SAMPLE INPUT 
9
0 0 0 0 0 0 0 0 0
0 1 0 1 0 1 0 1 0
0 0 0 0 0 0 0 0 0
0 1 0 1 0 1 0 1 0
0 0 0 0 0 0 0 0 0
0 1 0 1 0 1 0 1 0
0 0 0 0 0 0 0 0 0
0 1 0 1 0 1 0 1 0
0 0 0 0 0 0 0 0 0
SAMPLE OUTPUT 
8512
"""
n = int(input())
t = n
houses = []

while t > 0:
    houses.append(list(map(int, input().split(" "))))
    t -= 1

visited = [[0]*n for i in range(n)]
count = 0


def findWays(houses, x, y, n):
    print('x =', x, 'y =', y, 'n =', n)
    global count
    global visited
    if x == n-1 and y == n - 1:         # Base case
        count += 1
    else:
        if x + 1 < n and houses[x][y] == 0 and visited[x][y] < 1:
            print('Case1')
            visited[x][y] += 1
            findWays(houses, x + 1, y, n)
            visited[x][y] -= 1
        if y + 1 < n and houses[x][y] == 0 and visited[x][y] < 1:
            print('Case2')
            visited[x][y] += 1
            findWays(houses, x, y + 1, n)
            visited[x][y] -= 1
        if x - 1 >= 0 and houses[x][y] == 0 and visited[x][y] < 1:
            print('Case3')
            visited[x][y] += 1
            findWays(houses, x - 1, y, n)
            visited[x][y] -= 1
        if y - 1 >= 0 and houses[x][y] == 0 and visited[x][y] < 1:
            print('Case4')
            visited[x][y] += 1
            findWays(houses, x, y - 1, n)
            visited[x][y] -= 1

    return visited, count


visited, numWays = findWays(houses, 0, 0, n)
print('numWays is', numWays)

print('-'*50)
for v in visited:
    print(v)
print('-'*50)

def findWays1(houses, visited, x, y, n):
    print('x =', x, 'y =', y, 'n =', n)
    global count
    if x == n-1 and y == n - 1:         # Base case
        count += 1
    else:
        if x + 1 < n and houses[x][y] == 0 and visited[x][y] != 1:
            print('Case1')
            visited[x][y] = 1
            findWays(houses, visited, x + 1, y, n)
            visited[x][y] = 0
        if y + 1 < n and houses[x][y] == 0 and visited[x][y] != 1:
            print('Case2')
            visited[x][y] = 1
            findWays(houses, visited, x, y + 1, n)
            visited[x][y] = 0
        if x - 1 >= 0 and houses[x][y] == 0 and visited[x][y] != 1:
            print('Case3')
            visited[x][y] = 1
            findWays(houses, visited, x - 1, y, n)
            visited[x][y] = 0
        if y - 1 >= 0 and houses[x][y] == 0 and visited[x][y] != 1:
            print('Case4')
            visited[x][y] = 1
            findWays(houses, visited, x, y - 1, n)
            visited[x][y] = 0

    return count
