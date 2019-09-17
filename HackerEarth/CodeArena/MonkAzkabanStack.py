""""""
"""
Monk's wizard friend Harry Potter is excited to see his Dad fight Dementors and rescue him and his Godfather Sirius 
Black. Meanwhile their friend Hermoine is stuck on some silly arrays problem. Harry does not have time for all this, 
so he asked Monk to solve that problem for Hermoine, so that they can go.

Input Format:
First line consists of a single integer denoting N.
Second line consists of N space separated integers denoting the array A.

Output Format:
Print N space separated integers, denoting x+y for each i

SAMPLE INPUT 
5
5 4 1 3 2
SAMPLE OUTPUT 
-2 0 6 1 3 
Explanation
Values of x for each i: -1 1 2 2 4
Values of y for each i: -1 -1 4 -1 -1
So, x+y  for each i: -2 0 6 1 3
"""

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print(-1)
    else:
        return stack.pop()


def printNGE(arr):
    s = createStack()
    element , next = 0, 0

    # push the first element to stack
    push(s, arr[0])

    # iterate for rest of the elements
    for i in range(1, len(arr), 1):
        next = arr[i]

        if not isEmpty(s):
            element = pop(s)
            # print('element is', element)
            while element < next:
                print(str(element) + " -- " + str(next))
                if isEmpty(s):
                    break
                element = pop(s)

            if element > next:
                push(s, element)

        push(s, next)

    while not isEmpty(s):
        element = pop(s)
        next = -1
        print(str(element) + " -- " + str(next))


n = int(input())
a = list(map(int, input().split(" ")))
printNGE(a)

