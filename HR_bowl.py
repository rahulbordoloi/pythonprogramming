n=int(input())
b=[]
for i in range(n):
    b.append(int(input()))
flag=1;i=n-1
while flag is 1 and i>-1:
    if b[i] is not 9:
        print(i+1);
        exit()
    else:   i-=1
    
if flag is 1:
    print(0)
    