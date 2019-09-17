""""""
"""
You are given a string S. S consists of several words separated by one or more spaces. Word consists of Latin letters as well as other symbols (but not spaces).
In each word which starts from lowercase Latin letter replace starting letter with uppercase Latin letter.

Input
The only line contains S

Output
Output one line with modified string S.

SAMPLE INPUT 
Wish you were here
SAMPLE OUTPUT 
Wish You Were Here

"""

s = 'Wish you were here'.split(' ')

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))


def isLatin(c):
    return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z'))


t = [str(x[0]).upper()+x[1:] if isLatin(x[0]) else x for x in s]

print(' '.join(t))
