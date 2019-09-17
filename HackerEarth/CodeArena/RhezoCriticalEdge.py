""""""
"""
Rhezo likes to play with graphs having N nodes and M edges. Lonewolf is ready to give him such a graph only on one 
condition. He wants Rhezo to find the number of critical links in the graph.

A critical link in a graph is an edge that has the following property: If we cut the link/edge, the graph will have 
exactly one more connected component than it previously had, and the difference between the number of nodes on each 
side of the edge is less than a certain integer P.

Given P and the graph, can you help Rhezo calculate the number of critical links?

Input:  First line contains 3 integers N, M and P as described in the problem statement. Each of the next M lines 
contain 2 integers A and B, meaning that node number A has a link/edge with node number B.

Output: Find the number of critical links in the graph.

SAMPLE INPUT 
5 4 100
1 2
2 3
3 4
4 5
SAMPLE OUTPUT 
4
Explanation
Each edge is a critical link.


"""