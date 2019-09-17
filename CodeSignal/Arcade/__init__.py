"""
Code Signal
"""

""" 
*********************************
avoidObstacles

stringsRearrangement

spiralNumbers
*********************************
"""

# from CodeSignal.Arcade.AddBorder import addBorder

name = None


def setName():
    global name
    locals()['name'] = 'RaviTeja'
    globals()['name'] = 'Ravi'
    name = "Teja"
    # print('globals are', globals())
    # print('locals are', locals())
    print("in method", name, locals()['name'], globals()['name'])


# setName()
print("out method", name)

a = [2]

import copy

b = copy.deepcopy(a)

print(a, b)
b.append(3)
print(a, b)

