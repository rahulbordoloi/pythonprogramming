# Link - https://leetcode.com/problems/longest-common-prefix/
"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # zipObject = list(zip(*strs))
        commonPrefix = ""
        if (strs is None) | len(strs) == 0:
            return commonPrefix
        for item in list(zip(*strs)):
            if len(set(item)) == 1:
                commonPrefix += item[0]
            else:
                break
        return commonPrefix

