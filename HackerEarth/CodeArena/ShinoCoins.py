""""""
"""
Little Shino loves to play with coins. In the city she lives, there are different types of coins. Each coin is represented with a lowercase letter . Shino has some number of coins and she placed them in some random sequence, S, on the table. She is wondering how many pairs  are there, where , such that number of distinct coins in sequence  is exactly equal to K. Two coins of same type (same letters) are considered equal and two coins of different types (different letters) are considered distinct.

Input:
First line contains one integer, K.
Second line contains a string, S, consist of lowercase letters only.

Output:
Print one integer, number of pairs , where , such that number of distinct coins in sequence  is exactly equal to K.

Constraints:    S consists of lowercase letters only.

SAMPLE INPUT 
3
abcaa
SAMPLE OUTPUT 
5
Explanation: Since, 
Possible pairs  such that number of distinct coins in  is exactly equal to K are:
abc, abca, abcaa, bca, bcaa

So the answer is 5.
"""

k = 3
s = 'abcaa'

count = 0
for i in range(0, len(s)):
    for j in range(i+1, len(s)+1):
        v = s[i:j]
        if len(v) >= k and len(set(v)) == k:
            count += 1

print(count)

