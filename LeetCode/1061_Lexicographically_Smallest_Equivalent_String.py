"""
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde",
"acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

 Example 1:

Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
Example 2:

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
Example 3:

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m],
thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
"""


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        mapping_dict = {}
        mapping_list = [None for _ in range(len(s1) + len(s2))]
        for i in range(len(s1)):
            c1, c2 = s1[i], s2[i]
            if c1 not in mapping_dict and c2 not in mapping_dict:  # Both new characters
                mapping_dict[c1] = i
                mapping_dict[c2] = i
                mapping_list[i] = {c1, c2}
            elif c2 not in mapping_dict:  # Have only first character
                index_to_insert = mapping_dict[c1]
                new_list = mapping_list[index_to_insert]
                new_list.add(c2)
                mapping_list[index_to_insert] = new_list
                mapping_dict[c2] = index_to_insert
            elif c1 not in mapping_dict:  # Have only second character
                index_to_insert = mapping_dict[c2]
                new_list = mapping_list[index_to_insert]
                new_list.add(c1)
                mapping_list[index_to_insert] = new_list
                mapping_dict[c1] = index_to_insert
            elif c1 in mapping_dict and c2 in mapping_dict and c1 != c2:    # Have both characters
                print('Have both characters')
                index1_to_insert = mapping_dict[c1]
                new_list1 = mapping_list[index1_to_insert]

                index2_to_insert = mapping_dict[c2]
                new_list2 = mapping_list[index2_to_insert]

                new_list3 = set(new_list1).union(set(new_list2))
                mapping_list[index1_to_insert] = new_list3
                mapping_dict[c1] = index1_to_insert

            #     new_list2.add(c1)
                mapping_list[index2_to_insert] = new_list3
                mapping_dict[c2] = index2_to_insert
                
                print(new_list1, new_list2, new_list3, mapping_dict)

            print(c1, c2, mapping_list, '\n')

        print(mapping_dict)
        print(mapping_list)

        changed_str = ''
        for c in baseStr:
            if c not in mapping_dict:
                changed_str += c
            else:
                print(c, '-->', mapping_dict[c], '-->', mapping_list[mapping_dict[c]], '-->', min(mapping_list[mapping_dict[c]]))
                changed_str += min(mapping_list[mapping_dict[c]])

        # changed_str = [mapping_dict[c] if c in mapping_dict else c for c in baseStr]
        return changed_str


s = Solution()

# s1 = "parker"
# s2 = "morris"
# baseStr = "parser"
# print(s1, s2, s.smallestEquivalentString(s1, s2, baseStr))  #  == 'makkek'
#
#
# s1 = "hello"
# s2 = "world"
# baseStr = "hold"
# print(s1, s2, s.smallestEquivalentString(s1, s2, baseStr) == 'hdld')
#
#
# s1 = "leetcode"
# s2 = "programs"
# baseStr = "sourcecode"
# print(s1, s2, s.smallestEquivalentString(s1, s2, baseStr))
#
#
# s1 = "aabbbabbbbbabbbbaabaabbaaabbbabaababaaaabbbbbabbaa"
# s2 = "aabbaabbbabaababaabaababbbababbbaaaabbbbbabbbaabaa"
# baseStr = "buqpqxmnajphtisernebttymtrydomxnwonfhfjlzzrfhosjct"
# print(s1, s2, s.smallestEquivalentString(s1, s2, baseStr))
#
#
# s1 = "bcfeaabddgcdaefcbfadggfagfgfedeefbebdbeefbecggcgge"
# s2 = "feegaacabcfadggfcaabcbadbbecbfdcabgeaegfcagdfggdgg"
# baseStr = "mytnpodxbwxcxcplapgrqjzkfrkizffkbquwqbkxmpqjmxykvb"
# print(s1, s2, s.smallestEquivalentString(s1, s2, baseStr))

s1 = "opecenadojbodihfgmpijpfocomhcncicefpohkibjckijghii"
s2 = "ndlbhpaeppgekfhnjnmmplmdoifdhbglmedpjgleofgnahglbe"
baseStr = "ttusuhhrabgsswpaapxoxdanchyccmpjitwwmfioedtbiggfru"
print(s1, s2, s.smallestEquivalentString(s1, s2, baseStr))


# for i in range(len(s1)):
#     if s1[i] != s2[i]:
#         print(i, s1[i], s2[i])

"ttusuaaraaasswbaabxbxbabaayaabbbatwwbaababtaaaaaru"
"ttusuaaraaasswaaaaxaxaaaaayaaaaaatwwaaaaaataaaaaru"