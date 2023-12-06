"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        letter_order = []
        direction_down = True
        i = 0
        current_row = 0
        while i < len(s) and len(letter_order) < len(s):
            if direction_down:                
                current_row += 1
                letter_order.append(current_row)                                                
            if current_row == numRows: 
                direction_down = False 
            if not direction_down: 
                current_row -= 1                
                letter_order.append(current_row)
                
            if current_row == 1: direction_down = True 
            i += 1
        print(letter_order)
        
        new_string = ''
        for row in range(0, numRows+1):
            new_string += ''.join([s[i] for i in range(len(letter_order)) if letter_order[i] == row])

        return new_string


s1 = Solution()


# s = "PAYPALISHIRING"
# numRows = 3
# print(s1.convert(s, numRows))

# s = "PAYPALISHIRING"
# numRows = 4
# print(s1.convert(s, numRows))

# s = 'A'
# numRows = 1
# print(s1.convert(s, numRows))

s = 'AB'
numRows = 2
print(s1.convert(s, numRows))

"""
 P  A  Y  P  A  L  I  S  H  I  R  I  N  G
 1  2  3  2  1  2  3  2  1  2  3  2  1  2
[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]

P   A   H   N
A P L S I I G
Y   I   R

P A H N A P L S I I G Y I R

---
P A Y P A L I S H I R I N G
1 2 3 4 3 2 1 2 3 4 3 2 1 2

P     I    N
A   L S  I G
Y A   H R
P     I

P I N A L S I G Y A H R P I
---

P A Y P A L I S H I R I N G
1 2 3 4 5 4 3 2 1 2 3 4 5 4

P    H
A   S I
Y  I   R
P L     I G
A        N


------------------------------------------------------------
 P  A  Y  P  A  L  I  S  H  I  R  I  N  G          n=2
 0  1  2  3  4  5  6  7  8  9  10 11 12 13

 P Y A I H R N
 A P L S I I G
 
 0     0     0     0     0     0     0             2n                          (2+0)n                    2+(2-2)
    1     1     1     1     1     1     1          2n+1, 2n-1                  (2+0)n + 1, (2+0)n - 1

PYAIHRNAPLSIIG

 P  A  Y  P  A  L  I  S  H  I  R  I  N  G          n=3
 0  1  2  3  4  5  6  7  8  9  10 11 12 13

 0           0           0           0              0, 4, 8, 12                 (3+1)n                   3+(3-2)
    1     1     1     1     1     1     1           1, 3, 5, 7, 9, 11, 13       (3+1)n + 1, (3+1)n - 1  
       2           2           2                    2, 6, 10                    (3+1)n + 2

P A H N A P L S I I G Y I R
----
 P  A  Y  P  A  L  I  S  H  I  R  I  N  G         n=4,    PINALSIGYAHRPI
 0  1  2  3  4  5  6  7  8  9  10 11 12 13

 0                 0                 0               0, 6, 12                   (4+2)n                   4+(4-2)
    1           1     1            1    1            1, 5, 7, 11, 13            (4+2)n - 1, (4+2)n + 1
       2     2           2      2                    2, 4, 8, 10                (4+2)n - 2, (4+2)n + 2
          3                 3                        3, 9                       (4+2)n - 3, (4+2)n + 3


 P  A  Y  P  A  L  I  S  H  I  R  I  N  G         n=5,    PHASIYIRPLIGAN
 0  1  2  3  4  5  6  7  8  9  10 11 12 13

 0                       0                           0, 8                       (5+3)n                   5+(5-2)
    1                 1     1                        1, 7, 9                    (5+3)n - 1, (5+3)n + 1
       2           2           2                     2, 6, 10                   (5+3)n - 2, (5+3)n + 2
          3     3                 3     3            3, 5, 11, 13               (5+3)n - 3, (5+3)n + 3
             4                       4               4, 12                      (5+3)n - 4, (5+3)n + 4

P    H
A   S I
Y  I   R
P L     I G
A        N
"""