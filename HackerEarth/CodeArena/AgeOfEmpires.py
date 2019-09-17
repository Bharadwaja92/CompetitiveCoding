"""
Alice and Bob are playing the legendary game of Age of Empires. They are trying extremely hard to be strategic, and
smart - but are failing to do so. They’re newbies at the game, and are just learning the parts of the game.
"""

# t = int(input())
t = 1

while t > 0:
    # n = int(input())
    # alice = list(map(int, input().split(" ")))
    # bob = list(map(int, input().split(" ")))

    n = 4
    alice = [5, 6, 3, 1]
    bob = [10, 3, 5, 6]

    common = set(alice).intersection(set(bob))
    print(common)

    alice = list(set(alice).difference(common))
    bob = list(set(bob).difference(common))

    print(alice)
    print(bob)

    alice.sort()
    bob.sort()

    if len(alice) > 0:
        ac, bc = 0, 0

        for i in range(len(alice)):
            if alice[i] > bob[i]:
                ac += 1
            else:
                bc += 1

        if ac > bc:
            print('Alice')
        elif bc > ac:
            print('Bob')
    else:
        print('Tie')

    t -= 1

