"""
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. 
Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. 
If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. 
Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. 
If there are multiple shortest completing words, return the first one that occurs in words.

 Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.
Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest.
The answer is "pest" because it is the word that appears earliest of the 3.
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        licensePlate = licensePlate.lower()
        licensePlate = [c for c in licensePlate if c.isalpha()]
        shortest_word = ''
        i = 0
        while i < len(words):
            licensePlate_copy = [c for c in licensePlate]
            j = 0            
            curr_word = words[i]
            while j < len(curr_word) and len(licensePlate_copy) > 0:
                if curr_word[j] in licensePlate_copy:
                    # print('removed ', curr_word[j])
                    licensePlate_copy.remove(curr_word[j])
                # print('i = ', i, ' curr_word = ', curr_word, 'j = ', j, 'licensePlate_copy = ', licensePlate_copy)
                j += 1
            i += 1
            if len(licensePlate_copy) == 0: 
                if shortest_word == '': 
                    shortest_word = curr_word
                if len(curr_word) < len(shortest_word): 
                    shortest_word = curr_word
        #     print('Current shortest word =', shortest_word)
        #     print('\n')

        # print('Finally i =', i)
        return shortest_word


s = Solution()

licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
print(licensePlate, '-->', s.shortestCompletingWord(licensePlate, words))


licensePlate = "1s3 456" 
words = ["looks","pest","stew","show"]
print(licensePlate, '-->', s.shortestCompletingWord(licensePlate, words))
