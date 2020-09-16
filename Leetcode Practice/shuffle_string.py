# Link - https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        return ''.join([y for i, y in sorted(zip(indices, s))])
