"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", 
because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        actual_order = {order[i]: chr(ord('a')+i) for i in range(len(order))}
        # print(actual_order)
        new_words = []
        for w in words:
            nw = ''.join([actual_order[c] for c in w])
            new_words.append(nw)
        print(words)
        print(new_words)
        return new_words == sorted(new_words)


s = Solution()

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(s.isAlienSorted(words, order))

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))
