def is_empty(l):
    if len(l):      return True
    elif len(l) == 0:       return False

def match(p1, p2):

    if p1 == '{' and p2 == '}':    return True
    elif p1 == '(' and p2 == ')':    return True
    elif p1 == '[' and p2 == ']':    return True
    else:   return False

def is_balanced(s):

    stack = []
    if len(s) == 0:
        return False
    else:
        for x in s:
            if x in '([{':   
                stack.append(x)
                # print(*stack)
            else:
                # print('1')
                # print(len(stack), ' ', stack[-1], ' ', x)
                if len(stack) > 0 and match(stack[-1], x):
                    # print('2')
                    # print(stack[-1], ' ', x)     
                    stack.pop()
                    # print(*stack)
                else:   return False
    
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':

    tc = int(input())
    for _ in range(tc):
        if is_balanced(input()):
            print('YES')
        else:
            print('NO')        
