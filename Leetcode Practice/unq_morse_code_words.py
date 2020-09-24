# Link - https://leetcode.com/problems/unique-morse-code-words/

'''
Runtime: 28 ms, faster than 95.58% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.6 MB, less than 99.77% of Python3 online submissions for Unique Morse Code Words.
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        answers = []
        
        for i in words:
            
            z = ''
            for j in i:
                z += morse[ord(j) - 97]
            answers.append(z)
            
        return len(set(answers))
        

        
