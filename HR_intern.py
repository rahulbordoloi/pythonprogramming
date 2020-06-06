n=int(input())
id=[5000*x for x in range(1,n+1)]
for i in range(1,n+1):
    id[i]+=5000+(i-1) 
