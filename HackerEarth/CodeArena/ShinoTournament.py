""""""
"""
Little Shino is interested in the fighting tournaments. Once she went to watch one of the tournaments. There were N fighters and  fighter will be represented by i. Each fighter has some distinct strength. Rules of the tournament are:

Each fight will have 2 fighters. In a fight, fighter with more strength will win.
In one round, 1st fighter will fight against 2nd fighter, 3rd fighter will fight against 4th fighter and so on. If there is odd number of fighters, last one will qualify to the next round without fighting.
Input: First line contains 2 integers, N and Q, number of fighters and number of queries.
Second line contains N space separated integers.  integer represents the strength of  fighter.
Next Q line contain one integer i each, denoting Q queries.

Output:
For each query, print the number of fights  fighter will take part in.

SAMPLE INPUT 
5 5
1 2 3 4 5
1
2
3
4
5
SAMPLE OUTPUT 
1
2
1
3
1
Explanation
The fights in first round will be between (1, 2) and (3, 4).
From fight between (1, 2), 2 will win and from fight between (3, 4), 4 will win.
Second round will have 3 fighters left. {2, 4, 5}.
In second round there will be one fight between (2, 4) and 4 will win the fight.
Third round will have 2 fighters left. {4, 5}
There will one fight in the third round between (4, 5) and 5 will win in the fight.
Number of fight 1 took part in: 1
Number of fight 2 took part in: 2
Number of fight 3 took part in: 1
Number of fight 4 took part in: 3
Number of fight 5 took part in: 1
"""

# l1 = list(map(int, input().split(" ")))
l1 = list(map(int, '5 5'.split(" ")))

n, q = l1[0], l1[1]

# strengths = list(map(int, input().split(" ")))
strengths = list(map(int, '1 2 3 4 5'.split(" ")))

numMatches = {i+1: 0 for i in range(n)}

print('numMatches is', numMatches)


