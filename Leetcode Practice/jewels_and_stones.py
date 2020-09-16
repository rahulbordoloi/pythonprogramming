# Link - https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        c = 0
        for i in J:
            c += S.count(i)
        
        return c
        
