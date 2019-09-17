"""
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
 Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example

For s = "4[ab]", the output should be
decodeString(s) = "abababab";

For s = "2[b3[a]]", the output should be
decodeString(s) = "baaabaaa";

For s = "z1[y]zzz2[abc]", the output should be
decodeString(s) = "zyzzzabcabc".
"""

def decodeString(s):
    st, num, dc = '', s[0], ''

    for i in range(1, len(s)):
        if s[i].isdigit():
            num += s[i]
        elif s[i].isalpha():
            dc += s[i]
        elif s[i] == ']':
            st += dc * int(num)
            num = 0
            dc = ''
        print('At', i, 'num is', num,'dc is', dc, 'st is', st)
    return st


# s = "4[ab]"
s = "2[b3[a]]"
# s = "z1[y]zzz2[abc]"

print(decodeString(s))





