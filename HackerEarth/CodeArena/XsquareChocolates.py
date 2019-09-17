"""
Xsquare loves to eat chocolates like we all do. Xsquare's father has given him a chocolate bar B of length N where each
chocolate piece is either of strawberry flavour S or of caramel flavour C. Xsquare's mom does not want him to eat all
the chocolates as she thinks that consumption of too many chocolates will make him chocoholic. Therefore, she decided
to take some chocolates back from him. She has some empty boxes to keep chocolates. Each box can contain exactly
three chocolates. No box can contain all the chocolates of same flavour. She has ordered Xsquare to return her back,
the longest contiguous sub-bar of the original chocolate bar such that she can place every three consecutive chocolates
from that contiguous chocolate bar in an empty box. Each empty box can accomodate exactly three chocolates, neither
less, nor more. A sub-bar is defined as contiguous peices of chocolates in some particular range. Xsquare agrees to
whatever his mom has ordered. Now, he is wondering how many chocolates he is able to eat at the end after he returns
the longest contiguous sub-bar. Help him in accomplishing this task.

Input : First line of input contains a single integer T denoting the number of test cases. Each of the next T line of
input contains a string B denoting the chocolate bar, where ith character in the jth line denotes the flavour of ith
chocolate piece in jth chocolate bar.

Output : Output consists of T lines, each containing number of chocolates Xsquare manages to eat at the end.

SAMPLE INPUT
4
SSSSSSSSS
CCCCCCCCC
SSSSCSCCC
SSCCSSSCS
SAMPLE OUTPUT
9
9
3
0

Explanation
Test case 1 : Xsquare cannot return any such bar to his mom. So, he can eat all the chocolates.
Test case 2 : Xsquare cannot return any such bar to his mom. So, he can eat all the chocolates.
Test case 3 : Xsquare can return "SSCSCC" to his mom such that she can placed "SSC" in one box and "SCC" in other box.
            Therefore, xsquare can get only 3 chocolates at the end.
Test case 4 : Xsquare can return "SSCCSSSCS" to his mom such that she can placed "SSC" in first box, "CSS" in second box
 and "SCS" in third box. Therefore, xsquare will not receive any chocolate at the end.
"""

t = int(input())

while t > 0:
    chocs = input()
    l1 = len(chocs)
    dp = [0 for i in range(l1)]
    if len(chocs) > 0:
        for i in range(2, len(chocs)):
            if not (chocs[i] == chocs[i-1] and chocs[i-1] == chocs[i-2]):
                dp[i] = 3
                if i > 3:
                    dp[i] += dp[i-3]
        max1 = max(dp)
        print(l1 - max1)
    t -= 1


"""
    chocs1 = chocs
    print('chocs1 first is', chocs1)
    l1, i = len(chocs), 0
    while len(chocs1) > 0 and i < l1:
        if len(set(chocs1[i: i+3])) != 1:
            print('Removing', chocs1[i: i+3], ' From', i, ' to ', i+2)
            chocs1 = chocs1[:i] + chocs1[i+3:]
            print('Remaining from 0 to', i-1, ' and ', i+3, ' to ', len(chocs1))
            print('chocs1 is -> ', chocs1)
            i -= 3
        i += 1
    print('chocs1 is', chocs1, '\n\n')
"""


