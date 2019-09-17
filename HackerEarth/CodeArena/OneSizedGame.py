"""  https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/one-sized-game/ """
"""
Ladia and Kushagra are playing the One-Sized Game. The rules of this game are pretty simple.

They have an array consisting of N elements (1-indexed). In each step, one needs to find out the smallest element 
present in the array. Get the index of that element and subtract that value (index value) from every element of the 
array. If there is a clash/collision between the smallest element, pick the one that occurs first -- that is the one 
having smaller index. This process is repeated several times. Whenever an element's value goes below 0 this element 
gets removed from the array and the array gets re-sized.

During the game's play, if at any point of time, the array is left with only one element, Ladia wins the game otherwise 
Kushagra wins.

Given an array consisting of N elements, print whether Ladia will win or Kushagra.

Input:
The first line contains an integer T denoting the number of test-cases. Each test case begins with an integer N that 
denotes the size of the array. This is followed up by N space separated integers.

Output:
For each test case print whether "Ladia" wins or "Kushagra" (without quotes).

SAMPLE INPUT 
2
3
5 2 2
3
3 7 6
SAMPLE OUTPUT 
Ladia
Kushagra
Explanation
Game 1 :
The smallest element is 2 ,since there is a collision we pick index 2 over 3 as it is smaller. We then subtract 2 from the entire array.
New array- {3,0,0}
Smallest element is 0, again we pick index 2 and subtract 2 from entire array.
New array - {1,-2,-2}
Since we have elements <0 ,they get deleted. Modified array - {3}. The size of array is now 1. So Ladia wins this game.

Game 2:
Smallest element is 3,index is 1. So we subtract 1 from the entire array. Repeat this process 4 times. We get array
New array - {3,2}
Smallest element is 2,index is 2. So we subtract 2 from the entire array.
New array - {1,0}
Smallest element is 0, index is 2. Subtract 2 from the array.
New array - {-1,-2}. Negative element gets deleted. Modified array - { }. So Kushagra wins this game.
"""

t = int(input())
print('t =', t)

while t > 0:
    n = int(input())
    print('n =', n)
    l1 = list(map(int, input().strip().split(" ")))
    print('l1 =', l1)
    while len(l1) > 1:
        # Get index of smallest number
        smallest_index = l1.index(min(l1)) + 1
        # Subtract this index from all numbers and remove all negative numbers
        l1 = [v - smallest_index for v in l1 if v >= smallest_index]
        # print(l1)
    # print('Finally, l1=', l1)
    if len(l1) == 0:
        print('Kushagra')
    else:
        print('Ladia')
    t -= 1





