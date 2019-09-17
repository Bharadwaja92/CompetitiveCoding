""""""
"""
From the childhood we are taught that a comes before b then b comes before c and so on.So whenever we try to sort any given string we sort it in that manner only placing a before b and so on.But what happens if we initially change the pattern of sorting .This question arrived in Arav's young mind. He thought what would the final string be like if z comes before a and a comes after c and so on. He got really puzzled in finding out the final sorted string.So he asks you for help.
He gives you two strings.One the pattern string P which decides the order of alphabets and the second that is the final string F which needs to be sorted. Help him by telling him the final sorted string.

Input:  The first line contains T denoting the number of test cases.Each test case consists of two lines.The first line contains the pattern string P indicating the relative ordering of alphabets and the second line contains the final string F to be sorted.

Output: Print T lines where each line contains the sorted string.

SAMPLE INPUT 
2
wcyuogmlrdfphitxjakqvzbnes
jcdokai
miruqopsxthzdcnvkfbglwayje
wgfsyvno

SAMPLE OUTPUT 
codijak
osnvfgwy

"""

t = int(input())

while t > 0:
    l1 = input()
    sd1, sd2 = dict(), dict()
    for i in range(len(l1)):
        sd1[l1[i]] = i
        sd2[i] = l1[i]
    # print('sd1 is\n', sd1)
    # print('sd2 is\n', sd2)
    l2 = input()
    ls = []
    for c in l2:
        ls.append(sd1[c])
    # print('ls is', ls)
    for i in sorted(ls):
        print(sd2[i], end='')
    print()
    t -= 1



