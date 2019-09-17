"""
https://www.techgig.com/practice/question/day-29/aWxicTRicFVRREtFMytPL1YyUlA4T2psRHdweFpQLzhhQ1BvKysvVml5RWphYTJGVXNaN3ZxYzVhY3Z5ZCtYdQ==/1
"""
"""
For this challenge, you need to take a matrix as an input from the stdin , calculate the sum of the digits for each 
diagonal and compare them.For example, in the below matrix 
1 2 3 
4 5 6 
7 8 9 
Diagonal 1 is 1,5,9.  Diagonal 2 is 3,5,7. 

Input Format
A matrix is to be taken as input from stdin.On first line you need to tell that how many rows and columns your matrix 
need to have and these values should be separated by space. 

Constraints
1 < (n,m) < 100

Output Format
If sum of digits for diagonal 1 is found to be greater than diagonal 2, then print 'Diagonal 1' to the stdout. 
If sum of digits for diagonal 2 is found to be greater than diagonal 1, then print 'Diagonal 2' to the stdout. 
If both of the diagonal found to be equal, then print 'Equal' to the stdout. 

Sample TestCase 1
Input
3 3
2 3 4
1 4 6
3 8 9
Output
Equal
"""

ip = input().split()
nr, nc = int(ip[0]), int(ip[1])
mat = []
for i in range(nr):
    mat.append(list(map(int, input().split())))

# d1 = sum([mat[i][i] for i in range(nr)])
# d2 = sum([mat[i][nr-i-1] for i in range(nr)])

d1 = [mat[i][i] for i in range(nr)]
d2 = [mat[i][nr-i-1] for i in range(nr)]
print(d1, d2)

# v = 'Diagonal 1' if d1 > d2 else 'Diagonal 2' if d1 < d2 else 'Equal'
# print(v, end='')


