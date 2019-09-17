"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to
rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

"""

def sortByHeight(a):
    ps = [i for i in range(len(a)) if a[i] == -1]
    aps = sorted([i for i in a if i != -1])
    for i in ps:
        aps.insert(i, -1)
    return aps


print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))

