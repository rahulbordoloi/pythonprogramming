import math
def npow(a,b):
    x=round(math.log(b)/math.log(a))
    y=x+1
    if(abs((a**x)-b)>abs((a**y)-b)):
        return a**y
    else:
        return a**x
p=int(input("Enter your 1st Number:"))
q=int(input("Enter your 2nd Number:"))
print("The Nearest Power is:",npow(p,q))
