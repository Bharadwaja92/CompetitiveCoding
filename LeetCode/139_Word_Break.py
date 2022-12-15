"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
"""
6.4. You are given a string of n characters s[1 ... n], which you believe to be a
corrupted text document in which all punctuation has vanished (so that it looks
something like “itwasthebestoftimes...”). You wish to reconstruct the document
using a dictionary, which is available in the form of a Boolean function dict(·):
for any string w,
dict(w) =
{
true if w is a valid word
false otherwise.
}
(a) Give a dynamic programming algorithm that determines whether the
string s[·] can be reconstituted as a sequence of valid words. The running
time should be at most O(n2), assuming calls to dict take unit time.
(b) In the event that the string is valid, make your algorithm output the
corresponding sequence of words.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        WB = [False for _ in range(len(s)+1)]
        WB[-1] = True

        temp_str = ''
        for i in range(len(s)-1, -1, -1):
            temp_str = s[i] + temp_str
            if temp_str in wordDict:
                WB[i] = True
                print('Mapped ', temp_str)
                temp_str = ''
            
            # print(s[i], '-->', WB)


        print(list(s))
        print(WB)
        return WB[0]
    

s1 = Solution()

# s = "leetcode"
# wordDict = ["leet","code"]
# print(s, '-->', wordDict, '-->', s1.wordBreak(s, wordDict))


# s = "applepenapple"
# wordDict = ["apple","pen"]
# print(s, '-->', wordDict, '-->', s1.wordBreak(s, wordDict))


# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# print(s, '-->', wordDict, '-->', s1.wordBreak(s, wordDict))

# s = "catsanddog"
# wordDict = ["cats","dog","sand","and","cat"]
# print(s, '-->', wordDict, '-->', s1.wordBreak(s, wordDict))


s = "catsanddog"
wordDict = ["cats","dog","sand","cat"]
print(s, '-->', wordDict, '-->', s1.wordBreak(s, wordDict))


s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
print(s, '-->', wordDict, '-->', s1.wordBreak(s, wordDict))


s = "a"
wordDict = ["b"]
print(s, '-->', wordDict, '-->', s1.wordBreak(s, wordDict))


"""

"""
"""
def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        WB = [False for _ in range(len(s)+1)]
        true_indices = [len(s)-1]
        WB[-1] = True

        temp_str = ''
        for i in range(len(s)-1, -1, -1):
            temp_str = s[i] + temp_str
            if temp_str in wordDict:
                WB[i] = True
                true_indices.append(i)
                print('Mapped ', temp_str)
                temp_str = ''
            # print(s[i], '-->', WB)

        # print(list(s))
        # print(WB)
        # print(true_indices)
        # print(s[:true_indices[-2]])
        return WB[0] or s[:true_indices[-2]] in wordDict

"""