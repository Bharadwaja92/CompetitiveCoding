"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
"""

from typing import List
from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        if num_points < 3: return num_points
        slope_matrix = []

        for i in range(num_points-1):
            slopes = []
            for j in range(i, num_points):
                p1, p2 = points[i], points[j]
                p1_x, p1_y = p1
                p2_x, p2_y = p2
                s = (p2_y - p1_y) / (p2_x - p1_x) if p2_x != p1_x and p2_y != p1_y  \
                    else 'y' if p2_y == p1_y else 'x' if p2_x == p1_x else slope_matrix[i][j]
                slopes.append(s)
            slope_matrix.append(slopes)

        # for l in slope_matrix:
        #     print(l)
        # print('-----')

        global_value_count = float('-inf')
        for l in slope_matrix:
            c = Counter(l)
            if len(c) == 1 and ('x' in c or 'y' in c):
                print(c)
                return max(global_value_count+1, c[list(c.keys())[0]]) # num_points
            max_value_count = max(c.values())
            global_value_count = max(global_value_count, max_value_count)
            print(c, '-->', global_value_count)  # l,

        # print('-----')

        return global_value_count + 1


s = Solution()

# points = [[1, 1], [2, 2], [3, 3]]
# print(points, '-->', s.maxPoints(points) == 3)
#
# points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
# print(points, '-->', s.maxPoints(points) == 4)
# # #
# points = [[0,1],[0,0]]
# print(points, '-->', s.maxPoints(points) == 2)
#
# points = [[4,5],[4,-1],[4,0]]
# print(points, '-->', s.maxPoints(points) == 3)
#
# points = [[2,3],[3,3],[-5,3]]
# print(points, '-->', s.maxPoints(points) == 3)
#
# points = [[0,0],[1,-1],[1,1]]
# print(points, '-->', s.maxPoints(points) == 2)
#
# points = [[21,130],[-4,77],[429,115],[12,106],[0,-41],[-10,77],[-18,-33],[2,-21],[5,77],[-1,-45],[-29,-37],[14,-4],[5,-21],[16,41],[3,74],[-6,-65],[-3,-38],[-14,-12],[-20,13],[-5,82],[-3,-11],[-4,40],[16,-5],[-8,7],[0,77],[18,-6],[-8,77],[2,2],[4,1],[9,-5],[-2,73],[6,-29],[9,-35],[6,-17],[6,71],[-18,26],[10,-37],[-4,-57],[1,88],[3,77],[-12,42],[10,-1],[-46,-45],[4,-11],[6,90],[-16,11],[8,69],[-9,86],[-1,-15],[-9,1],[-27,-34],[30,154],[9,138],[7,-13],[10,67],[5,72],[27,146],[-3,-53],[-3,80],[10,-2],[-2,-49],[50,-17],[10,6],[-10,-81],[-7,-69],[-7,84],[0,3],[-8,85],[-5,-61],[-17,-37],[-10,87],[1,76],[1,-37],[-15,34],[8,-1],[3,82],[-3,77],[-10,33],[-21,18],[-4,63],[0,-17],[9,98],[9,-42],[-8,43],[-27,2],[40,-23],[20,-7],[2,77],[-6,77]]
# print(points, '-->', s.maxPoints(points) == 15)

points = [[0,1],[0,2],[2,2],[1,0],[2,0]]
print(points, '-->', s.maxPoints(points))

# print(points, '-->', s.maxPoints(points))
