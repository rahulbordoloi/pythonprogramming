# Link - https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        x = Counter(arr)
        for i in x:
            if x[i] / len(arr) > 0.25:
                return i
