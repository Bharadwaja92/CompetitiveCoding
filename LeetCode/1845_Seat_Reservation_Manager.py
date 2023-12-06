"""
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. 
All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
 

Example 1:

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
"""

class SeatManager:

    def __init__(self, n: int):
        self.available_seat = 1
        self.seats = [0 for _ in range(n+1)]
        return None

    def reserve(self) -> int:
        # print('Current avlbl seat =', self.available_seat)
        self.seats[self.available_seat] = 1
        self.available_seat += 1
        return self.available_seat - 1

    def unreserve(self, seatNumber: int) -> None:
        self.seats[seatNumber] = 0
        self.available_seat = min(self.available_seat, seatNumber)

# cmds = ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
# unres = [[5], [], [], [2], [], [], [], [], [5]]

cmds = ["SeatManager","reserve","unreserve","reserve","unreserve","reserve","unreserve","reserve","reserve","reserve","reserve","reserve","unreserve","unreserve",
        "unreserve","reserve","unreserve","reserve","reserve","unreserve","unreserve","reserve","unreserve","unreserve","unreserve","reserve","unreserve","reserve",
        "reserve","reserve","reserve","unreserve","reserve","reserve","reserve","unreserve","unreserve","unreserve","reserve","unreserve","reserve","reserve","reserve",
        "unreserve","reserve","unreserve","unreserve","unreserve","unreserve","reserve","unreserve","unreserve","reserve","unreserve","unreserve","reserve","reserve",
        "reserve","reserve","unreserve","reserve"]
unres = [[798],[],[1],[],[1],[],[1],[],[],[],[],[],[5],[3],[2],[],[4],[],[],[1],[3],[],[2],[4],[1],[],[1],[],[],[],[],[1],[],[],[],[1],[3],[2],[],[5],[],[],[],[5],[],
         [6],[4],[5],[1],[],[2],[3],[],[1],[2],[],[],[],[],[2],[]]

op = [[],1,[],1,[],1,[],1,2,3,4,5,[],[],[],2,[],3,4,[],[],1,[],[],[],1,[],1,2,3,4,[],1,2,3,[],[],[],1,[],2,3,4,[],5,[],[],[],[],1,[],[],2,[],[],1,2,3,4,[],2]
ex = [[],1,[],1,[],1,[],1,2,3,4,5,[],[],[],2,[],3,4,[],[],1,[],[],[],1,[],1,2,3,4,[],1,5,6,[],[],[],1,[],2,3,5,[],5,[],[],[],[],1,[],[],2,[],[],1,2,3,4,[],2]

# for i in range(len(cmds)):
#     print(i, unres[i], anss[i])

ans = []
for i in range(len(cmds)):
    c, v = cmds[i], unres[i]
    if c == "SeatManager": 
        obj = SeatManager(v[0])
        ans.append(None)
        # print(obj.available_seat)
        # print(obj.seats)
    elif c == "reserve":
        v = obj.reserve()
        # print('After reserving seat', obj.seats)
        ans.append(v)
    elif c == "unreserve":
        obj.unreserve(seatNumber=v[0])
        # print('After reserving seat', obj.seats)
        ans.append(None)

    print(op[:i])
    print(ans)




