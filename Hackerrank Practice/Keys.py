'''
You have bought a new strange keyboard. When you press the   key, you cannot use any number. And sometimes the  key,  key or  key gets accidentally pressed.

You had to send an email to your supervisor. Since you were in hurry, you didn’t even notice that the text was messed up. After you sent the email, you knew that you need some help.

Given the text you wrote, print the text your supervisor will receive.

Note: The  key changes the writing cursor's position to the beginning of the line, which means whatever after '<' goes before what is already written.

The  key changes the writing cursor's position to the end of the line, which means whatever after '>' goes after what is already written.

The  key removes the previous character to the current position. And if there is nothing written, nothing happens.

The   key enables the numbers on the keyboard if they were disabled previously, and vice-versa. Initially, the   is on, that is you can use the numbers.

Input Format

The only line of input consists of a string , denotes the text contained in the email.

Constraints

String contains Latin letters, underscores, digits, and four special characters:
 key represented by '<'
 key represented by '>'
 key represented by '*'
  key represented by '#'
Output Format

Print the text which your supervisor will receive.

Sample Input 0

HE*<LL>O
Sample Output 0

LLHO
Explanation 0

The first two letters will be written normally. So, the output is  so far.

The third character indicates that  key was pressed. Then, it deletes letter E. So, the output is  so far.

The fourth character indicates that  key was pressed. Then, the typing cursor moves to the start of the text.

The next two letters will be written at the start, since the previous character was the key. So, the output is  so far.

The seventh character indicates that  key was pressed. Then, the typing cursor moves to the end of the text.

The next letter will be written at the end, since the previous character was the  key. So, the output is .
'''

#!/bin/python3

import math
import os
import random
import re
import sys


def receivedText(S):
    
    text = S
    # print(len(text))
    i=0
    while i<len(S):              # for i in range(len(text)): 
        
        if S[i] == '*':
            
            print(S[i])
            x = S[:i]
            y = S[i+1:]
            text = x + y
            i+=1
            print('1')
            
        if S[i] == '<':
            
            print(S[i])
            x = S[:i]
            y = S[i+1:]
            text = y + x
            i+=1
            print('2')
            
        if S[i] == '>':
            
            print(text[i])
            x = S[i+1:]
            y = S[:i]
            text = y + x
            i+=1
            print('3')
            
        else:      

            text.append(S[i])
            i+=1
            print('pass')
            print(text[i])
            
            # pass
            
    return text
            

if __name__ == '__main__':
    
    '''fptr = open(os.environ['OUTPUT_PATH'], 'w')

    S = input()

    result = receivedText(S)

    fptr.write(result + '\n')

    fptr.close()'''


    S = 'HE*<LL>O'
    result = receivedText(S)
    print(result)
