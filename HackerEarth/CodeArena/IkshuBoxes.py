"""
https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/ikshu-and-his-machine-gun/
"""

l = int(input('Enter l'))

l1 = list(map(int, input('Enter l1').split(" ")))     # To be knocked off

st = ''

count = 0

for v in l1:
    st += str(v - count) + ' '
    count += 1

print('st is ', st)