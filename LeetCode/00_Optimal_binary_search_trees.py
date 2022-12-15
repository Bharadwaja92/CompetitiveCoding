"""
6.20. Optimal binary search trees. Suppose we know the frequency with which
keywords occur in programs of a certain language, for instance:
begin 5%
do 40%
else 8%
end 4%
if 10%
then 10%
while 23%
We want to organize them in a binary search tree, so that the keyword in the root
is alphabetically bigger than all the keywords in the left subtree and smaller than
all the keywords in the right subtree (and this holds for all nodes).

Figure 6.12 has a nicely-balanced example on the left. In this case, when a
keyword is being looked up, the number of comparisons needed is at most three:
for instance, in finding “while”, only the three nodes “end”, “then”, and “while”
get examined. But since we know the frequency with which keywords are
accessed, we can use an even more fine-tuned cost function, the average number
of comparisons to look up a word. For the search tree on the left, it is
cost = 1(0.04) + 2(0.40 + 0.10) + 3(0.05 + 0.08 + 0.10 + 0.23) = 2.42.
By this measure, the best search tree is the one on the right, which has a cost of
2.18.
Give an efficient algorithm for the following task.
Input: n words (in sorted order); frequencies of these words:
p1, p2,..., pn.
      Chapter 6 Algorithms 183
Output: The binary search tree of lowest cost (defined above as the
expected number of comparisons in looking up a word).
"""

"""
https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
"""