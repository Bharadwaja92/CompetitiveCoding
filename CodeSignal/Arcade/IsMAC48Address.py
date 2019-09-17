"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications
on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal
digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
isMAC48Address(inputString) = false.
"""
import re
def isMAC48Address(inputString):
    return bool(re.match('^([\dA-F]{2}-){5}([\dA-F]{2})$', inputString))


def isMAC48Address1(inputString):
    sp = inputString.split('-')
    if len(sp) != 6:
        return False
    validChars = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9', 'A', 'B','C', 'D', 'E', 'F']
    for seg in sp:
        print('Seg is', seg)
        if seg[0] not in validChars or seg[1] not in validChars:
            return False
    return True


inputString = "00-1B-63-84-45-E6"
# inputString = "Z1-1B-63-84-45-E6"
inputString = "not a MAC-48 address"

print(isMAC48Address(inputString))