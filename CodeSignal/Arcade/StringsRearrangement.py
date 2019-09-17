""""""
"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the
rearrangement the strings at consecutive positions would differ by exactly one character.

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false.

All rearrangements don't satisfy the description condition.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Strings can be rearranged in the following way: "aa", "ab", "bb".
"""

"""***************************   USE PERMUTATIONS   ***************************"""

def stringsRearrangement(inputArray):
    inputArray.sort()
    for i in range(len(inputArray)-1):
        s1, s2 = inputArray[i], inputArray[i+1]
        # print(s1, s2)
        count = 0
        for c1, c2 in zip(s1, s2):
            # print('>>', c1, c2, count)
            if c1 != c2:
                count += 1
            if count > 1:
                return False
        # print('\n')
    return True


# inputArray = ["q", "q", "q"]             # False
# print(stringsRearrangement(inputArray))

inputArray = ["ab", "ad", "ef", "eg"]       # false
print(stringsRearrangement(inputArray))

inputArray = ["aba", "bbb", "bab"]             # False
print(stringsRearrangement(inputArray))

inputArray = ["ab", "bb", "aa"]             # True
print(stringsRearrangement(inputArray))

inputArray = ["abc", "bef", "bcc", "bec", "bbc", "bdc"]     # True
print(stringsRearrangement(inputArray))

inputArray = ["a", "b", "c"]     # True
print(stringsRearrangement(inputArray))

inputArray = ["ff", "gf",  "af", "ar", "hf"]     # True
print(stringsRearrangement(inputArray))
