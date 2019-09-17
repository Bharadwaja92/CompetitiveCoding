""""""
"""
It's a fine sunny afternoon today in California. Looking at the pleasant weather, Sumit is all ready to go out and play with his friend Rohil. Unfortunately, Rohil is down with fever. Seeing that his friend is ill, Sumit decides not to go out - instead play with Rohil inside the house. Sumit loves math, on the contrary Rohil loves strings. Sumit decides to play a game that involves more of strings and less of Maths so that Rohil could be at ease and have fun playing it.
The game is simple and is played on a piece of paper. Sumit writes down a long list of names on that paper and passes it to Rohil. Rohil gets confused on seeing so many names on that paper and asks Sumit about the game. So, Sumit explains him the rules of the game. Rohil is supposed to partition the names into groups, such that:

Each name belongs to exactly one group.
Names that belong to the same group are pairwise anagrams.
The first character of all the names in the same group are equal.
The last character of all the names in the same group are equal.
The number of groups is minimum possible.
Note: Two strings are called anagrams if it's possible to form one string from the other by changing the order of its characters.

Rohil would have won the game easily, if he would have been fit and fine but since he is ill right now he needs your help in winning the game. So, help out Rohil and do give him your blessings.

Input: The first line contains a single integer N indicating the size of the list. 
This is followed by N lines where each line contains a name listed by Sumit.

Output:  In a single line print minimum number of groups in a partition that satisfy above conditions

Constraints:
1<= N <=100
1 <= Length of a name <= 100

All names will consist of lowercase English alphabets(a-z).

SAMPLE INPUT 
6
vinay
vainy
vinit
viint
avinash
aasivnh
SAMPLE OUTPUT 
3
Explanation
There are 3 special groups

1) vinay and vainy
2) vinit and viint
3) avinash and aavsinh
"""

words = []
groups = {}
t = int(input())

for i in range(t):
    words.append(input())

# print('Words are', words)
selected = [False] * t
k = 0

for i in range(t-1):
    for j in range(i+1, t):
        groups[i] = []
        w1, w2 = words[i], words[j]
        print(w1, w2)
        if w1[0] == w2[0] and w1[-1] == w2[-1] and sorted(w1) == sorted(w2) and not selected[i] and not selected[j]:
            print('IN')
            groups[i].append(w1)
            groups[i].append(w2)
            selected[j] = True
    selected[i] = True
    print('----------------------')


for k in groups:
    print(k, '->', groups[k])

"""
24
abcd
abdc
acbd
acdb
adbc
adcb
bacd
badc
bcad
bcda
bdac
bdca
cabd
cadb
cbad
cbda
cdab
cdba
dabc
dacb
dbac
dbca
dcab
dcba

12
"""
# flag = True
# k = 0
"""
while True:
    w1 = words[0]
    print('w1 is', w1)
    groups[k] = []
    i = 1
    while len(words) > 1 and w1[0] == words[i][0] and w1[-1] == words[i][-1] and len(words) > 1:
        if sorted(w1) == sorted(words[i]):
            print('Found match with', words[i])
            groups[k].append(w1)
            groups[k].append(words[i])
            words.remove(words[i])
        i += 1
    words.remove(w1)
    k += 1
    print('Words after removal is', words)
    flag = len(words) > 0
    if not flag:
        break
    print('------------------')

print(len(groups))
print('*'*60)

"""
















