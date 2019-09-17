
xs = [()]

res = [False] * 2

print(res)

if xs:
    res[0] = True

if xs[0]:
    res[0] = True

print(res)

x = 1302

b = bin(x)
h = hex(x)

print(b, type(b), int(b[2:]))
print(h, type(h))

print('>>>', format(516, 'x'))

# print(hex(int(bin(x)[2:])))