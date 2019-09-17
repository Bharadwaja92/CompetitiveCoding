""""""
"""
You have been given a String  consisting of lowercase alphabets of the English Language. Now, we call a String  an 
anagram of another String , if we can obtain String  be rearranging the characters of String .
For example , the word  has  anagrams i.e  .

Now, you need to find all the disitnct anagrams of String  , sort them lexicographically and then print to output the 
anagram that occurs at the  position in this sorted order.

INPUT: The first line of input contains the number of test cases denoted by T. The next T lines of input contain a 
string S and a number N.

OUTPUT: You need to find and print the anagram of the given string which occurs at the $$N^{th} position when they are 
arranged in lexicographical order.

SAMPLE INPUT 
4
bcda 20
cbad 5
ydvtrs 268
asfda 32
SAMPLE OUTPUT 
dacb
adbc
srdvyt
dfasa
Explanation
For case 2, one need to find the anagram of "cbad" which occurs at 5th place when arranged in lexicographical order.

The anagrams that occur at the first four positions are abcd, abdc, acbd and acdb respectively. The fifth anagram is adbc.

"""
from itertools import permutations

t = int(input())

while t > 0:
    l1 = input().split(' ')
    s, n = l1[0], int(l1[1])
    allAnagrams = [''.join(perm) for perm in permutations(s)]
    allAnagrams = sorted(list( dict.fromkeys(allAnagrams)))
    print(allAnagrams[n-1])
    t -= 1

