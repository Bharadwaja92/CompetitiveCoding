""""""
"""
You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, 
you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. 
After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the 
corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

Example

For code = "010010000110010101101100011011000110111100100001", the output should be
messageFromBinaryCode(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the 
ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.
"""


def messageFromBinaryCode(code):
    decoded = ''
    for i in range(0, len(code), 8):
        decoded += chr(int(code[i:i+8], 2))
    return decoded


code = "010010000110010101101100011011000110111100100001"       # "Hello!"
print(messageFromBinaryCode(code))

code = "01001101011000010111100100100000011101000110100001100101001000000100011001101111011100100110001101100101001000000110001001100101001000000111011101101001011101000110100000100000011110010110111101110101"
#  "May the Force be with you"
print(messageFromBinaryCode(code))

code = "01000101011101100110010101110010011110010010000001101101011011110110110101100101011011100111010000100000011010010111001100100000011000010010000001100110011100100110010101110011011010000010000001100010011001010110011101101001011011100110111001101001011011100110011100101110"
print(messageFromBinaryCode(code))

