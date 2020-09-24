# Link - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        res = nums1 + nums2
        res.sort()
        if len(res) % 2 != 0:
            return res[len(res) // 2]
        else:
            return sum(res[len(res) // 2 - 1 : len(res) // 2 + 1]) / 2
