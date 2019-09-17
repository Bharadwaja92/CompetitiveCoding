""""""
"""
https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/the-legend-of-tanmay/

Tanmay is a legendary spammer - everyone in the spamming world knows and admires his abilities to spam anyone, anytime, 
anywhere. He decided to guide one of his mentors, named Arjit, as part of the Apex body of spamming. Tanmay has no 
doubts on his skills of teaching and making his mentor, Arjit, learn about the art of spamming. But, he surely has 
serious doubt on Arjit's skills of learning, implementing and executing whatever he has decided to teach him as part of 
the syllabus of spamming. Tanmay has sent Arjit to test his skills, but he's getting extremely anxious about the 
performance of his mentee. So, to calm himself down he asks you to help him find out the maximum and the minimum 
productivity attained by Arjit in his travel.

Arjit has the option to visit N Facebook groups - where every Facebook group has some potential which can be negative, 
zero or positive. Now, he can decide to visit a group if he wants to or not. (Depending on the lessons taught to him by 
the great master!) The total productivity attained by Arjit is the product of all the groups he decides to visit.
Given the values of all the groups, find out the maximum and minimum spamming potential he can achieve and let Tanmay 
know about it, so that he calm himself down.

Input format:   The first line contains an integer, T, denoting the number of test cases. 
Each line of the test case contains an integer, N, denoting the size of the array. The next line contains N integers, 
denoting the value of the numbers in the array.

Output format:  Print the maximum product you can obtain followed by the minimum product. A space separates both these 
outputs. Answer to each test case is on a new line.

Constraints:
1 ≤ T ≤ 500
1 ≤ N ≤ 18
-10 ≤ Ni ≤ 10

Note:
In some cases only one element may be considered for minimum or maximum product.
If the array is (1, 2, 3), minimum product is 1 whereas maximum product is 6.
When the array is (-1, -2), minimum product is -2 whereas maximum product is 2.

SAMPLE INPUT 
2
4
1 0 2 10
3
0 0 0
SAMPLE OUTPUT 
20 0
0 0
Explanation
In the first test case, the maximum product is the product of all the numbers except 0, whereas the minimum product is 
the product of all numbers including 0.
In the second test case, the maximum and minimum product both are 0 as 0 is the only available number.
"""

from functools import reduce

t = int(input())

while t > 0:
    n = int(input())
    l1 = list(map(int, input().split(" ")))

    poss = [x for x in l1 if x > 1]
    negs = [x for x in l1 if x < 0]
    zeroPresent = 0 in l1
    numNegs = len(negs)

    if len(poss) > 0:
        posProd = reduce((lambda x, y: x*y), poss)      # Keep it aside
    else:
        posProd = 1
    if len(negs) > 0:
        negProd = reduce((lambda x, y: x * y), negs)
    else:
        negProd = 1

    minProd, maxProd = 0, 0

    if numNegs > 0:
        if numNegs % 2 == 0:
            print('Even negs')
            print('Min = product of (all negs except the largest neg) and (All poss)')
            negProd /= max(negs)
            maxProd = negProd * posProd
            minProd = negProd * posProd / min(negs)
        else:
            print('Odd negs')
            print('Min = Product of all the numbers')
            minProd = negProd * posProd
            maxProd = posProd * negProd / min(negs)
    elif numNegs == 0:
        print('Only poss - Max = prod of all pos')
        if zeroPresent:
            print('Min = 0')
            minProd = 0
            maxProd = posProd
        else:
            print('Zero not there, min = minimum pos number')
            minProd = min(poss)
            maxProd = posProd

    t -= 1



