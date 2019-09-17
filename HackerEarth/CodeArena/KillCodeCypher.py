""""""
"""
KillCode is trying to learn strings but failing to solve the recursive approach given by his Teacher. His Teacher gave him a string consisting of lower case alphabetes only , He asked to find a substring in the given string after removing any charaters from the original string . For example if the string is
" Cypher" and the substring is "yer", Killcode can remove p,h from the string and can form the given substring.

Now the Teacher got impressed from Killcode and decided to increase the difficulty by asking to find the substring and 
reverse of substring in given string. If both substring can be formed by a given string by removing certain characters ,
 print "GOOD STRING " else print "BAD STRING".

Input - First line contains integer t denoting the test cases, each test case contains two lines containing two strings.
Output- Print "GOOD STRING"(without quotes) both strings can be formed by given string else print "BAD STRING".

SAMPLE INPUT 
3
abta
aba
oley
le
tereo
re
SAMPLE OUTPUT 
GOOD STRING
BAD STRING
GOOD STRING
Explanation
Test case 1: "abta" is given string and "aba" is given substring , now Killcode will remove 't' from given string and will get both substring and reverse of sub-string.
Test case 2: Killcode cannot find the substring and reverse of of sub-string after removing any charaters.
"""

# t = int(input())
t = 1

while t > 0:
    # s1 = input()
    # s2 = input()
    s1 = 'abcda'
    s2 = 'ac'
    s2r = s2[::-1]

    i, j1, j2 = 0, 0, 0
    while i < len(s1) and j1 < len(s2):
        if s2[j1] == s1[i]:
            print('j1 +ed at i=',i, 'for char', s1[i])
            j1 += 1
        i += 1

    print('j1 is', j1)

    i = 0
    while i < len(s1) and j2 < len(s2r):
        if s2r[j2] == s1[i]:
            print('j2 +ed at i=', i, 'for char', s1[i])
            j2 += 1
        i += 1

    print('j2 is', j2)

    if j1 == len(s2) and j2 == len(s2):
        print('GOOD STRING')
    else:
        print('BAD STRING')

    t -= 1


