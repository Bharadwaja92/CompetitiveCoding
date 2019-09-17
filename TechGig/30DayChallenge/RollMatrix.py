""""""
"""
Roll your matrix (100 Marks)
For this challenge, you need to take a matrix as an input from the stdin , transpose it and print the resultant matrix to the stdout. 

Input Format
A matrix is to be taken as input from stdin. On first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space. Below lines will represent the elements of the matrix where each line will represent the row of the matrix.

Constraints
1 < (n,m) < 100

Output Format
Print the resultant matrix to the stdout where each line should represent each row and values in the row should be separated by a space. 

Sample TestCase 1
Input
3 3
1 2 3
4 5 6
7 8 9
Output
1 4 7
2 5 8
3 6 9
"""

def run():
    nums = list(map(int, input().split(' ')))
    r, c = nums[0], nums[1]
    mat1 = []

    for i in range(r):
        mat1.append(list(map(int, input().split(' '))))

    mat2 = []
    for i in range(r):
        x = []
        for j in range(c):
            x.append(str(mat1[j][i]))
        mat2.append(x)

    for i in range(r-1):
        print(' '.join(mat2[i]))
    print(' '.join(mat2[-1]), end='')

    # mat2 = [[mat1[i][j] for i in range(r)] for j in range(c)]
    # for r1 in mat2[:-1]:
    #     print(' '.join(list(map(str, r1))))
    #
    # print(' '.join(list(map(str, mat2[-1]))), end='')


run()