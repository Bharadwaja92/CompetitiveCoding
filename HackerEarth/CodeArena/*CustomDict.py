""""""
"""
Consider a new order of english alphabets (a to z), that we are not aware of. What we have though, dictionary of words, 
ordered according to the new order.
Our task is to give each alphabet a rank, ordered list of words. The rank of an alphabet is the minimum integer R that 
can be given to it, such that:

if alphabet Ai has rank Ri and alphabet Aj has Rj, then
Rj > Ri if and only if Aj > Ai
Rj < Ri if and only if Aj < Ai

Points to note: We only need to find the order of alphabets that are present in the words
There might be some cases where a strict ordering of words cannot be inferred completely, given the limited information. 
In that case, give the least possible Rank to every alphabet
It can be assumed that there will be no direct or indirect conflict in different inferences got from the input

Input:
First line consists of integer 'W', the number of words. 1 <= W <= 100
Second line onwards, there are 'W' lines, given ordered list of words. The words will be non-empty, and will be of 
length <= 20 characters. Also all the characters will be lowercase alphabets, a to z

Output:
The alphabets, in order of their Rank, for alphabets with the same rank, print them in the order as we know it today

Examples

1)
Input: 2 ba ab
Output: b a
Explanation: ab comes after ba implies that b < a

2)
Input: 3 abc aca ca
Ouput: ab c
Explanation: from the first 2 words, we know b < c, and from the last 2 words, we know a < c. We don't have an ordering between a and b, so we give both of them the same rank, and print them in the order as we know today: ab

SAMPLE INPUT 
6
aaabc
aaade
bacd
cde
cda
cca
SAMPLE OUTPUT 
e
a
b
d
c
"""


def doDFS(graph, vertex, path = []):
    if vertex not in path:
        path.append(vertex)
    for connectedLetter in graph[vertex]:
        if connectedLetter not in path:
            path = doDFS(graph=graph, vertex=connectedLetter, path=path)
    return path


def DFS(graph):
    print('Graph is', graph)
    path = []
    i = 0
    v = ''
    while i < len(graph): #and len(path) < len(graph)-1:
        v = list(graph.keys())[i]
        path = doDFS(graph, v)
        print(v, '-> ', path)
        i += 1
    print(v, path[:len(graph)-1])


w = int(input())
t = w

words, letters = [], []
letterRelations = {}

while t > 0:
    s = input()
    words.append(s)
    t -= 1

for i in range(1, w):
    w1, w2 = words[i-1], words[i]
    j = 0
    flag = True
    while flag and j < len(w1) and j < len(w2):
        c1, c2 = w1[j], w2[j]
        j += 1
        flag = c1 == c2
        if c1 not in letters:
            letters.append(c1)
        if c2 not in letters:
            letters.append(c2)

    c1, c2 = w1[j-1], w2[j-1]
    if c1 not in letterRelations.keys():
        letterRelations[c1] = [c2]
    else:
        letterRelations[c1].append(c2)

print('letters are', letters, '->  Create nodes for these')
print('letterRelations are', letterRelations)

for x in letters:
    if x not in letterRelations:
        letterRelations[x] = []

DFS(letterRelations)




