""""""
"""
Although Python does provide a bunch of useful built-in functions, some of them are simply missing for no apparent 
reason. One example of such function is a sign function implemented in many other languages. sign(x) returns 1 if x is 
positive, -1 if x is negative, and 0 if x is equal to zero.

You decided to build your own package of useful functions, and would like to start with the sign function. 
Given the value of x, return the result of applying the sign function to it.

Example

For x = -34, the output should be
sign(x) = -1.

-34 is a negative number, thus the output should be -1.
"""

class Functions(object):
    @staticmethod
    def sign(x):
        return 1 if x > 0 else -1 if x < 0 else 0

def sign(x):
    return Functions.sign(x)


print(sign(-34))
print(sign(35))
print(sign(0))