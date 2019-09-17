""""""
"""
For this challenge, you need to read a line from stdin and check whether it is of type integer, float or string. 
If input is- 
    Integer print 'This input is of type Integer.' to the stdout 
    Float print 'This input is of type Float.' to the stdout 
    String print 'This input is of type string.' to the stdout 
    else print 'This is something else.' to the stdout. 

Input Format
A single line to be taken as input as save it to a variable(name of your choice). 

Constraints
1 < |s| < 10000

Output Format
Print the text according to the data type you get as an input. 

Sample TestCase 1
Input
-32767
Output
This input is of type Integer.

"""

x1 = ['32', '32.2', '32a', '-32767', '1.2.3', '1.2@3']


def isInt(x):
    try:
        x = int(x)
        return True
    except Exception:
        return False


def isFloat(x):
    try:
        x = float(x)
        return True
    except Exception:
        return False

def isString(x):
    return isinstance(x, str)


for x in x1:
    print(x)
    if isInt(x):
        print('This input is of type Integer.')
    elif isFloat(x):
        print('This input is of type Float.')
    elif isString(x):
        print('This input is of type string.')
    else:
        print('This is something else.')


"""
import re

    # flagIsNegative = x[0] == '-'
    # print(all(c.isalnum() for c in x), any(c.isalnum() for c in x), any(c.isspace() for c in x))
    # print(x)
    # if any(c.isalpha() for c in x) or x.count('.') > 1:
    #     print('This input is of type string.')
    # elif x.count('.') == 1:
    #     print('This input is of type Float.')
    # elif x.count('.') == 0:
    #     print('This input is of type Integer.')
    # else:
    #     print('This is something else.')
"""
