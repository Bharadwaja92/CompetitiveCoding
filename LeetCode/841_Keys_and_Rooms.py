"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. 
However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. 
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
return true if you can visit all the rooms, or false otherwise.

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
"""

from typing import List, Set


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys_found_set = set([0])
        visited_rooms = set([0])

        def visit_rooms(rooms: List[List[int]], visited_rooms: Set, keys_found_set: Set, room_index: int):
            # Add all the keys found in this room to  keys_found_set
            print('visited_rooms =', visited_rooms)
            print('keys_found_set =', keys_found_set)
            keys = rooms[room_index]
            keys_found_set = keys_found_set.union(keys)
            if len(keys_found_set) == len(rooms): return True
            for key in keys:
                if key not in visited_rooms:
                    visited_rooms = visited_rooms.union([key])
                    can_visit_rooms = visit_rooms(rooms=rooms, visited_rooms=visited_rooms, keys_found_set=keys_found_set, room_index=key)
                    if can_visit_rooms: 
                        return True
            return False

        # print('keys_found_set =', keys_found_set)
        # print('visited_rooms =', visited_rooms)
        return visit_rooms(rooms=rooms, visited_rooms=visited_rooms, keys_found_set=keys_found_set, room_index=0)
        

s = Solution()

# rooms = [[1],[2],[3],[]]
# print(rooms, '-->', s.canVisitAllRooms(rooms), '\n')

# rooms = [[1,3],[3,0,1],[2],[0]]
# print(rooms, '-->', s.canVisitAllRooms(rooms), '\n')

# rooms = [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
# print(rooms, '-->', s.canVisitAllRooms(rooms), '\n')

# rooms = [[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]
# print(rooms, '-->', s.canVisitAllRooms(rooms), '\n')

# rooms = [[2], [], [1]]
# print(rooms, '-->', s.canVisitAllRooms(rooms), '\n')

# rooms = [[1], [2], [], [3]]
# print(rooms, '-->', s.canVisitAllRooms(rooms), '\n')

rooms = [[13],[15,29,22],[5,18,9],[7],[27],[27],[6,28],[26],[34],[1,44,11],[8,36],[17,35],[11,45,46,10,49],[19,38,47,39],[20,30],[34],[32,31],[25,19,21,29],[36],[],[38],[2,13,17,47],[12],[49,46],[],[40],[],[39,16,24],[24,41],[14,3,40],[14,43],[],[3,20,23],[37,48],[6,10],[26,1,4],[],[41,45],[23,33],[],[22,18,37],[4,33,43],[28,31,42],[30,48],[16,35],[5,8,44],[2,25],[9,21,42],[7,12,32],[]]
print(len(rooms))
# print(rooms, '-->', s.canVisitAllRooms(rooms), '\n')


"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_dict = {0: True}
        for room in rooms:
            for r in room:  
                if r not in room_dict.keys(): room_dict[r] = False
            keys_found = rooms[r]
            for k in keys_found:
                room_dict[k] = True
        print('room_dict = ', room_dict)
        return False
"""
"""
keys_found_dict = {i: False for i in range(len(rooms))}
        keys_found_dict[0] = True
        for i in range(len(rooms)-1):            
            # if keys_found_dict[i]:
            keys_in_room_i = rooms[i]
            for k in keys_in_room_i: 
                if k != i: keys_found_dict[k] = True
                print('In room ', i, 'keys_found_dict before =', keys_found_dict)

        # last_room_keys = rooms[-1]
        # for l in last_room_keys:
        #     if l != len(rooms)-1: keys_found_dict[l] = True
        # print('keys_found_dict after  =', keys_found_dict)
        return all(keys_found_dict.values())
"""

