""""""
"""
Stranger Things have started happening in the town of Hawkins, Indiana after Will Byers disappeared last week. Will's 
friends Dustin, Mike, and Lucas discover a psychokinetic girl, Eleven who claims to know Will's location.
They gather total N kids from neighbourhood (including them with their special monster killing guns and went at the 
location given by Eleven. As soon as they reach the place, they find an army of K deadly monsters ready to kill whatever 
comes in their way. Eleven uses her psychic powers and finds a way to kill some of the monsters.

A monster can be killed by a kid's gun if and only if the power of monster is divisible by the gun's power. 
Monster are numbered from 1 to K and the power of  monster is i. The power of the gun  kid is holding is a[i].

Find the maximum number of monsters the kids will be able to kill.

Input:
First line of input consist of a single integer T denoting the total number of test case. T test cases follow.
The first line of test case contains a single integer N denoting the number of kids.
Second line of test case contains N space separated integers denoting the power of gun  kid is holding.
Third line of test case contains a single integer K representing the army of monsters.

Output: For each test case output a single integer in new line representing the maximum number of monsters the kids 
    will be able to kill.

SAMPLE INPUT 
1
2
2 5
10
SAMPLE OUTPUT 
6
Explanation
There are 10 monsters having powers 1,2,3,4,5,6,7,8,9,10. only {2,4,5,6,8,10} are the monsters than can be killed with guns with power{2,5}

"""

t = int(input())

while t > 0:
    n = int(input())
    powers = list(map(int, input().split(" ")))
    numMonsters = int(input())
    monsters = [0] * numMonsters
    for f in powers:
        dd = [i for i in range(numMonsters) if i % f == 0]
    t -= 1




