"""
You are provided with a source directory and two methods. 
One method will return all the files and subdirectories in that folder. 
The other method will return the size of the file. It will return minus one if that is not a file. 
storage.list --> Gives list of files and subdirectories
storage.size --> Gives size of the file, returns -1 if it is not a file

We can use a tree structure wherein we will iterate through all the children of a particular node. And we can find out if that child is a file or a subfolder. Depending upon that, we can save the files and their sizes. Also, the question was to return the top ten files along with their sizes. I maintained a list that contained tuples. Each tuple will have the path of the file and the size of the file. To get the top ten files, I used Insertion Sort. I can get to know where exactly do I need to insert the new file that is coming in. 
"""
ans = []  # [(file_path, file_size)]
min_size, max_size = float('inf'), float('-inf')

def dfs(curr_dir):
	children = storage.list(curr_dir)
	for c in children:
		curr_file_size = storage.size(c)
		if curr_file_size != -1:  # Found a file
			if len(ans) <= 10:
				# Find the correct place to put the file
				i = 0
				while i < len(ans) and ans[i][1] < curr_file_size:
					i += 1
				ans.append(i, (c, curr_file_size)) 
			else: # Found 10. So find the appropriate position and pop the file with min size
				i = 10
				while i >= 0 and ans[i][1] > curr_file_size:
					i -= 1
				ans.append(i, (c, curr_file_size))
		else: # Recurse over this sub folder
			dfs(c)


dfs('/')
return ans

#############################  TIME AND SPACE COMPLEXITIES ########################################
"""
### 1. Time and Space Complexities in BigO Notation

#### Your Initial Approach

**Time Complexity:**

1. **DFS Traversal**:
   - The DFS traversal itself will visit each directory and file once, so this part takes \(O(N + M)\), where \(N\) is the number of directories and \(M\) is the number of files.
   
2. **Insertion Sort for Top Ten Files**:
   - For each file, you find the appropriate position in the list of top ten files.
   - In the worst case, inserting an element into a list of ten elements takes \(O(10) = O(1)\).
   - Since you process each file individually, the total cost for insertion operations is \(O(M \times 10) = O(M)\).

**Overall Time Complexity**: \(O(N + M)\)

**Space Complexity:**

1. **DFS Stack**: In the worst case, the depth of the recursion stack is the depth of the directory tree, which can be up to \(O(N)\).
2. **Top Ten Files List**: You are maintaining a list of up to ten files, so this is \(O(10) = O(1)\).

**Overall Space Complexity**: \(O(N)\)

#### Updated Approach (Using Min-Heap)

**Time Complexity:**

1. **DFS Traversal**:
   - The DFS traversal itself will visit each directory and file once, so this part takes \(O(N + M)\).

2. **Heap Operations for Top Ten Files**:
   - For each file, you perform a `heappush` or `heappushpop` operation on a heap of size ten.
   - Both `heappush` and `heappushpop` operations take \(O(\log 10) = O(1)\) time.
   - Since you process each file individually, the total cost for heap operations is \(O(M \times \log 10) = O(M)\).

**Overall Time Complexity**: \(O(N + M)\)

**Space Complexity:**

1. **DFS Stack**: In the worst case, the depth of the recursion stack is the depth of the directory tree, which can be up to \(O(N)\).
2. **Min-Heap**: The heap will contain up to ten elements, so this is \(O(10) = O(1)\).

**Overall Space Complexity**: \(O(N)\)

### 2. Change in Complexities for Top X Files

#### Time Complexity:

1. **Insertion Sort for Top X Files (Your Approach)**:
   - Finding the appropriate position in a list of size \(X\) takes \(O(X)\).
   - Inserting \(M\) files into this list takes \(O(M \times X)\).

2. **Heap Operations for Top X Files (Updated Approach)**:
   - Both `heappush` and `heappushpop` operations on a heap of size \(X\) take \(O(\log X)\).
   - Processing \(M\) files with heap operations takes \(O(M \times \log X)\).

#### Space Complexity:

1. **Top X Files List**: In both approaches, maintaining a list or heap of size \(X\) takes \(O(X)\).

### 3. Complexities in Terms of Number of Subdirectories and Files

Let \(N\) be the number of subdirectories and \(M\) be the number of files.

#### Your Initial Approach

**Time Complexity**:
- **DFS Traversal**: \(O(N + M)\)
- **Insertion Sort for Top X Files**: \(O(M \times X)\)

**Overall Time Complexity**: \(O(N + M \times X)\)

**Space Complexity**:
- **DFS Stack**: \(O(N)\)
- **Top X Files List**: \(O(X)\)

**Overall Space Complexity**: \(O(N + X)\)

#### Updated Approach (Using Min-Heap)

**Time Complexity**:
- **DFS Traversal**: \(O(N + M)\)
- **Heap Operations for Top X Files**: \(O(M \times \log X)\)

**Overall Time Complexity**: \(O(N + M \times \log X)\)

**Space Complexity**:
- **DFS Stack**: \(O(N)\)
- **Min-Heap**: \(O(X)\)

**Overall Space Complexity**: \(O(N + X)\)

In summary, the min-heap approach is more efficient for larger values of \(X\) due to its logarithmic complexity for maintaining the top \(X\) files, while the insertion sort approach may be simpler but less efficient as \(X\) increases. Both approaches are efficient in terms of space, with the dominant factor being the depth of the directory tree (number of subdirectories).
"""


############  BETTER SOLUTION ##############

import heapq

ans = []  # Min-heap to store the top ten largest files

def dfs(curr_dir):
    children = storage.list(curr_dir)
    for c in children:
        curr_file_size = storage.size(c)
        if curr_file_size != -1:  # Found a file
            if len(ans) < 10:
                heapq.heappush(ans, (curr_file_size, c))
            else:
                # If the current file is larger than the smallest file in the heap
                if curr_file_size > ans[0][0]:
                    heapq.heappushpop(ans, (curr_file_size, c))
        else:  # Recurse over this sub folder
            dfs(c)

dfs('/')

# Convert the heap to a sorted list in descending order
ans.sort(reverse=True, key=lambda x: x[0])
return ans


