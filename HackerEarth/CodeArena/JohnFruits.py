""""""
"""
John loves fruits. He eats one apple, banana or pear literally every hour.
John came to fruit shop to buy some fruits. He has m coins that he is going to spend to buy as many fruits as he can. 
He counted the number of apples, bananas and pears, and he also knows the price of a single apple, the price of a 
single banana and the price of a single pear in this shop.

Help John to buy the maximum number of fruits.

Input format
First line contains three integers a, b and p — the number of coins needed to be spend to buy one apple, one banana and 
one pear ().

Second line contains three integers ca, cb, cp,  and  — the number of apples, the number of bananas and the number of 
pears available in the store ().

Third line contains integer m — the number of coins John owns ().

Output format:  Output single integer — the maximum number of fruits John can buy.

SAMPLE INPUT 
1 5 10
2 4 1
14
SAMPLE OUTPUT 
4
Explanation
John buys two apples and two bananas, spending 12 coins.
"""

costs = list(map(int, input().split(" ")))
pricea, priceb, pricep = costs[0], costs[1], costs[2]
nums = list(map(int, input().split(" ")))
numa, numb, nump = nums[0], nums[1], nums[2]
m = int(input())

sum1, count1 = 0, 0
flag = True

while flag:
    if numa >= 0 and numb >= 0:
        if sum1 + pricea + priceb <= m:
            numa -= 1
            numb -= 1
            count1 += 2
            sum1 += pricea + priceb
        else:
            flag = False
    else:
        if numa >= 0 and nump >= 0:
            if sum1 + pricea + pricep <= m:
                numa -= 1
                nump -= 1
                count1 += 2
                sum1 += pricea + pricep
        else:
            flag = False
    print(sum1, count1)

print(count1)



