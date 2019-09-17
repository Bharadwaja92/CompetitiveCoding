"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;
For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;
For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.
"""


def isBeautifulString(inputString):
    st = [0]*26
    for c in inputString:
        st[ord(c)-ord('a')] += 1
    print(st)
    i = 0
    flag = True
    while i < 25 and flag:
        print(i, '->', st[i], st[i+1])
        flag = st[i] >= st[i+1]
        i += 1
    return flag


inputString = "bbbaacdafe"
inputString = "aabbb"
# inputString = "bbc"
print(isBeautifulString(inputString))