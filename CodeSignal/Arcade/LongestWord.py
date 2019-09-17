"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
"""
import re

def longestWord1(text):
    w = [re.findall('[A-Za-z]+', s)[0] for s in text.split(' ')]
    print('w is ',w)
    return max(w, key=len)

def longestWord(text):
    s = re.split('[^A-Za-z]+', text)
    return max(s, key=len)


text = "Ready, steady, go!"
text = "Ready[[[, steady, go!"
text = "You are the best!!!!!!!!!!!! CodeFighter ever!"
text = "To be or not to be"
print(longestWord1(text))
