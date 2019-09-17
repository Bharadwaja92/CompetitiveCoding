""""""
"""
Debit Cards Validation is an important step in E- Commerce. Using Regex on the Client Side itself, once can reduce the 
load on the server.
Here, we have few Debit Card Numbers with us. You have to output "Valid" for a Valid Debit Card, "Invalid" for a 
Invalid Debit Card.
Valid Debit Cards have following properties : 
It must start with a 7, 8 or 9. 
It must contain exactly  digits 16 digits. 
It may have digits in groups of 4, separated by one hyphen "-". 

Input Format
First line will contain an Integer, denoting the number of Debit  Cards to validate.
Each of the next N lines will contain a string denoting the Debit Card Number.

Constraints
1 <= N <= 50

Output Format
Output a string "Valid" if the given Debit Card is Valid, otherwise print "Invalid".

Sample TestCase 1
Input
3
1234421312224231
7293-3124-5232-4231
7982214254367642
Output
Invalid
Valid
Valid
"""

import re


def main():
    n = int(input())
    for i in range(n):
        num = input()
        if num[0] in ['7', '8', '9'] and bool(re.search(r'''\d{3}[-]?\d{4}[-]?\d{4}[-]?\d{4}''', num[1:])):
            print('Valid', end='')
        else:
            print('Invalid', end='')


main()


