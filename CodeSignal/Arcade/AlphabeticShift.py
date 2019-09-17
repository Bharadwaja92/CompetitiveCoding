"""
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".

"""

def alphabeticShift(inputString):
    shifted = [chr(ord('a') + ord(c)%ord('z')) if ord(c)+1 > ord('z') else chr(ord(c)+1) for c in inputString]
    return "".join(shifted)

inputString = "crazy"
inputString = "ghytra"
print(alphabeticShift(inputString)) #= "dsbaz".