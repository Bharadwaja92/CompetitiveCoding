"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. 
Return false otherwise.

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        steps = ['0_0']
        curr_pos = [0, 0]
        flag = False
        i = 0
        while i < len(path) and not flag:
            s = path[i]
            if s == 'N':
                curr_pos[1] += 1
            if s == 'S':
                curr_pos[1] -= 1
            if s == 'E':
                curr_pos[0] += 1
            if s == 'W':
                curr_pos[0] -= 1
            # print('curr_pos =', curr_pos)
            curr_pos_str = '{}_{}'.format(curr_pos[0], curr_pos[1])            
            if curr_pos_str in steps:
                flag = True
            else:
                steps.append(curr_pos_str)
            i += 1
        return flag


s = Solution()


# path = "NESWW"
# print(path, '-->', s.isPathCrossing(path))

# path = "NES"
# print(path, '-->', s.isPathCrossing(path))

# path = "NNNNNNSSSSSS"
# print(path, '-->', s.isPathCrossing(path))

# path = "EEEEEEWWEEWWWWWW"
# print(path, '-->', s.isPathCrossing(path))

path = "NNSWWEWSSESSWENNW"
print(path, '-->', s.isPathCrossing(path))


"""
"""
