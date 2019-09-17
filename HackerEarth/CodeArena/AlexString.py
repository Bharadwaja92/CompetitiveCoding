""""""
"""
https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/lexicographically-minimum-string-269d7f34/

Alex has a string S of length N consisting of lowercase alphabets. He wants to find lexicographically smallest string X 
of length N that can be formed using the following operation.

In one operation, he can select any one character among the at most first K characters of string S, remove it from 
string S and append it to string X. He can apply this operation as many times as he wants.

Help Alex find the string X.

Input format
The first line consists of a string of length N
The second line consists of an integer K.

Output format: Print the lexicographically minimum string that can be formed using the above operation.

SAMPLE INPUT 
hackerearth
3
SAMPLE OUTPUT 
aceheakrhrt
Explanation
First you can select 'a' from "hackerearth". Now the string X becomes "a" and string S becomes "hckerearth".
Now after applying the operation again, the string X becomes "ac" and the string S becomes "hkerearth".
Similarly after applying the operation n times, the string X becomes "aceheakrhrt".

k=3
hackerearth		
hac       hckerearth  	a       
ahc       hkerearth     ac
hke       hkrearth      ace   
hkr       krearth       aceh 
kre       krarth        acehe 
kra       krrth         acehea 
krr       rrth          aceheak
rrt       rth           aceheakr
rth       rt            aceheakrh
rt        r             aceheakrhr
t                       aceheakrhrt
"""

"""
HEAP
/home/saibharadwaj/PycharmProjects/DSP/DS_Algo/Interactive_org/Trees*/BinaryHeap.py
"""

# s = input()
s = list('hackerearth')
k = 3
ns = []

for i in range(0, len(s)-k):
    s1 = s[:k]
    minchar = min(s1)
    s.remove(minchar)
    ns.append(minchar)

ns.extend(sorted(s))
print(''.join(ns))




