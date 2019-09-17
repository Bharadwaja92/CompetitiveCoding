""""""
"""
For this challenge, you need to take 2 matrices as an input from the stdin , add them and print the resultant matrix to 
the stdout. 

Input Format
Two matrices to be taken as an input. 
For each matrix, on first line you need to tell that how many rows and columns your matrix need to have and these values 
should be separated by space. Then after that, each line will represent will represent each row and you need to enter 
numbers which each rows should have separated by a space. 

Constraints: 1 <  (n,m) < 100,  1 <  (p,q) < 100

Output Format: Print the resultant matrix to the stdout where each each line should represent 
Note : Please do not include space after the numbers which are in the last column as it will affect your submission and 
you will not get marks. Each row and values in the row should be separated by a space. 

Sample TestCase 1
Input
3 3
1 2 3
4 5 6
7 8 9
3 3
2 3 4
5 6 7
7 8 9
Output
3 5 7
9 11 13
14 16 18

Explanation
Two matrices must have an equal number of rows and columns to be added. The sum of two matrices A and B will be a 
matrix which has the same number of rows and columns as do A and B. The sum of A and B, denoted A + B, is computed by 
adding corresponding elements of A and B.
"""

nums = list(map(int, input().split(' ')))
r, c = nums[0], nums[1]
mat1, mat2 = [], []

for i in range(r):
    mat1.append(list(map(int, input().split(' '))))

nums = list(map(int, input().split(' ')))
r, c = nums[0], nums[1]
for i in range(r):
    mat2.append(list(map(int, input().split(' '))))

print(mat1, mat2)

mat3 = [[mat1[i][j]+mat2[i][j] for j in range(c)] for i in range(r)]

for r1 in mat3[:-1]:
    print(' '.join(list(map(str, r1))))

print(' '.join(list(map(str, mat3[-1]))), end='')
