"""""""""
Fatal Eagle has decided to do something to save his favorite city against the attack of Mr. XYZ, since no one else surprisingly seems bothered about it, and are just suffering through various attacks by various different creatures.
Seeing Fatal Eagle's passion, N members of the Bangalore City decided to come forward to try their best in saving their city. Now Fatal Eagle decided to strategize these N people into a formation of AT LEAST K people in a group. Otherwise, that group won't survive.

Let's demonstrate this by an example. Let's say that there were 10 people, and each group required at least 3 people in it for its survival. Then, the following 5 groups can be made:

10 - Single group of 10 members.
7, 3 - Two groups. One consists of 7 members, the other one of 3 members.
6, 4 - Two groups. One consists of 6 members, the other one of 4 members.
5, 5 - Two groups. One consists of 5 members, the other one of 5 members.
4, 3, 3 - Three groups. One consists of 4 members, the other two of 3 members.

Given the value of N, and K - help Fatal Eagle in finding out the number of ways he can form these groups (anti-squads) to save his city.

Input format:
The first line would contain, T - denoting the number of test cases, followed by two integers, N and K denoting 
the number of people who're willing to help and size of the smallest possible group which can be formed.

Output format:  You've to print the number of ways in which groups can be formed.

SAMPLE INPUT 
2
10 3
20 5
SAMPLE OUTPUT 
5
13
"""

# t = int(input())
# l1 = list(map(int, input().split(" ")))

t = 1

while t > 0:
    l1 = [10, 3]
    n, k = l1[0], l1[1]
    maxSize = n // k
    print('maxsize is', maxSize)
    print('k is', k)
    for i in range(k, maxSize+1):
        print(i, '->', n//i)
    t -= 1



