"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial
string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""


def checkPalindrome(st):
    return st[::-1] == st


def buildPalindrome(str):
    for i in range(len(str)):
        s = str + str[i::-1]
        if s == s[::-1]:
            return s

def buildPalindrome(st):
    r = st[::-1]
    if (checkPalindrome(st)):
        return st

    for i in range(len(st)):
        if (checkPalindrome(st + r[len(st) - i::])):
            return st + r[len(st) - i::]
    else:
        return st + r[1::]

st = "abcdc"
print(buildPalindrome(st))