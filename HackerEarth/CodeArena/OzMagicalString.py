""""""
"""
Recently Oz has found a magical string consisting of single digit "1". After experimenting on the string, Oz found a 
weird magical property of the string that is whenever he touches the string then each digit "1" of string changed to 
digit "0" and each digit "0" of string changed to "01". Oz found this property interesting and immediately asked a 
question to RK : "How many 1's and 0's will be in the magical string if he touches the string M times ?"

Input :

The first line contains the number of test cases T . Each test case consists of a positive integer - M .

Output :

For each test case output two space-separated integers, number of 1's and number of 0's in the magical string if Oz 
touches the string M times.

Constraints :

1<= T <=20
1<= M <=90

SAMPLE INPUT 
2
1
2
SAMPLE OUTPUT 
0 1
1 1
"""
"""
1 to 0     and  0 to 01

2-->  1 -> 0 -> 01 ->  010 -> 10001 -> 00101010 -> 0101001001001
           01   11     21      32         43            85 
"""

zs, vs = 0, 0
zv = [0, 0]

t = 6

while t > 1:
    x, y = zv[0], zv[1]
    while x > 0:
        vs += 1
        zs += 1
        x -= 1
    while y >= 0:
        zs += 1
        y -= 1
    zv = [zs, vs]
    print('zv is', zv)
    t -= 1



