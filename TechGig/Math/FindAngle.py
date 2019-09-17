""""""
"""
Given a right angled triangle ABC, right angled at B. Find angle ABD, where D is the mid-point of the hypotenuse(side AC).
You will be given two integers denoting sides AB and BC respectively.
Round off your answer to the nearest Integer.

Input Format: First line will contain an Integer denoting side AB.
Second line will contain an Integer denoting side BC.

Constraints
1 <= side AB <= 200
1 <= side BC <= 200

Output Format:  Output Angle ABD, rounded off to nearest integer.

Sample TestCase 1
Input
6
6
Output
45
"""
import math

# ab, bc = int(input()), int(input())
# angle = 90 - round(math.degrees(math.atan(ab / bc)))
# print(str(angle), end='')

# print(math.degrees(math.atan(ab / bc)))

# ab, bc = int(input()), int(input())

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, IterativeImputer

si = SimpleImputer(strategy='mean')
ii = IterativeImputer()
print(si)
print(ii)
