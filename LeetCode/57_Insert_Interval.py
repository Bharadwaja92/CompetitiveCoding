"""
You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of the ith interval and
intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""
from typing import List


def areIntervalsOverlapping(a, b) -> bool:
    flag = min([a[1], b[1]]) - max([a[0], b[0]]) >= 0
    # print(a, ' and ', b, ' overlapping ->', flag)
    return flag


def merge_intervals(a, b):
    # print('Merging ', a, 'and', b)
    return [min([a[0], b[0]]), max([a[1], b[1]])]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        answer = []
        l_new, r_new = newInterval
        # Insert the new interval in the Intervals list
        is_inserted = False
        i = 0
        while i < len(intervals) and not is_inserted:
            l_current, r_current = intervals[i]
            if l_new < l_current:
                intervals.insert(i, newInterval)
                is_inserted = True
            i += 1

        if not is_inserted:
            intervals.append(newInterval)  # New interval is outside all left limits

        j = 0           # for j in range(0, len(intervals)):
        while j < len(intervals):
            # print('Out1 j =', j)
            curr_interval = intervals[j]
            i = j
            while i < len(intervals) and areIntervalsOverlapping(curr_interval, intervals[i]):
                # print('In i = ', i)
                curr_interval = merge_intervals(curr_interval, intervals[i])
                i += 1
            # print('After while curr_interval =', curr_interval)
            # print('Out2 i =', i)
            # j -= 1
            j = i
            answer.append(curr_interval)
            # print('Answer =', answer)

        return answer


s = Solution()

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(intervals, '-->', newInterval, '-->', s.insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(intervals, '-->', newInterval, '-->', s.insert(intervals, newInterval))

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         l_new, r_new = newInterval
#         print(newInterval, '\n')
#         i = 0
#         while i < len(intervals):
#             interval = intervals[i]
#             print(interval)
#             l_current, r_current = interval
#             if l_current > l_new: pass  # Interval not reached yet ---
#             elif r_current < l_new: pass # Interval not reached yet ---
#             elif l_current <= l_new <= r_current:  # New interval starts between this interval
#                 updated_interval = [l_current, r_new]
#                 print('-->', updated_interval)
#             elif l_new <= l_current <= r_new:      # New interval starts before this interval and overlaps
#                 updated_interval = [l_new, r_current]
#                 print('-->', updated_interval)
#             i += 1
#
#         return intervals
