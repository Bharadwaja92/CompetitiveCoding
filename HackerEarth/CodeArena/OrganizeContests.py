""""""
"""
Everyone who is involved with HackerEarth in what so ever form knows who Little Kuldeep is. He's not so little, but he's called that. (No one knows why!) He's pretty efficient at organizing, mentoring, managing various hiring challenges, contests happening on HackerEarth all the time. But age has caught up with him, finally. He's turned into little, old Kuldeep from little Kuldeep.
Earlier, he could've handled multiple contests like a piece of cake, but it is not possible for him now. In the present scenario, he needs other people to moderate contests, because he's busy moderating some other contest which is happening at the same time.

Given the timings of the contests happening, can you check and tell little, old Kuldeep if he would need a 
moderator to help him out, or not?

Input format: The input starts with a number, t, denoting the number of contests in a single day. 
On the next n lines, the time at which a contest starts and finishes is given.

Output format:  For every case, you need to print a single line stating 
"Will need a moderator!" if contests are clashing, or "Who needs a moderator?" if the events are NOT clashing.


Example Input:
2
09:30-11:00
11:00-12:00

Example Output:
Who needs a moderator?

SAMPLE INPUT 
2
11:00-13:30
13:00-13:45
SAMPLE OUTPUT 
Will need a moderator!
"""

import datetime
# n = int(input())
# l1 = list(map(int, input().split(" ")))

t1, t2 = '09:30', '11:00'
t3, t4 = '11:00', '12:00'
t5, t6 = '11:00', '13:30'
t7, t8 = '13:00', '13:45'

print(datetime.datetime.strptime(t3, '%I:%M'))
print(datetime.datetime.strptime(t2, '%I:%M'))
print(datetime.datetime.strptime(t1, '%I:%M'))
print(datetime.datetime.strptime(t4, '%I:%M'))
print(datetime.datetime.strptime(t5, '%H:%M'))
print(datetime.datetime.strptime(t6, '%H:%M'))
print(datetime.datetime.strptime(t7, '%H:%M'))
print(datetime.datetime.strptime(t8, '%H:%M'))

print()




