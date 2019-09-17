""""""
"""
After Governor's attack on prison, Rick found himself surrounded by walkers. They are coming towards him from all sides. 
Now, suppose Rick have infinite number of bullets with him. Suppose Rick need 1 bullet to kill each walker (yeah he is 
good in killing walkers. They need to be shot at head. See, how good he is). Now as soon as he kills 1 walker rest of 
the walkers move forward by 1 m. There are n walkers each at some distance from Rick. If any walker is able to reach 
Rick, he dies. Now, you need to tell if he survives or not. If he survives print "Rick now go and save Carl and Judas" 
else print "Goodbye Rick" followed by no.of walkers he was able to kill before he died in next line. One more thing 
Rick's gun can fire 6 shots without reload. It takes him 1 sec to reload and during this time walkers move 1 m forward.

[Input] First line contains an integer t indicating number of test cases.
Next line contains an integer n denoting no.of walkers followed by n space separated integers denoting the distance of 
walkers from him.

[Output]    For each test case output one line denoting the answer as explained above.

SAMPLE INPUT 
2
5
2 4 2 5 6
4
2 2 2 2
SAMPLE OUTPUT 
Rick now go and save Carl and Judas
Goodbye Rick
2
"""

t = int(input())


def findRickFate(n, l1):
    c = 0
    l1 = sorted(l1)
    while len(l1) > 0:
        if 0 in l1:
            return 'Goodbye Rick\n'+str(n-len(l1))
        l1.remove(l1[0])
        l1 = [x-1 for x in l1]
        c += 1
        if c == 6:
            l1 = [x - 1 for x in l1]
            c = 0
    return 'Rick now go and save Carl and Judas'


while t > 0:
    n = int(input())
    l1 = sorted(list(map(int, input().split(" "))))
    print(findRickFate(n, l1))
    t -= 1


