""""""
"""
Yes, you read it right - Little Jhool is back, but no, he's not over his break up, still. And he's sad, broken and 
depressed; thus, he decided to visit a psychologist. She tells him to think about his pleasant memories of childhood, 
and stay busy so as to not miss his ex-girlfriend.

She asks him about his favorite memories from childhood, and being the genius Mathematician Little Jhool is, he 
remembered that solving Mathematics problem given to him by his teacher was his favorite memory.

He had two types of notebooks, when he was a kid.

10 problems could be solved in one page, in the first notebook.
12 problems could be solved in one page, in the second notebook.
Little Jhool remembered how in order to maintain symmetry, if he was given with n problems in total to solve, he tore 
out pages from both notebooks, so no space was wasted. EVER!

But, now he's unable to solve his own problem because of his depression, and for the exercise of the week, he has to 
answer the queries asked by his psychologist.

Given n number of questions, print the minimum number of pages he needs to tear out from the combination of both the 
notebooks, so that no space is wasted.

Input Format:
The first line will contain t - number of test cases.

The second will contain an integer n - number of questions.

Output Format:
Corresponding to the input, print the minimum number of pages Little Jhool needs to tear out from the combination of 
both the notebooks. If it is NOT possible, print "1".

Constraints: 
t ---> 1-100
n ---> 1-113 

SAMPLE INPUT 
2
23
32
SAMPLE OUTPUT 
-1
3
Explanation
For 32: 2 pages from the notebook, where 10 can be solved; 1 page from the notebook, where 12 can be solved.
"""

t = int(input())

while t > 0:
    n = int(input())        # V
    numpages = [10, 12]     # Coins
    m = len(numpages)

    # Base case (If given value V is 0)
    # Initialize all table values as Infinite
    table = [0 if i==0 else 10**5 for i in range(n + 1)]

    # Compute minimum coins required for all values from 1 to V
    for i in range(1, n + 1):
        for j in range(m):
            if numpages[j] <= i:
                sub_res = table[i - numpages[j]]
                if (sub_res != 10**5 and
                        sub_res + 1 < table[i]):
                        table[i] = sub_res + 1
    if table[n] == 10**5:
        print(-1)
    else:
        print(table[n])

    t -= 1


