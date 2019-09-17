""""""
"""
You are given positive integer N. How many unordered pairs of integers from 1 to N are coprime?

Input: The finrst line contains one integer T denoting the number of test cases. The following T lines contain one 
number each - N and describe each test case.

Output: For each test case output one integer per line - answer for the question.

Constraints
N <= 10^7
T <= 10
SAMPLE INPUT 
2
3
4
SAMPLE OUTPUT 
4
6
"""



def getNumCoprimes(n):
    count = 0

    return count


t = int(input())
maxi = 10**2
phi = [0] * maxi
phiphi = [i for i in range(maxi)]

# for p in range(2, maxi):
#     if phiphi[p] == p:
#         phiphi[p] = p - 1;
#
#     for (int i = 2 * p; i < maxi; i += p)
#     {
#         phi[i] = (phi[i] / p) * (p-1);
#     }
#     }
#     }
#

while t > 0:
    n = int(input())
    print(phiphi[n])
    t -= 1

