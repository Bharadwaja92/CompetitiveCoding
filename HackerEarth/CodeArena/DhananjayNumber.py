""""""
"""
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/magical-word/

Dhananjay has recently learned about ASCII values.He is very fond of experimenting. With his knowledge of ASCII values 
and character he has developed a special word and named it Dhananjay's Magical word.

A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. An alphabet is 
Dhananjay's Magical alphabet if its ASCII value is prime.

Dhananjay's nature is to boast about the things he know or have learnt about. So just to defame his friends he gives 
few string to his friends and ask them to convert it to Dhananjay's Magical word. None of his friends would like to get 
insulted. Help them to convert the given strings to Dhananjay's Magical Word.

Rules for converting:
1.Each character should be replaced by the nearest Dhananjay's Magical alphabet.
2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be 
    considered as its replacement.

Input format:
First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the 
length of the string) and a string S.

Output Format: 
For each test case, print Dhananjay's Magical Word in a new line.

Constraints:
1 <= T <= 100
1 <= |S| <= 500

SAMPLE INPUT 
1
6
AFREEN
SAMPLE OUTPUT 
CGSCCO
Explanation
ASCII values of alphabets in AFREEN are 65, 70, 82, 69 ,69 and 78 respectively which are converted to CGSCCO with ASCII 
values 67, 71, 83, 67, 67, 79 respectively. All such ASCII values are prime numbers.
"""

t = int(input())

primes = [2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113]   # 127, 131, 137, 139, 149, 151, 157, 163, 167

while t > 0:
    n = int(input())
    s = input()
    outs = []
    for c in s:
        v = ord(c)
        # print('c is', c)
        # Get nearest prime
        flag, i1 = False, -1
        while not flag and i1 < len(primes)-1:
            i1 += 1
            flag = primes[i1] > v and i1 < len(primes)
            # print('i1 is', i1, '-->', primes[i1])

        sm, lg = primes[i1-1], primes[i1]
        d1, d2 = v - sm, lg - v
        if d1 <= d2:
            outs.append(sm)
        else:
            outs.append(lg)

    # print('outs is', outs)
    # print(s)
    print(''.join([chr(x) for x in outs]))
    t -= 1





