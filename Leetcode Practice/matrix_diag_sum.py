# Link - https://leetcode.com/problems/matrix-diagonal-sum

# Matrix Diagonal Sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum = 0
        
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][len(mat) - i - 1]
        
        if len(mat) % 2 != 0:
            sum -= mat[len(mat)//2][len(mat)//2]
        
        return sum
        
