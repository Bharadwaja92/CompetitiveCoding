"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the
 same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
"""


def avoidObstacles(inputArray):
    obstacles = sorted(inputArray)
    print('obstacles is ', obstacles)
    conlist = [obstacles[0]]
    maxJump = len(conlist)
    for i in range(1, len(obstacles)):
        print('conlist is ',conlist)
        if obstacles[i] - obstacles[i-1] == 1:
            conlist.append(obstacles[i])
        else:
            temp = len(conlist)
            conlist = [obstacles[i]]
            if maxJump < temp:
                maxJump = temp
    return maxJump+1

def avoidObstacles(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1


# inputArray = [5, 3, 6, 7, 9, 10, 11, 12, 15]
inputArray = [1, 4, 10, 6, 2]
inputArray = [19, 32, 11, 23]       # 3
print(avoidObstacles(inputArray))



