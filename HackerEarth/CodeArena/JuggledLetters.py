"""
From the childhood we are taught that a comes before b then b comes before c and so on.So whenever we try to sort
any given string we sort it in that manner only placing a before b and so on.But what happens if we initially change
the pattern of sorting .This question arrived in Arav's young mind. He thought what would the final string be like
if z comes before a and a comes after c and so on. He got really puzzled in finding out the final sorted string.So
he asks you for help.
"""

# t = int(input())
# l1 = list(map(int, input().split(" ")))
#
# while t > 0:
#
#     t -= 1            ???????????????????????

juggled = 'wcyuogmlrdfphitxjakqvzbnes'
ip = 'jcdokai'
opr = 'codijak'  # Need to get this

lo = {}

i = 0
for c in juggled:
    lo[c] = i
    i += 1

op = ip[0]
start, end = lo[op], lo[op]

for i in range(1, len(ip)):
    if lo[ip[i]] > end:
        op = op + ip[i]
        end = lo[ip[i]]
    elif lo[ip[i]] < start:
        op = ip[i] + op
        start = lo[ip[i]]

print(op)


