"""""""""
https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/collecting-apples-69/description/

Monk is a fitness freak. He recently joined a gym and he is very serious about it. He follows his instructor's 
instructions very seriously. His instructor suggested him to eat as many apples as possible. Monk knows that apples 
from market are not that good so he goes daily to the farms and gets apples for himself.

Initially Monk is at his house, and to move to the first farm it shall take him one unit of energy. He can move 
sequentially from his house to the first farm, from the first one to the second one, from the second one to the third 
one and so on.

There are N farms in a line. Running from one farm to the next one consumes a single unit of Monk's current energy . 
So sometimes he may have to refill his energy. He can ask a farm owner to give some milk so that he can gain some energy 
The Farm owner agrees to give him milk only on one condition that he wont be allowed to take apples from that farm.

So, at each farm, Monk has one choice either to take milk ( for increasing his energy) or apples from the farm. Each 
farm has different amount of apples and milk. So, from each farm, Monk is allowed to take only either the entire amount 
of Milk or the entire amount of apples and not none or both.

By following so, what is the maximum number of apples Monk can collect, always having non-negative energy ?

Initially Monk is at his house, and to move to the first farm it shall take him one unit of energy.

Input :
The first line contains a single integer t denoting the number of test cases in a single test file
The second line contains N and P denoting the number of farms and Monk's initial Energy level.
The next line contains N space separated integers, where the i'th integer is Milk[i] and denotes the amount of energy 
Monk can gain by taking Milk from the  farm.
The next line contains N space separated integers, where the i'th integer denotes Apples[i] ie the number of Apples 
Monk can collect from the  Farm if he will not take Milk from that farm.

SAMPLE INPUT 
1
3 2
1 2 1
100 1 100

SAMPLE OUTPUT 
200
Explanation
In the first test of the sample, there are 3 farms in a row, and Monk's initial energy is 2.

He shall first move from his house to the first farm. After this,

Energy : 1, Apples : 0

He shall then collect all apples available in the first farm, and then move to the second farm

Energy :0, Apples : 100

He shall then Have all the Milk available in the second farm and move to the  farm.

Energy : 1 , Apples: 100

He shall then Collect all the apples available in the last farm and end his journey.

Energy : 0 ,Apples : 200

This is the maximum number of apples Monk can collect.
"""
