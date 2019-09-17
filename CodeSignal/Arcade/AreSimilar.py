""""""
"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of
the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
"""

def areSimilar(A, B):
    print('sorted(B) is', sorted(B))
    for a1 in A:
        print(a1)
    print('---------------')
    for b1 in B:
        print(b1)

    for c in list(zip(A,B)):
        print(c)

    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2


a = [1, 2, 2]
b = [2, 1, 1]
print(areSimilar(a, b))

"""
a = [1, 2, 2]
b = [2, 1, 1]
print(areSimilar(a, b))

a = [1, 2, 3]
b = [2, 1, 3]
print(areSimilar(a, b))

a = [1, 2, 3]
b = [1, 2, 3]
print(areSimilar(a, b))
"""