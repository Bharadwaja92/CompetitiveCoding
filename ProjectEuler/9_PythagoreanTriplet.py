"""     https://projecteuler.net/problem=9        """
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

allCombosToGetSum1000 = []
count = 0
for i in range(1, 999):
    for j in range(i, 1000):
        k = 1000 - (i+j)
        if i + j < 1000:
            lt = sorted([i, j, k])
            if lt not in allCombosToGetSum1000:
                count += 1
                print(lt)
                # allCombosToGetSum1000.append(lt)
            # print(i, j, k)
print(len(allCombosToGetSum1000))

print(count)