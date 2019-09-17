""""""
"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For   picture = ["abc",
                 "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

def addBorder(picture):
    top = '*'*(len(picture[0])+2)
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    picture.insert(0, top)
    picture.insert(len(picture), top)
    return picture


picture = ["abcd",
           "dedf"]

x = addBorder(picture)

for y in x:
    print(y)